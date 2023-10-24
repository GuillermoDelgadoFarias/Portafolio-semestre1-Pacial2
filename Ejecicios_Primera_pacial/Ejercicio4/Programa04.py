#Ejercicio 4 Promedio de n números positivos leídos del teclado

from guizero import App, Text, TextBox, PushButton

con=0
suma=0

def agregar_numero():
    try:
        global con, suma
        numero = name.value
        numero = float(numero)
        if numero>0:
            num=int(name.value)
            suma=suma+num
            con=con+1
            name.clear()
        else:
            app.error("Error", "El numero ingresado debe ser positivo")
    except ValueError:
        app.error("Error", "Ingresa numeros")
        suma=0
        con=0
def calcular_promedio():
    if suma>=2:
        resultado = suma/con
        app.info(title="Resultado", text=f"El promedio es: {resultado}")
    else:
        app.info("Resultado", "No se ingresaron números")

app = App(title="Suma de Números")
message = Text(app, text="Ingresa números para sumarlos")
name = TextBox(app, width=20)
add_button = PushButton(app, text="Agregar Número", command=agregar_numero)
message1 = Text(app, text="Presiona para sacar promedio de los números sumados")
calculate_button = PushButton(app, text="Calcular promedio", command=calcular_promedio)

app.display()
