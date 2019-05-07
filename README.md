# Introducción a las colas
La cola (queue) es un objeto clásico en programación, que consiste en un conjunto de elementos ordenados que deben consumirse siguiendo el concepto FIFO (First In, First Out: primero en entrar, primero en salir).

Generar un flujo de mensajes entre procesos en Python, es relativamente sencillo usando dos herramientas de software libre basadas en el protocolo AMPQ: el servicio de mensajería RabbitMQ y el cliente Pika.

**RabbitMQ** es un gestor de mensajes (message broker) desarrollado en Erlang.

Para el intercambio de mensajes, RabbitMQ implementa un protocolo estándar llamado AMQP (Advanced Message Queue Protocol). Dado que es un estándar, podemos interactuar con él usando cualquier lenguaje que tenga una librería cliente para dicho protocolo. En este artículo vamos a usar la librería Pika en Python, pero hay otras similares para montones de lenguajes, incluidos Java, PHP, Javascript, C# y un largo etcétera.

- Comprobar que el servicio está arriba

```unix
sudo rabbitmqctl status
```

- Arrancar servicio

```unix
sudo service rabbitmq-server start
```

- Consultar listas publicadas

```unix
sudo rabbitmqctl list_queues
```

## Productor.py

Este script es quién se encarga de publicar mensajes (json en este caso, podría ser xml, yaml, etc...) en la cola declarada y una vez se tenga conexión con el servidor de mensajeria RabbitMQ, en nuestro ejemplo corriendo en la máquina local, pero podría ser la ip de un servidor externo.

## Consumidor.py

Script encagado de consumir trabajos en orden de llegada enviados por productor.py. Se debe definir una función callback para indicar que hacer con los trabajos según se van consumiendo. En nuestro caso tenemos la función process que envia el trabajo deserializado al script proceso y función ejecutar.

## job.py

Clase que define nuestro trabajo de ejemplo

```python
class Job:
    def __init__(self, operacion, entrada=None):
        self.operacion = operacion
        self.entrada = entrada
```

Junto con las operaciones para serializar(exportar) y deserializar(importar)

Crear un trabajo:

```python
t = Job('hola', 'mundo')
```

Serializarlo:

```python
cadena = t.exportar()
```

Deserializarlo:

```python
t2 = Job.importar(cadena)
```

## Un par de detalles a destacar

- Dado que el body de los mensajes ha de ser binario, hacemos la correspondiente conversión desde/hacia UTF-8.
- Para mantener el código debidamente modular, hemos separado la gestión de los trabajos por un lado y la propia ejecución de los mismos. Para ello hemos creado un módulo proceso.py con una función ejecutar().