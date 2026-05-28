# Funcion para solicitar texto y evitar campos vacios
def solicitar_texto(mensaje):
    texto = input(mensaje).strip()

    while texto == "":
        print("El campo no puede estar vacio.")
        texto = input(mensaje).strip()

    return texto


# Limpia el RUT para validar puntos y guion
def limpiar_rut(rut):
    rut_limpio = rut.strip().upper()
    rut_limpio = rut_limpio.replace(".", "")
    rut_limpio = rut_limpio.replace("-", "")

    return rut_limpio


def formatear_rut(rut):
    rut_limpio = limpiar_rut(rut)
    numeros = rut_limpio[:-1]
    digito = rut_limpio[-1]

    return numeros + "-" + digito


# Calcula el digito verificador del RUT
def calcular_digito_verificador(numeros):
    suma = 0
    multiplicador = 2
    posicion = len(numeros) - 1

    while posicion >= 0:
        suma = suma + int(numeros[posicion]) * multiplicador
        multiplicador = multiplicador + 1

        if multiplicador > 7:
            multiplicador = 2

        posicion = posicion - 1

    resultado = 11 - (suma % 11)

    if resultado == 11:
        return "0"
    elif resultado == 10:
        return "K"
    else:
        return str(resultado)


# Validacion del RUT con digito verificador
def validar_rut(rut, lista_ruts):
    rut_limpio = limpiar_rut(rut)

    if rut_limpio == "":
        print("El RUT no puede estar vacio.")
        return False
    elif len(rut_limpio) < 2:
        print("El RUT ingresado no es valido.")
        return False
    else:
        numeros = rut_limpio[:-1]
        digito = rut_limpio[-1]

    if numeros.isdigit() == False:
        print("El RUT debe tener numeros antes del digito verificador.")
        return False
    elif digito.isdigit() == False and digito != "K":
        print("El digito verificador debe ser un numero o K.")
        return False
    elif formatear_rut(rut) in lista_ruts:
        print("El RUT ya fue registrado.")
        return False
    elif calcular_digito_verificador(numeros) != digito:
        print("El digito verificador del RUT no es correcto.")
        return False
    else:
        return True


def solicitar_rut(lista_ruts):
    rut = input("Ingrese RUT: ").strip()

    while validar_rut(rut, lista_ruts) == False:
        rut = input("Ingrese RUT: ").strip()

    return formatear_rut(rut)


def solicitar_contrasena():
    contrasena = input("Ingrese contrasena: ").strip()

    while contrasena == "" or len(contrasena) < 6:
        print("La contrasena debe tener al menos 6 caracteres.")
        contrasena = input("Ingrese contrasena: ").strip()

    return contrasena


def preguntar_continuar():
    respuesta = input("Desea continuar ingresando otra cuenta? (si/no): ").strip().lower()

    while respuesta != "si" and respuesta != "no":
        print("Debe responder si o no.")
        respuesta = input("Desea continuar ingresando otra cuenta? (si/no): ").strip().lower()

    return respuesta


def crear_cuenta(lista_ruts):
    print("")
    print("Inicio de creacion de cuenta")

    nombre = solicitar_texto("Ingrese nombre: ")
    apellido_paterno = solicitar_texto("Ingrese apellido paterno: ")
    apellido_materno = solicitar_texto("Ingrese apellido materno: ")
    rut = solicitar_rut(lista_ruts)
    contrasena = solicitar_contrasena()

    lista_ruts.append(rut)

    usuario = [nombre, apellido_paterno, apellido_materno, rut, contrasena]

    print("")
    print("Cuenta creada correctamente.")

    return usuario


def mostrar_resumen(usuarios):
    print("")
    print("Usuarios registrados:")

    if len(usuarios) == 0:
        print("No se registraron usuarios.")
    else:
        numero = 1

        while numero <= len(usuarios):
            usuario = usuarios[numero - 1]
            print(str(numero) + ". " + usuario[0] + " " + usuario[1] + " " + usuario[2] + " - RUT: " + usuario[3])
            numero = numero + 1


# Ciclo principal del programa
def main():
    usuarios = []
    lista_ruts = []
    continuar = "si"

    print("Bienvenido al sistema de creacion de cuentas")

    while continuar == "si":
        usuario = crear_cuenta(lista_ruts)
        usuarios.append(usuario)
        print("")
        continuar = preguntar_continuar()

    mostrar_resumen(usuarios)
    print("")
    print("Programa finalizado.")


main()
