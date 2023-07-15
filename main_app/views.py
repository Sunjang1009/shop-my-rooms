from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Theme, Lookbook, Product, Shoppinglist

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shoppinglists"] = Shoppinglist.objects.all()
        return context

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
            context["header"] = "Shop My Rooms"
        return context

class ThemeDetail(DetailView):
    model = Theme
    template_name = "theme_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lookbooks"] = Lookbook.objects.all()
        return context

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shoppinglists"] = Shoppinglist.objects.all()
        return context

class LookbookUpdate(UpdateView):
    model = Lookbook
    fields = ['name', 'image', 'items']
    template_name = "lookbook_update.html"
    def get_success_url(self):
        return reverse('theme_detail', kwargs={'pk':self.object.theme.pk})

class LookbookDelete(DeleteView):
    model = Lookbook
    template_name = "lookbook_delete_confirmation.html"
    def get_success_url(self):
        return reverse('theme_detail', kwargs={'pk':self.object.theme.pk})

class ProductCreate(View):
    def post(self, request, pk):
        name = request.POST.get("name")
        image = request.POST.get("image")
        price = request.POST.get("price")
        lookbook = Lookbook.objects.get(pk=pk)
        Product.objects.create(name=name, image=image, price=price, lookbook=lookbook)
        return redirect('lookbook_detail', pk=pk)

# have some issue with my reverse function
class ProductUpdate(UpdateView):
    model = Product
    fields = ["name", "image", "price"]
    template_name = "product_update.html"
    # have to update kwargs as pk lookbook pk not product pk
    def get_success_url(self):
        return reverse('lookbook_detail', kwargs={'pk':self.object.pk})

class ShoppinglistProductAssoc(View):
    def get(self, request, pk, product_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Shoppinglist.objects.get(pk=pk).products.remove(product_pk)
        if assoc == "add":
            Shoppinglist.objects.get(pk=pk).products.add(product_pk)
        return redirect('home')
