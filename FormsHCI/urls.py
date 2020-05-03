from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form.html', views.form, name='form'),
    path('create.html', views.create, name='create'),
    path('results<form_id>.html', views.results, name='results'),
    path('completed.html', views.completed, name='completed')
]
