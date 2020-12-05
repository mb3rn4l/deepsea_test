from django.db import models


class Team(models.Model):

    name = models.CharField(null=False, blank=False, unique=True, max_length=100, verbose_name='Name')
    image = models.ImageField(null=False, blank=True, verbose_name="Team Picture", upload_to='teams_picture')
    members = models.ManyToManyField('teams.User', through='teams.UsersByTeam', through_fields=('team', 'user'))
