from django.views.generic import ListView

from .models import Project, ProjectPost


class ProjectListView(ListView):
    http_method_names = ['get']
    queryset = Project.objects.all().order_by('project_date')
    template_name = "projects/list.html"


class ProjectPostListView(ListView):
    http_method_names = ['get']
    template_name = "projects/post_list.html"

    def get_queryset(self):
        return ProjectPost.objects.filter(
            project=self.kwargs['project_id']).order_by('project_post_date')
