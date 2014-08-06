mqtt服务和客户端
===============
JunJian from 2014.08.06

>   目的

由一个mqtt消息分发中心（服务）和自由的客户端结构

>   服务

Mosquitto：http://mosquitto.org/files/source/

Modify the config.mk make sure the WITH_PYTHON is opened

make & make install

Modify the /etc/mosquitto/mosquitto.conf or use the default

run the server by mosquitto -c /etc/mosquitto/mosquitto.conf -d or just mosquitto -d

It is just a broker.

>   客户端

May use the local demo mosquitto_sub and mosquitto_pub

Also start to use the python to make the sub or pub client

