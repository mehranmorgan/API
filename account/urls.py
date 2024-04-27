from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('User_view', views.UserView.as_view())

]
