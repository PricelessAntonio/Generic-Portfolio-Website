from django.db import models

from django.contrib.auth.models import User


class Project(models.Model):
    project_date = models.DateTimeField(auto_now_add=True)
    project_title = models.CharField(max_length=100)
    project_description = models.CharField(max_length=300)
    project_completion_status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,
                             null=True)


class ProjectPost(models.Model):
    project_post_date = models.DateTimeField(auto_now_add=True)
    project_post_title = models.CharField(max_length=100)
    project_post_content = models.CharField(max_length=40000)
    project_post_image = models.ImageField()
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True,
                                null=True)
