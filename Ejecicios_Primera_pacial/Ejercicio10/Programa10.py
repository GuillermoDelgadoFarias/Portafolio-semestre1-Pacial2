#Ejercicio 10 capture n números enteros positivos, obtenga la suma del cuadrado de los pares y el cubo de los impares

from guizero import App, Text, TextBox, PushButton
suma_cuadrado=0
suma_cubo=0

def agregar_numero():
    try:
        global suma_cuadrado, suma_cubo
        numero=(dato.value)
        numero=float(numero)
        if numero%2==0:
            suma_cuadrado=suma_cuadrado+(numero*numero)
            app.info(title="Resultado de cuadrado", text=f"El cuadrado del numero es: {numero*numero}")
            dato.clear()
        else:
            suma_cubo=suma_cubo+(numero*numero*numero)
            app.info(title="Resultado de cubo", text=f"El cubo del numero es: {numero*numero*numero}")
            dato.clear()
    except ValueError:
        app.error("Error", "Ingresa números")

def sacar_suma():
    app.info(title="Resultado de suma", text=f"La suma del cuadrado de los numeros pares es {suma_cuadrado} y la de los impares es {suma_cubo}")


app = App(title="Cuadrado de numeros pares y cubo de numeros impares")
message = Text(app, text="Ingresa numero para sacar su cuadrado o cubo")
message1= Text(app, text="Si el numero es par sacará el cuadrado, si es impar sacará el cubo")
dato = TextBox(app, width=20)
add_button = PushButton(app, text="Sacar y agregar numero", command=agregar_numero)
message2=Text(app, text="Cuando ya sean todos los numeros presione 'Sacar suma de resultados'")
add_button2 = PushButton(app, text="Sacar suma de resultados", command=sacar_suma)

app.display()