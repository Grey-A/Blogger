"""MainBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib import sitemaps

from .sitemaps import CategorySitemap, PostSitemap, SubscribeSitemap
from blog.views import robots_txt

sitemaps = {'category':CategorySitemap, 'post':PostSitemap, 'subscribe':SubscribeSitemap }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('robots.txt/', robots_txt, name="robots.txt"),
    path('sitemap.xml/', sitemap, {'sitemaps':sitemaps})

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
