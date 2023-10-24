#Ejercicio 17 Crea el dfd del menú de una calculadora funcional que pueda sumar, restar, multiplicar 
#y dividir al seleccionar el tipo de operación y dar dos números

from guizero import App, Text, TextBox, PushButton

contador=0
numeros=[]
def dos_numeros():
    try:
        global contador
        numero=dato.value
        numero=int(numero)
        if contador<2:
            contador +=1
            numeros.append(numero)
            dato.clear()
        else:
            app.info(title="Dos números",text=f"Ya se han ingresado dos números")
    except ValueError:
        app.error("Error","Ingresa números")

def operacion():
    try:
        operacion=dato1.value
        operacion=int(operacion)
        if operacion>0 and operacion<5:
            match operacion:
                case(1):
                    resultado = numeros[0]+ numeros[1]
                case(2):
                    resultado = numeros[0] - numeros[1]
                case(3):
                    resultado = (numeros[0] * numeros[1])
                case(4):
                    resultado = (numeros[0] / numeros[1])
        else:
            app.error("Error","Ingresa un numero valido para la operación")
            exit()
        app.info(title="Resultado",text=f"El resultado de la operación es {resultado}")
        exit()
    except ValueError:
        app.error("Error","Ingresa números")


app = App(title="Calculadora de dos numeros")
message = Text(app, text="Ingresa dos numeros para calcularlos")
dato = TextBox(app, width=20)
add_button = PushButton(app, text="Añadir numero", command=dos_numeros)
message1 = Text(app, text="Ingresa un numero para hacer una operación")
message2 = Text(app, text=f"1=Suma 2=Resta 3=Multiplicación 4=División")
dato1 = TextBox(app, width=20)
add_button1 = PushButton(app, text="Hacer operación", command=operacion)


app.display()