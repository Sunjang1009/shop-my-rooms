from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('themes/', views.ThemeList.as_view(), name="theme_list"),
    path('themes/<int:pk>/', views.ThemeDetail.as_view(), name="theme_detail"),
    path('themes/<int:pk>/lookbooks/new/', views.LookbookCreate.as_view(), name="lookbook_create"),
    path('lookbooks/<int:pk>/', views.LookbookDetail.as_view(), name="lookbook_detail"),
    path('lookbooks/<int:pk>/new/', views.ProductCreate.as_view(), name="product_create"),
    path('lookbooks/<int:lookbook_pk>/products/<int:pk>/update/',views.ProductUpdate.as_view(), name="product_update"),
]











