from django.urls import path, re_path

from .views import ProjectDetailView, ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    re_path(r'^(?P<project_id>[-\w]+)/$', ProjectDetailView.as_view(),
            name='project_detail'),
]
