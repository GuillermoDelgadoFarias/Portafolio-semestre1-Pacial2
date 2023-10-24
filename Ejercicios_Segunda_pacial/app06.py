from guizero import App, Text, TextBox

app= App(title="ICI app")
message = Text(app,text="Dame tu nombre")
name=TextBox(app, width=20)

app.display()