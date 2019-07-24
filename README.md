# Enhanced Python MQTT Controller

Improved paho MQTT client, featuring:

- Reconnection on startup, avoiding client to give up reconnecting if broker is down/unreachable during the initial 
  connection attempt.
- Simpler import, avoid the `import paho.mqtt.client as mqtt` ugly import line.
- Function decorators for all the client handlers (e.g. on_message, on_connect).
- New MQTTClient class inherits from original paho.mqtt Client class, so all its original features are still available.
  Only replaced method is `connect`.

## Example

```python
from bettermqtt import MQTTClient

client = MQTTClient()

@client.on_connect_register
def on_connect(*args):
    print("Connected!")
    client.subscribe("test/cmd")

@client.on_message_register
def on_message(*args):
    message = next(a for a in args if isinstance(a, MQTTMessage))
    print(f"Rx Message @ {message.topic}: {message.payload.decode()}")

client.connect("localhost")
client.publish("test/stat", "I'm connected!")
client.loop_start()
```

## Available decorators

- on_message_register
- on_connect_register
- on_disconnect_register
- on_subscribe_register
- on_unsubscribe_register
- on_log_register
- on_publish_register
- on_socket_close_register
- on_socket_open_register
- on_socket_register_write_register
- on_socket_unregister_write_register
