#!/usr/bin/env python
import time

def ejecutar(job):
    if job.operacion =='esperar':
        print('Esperando %d segundos...' % job.entrada)
        time.sleep(job.entrada)
        print('DONE!!!')
    else:
        raise NotImplementedError('Operación "%s" no soportada.' % job.operacion)