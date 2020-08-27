
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema__view = get_swagger_view()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/',include('cmdapp.urls')),
    path('api-auth/',include('rest_framework.urls')),
    url(r'swagger/',schema__view)
]

