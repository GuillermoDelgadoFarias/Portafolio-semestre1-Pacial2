#Ejercicio 15 Preguntar un número y determinar que día es

from guizero import App, Text, TextBox, PushButton

def dia():
    try:
        numero=(dato.value)
        numero=int(numero)
        if numero>0 and numero <8:
            match numero:
                case(1):
                    app.info(title="Día de la semana", text="Hoy es lunes")
                case(2):
                    app.info(title="Día de la semana", text="Hoy es martes")
                case(3):
                    app.info(title="Día de la semana", text="Hoy es miercoles")
                case(4):
                    app.info(title="Día de la semana", text="Hoy es jueves")
                case(5):
                    app.info(title="Día de la semana", text="Hoy es viernes")
                case(6):
                    app.info(title="Día de la semana", text="Hoy es sabado")
                case(7):
                    app.info(title="Día de la semana", text="Hoy es domingo")
        else:
            app.error("Error","Ingresa numero en el rango [1,7]")

    except ValueError:
        app.error("Error","Ingresa números")

app = App(title="Checar día de la semana")
message = Text(app, text="Ingresa un numero que esté en el rango [1,7]")
dato = TextBox(app, width=20)
add_button = PushButton(app, text="Ingresa numero de la semana", command=dia)


app.display()