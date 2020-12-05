from django.contrib import admin
from django import forms
from apps.teams.models import User, Team, UsersByTeam


class UserByTeamInline(admin.TabularInline):
    model = Team.members.through
    extra = 1
    readonly_fields = ('joining_date',)


class UserAdmin(admin.ModelAdmin):
    inlines = (UserByTeamInline,)


class UsersByTeamAdmin(admin.ModelAdmin):
    readonly_fields = ('joining_date',)


admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(UsersByTeam, UsersByTeamAdmin)
