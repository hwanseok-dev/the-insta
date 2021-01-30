from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include  # add this
from rest_framework import routers  # add this
from todo import views  # add this
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='the insta API')

router = routers.DefaultRouter()  # add this
router.register(r'todos', views.TodoView, 'todo')  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # add this
    url(r'^$', schema_view)
]
