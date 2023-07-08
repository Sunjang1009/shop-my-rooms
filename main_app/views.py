from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Theme:
    def __init__(self, name, image):
        self.name = name
        self.image = image

themes = [
    Theme("modern", "https://i.pinimg.com/236x/09/71/17/09711788c0cda08d318e1b446e739003.jpg"),
    Theme("colorful", "https://i.pinimg.com/236x/da/6f/f3/da6ff36deea78497b5d3cfb1ba8c8355.jpg"),
    Theme("bohemian", "https://i.pinimg.com/236x/0d/cb/14/0dcb14d1029cdc29d51d23aed35d2ac1.jpg"),
    Theme("romantic", "https://i.pinimg.com/564x/92/6c/0e/926c0ecad7c6afd7149902697b4eea10.jpg"),
]

class ThemeList(TemplateView):
    template_name = "theme_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["themes"] = themes
        return context

