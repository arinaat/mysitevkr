"""
URL configuration for mysite project.

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.conf.urls import url
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from main.views import (
  Home,
)

from gallery.views import (
  Gallery, post,


)

from users.views import (
  login_view,
  registration_view,
  logout_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('gallery/', Gallery, name='gallery'),
    # path('<uuid:post_id>', Likes, name='likes'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('upload/', post, name='upload'),
    # re_path(r'^(?P<slug>[\w-]+)/like/$', PostLikeRedirect.as_view(), name='like')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)