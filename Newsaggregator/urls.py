from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    #URL FOR ADMIN PAGE
    path('admin/', admin.site.urls),
    #URL FOR HOME PAGE
    path('', views.index, name = "home"),
    #URL FOR SCRAPING LATEST NEWS
    path('scrape/', views.get_kun, name="get_kun"),
    #URL FOR SPORT PAGE
    path('sport/', views.sport, name="get_sport"),
    #URL FOR SCRAPING SPORT NEWS
    path('loadsport/', views.get_sport, name="load_sport"),
    #URL FOR POLITICS PAGE
    path('politics/', views.siyosat, name="siyosat"),
    #URL FOR SCRAPING POLITICAL NEWS
    path('loadpolitics/', views.get_siyosat, name="load_siyosat"),
    #URL FOR ECONOMICS PAGE
    path('jahon/', views.jahon, name="jahon"),
    #URL FOR SCRAPING ECONOMIC NEWS
    path('loadeconomy/', views.get_economy, name="load_economy"),
]