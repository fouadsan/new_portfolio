from django.contrib import admin

from .models import Profile, Skill, Education, Experience, Service, Project, Social

admin.site.register(Profile),
admin.site.register(Skill),
admin.site.register(Education),
admin.site.register(Experience),
admin.site.register(Service),
admin.site.register(Project),
admin.site.register(Social)
