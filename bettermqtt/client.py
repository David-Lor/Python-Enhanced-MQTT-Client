
# # Native # #
from time import sleep

# # Installed # #
import paho.mqtt.client as mqtt


class MQTTClient(mqtt.Client):
    def connect(self, host, port=1883, keepalive=60, bind_address="", reconnect=True, retry_freq=2):
        connected = False
        try:
            mqtt.Client.connect(self, host=host, port=port, keepalive=keepalive, bind_address=bind_address)
        except ConnectionError as ex:
            # TODO improve error detection
            if not reconnect:
                raise ex
            else:
                while not connected:
                    try:
                        super(MQTTClient, self).reconnect()
                    except ConnectionError:
                        sleep(retry_freq)
                    else:
                        connected = True

    def _register(self, func, context: str):
        self.__setattr__(context, func)

    def on_message_register(self, func):
        return self._register(func, "on_message")

    def on_connect_register(self, func):
        return self._register(func, "on_connect")

    def on_disconnect_register(self, func):
        return self._register(func, "on_disconnect")

    def on_subscribe_register(self, func):
        return self._register(func, "on_subscribe")

    def on_unsubscribe_register(self, func):
        return self._register(func, "on_unsubscribe")

    def on_log_register(self, func):
        return self._register(func, "on_log")

    def on_publish_register(self, func):
        return self._register(func, "on_publish")

    def on_socket_close_register(self, func):
        return self._register(func, "on_socket_close")

    def on_socket_open_register(self, func):
        return self._register(func, "on_socket_open")

    def on_socket_register_write_register(self, func):
        return self._register(func, "on_socket_register_write")

    def on_socket_unregister_write_register(self, func):
        return self._register(func, "on_socket_unregister_write")
