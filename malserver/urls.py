from django.urls import path
from . import views
urlpatterns = [
    path("malpredict",views.mal_prediction),
    path("maltest",views.mEndpointTest),
    path("",views.index),


    
]