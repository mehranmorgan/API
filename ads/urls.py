from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('ads_view', views.AdView.as_view(), name='ad_view'),
    path('create_ad', views.CreateAd.as_view(), name='create_ad'),
    path('ad_detail_view/<int:pk>', views.AdDetailView.as_view(), name='ad_detail_view'),
    path('search/', views.AdSearchView.as_view(), name='ad_search_view'),
]
