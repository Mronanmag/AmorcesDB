from django.contrib import admin
from django.urls import path, include
from db_explorer import views

urlpatterns = [
    path('', views.AccueilView.as_view(), name='index'),
    path('amorces/', views.AmorcesView.as_view(), name='amorces'),
    path('couples/', views.CouplesView.as_view(), name='couples'),
    path('admin/', admin.site.urls),
    path('Reverse_Complement/', views.RevCompView.as_view(), name='Reverse_Complement'),
]