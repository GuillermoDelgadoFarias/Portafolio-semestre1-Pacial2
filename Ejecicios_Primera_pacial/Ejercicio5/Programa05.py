#Ejercicio 5 obtener la edad promedio de n personas preguntando su año de nacimiento y asumiendo que el año actual es 2023

from guizero import App, Text, TextBox, PushButton
contador=0
edades=0

def agregar_a_nacimiento():
    try:
        global contador, edades
        a_nacimiento = name.value
        a_nacimiento=int(a_nacimiento)
        if a_nacimiento<2023 and a_nacimiento>0:
            a_nacimiento = float(a_nacimiento)
            edad=2023-a_nacimiento
            edades=edades+edad
            contador=contador+1
            name.clear()
        else:
            app.error("Error","El año de nacimiento debe ser menor a 2023 y tambien positivo")
    except ValueError:
        app.error("Error","Ingresa numeros")
def calcular_promedio():
    if contador>=2:
        resultado = edades/contador
        app.info(title="Resultado", text=f"El promedio de las edades es: {resultado}")
        exit()
    else:
        app.error("Error","No se ingresaron suficientes años (deben ser minimo dos)")

app = App(title="Promedio de edades de n personas")
message = Text(app, text="Ingresa los años de nacimiento de cada persona")
name = TextBox(app, width=20)
add_button = PushButton(app, text="Agregar año de nacimiento", command=agregar_a_nacimiento)
message1 = Text(app, text="Presiona para calcular los promedios de edades")
calculate_button = PushButton(app, text="Calcular promedio", command=calcular_promedio)

app.display()