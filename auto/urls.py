"""
URL configuration for auto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from auto import settings
from main import views

app_name = "main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.MainView.as_view(),name='home'),
    path('car/<slug:brand>/<slug:model>/', views.DetailView.as_view(), name='detail-car'),
     path('car/<slug:brand>/',views.DetailPage.as_view(),name='brand-detail'),
    # path('news/',views.news,name='news'),
     path('search/<str:brand>/', views.SearchView.as_view(), name='search-car-with-brand'),
     path('search/', views.SearchView.as_view(), name='search-car'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)