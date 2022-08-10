
from django.urls import path, include
from . import views
urlpatterns = [
    path('1/', views.post1),
    path('2/', views.post2)

]