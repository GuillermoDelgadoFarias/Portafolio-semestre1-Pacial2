#Ejercicio 8 obtenga la suma del cuadrado de todos los números pares entre 0 y 20 consecutivos

from guizero import App, Text, TextBox, PushButton

num=2
resultado=0

def calcualar_al_cuadrado():
    global num, resultado
    if num<22:
        resultado=num*num
        num=num+2
        app.info(title="Resultado", text=f"El numero al cuadrado es: {resultado}")
        message1.value=num
    else:
        app.info(title="Fin del programa", text=f"El programa ha terminado")
    
        
app = App(title="Sacar cuadrado de número al cuadrado hasta el 20")
message = Text(app, text=f"El numero actual es:")
message1= Text(app, text=f"{num}")
message2 = Text(app, text="Presiona 'Calcular al cuadrado'")
add_button = PushButton(app, text="Calcular al cuadrado", command=calcualar_al_cuadrado)

app.display()