#Ejercicio 11 Programa que dado el año de nacimiento indique cuantos años va a cumplir una persona el siguiente año

from guizero import App, Text, TextBox, PushButton

def sacar_edad():
    try:
        numero=(dato.value)
        numero=int(numero)
        if numero>0 and numero<2023:
            numero=2024-numero
            app.info(title="Año a cumplir",text=f"Los años que vas acomplir el siguiente año son {numero}")
        else:
            app.error("Error","El año de nacimiento debe ser un numero positivo menor que 2023")
    except ValueError:
        app.error("Error", "Ingresa números")

app = App(title="Año que cumplirás")
message = Text(app, text="Ingresa tu año de nacimiento")
dato = TextBox(app, width=20)
add_button = PushButton(app, text="Sacar años a cumplir", command=sacar_edad)


app.display()