#Ejercicio 3 Promedio de 2 números positivos leídos del teclado

from guizero import App, Text, TextBox, PushButton

def calcular_promedio():
    try:
        num1=int(name.value)
        num2=int(name2.value)
        if num1 and num2 > 0:
            promedio=(num1+num2)/2
            app.info(title="Resultado", text=f"El promedio es: {promedio}")
        else:
            app.error("Error","Los numeros deben ser positivos")
    except ValueError:
        app.error("Error","Ingresa numeros")

app = App(title="Promedio de dos numeros")
message = Text(app, text="Ingresa el primer número")
name = TextBox(app, width=20)
message2=Text (app, text="Ingresa el segundo número")
name2 = TextBox(app, width=20)
calculate_button = PushButton(app, text="Calcular promedio", command=calcular_promedio)

app.display()
