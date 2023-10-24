#Ejercicio 1. Saca el promedio de tres números.

from guizero import App, Text, TextBox, PushButton
n1=8
n2=6
n3=10
def sumar():
    suma=(n1+n2+n3)
    app.info(title="Resultado", text=f"La suma es: {suma}")
    exit()
app = App(title="Suma de tres números")
message = Text(app, text="Los tres números a sumar son 8, 6, 10")
add_button = PushButton(app, text="Sumar los números", command=sumar)
app.display()