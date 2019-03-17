from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('complete/<list_id>', views.complete, name="complete"),
    path('incomplete/<list_id>', views.incomplete, name="incomplete"),
    path('edit/<list_id>', views.edit, name="edit"),

]
