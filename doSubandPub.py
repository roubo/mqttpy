#!/usr/bin/env python
# encoding: utf-8
"""
It can do the subscribe and public the msg throught mosquitto broker
"""
import mosquitto as mqtt
import pyttsx
import time

def speakToMe(what, **justwith):
    """
    speak to me about something with some special
    justwith key:
        "speed": "slow","medium","fast"
        "faster": number type (1-10)
        "volume": "low", "medium","loud"
        "louder": number type(0.01-0.1)
    """
    defspeed={"slow":0.01,"medium":80,"fast":210}
    defvolume={"low":0.3,"medium":0.5,"loud":1}
    engine = pyttsx.init("espeak")
    engine.setProperty('languages','zh')
    if justwith == None :
        # Just say out
        engine.say(what)
    else:
        if justwith['speed'] != None:
            engine.setProperty('rate',defspeed[justwith['speed']])
        if justwith['volume']!= None:
            engine.setProperty('volume', defvolume[justwith['volume']])
        if justwith['faster'] != None:
            if isinstance(justwith['faster'], int):
                sp = engine.getProperty('rate')
                engine.setProperty('rate',sp+justwith['faster'])
        if justwith['louder'] != None:
            if isinstance(justwith['louder'], float):
                vo = engine.getProperty('volume')
                engine.setProperty('volume',vo+justwith['louder'])
        engine.say(what)
        engine.runAndWait()

def on_connect(mosq, obj, rc):
    print("connect->"+"rc: "+str(rc))

def on_message(mosq, obj, msg):
    print("message->"+msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    speakToMe(msg.payload \
              ,speed="slow",volume="loud",faster=0,louder=0)


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
    subScribeMsg("i7", "182.92.163.51")
    #time.sleep(2)
    #pubLishMsg("Hello", "Hi man", "127.0.0.1")
