from django.views.generic import TemplateView


class ProjectDetailView(TemplateView):
    http_method_names = ['get']
    template_name = "projects/detail.html"


class ProjectListView(TemplateView):
    http_method_names = ['get']
    template_name = "projects/list.html"
