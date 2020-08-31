import validation
import register


def crear_vector(n):
    """ Crear un vector con n elementos del tipo obra
    :param n: cantidad de obras
    :return: Un vector con n obras con valores aleatorios"""

    vec = [None] * n

    for i in range(n):
        vec[i] = register.crear_obra_aleatoria()

    return vec


def mostrar_vector(obras):
    """Muestra los elementos de un vector de obras
    :param obras: El vector a mostar
    :return: None"""

    for una_obra in obras:
        print(register.to_string(una_obra))


def contar_por_tipo(obras):
    """Muestr las obras por tipo
    :param obras: Vector obras
    :retunr: Vector conteo"""

    vec_conteo = [0] * 5

    for una_obra in obras:
        vec_conteo[una_obra.tipo_obra - 1] += 1
    return vec_conteo


def ordenar_obras(obras):
    """ Ordenar por seleccion directa
    :param obras: el vector a ordenar
    :return: None"""

    n = len(obras)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if obras[i].presupuesto > obras[j].presupuesto:
                obras[i], obras[j] = obras[j], obras[i]


def buscar_obra(obras, a_buscar):
    """Busqueda secuencial
    :Param obras: vector
    :Param a_buscar: numero de obra a buscar
    :return: Indice"""

    for i in range(len(obras)):
        if obras[i].numero == a_buscar:
            return i
    return -1


def contar_presupuesto_mayor(obras, monto_minimo):
    """
    Contar cuantas obras existen con un monto mayor a monto_minimo
    :param obras: las obras
    :param monto_minimo: Monto minimo a buscar
    :return: La cantidad de obras
    """

    cantidad = 0

    for una_obra in obras:
        if una_obra.presupuesto > monto_minimo:
            cantidad += 1

    return cantidad


def main():
    menu = '==== Menu ===\n' \
           '1) Cargar Obras\n' \
           '2) Mostrar Obras\n' \
           '3) Contar por tipo\n' \
           '4) Ordenar por presupuesto\n' \
           '5) Buscar una obra por numero\n' \
           '6) Contar obras con presupuesto mayor\n' \
           '0) Salir\n'

    obras = None
    op = -1

    while op != 0:
        print(menu)
        op = int(input('Ingrese opcion: '))

        if op == 0:
            print('Hasta luego!')
        elif op == 1:
            n = int(input('Ingrese cantidad de obras:'))
            obras = crear_vector(n)
        elif obras is None:
            print('Debe cargar los datos')

        elif op == 2:
            mostrar_vector(obras)

        elif op == 3:

            obras_cont = contar_por_tipo(obras)

            for i in range(len(obras_cont)):
                print('Tipo: ' + str(i + 1) + ' -> ' + str(obras_cont[i]))

        elif op == 4:
            ordenar_obras(obras)
            print('Obras ordenadas por presupuesto: ')
            mostrar_vector(obras)

        elif op == 5:
            a_buscar = int(input('Ingrese obra a buscar: '))

            pos = buscar_obra(obras, a_buscar)

            if pos != -1:
                obra_encontrada = obras[pos]
                print("Obra encontrada!")
                print("Responsable: " + obra_encontrada.responsable)
                print('Desviacion: ' + str(obra_encontrada.costo_total - obra_encontrada.presupuesto))
            else:
                print('No existe')

        elif op == 6:
            monto_minimo = int(input('Ingrese monto minimo: '))
            cantidad_mayores = contar_presupuesto_mayor(obras, monto_minimo)
            print('La cantidad de obras con presupuesto mayor a ', monto_minimo, 'es :', cantidad_mayores)


main()
