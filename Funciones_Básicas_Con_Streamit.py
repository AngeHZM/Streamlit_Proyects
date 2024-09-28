import streamlit as st

# Función 1: Saludo simple (nombre)
def saludar(nombre):
    return f"Hola, {nombre}! Mucho Gusto, Bienvenido ദ്ദി ˉ͈̀꒳ˉ͈́ )"

# Función 2: Suma de dos números ( a y b )
def sumar(a, b):
    return a + b

# Función 3: Área de un triángulo, Formula: (base x altura / 2)
def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

# Función 4: Calculadora de descuento (primero calcular el descuento, despues el IVA)
def calcular_precio_final(precio, descuento = 5, impuesto = 16):
    precio_descuento = precio * ( 1 - descuento / 100)
    precio_final = precio_descuento * ( 1 + impuesto / 100)
    return precio_final

# Función 5: Suma de una lista
def sumar_lista(lista):
    return sum(lista)

# Función 6: Producto con valores
def producto(nombre, cantidad = 1, precio = 10):
    return f"Producto: {nombre}, ٩(ˊᗜˋ*)و El Total a pagar es: {cantidad * precio}"

# Función 7: Números pares e impares (en lista)
def numeros_pares_e_impares(lista):
    pares = [num for num in lista if num % 2 == 0] #(terneario 1)
    impares = [num for num in lista if num % 2 != 0] #(terneario 2)
    return pares, impares

# Función 8: Multiplicar todos con *args
def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado if args else 1

# Función 9: Información personal con **kwargs
def informacion_personal(**kwargs):
    return kwargs

# Función 10: Calculadora flexible
def calculadora_flexible(a, b, operacion='suma'):
    operaciones = {
        'suma': a + b,
        'resta': a - b,
        'multiplicación': a * b,
        'división': a / b if b != 0 else 'Error: División por cero'
    }
    return operaciones.get(operacion, 'Operación no válida')

# Titulo de Web:
st.title("_Funciones En Streamlit_  :blue[by Ángel] :star:")

# Usar la barra lateral para elegir alguna de las opciones
opcion = st.sidebar.selectbox('✿ _Selecciona un ejercicio_ ✿ :', [
    'Saludo simple', 'Suma de dos números', 'Área de un triángulo', 
    'Calculadora de descuento', 'Suma de una lista', 
    'Producto con valores predeterminados', 'Números pares e impares',
    'Multiplicar todos con *args', 'Información personal con **kwargs', 
    'Calculadora flexible'
])

#  Saludo simple
if opcion == 'Saludo simple':
    nombre = st.text_input("Ingresa tu nombre")
    if nombre:
        st.write(saludar(nombre))

#  Suma de dos números
elif opcion == 'Suma de dos números':
    a = st.number_input("Número 1", value=0)
    b = st.number_input("Número 2", value=0)
    if st.button("Sumar"):
        st.write("Resultado:", sumar(a, b))

# Área de un triángulo
elif opcion == 'Área de un triángulo':
    base = st.number_input("Base", value=0.0)
    altura = st.number_input("Altura", value=0.0)
    if st.button("Calcular área"):
        st.write("Área del triángulo:", calcular_area_triangulo(base, altura))

# Calculadora de descuento
elif opcion == 'Calculadora de descuento':
    precio = st.number_input("Precio", value=0.0)
    descuento = st.number_input("Descuento (%)", value=10.0)
    impuesto = st.number_input("Impuesto (%)", value=16.0)
    if st.button("Calcular precio final"):
        st.write("Precio final:", calcular_precio_final(precio, descuento, impuesto))

# Suma de una lista
elif opcion == 'Suma de una lista':
    lista = st.text_input("Ingresa los números separados por comas")
    if lista:
        numeros = list(map(int, lista.split(',')))
        st.write("Suma de la lista:", sumar_lista(numeros))

# Producto con valores predeterminados
elif opcion == 'Producto con valores predeterminados':
    nombre = st.text_input("Nombre del producto", value="Producto X")
    cantidad = st.number_input("Cantidad", value=1)
    precio = st.number_input("Precio por unidad", value=10.0)
    if st.button("Calcular total"):
        st.write(producto(nombre, cantidad, precio))

# Números pares, impares
elif opcion == 'Números pares e impares':
    lista = st.text_input("Ingresa los números separados por comas")
    if lista:
        numeros = list(map(int, lista.split(',')))
        pares, impares = numeros_pares_e_impares(numeros)
        st.write("Pares:", pares)
        st.write("Impares:", impares)

# Multiplicar con *args
elif opcion == 'Multiplicar todos con *args':
    lista = st.text_input("Ingresa los números separados por comas")
    if lista:
        numeros = list(map(int, lista.split(',')))
        st.write("Resultado de la multiplicación:", multiplicar_todos(*numeros))

# Información personal con **kwargs
elif opcion == 'Información personal con **kwargs':
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", value=0)
    direccion = st.text_input("Dirección")
    if st.button("Mostrar información"):
        info = informacion_personal(nombre=nombre, edad=edad, direccion=direccion) #Diccionario
        for clave, valor in info.items():
            st.write(f"{clave}: {valor}")

# Calculadora flexible
elif opcion == 'Calculadora flexible':
    a = st.number_input("Número 1", value=0)
    b = st.number_input("Número 2", value=0)
    operacion = st.selectbox("Operación", ['suma', 'resta', 'multiplicación', 'división'])
    if st.button("Calcular"):
        st.write("Resultado:", calculadora_flexible(a, b, operacion))
