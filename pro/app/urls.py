from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('display', views.display_contact, name='display_contact'),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('api-info',views.apioverview, name="apioverview"),
    path('list',views.list, name="list"),
    path('detail/<str:pk>',views.detail, name="detail"),
    path('create',views.create, name="create"),
    path('update/<str:pk>',views.update, name="update"),
    path('delete/<str:pk>',views.delete, name="delete"),
]
