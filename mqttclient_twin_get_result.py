#https://www.jianshu.com/p/b76dbc675141
import paho.mqtt.client as mqtt
 
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
  print(msg.topic+" "+str(msg.payload))

print("start")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1", 1884, 600)
client.subscribe('$hw/events/device/led-light-instance-01/twin/get/result',qos=0)
#client.loop_start()
client.loop_forever()
print("end")
