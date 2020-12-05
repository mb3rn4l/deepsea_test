from rest_framework.viewsets import ModelViewSet

from apps.teams.models import Team
from apps.teams.serializers import CreateUpdateTeamSerializer, ListRetrieveTeamSerializer


class TeamsViewSet(ModelViewSet):
    queryset = Team.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return ListRetrieveTeamSerializer
        else:
            return CreateUpdateTeamSerializer
