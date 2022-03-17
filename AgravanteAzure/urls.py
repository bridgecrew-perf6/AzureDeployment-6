from AgravanteAzure import views
from django.urls import path

#paths arranged alphabetically by name
app_name = 'AgravanteFirstAzure'

urlpatterns = [
    path('', views.Index.as_view(), name="index")
]