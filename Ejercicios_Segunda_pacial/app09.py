from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine = pyttsx3.init()

def mensaje_cuadrado():
    resultado=str(int(name.value)**2)
    cadena=f"El cuadrado de {name.value} es {resultado}"
    engine.say(cadena)
    engine.runAndWait()
#Mira bien hijo de tu putamadre no se te olvide ponerle los () a los "Cubos"
app= App(title="ICI app")
message = Text(app,text="Dame un numero")
name=TextBox(app, width=20)
button=PushButton(app,text="Calcular al cuadrado",command=mensaje_cuadrado)

app.display()