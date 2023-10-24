#Ejercicio 7 Algoritmo para calcular el cuadrado de un número positivo

from guizero import App, Text, TextBox, PushButton

Alumnos_aprovados=0

def calcualar_al_cuadrado():
    try:
        numero = dato.value
        numero = float(numero)
        if numero>0:
            numero=(numero*numero)
            app.info(title="Resultado", text=f"El numero al cuadrado es: {numero}")
        else:
            app.error("Error", "El numero ingresado debe ser positivo")
    except ValueError:
        app.error("Error", "Ingresa números")

app = App(title="Calcular número al cuadrado")
message = Text(app, text="Ingresa numero y presiona 'Calcular al cuadrado'")
dato = TextBox(app, width=20)
add_button = PushButton(app, text="Calcular al cuadrado", command=calcualar_al_cuadrado)

app.display()