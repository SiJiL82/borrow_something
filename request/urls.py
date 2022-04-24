from . import views
from django.urls import path

urlpatterns = [
    path('', views.RequestList.as_view(), name='home'),
    path('request/', views.NewRequest.as_view(), name='new_request'),
    path('myrequests/', views.MyRequestList.as_view(), name='my_requests'),
    path('<slug:slug>/', views.RequestDetail.as_view(), name='request_detail'),
]
