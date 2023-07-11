from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('themes/', views.ThemeList.as_view(), name="theme_list"),
    path('themes/<int:pk>/', views.ThemeDetail.as_view(), name="theme_detail"),
    path('themes/<int:pk>/lookbooks/new/', views.LookbookCreate.as_view(), name="lookbook_create"),
    path('themes/<int:pk>/lookbooks/<int:lookbook_pk>/', views.LookbookDetail.as_view(), name="lookbook_detail"),
]








