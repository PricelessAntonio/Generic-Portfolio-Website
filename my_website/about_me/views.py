from django.views.generic import TemplateView


class AboutMeView(TemplateView):
    http_method_names = ['get']
    template_name = "about_me/about.html"
