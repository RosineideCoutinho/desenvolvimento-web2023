
from django.urls import path, include
from rest_framework import routers
from .viewsets import PersonViewSet
from.import views

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet, basename="Person")


urlpatterns = [
    path('register', views.register),


    path("create_person", views.person_create, name='create_person'),
    path("read_person", views.person_read, name='read_person'),
    path("update_person/<int:id>", views.person_update, name='update_person'),
    path("delete_person/<int:id>", views.person_delete, name='delete_person'),
    path('api/', include(routers.urls)),

]
