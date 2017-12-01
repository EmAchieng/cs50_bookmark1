"""cs50_bookmark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.url import url
from django.contrib import admin

from bookmark import views as  bk_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', bk_views.current_datetime, name='index')
]


      def current_datetime(request):
          now = datetime.datetime.now()
          html="<html><body> It is now %s. </body></html>" % now
          return HttpResponse(html)
