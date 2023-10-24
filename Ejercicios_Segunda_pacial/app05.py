from guizero import App, Text, PushButton

def change_message():
    message.value="Coman polla gilipollas"
app= App(title="ICI app")
message = Text(app,text="Hola buenos dias")
button=PushButton (app,text="Presioname w",command=change_message)

app.display()