from django.urls import path
from . import views
urlpatterns = [
    path("malpredict",views.mal_prediction),
    path("maltest",views.mTest1),
    path("maltest2",views.mTest2),
]