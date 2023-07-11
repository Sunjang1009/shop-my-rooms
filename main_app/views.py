from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Theme, Lookbook

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"


class ThemeList(TemplateView):
    template_name = "theme_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["themes"] = Theme.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["themes"] = Theme.objects.all()
            context["header"] = "Themes"
        return context

class ThemeDetail(DetailView):
    model = Theme
    template_name = "theme_detail.html"

class LookbookCreate(View):
    def post(self, request, pk):
        name = request.POST.get("name")
        image = request.POST.get("image")
        items = request.POST.get("items")
        theme = Theme.objects.get(pk=pk)
        Lookbook.objects.create(name=name, image=image, items=items, theme=theme)
        return redirect('theme_detail', pk=pk)

class LookbookDetail(DetailView):
    model = Lookbook
    template_name = "lookbook_detail.html"



