import random


class Obra:
    def __init__(self, nro, tipo, presupuesto, costo, resp):
        self.numero = nro
        self.tipo_obra = tipo
        self.presupuesto = presupuesto
        self.costo_total = costo
        self.responsable = resp


def to_string(obra):
    """ Esta funcion genera una cadena que representa el cotenido
     de un registro
     :param obra: Obra a string
     :return: Un string representando a la obra"""

    cadena_obra = 'Numero: ' + str(obra.numero) + ' - '
    cadena_obra += 'Tipo: ' + str(obra.tipo_obra) + ' - '
    cadena_obra += 'Presupuesto: ' + str(obra.presupuesto) + ' - '
    cadena_obra += 'Costo Total: ' + str(obra.costo_total) + ' - '
    cadena_obra += 'Responsable: ' + str(obra.responsable) + ' - '

    return cadena_obra


def crear_obra_aleatoria():
    """ Crea un registro de datos aleatoris
    :return: Una obra aleatoria"""

    nro = random.randint(1, 1000)
    tipo = random.randint(1, 5)
    presupuesto = random.randint(100000, 3000000)
    costo_total = random.randint(100000, 3000000)
    responsable = 'Ing. Numero ' + str(random.randint(1, 20))

    obra = Obra(nro, tipo, presupuesto, costo_total, responsable)

    return obra
