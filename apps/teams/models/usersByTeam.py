from django.db import models


class UsersByTeam(models.Model):
    user = models.ForeignKey('teams.User', on_delete=models.CASCADE, verbose_name="user", blank=False, null=False,)
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, verbose_name="team", blank=False, null=False,)
    joining_date = models.DateTimeField(blank=False, null=False, auto_now=True, verbose_name="joining date")
