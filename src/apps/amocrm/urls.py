from django.urls import path
from .views import ClientDataAPIView

urlpatterns = [
    path("client-data/", ClientDataAPIView.as_view(), name="client-data"),

]