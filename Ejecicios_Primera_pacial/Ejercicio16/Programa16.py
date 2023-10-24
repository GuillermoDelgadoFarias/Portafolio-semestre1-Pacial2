#Ejercicio 16 La tienda “brancos” debe vender productos a n alumnos, 
#ofrecen: tortas, tacos, hot dogs y pizza. Imprime los productos vendidos en total.

from guizero import App, Text, TextBox, PushButton

tortas=0
tacos=0
hotdogs=0
pizza=0
alumnos=0
def agregar_compra():
    try:
        global tortas, tacos, hotdogs, pizza, alumnos
        comida=(dato.value)
        comida=int(comida)
        if comida>0 and comida<5:
            match comida:
                case(1):
                    tortas +=1
                    alumnos +=1
                    dato.clear()
                    message3.value=alumnos
                case(2):
                    tacos +=1
                    alumnos +=1
                    dato.clear()
                    message3.value=alumnos
                case(3):
                    hotdogs +=1
                    alumnos +=1
                    dato.clear()
                    message3.value=alumnos
                case(4):
                    pizza +=1
                    alumnos +=1
                    dato.clear()
                    message3.value=alumnos
        else:
            app.error("Error","Ingresa numero en el rango [1,4]")
    except ValueError:
        app.error("Error","Ingresa números")

def resultados():
    app.info(title="Resultados de calculos",text=f"Las comidas vensidas fueron: {tortas} tortas, {tacos} tacos, {hotdogs} hotdogs, {pizza} pizzas")

app = App(title="Venta de 'broncos'")
message = Text(app, text="Dependiendo de la comida comprada ingresa un numero")
message2 = Text(app, text="1=Torta 2=Taco 3=Hotdog 4=Pizza")
dato = TextBox(app, width=20)
add_button = PushButton(app, text="Añadir venta", command=agregar_compra)
add_button1 = PushButton(app, text="Mostrar resultados de ventas", command=resultados)
message1 = Text(app, text="Los alumnos calculados han sido:")
message3 = Text(app, text=f"{alumnos}")
app.display()