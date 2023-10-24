#Ejercicio 12 Obtenga la suma de 5 números capturados entre [5, 10]

from guizero import App, Text, TextBox, PushButton

contador=0
suma=0

def agregar_numero():
    try:
        global suma, contador
        numero=(dato.value)
        numero=int(numero)
        if numero>=5 and numero<=10:
            suma=suma+numero
            contador=contador+1
            dato.clear()
            if contador >4:
                app.info(title="Resultado de la suma", text=f"La suma de los 5 numeros es {suma}")
                exit()
        else:
            app.error("Error","Ingresa un numero en el rango [5,10]")
    except ValueError:
        app.error("Error","Ingresa números")

app = App(title="Suma de 5 numeros")
message = Text(app, text="Ingresa un numero que esté en el rango [5,10]")
dato = TextBox(app, width=20)
add_button = PushButton(app, text="Agregar numero", command=agregar_numero)


app.display()