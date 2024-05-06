"""
URL configuration for drf_test_task_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from events.views import EventViewSet, RegisterEvent

router = SimpleRouter()
# http://127.0.0.1:8000/api/v1/event/
router.register(r'api/v1/event', EventViewSet)

# http://127.0.0.1:8000/api/v1/register
router.register(r'api/v1/register', RegisterEvent)

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    # http://127.0.0.1:8000/api/v1/auth/session/login/
    # http://127.0.0.1:8000/api/v1/auth/session/logout/
    path('api/v1/auth/session/', include('rest_framework.urls')),

    # http://127.0.0.1:8000/api/v1/users/
    path('api/v1/', include('djoser.urls')),

    # http://127.0.0.1:8000/api/v1/auth/token/login/
    # http://127.0.0.1:8000/api/v1/auth/token/logout/
    path('api/v1/auth/', include('djoser.urls.authtoken')),
]

urlpatterns += router.urls
