from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('peep/', views.PeepList.as_view(), name='peep_list'),
    path('peep/<int:pk>', views.PeepDetail.as_view(), name='peep_detail'),
    path('chirp/', views.ChirpList.as_view(), name='peep_list'),
    path('chirp/<int:pk>', views.ChirpDetail.as_view(), name='peep_detail')
]
