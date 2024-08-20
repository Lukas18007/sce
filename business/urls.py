from django.urls import path
from . import views

urlpatterns = [
    path('business/', views.BusinessCreateView.as_view(), name='business-create-list')
]