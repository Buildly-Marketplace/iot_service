import json

from rest_framework import status, views
from rest_framework.response import Response

from iot.mqtt_client import MQTTClient

MQTT_TOPIC = 'hello/world'
MQTT_HOSTNAME = 'mosquitto_server'


class IotCommand(views.APIView):
    def post(self, request, *args, **kwargs):
        client = MQTTClient(
            topic=MQTT_TOPIC,
            hostname=MQTT_HOSTNAME
        )

        message = json.dumps(request.data)
        client.publish(message)

        return Response(status=status.HTTP_200_OK)
