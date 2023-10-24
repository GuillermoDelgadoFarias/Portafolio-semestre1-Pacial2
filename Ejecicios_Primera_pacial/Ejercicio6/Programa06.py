#Ejercicio 6 Pedir calificacion e imprimir cuantos aprobaron. la calificacion aprovatoria es 7
from guizero import App, Text, TextBox, PushButton

Alumnos_aprovados=0

def agregar_calificacion():
    try:
        global Alumnos_aprovados
        calificacion = calf.value
        calificacion = float(calificacion)
        if calificacion>=0 and calificacion<=10:
            if calificacion>=7:
                Alumnos_aprovados=Alumnos_aprovados+1
                calf.clear()
            else:
                calf.clear()
        else:
            app.error("Error", "La calificacion debe ser en el rango [0,10]")
    except ValueError:
         app.error("Error", "Ingresa números")
def Checar_aprovados():
        app.info(title="Resultado", text=f"Los alumnos aprovados fueron: {Alumnos_aprovados}")

app = App(title="Calificacion de alumnos")
message = Text(app, text="Ingresa calificaciones y presiona 'Checar calificacion'")
calf = TextBox(app, width=20)
add_button = PushButton(app, text="Agregar calificación", command=agregar_calificacion)
calculate_button = PushButton(app, text="Checar calificaciones", command=Checar_aprovados)

app.display()