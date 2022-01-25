from django.contrib import admin
from django.urls import include , path
from . import views

urlpatterns = [
#     path('admin/', admin.site.urls),
    path("", views.all_things, name="all_things"),
    path('<int:pk>/', views.thing_read, name="thing_read"),
    path("create/", views.thing_create, name="thing_create"),    
    path("update/<int:pk>", views.thing_update, name="thing_update"),
    path("delete/<int:pk>", views.thing_delete, name="thing_delete"),

]