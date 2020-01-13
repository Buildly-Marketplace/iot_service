from paho.mqtt import client as paho, publish as paho_pub


class MQTTClient(object):

    def __init__(self, topic: str, hostname: str, port: int = 1883):
        self.__topic = topic
        self.__hostname = hostname
        self.__port = port

    @property
    def topic(self):
        return self.__topic

    @property
    def hostname(self):
        return self.__hostname

    @property
    def port(self):
        return self.__port

    def publish(self, message):
        paho_pub.single(
            topic=self.topic,
            hostname=self.hostname,
            port=self.port,
            payload=message,
        )

    def subscribe(self):
        def on_message(mosq, obj, msg):
            print(msg.payload)
            mosq.publish('pong', 'ack', 0)

        # create client object
        client = paho.Client()
        client.on_message = on_message

        # connect to broker and subscribe to topic
        client.connect(self.hostname, self.port)
        client.subscribe(self.topic)

        while client.loop() == 0:
            pass
