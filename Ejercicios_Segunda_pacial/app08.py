from guizero import App, Text, TextBox, PushButton

def generar_cuadrado():
    resultado=str(int(name.value)**2)
    app.info(title="Resultado",text=resultado)
app= App(title="ICI app")
message = Text(app,text="Dame un numero")
name=TextBox(app, width=20)
button=PushButton(app,text="Al cuadrado",command=generar_cuadrado)

app.display()