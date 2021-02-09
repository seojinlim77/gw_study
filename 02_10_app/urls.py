from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', views.Userviewset)

urlpatterns = [
    path("login/", views.login_with_file),
    path("show/", views.dbcontext),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('sshow/', views.user_list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
