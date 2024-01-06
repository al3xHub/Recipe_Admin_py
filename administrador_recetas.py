# Saludo al usuario
# mostrar carpeta del recetario
# indicar cuántas recetas tenemos en la carpeta
"""
pedir usuario opciones a elegir :
    (1-leer receta:
        - elegir categoría
        - mostrar recetas
        - leer recetas
    2-crear receta:
        - elegir categoría
        - crear nombre
        - crear contenido
    3-crear categoria:
        - crear nombre carpeta
        - crear categoria
    4-eliminar receta:
        - elegir categoría
        - mostrar recetas
        - elegir receta
        - eliminarla
    5-eliminar categoría:
        - elegir categoría
        - eliminarla
    6-finalizar programa:
        -  finalizar ejecución del código
"""
"""
    Cuestiones a considerar:
        - bucle while donde dentro se muestra las opciones a elegir hasta que se pulse un 6 que es finalizar.
        - algunos métodos deben de ser buscadas en la documentación ya que no está en el temario.
        - ayudate creando funciones ej: def elegir_categoria()
        - hacer diagrama de flujo
"""

#######################################################################################################################

import os
from pathlib import Path

mi_ruta = Path(Path.home(), "Recetas")


# funciones

def contador_recetas(ruta):
    # Cuenta cuántas recetas tenemos en la carpeta "Recetas".
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador


def inicio():
    opciones = "x"
    print('Bienvenido al administrador de recetas :D\n')
    print(f'La carpeta receta se encuentra en el directorio -->{mi_ruta}\n')
    print(f'El total de recetas que tenemos es de -->{contador_recetas(mi_ruta)}\n')

    while not opciones.isnumeric() or int(opciones) not in range(1, 7):
        opciones = input(
            '¿Qué te apetece hacer?:\nEscribe el número correspondiente.\n1- Leer recetas\n2- Crear '
            'receta\n3- Crear categoría\n4- Eliminar receta\n5- Eliminar categoría\n6- Finalizar programa\n'
        )
    return opciones


def mostrar_categorias(ruta):
    print('Categorías:')
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for categoria in ruta_categorias.iterdir():
        categoria_str = str(categoria.name)
        print(f'[{contador}] - {categoria_str}')
        lista_categorias.append(categoria)
        contador += 1

    return lista_categorias


def elegir_categoria(lista_categorias):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista_categorias) + 1):
        eleccion_correcta = input('Elige la categoría indicando el nº:')

    return lista_categorias[int(eleccion_correcta) - 1]


def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}] - [{receta_str}]')
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas


def elegir_receta(lista_recetas):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista_recetas) + 1):
        eleccion_correcta = input('Elige la receta indicando el nº:')

    return lista_recetas[int(eleccion_correcta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))


def crear_receta(ruta):
    existe = False

    while not existe:
        print('Escribe el nombre de la receta:')
        nombre_receta = input() + '.txt'
        print('Escribe el contenido de tu nueva receta:')
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada con correctamente!')
            existe = True
        else:
            print('Lo siento, esta receta ya existe.')


def crear_categoria(ruta):
    existe = False

    while not existe:
        print('Escribe el nombre de la categoria:')
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu categoria {nombre_categoria} ha sido creada con correctamente!')
            existe = True
        else:
            print('Lo siento, esta categoria ya existe.')


def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta.name} ha sido eliminada.')


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoria {categoria.name} ha sido eliminada.')


def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input('\nPor favor para volver al inicio pulse la tecla "v":')


finalizar_programa = False

while not finalizar_programa:
    menu = inicio()

    if menu == "1":
        # mostrar categoria
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)

        if len(mis_recetas) < 1:
            print('Lo siento no hay recetas en esta categoría')
        else:
            # elegir receta
            mi_receta = elegir_receta(mis_recetas)
            # leer receta
            leer_receta(mi_receta)
            # volver inicio
            volver_inicio()

    elif menu == "2":
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # crear receta
        crear_receta(mi_categoria)
        # volver inicio
        volver_inicio()

    elif menu == "3":
        # crear categoria
        crear_categoria(mi_ruta)
        # volver inicio
        volver_inicio()

    elif menu == "4":
        # mostrar categoria
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        # elegir receta
        mi_receta = elegir_receta(mis_recetas)
        # eliminar receta
        eliminar_receta(mi_receta)
        # volver inicio
        volver_inicio()

    elif menu == "5":
        # mostrar categoria
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # eliminar categoría
        eliminar_categoria(mi_categoria)
        # volver inicio
        volver_inicio()


    elif menu == "6":
        finalizar_programa = True
