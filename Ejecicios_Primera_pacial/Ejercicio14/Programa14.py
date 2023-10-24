#Ejercicio 14 Genere una secuencia de n números los cuales sean 01010101010

from guizero import App, Text, TextBox, PushButton

num=0
secuencia=[]

def generar_numero():
    global num
    if num == 0:
        secuencia.append(num)
        app.info(title="Número", text=f"{secuencia}")
        num=1

    else:
        secuencia.append(num)
        app.info(title="Número", text=f"{secuencia}")
        num=0

app = App(title="Secuencia 0 y 1")
message = Text(app, text="Presione boton para generar un numero en la secunecia 01")
add_button = PushButton(app, text="Generar numero numero", command=generar_numero)


app.display()