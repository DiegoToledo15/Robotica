# Registro de Cuentas en Python

Proyecto simple desarrollado para la asignatura **Introduccion a la Programacion y Robotica Aplicada**.

El programa permite registrar una o mas cuentas de usuario desde la consola, solicitando datos personales basicos y validando la informacion ingresada.

## Objetivo

Crear un programa en Python que siga el flujo de un diagrama de flujo para el registro de cuentas de usuario.

El sistema solicita:

- Nombre
- Apellido paterno
- Apellido materno
- RUT
- Contrasena

Al finalizar, muestra un resumen con los usuarios registrados.

## Caracteristicas

- Registro de una o mas cuentas.
- Validacion de campos vacios.
- Validacion de contrasena con minimo 6 caracteres.
- Validacion de RUT chileno con digito verificador.
- Control de RUT repetidos.
- Uso de funciones simples.
- Codigo escrito con contenidos basicos de Python.

## Contenidos usados

El programa utiliza conceptos iniciales de programacion:

- `print()`
- `input()`
- Variables
- Condicionales `if`, `elif`, `else`
- Ciclos `while`
- Funciones con `def`
- Listas simples
- Metodos basicos de texto como `.strip()`, `.upper()`, `.replace()` y `.isdigit()`

## Requisitos

Tener instalado Python 3.

Para verificar la instalacion:

```bash
python --version
```

## Como ejecutar el programa

Desde la terminal, entrar a la carpeta del proyecto:

```bash
cd ruta/del/proyecto
```

Luego ejecutar:

```bash
python registro_cuentas.py
```

## Ejemplo de uso

```text
Bienvenido al sistema de creacion de cuentas

Inicio de creacion de cuenta
Ingrese nombre: Diego
Ingrese apellido paterno: Toledo
Ingrese apellido materno: Soto
Ingrese RUT: 12345678-5
Ingrese contrasena: 123456

Cuenta creada correctamente.

Desea continuar ingresando otra cuenta? (si/no): no

Usuarios registrados:
1. Diego Toledo Soto - RUT: 12345678-5

Programa finalizado.
```

## Validaciones del programa

### Nombre y apellidos

No pueden quedar vacios ni contener solo espacios.

### RUT

El RUT:

- No puede estar vacio.
- No puede repetirse.
- Debe tener un digito verificador correcto.
- Puede ingresarse con o sin puntos.

Ejemplos aceptados:

```text
12345678-5
12.345.678-5
```

### Contrasena

La contrasena:

- No puede estar vacia.
- Debe tener al menos 6 caracteres.

### Continuar registro

El programa solo acepta:

```text
si
no
```

Si se ingresa otra respuesta, vuelve a preguntar.

## Estructura del proyecto

```text
Robotica/
|-- registro_cuentas.py
|-- README.md
`-- Informe_Final_Programacion_Python.docx
```

## Archivo principal

El archivo principal del proyecto es:

```text
registro_cuentas.py
```

Contiene todas las funciones necesarias para registrar usuarios, validar datos y mostrar el resumen final.

## Autor

Proyecto creado como parte de una evaluacion academica de programacion inicial en Python.
