from django.contrib import admin
from django.urls import path
from news import views, crawler

urlpatterns = [
    #URL FOR ADMIN PAGE
    path('admin/', admin.site.urls),
    #URL FOR HOME PAGE
    path('', views.index, name = "home"),
    #URL FOR SCRAPING LATEST NEWS
    path('scrape/', crawler.get_latest, name="get_kun"),
    #URL FOR SPORT PAGE
    path('sport/', views.sport, name="get_sport"),
    #URL FOR SCRAPING SPORT NEWS
    path('loadsport/', crawler.get_sport, name="load_sport"),
    #URL FOR POLITICS PAGE
    path('politics/', views.siyosat, name="siyosat"),
    #URL FOR SCRAPING POLITICAL NEWS
    path('loadpolitics/', crawler.get_siyosat, name="load_siyosat"),
    #URL FOR ECONOMICS PAGE
    path('economy/', views.economy, name="economy"),
    #URL FOR SCRAPING ECONOMIC NEWS
    path('loadeconomy/', crawler.get_economy, name="load_economy"),
    path('body/str:<pk>/', views.body, name="body"),
    path('body/sport/str:<pk>/', views.body_sport, name="body_sport"),
    path('body/politics/str:<pk>/', views.body_politics, name="body_politics"),
    path('body/economy/str:<pk>/', views.body_economy, name="body_economy"),
]