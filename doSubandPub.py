#!/usr/bin/env python
# encoding: utf-8
"""
It can do the subscribe and public the msg throught mosquitto broker
"""
import mosquitto as mqtt
import time
def on_connect(mosq, obj, rc):
    print("connect->"+"rc: "+str(rc))

def on_message(mosq, obj, msg):
    print("message->"+msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mosq, obj, mid):
    print("publish->"+"mid: "+str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed-> "+str(mid)+" "+str(granted_qos))

def subScribeMsg(topic, broker):
    """
    subscribe the topic from broker
    """
    mqttclient = mqtt.Mosquitto()
    mqttclient.on_message = on_message
    mqttclient.on_connect = on_connect
    mqttclient.on_subscribe = on_subscribe
    if broker == None :
        broker = "127.0.0.1"
    mqttclient.connect(broker, 1883, 60)
    mqttclient.subscribe(topic, 0)
    rc = 0
    while rc == 0:
        rc = mqttclient.loop()

def pubLishMsg(msg, topic, broker):
    """
    publish the msg with the topic to broker
    """
    mqttclient = mqtt.Mosquitto()
    mqttclient.on_message = on_message
    mqttclient.on_connect = on_connect
    mqttclient.on_publish = on_publish
    if broker == None :
        broker = "127.0.0.1"
    mqttclient.connect(broker, 1883, 60)
    mqttclient.publish(topic, msg, 0, True)
    rc = 0
    while rc == 0:
        rc = mqttclient.loop()
if __name__ == '__main__':
    #subScribeMsg("Hello", "127.0.0.1")
    #time.sleep(2)
    pubLishMsg("Hello", "Hi man", "127.0.0.1")
