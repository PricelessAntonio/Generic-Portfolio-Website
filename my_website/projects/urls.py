from django.urls import path

from .views import ProjectPostListView, ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<int:project_id>', ProjectPostListView.as_view(),
         name='project_post_list'),
]
