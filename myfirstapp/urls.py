from django.contrib import admin
from django.urls import path
from . import views


app_name = 'myfirstapp'
urlpatterns = [
    # ex: /myfirstapp/
    path('', views.index, name = 'index'),
    # ex: /myfirstapp/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /myfirstapp/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: myfirstapp/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]