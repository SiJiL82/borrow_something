from . import views
from django.urls import path

urlpatterns = [
    path('', views.RequestList.as_view(), name='home'),
    path('request/', views.Request.as_view(), name='new_request'),
]
