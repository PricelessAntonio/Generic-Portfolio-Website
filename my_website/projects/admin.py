from django.contrib import admin

from .models import Project, ProjectPost, ProjectImage

admin.site.register(Project)
admin.site.register(ProjectPost)
admin.site.register(ProjectImage)
