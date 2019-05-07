import json

class Job:
    def __init__(self, operacion, entrada=None):
        self.operacion = operacion
        self.entrada = entrada

    def exportar(self):
        return json.dumps(self.__dict__)
    
    @classmethod
    def importar(cls, datos):
        dic = json.loads(datos)
        return cls(dic['operacion'], dic['entrada'])
