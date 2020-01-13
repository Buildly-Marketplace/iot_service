from django.urls import path

from iot.views import IotCommand

urlpatterns = [
    path('commands/', IotCommand.as_view())
]
