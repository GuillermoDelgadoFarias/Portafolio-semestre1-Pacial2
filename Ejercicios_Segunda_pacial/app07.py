from guizero import App, Text, TextBox, PushButton

def generar_cuadrado():
    message_cuadrado.value=str(int(name.value)**2)
app= App(title="ICI app")
message = Text(app,text="Dame un numero")
name=TextBox(app, width=20)
message_cuadrado= Text(app, text="")
button=PushButton(app,text="Al cuadrado",command=generar_cuadrado)

app.display()