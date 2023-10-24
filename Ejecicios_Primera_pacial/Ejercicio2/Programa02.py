#Ejercicio 2 Programa de la edad de una persona dando el año actual y el año de nacimiento

from guizero import App, Text, TextBox, PushButton

def calcular_edad():
    try:
        a_actual=int(name.value)
        a_nacimiento=int(name2.value)
        if a_actual and a_nacimiento > 0:
            if a_actual>a_nacimiento:
                edad=(a_actual-a_nacimiento)
                app.info(title="Resultado", text=f"La edad es: {edad}")
            else:
                app.error("Error","El año actual debe ser menor al año de nacimiento")
        else:
            app.error("Error","Los numeros deben ser positivos")
    except ValueError:
        app.error("Error","Ingresa datos correctos")

app = App(title="Calcular edad")
message = Text(app, text="Ingresa el año actual")
name = TextBox(app, width=20)
message2=Text (app, text="Ingresa el año de nacimiento")
name2 = TextBox(app, width=20)
calculate_button = PushButton(app, text="Calcular edad", command=calcular_edad)

app.display()
