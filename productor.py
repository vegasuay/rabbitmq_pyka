#!/usr/bin/env python
import pika
from job import Job
from random import randint

# Establecer conexion
con = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = con.channel()

# Declarar la cola
ch.queue_declare(queue='trabajos')

# Generar un trabajo
t = Job('esperar', randint(1,10))

# Publicar el mensaje
ch.basic_publish(exchange='',
                 routing_key='trabajos',
                 body=t.exportar().encode('utf-8'))
print("mensaje enviado")

# Cerrar conexion
con.close()
