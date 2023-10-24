#Ejercicio 9 obtenga la suma de todos los cuadrados de n números capturados del teclado

from guizero import App, Text, TextBox, PushButton

suma=0

def agregar_numero():
    try:
        global suma
        numero=(dato.value)
        numero=float(numero)
        if numero>0:
            suma=suma+(numero*numero)
            dato.clear()
        else:
            app.error("Error","El numero ingresado debe ser positivo")
    except ValueError:
        app.error("Error", "Ingresa número")

def sacar_suma():
    app.info(title="Resultado de suma", text=f"La suma del cuadrado de los numeros {suma}")


app = App(title="Suma de números al cuadrado")
message = Text(app, text="Ingresa numero y presiona 'Agregar numero'")
dato = TextBox(app, width=20)
add_button = PushButton(app, text="Agregar número", command=agregar_numero)
message2=Text(app, text="Cuando ya sean todos los numeros presione 'Sacar suma de cuadrados'")
add_button2 = PushButton(app, text="Sacar suma de cuadrados", command=sacar_suma)

app.display()