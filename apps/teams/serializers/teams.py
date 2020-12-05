import base64
import pathlib
from rest_framework import serializers
from drf_base64.fields import Base64ImageField
from apps.teams.taskapp.tasks import send_creation_team_email
from apps.teams.models import Team, UsersByTeam, User


class CustomBase64Field(Base64ImageField):

    def to_representation(self, value):
        try:
            extesion = pathlib.Path(value.path).suffix.replace('.', '')
            with open(value.path, 'rb') as f:
                base64_code = base64.b64encode(f.read()).decode()
            return "data:image/{extension};base64,{base64Code}".format(extension=extesion, base64Code=base64_code)

        except Exception:
            raise IOError("Error encoding file")


class ListRetrieveUsersByTeamSerializer(serializers.ModelSerializer):

    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UsersByTeam
        fields = ('username', 'joining_date',)
        read_only_fields = ['joining_date']


class CreateUpdateTeamSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    image = CustomBase64Field(required=True, label="Team Picture")

    def get_image(self, obj):
        print("entra")
        try:
            extesion = pathlib.Path(obj.image.path).suffix.replace('.', '')
            with open(obj.image.path, 'rb') as f:
                base64_code = base64.b64encode(f.read()).decode()
            return "data:image/{extension};base64,{base64Code}".format(extension=extesion, base64Code=base64_code)

        except Exception:
            raise IOError("Error encoding file")

    def create(self, validated_data):

        data = super(CreateUpdateTeamSerializer, self).create(validated_data)
        # sendind email
        send_creation_team_email.delay(team_name=data.name)
        return data

    class Meta:
        model = Team
        fields = ('name', 'image', 'members')
        extra_kwargs = {'members': {'required': False}}


class ListRetrieveTeamSerializer(serializers.ModelSerializer):

    image = CustomBase64Field(required=True, label="Team Picture")
    members = ListRetrieveUsersByTeamSerializer(many=True, source='usersbyteam_set')

    class Meta:
        model = Team
        fields = ('name', 'image', 'members')
