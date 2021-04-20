from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path("add-contact/",views.addContact,name="addContact"),
    path("profile/<str:pk>",views.contactProfile,name="profile"),
]
