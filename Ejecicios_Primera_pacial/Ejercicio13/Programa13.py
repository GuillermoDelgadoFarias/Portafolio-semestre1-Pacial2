#Ejercicio 13 Una empresa desea calcular el sueldo total de una persona bajo los
#siguientes rubros: sueldo base, 5% canasta básica, 3% prima de antigüedad y deducciones 
#si el salario base excede los 10000 30% y menos de ese 20% indique cual es el total de la 
#nómina a pagar y cuantos son los impuestos que el jefes debe pagar al SAT

from guizero import App, Text, TextBox, PushButton

impuestos=0
salarios=0
empleados=0
imp=0
pr=0
def sacar_edad():
    try:
        global imp, impuestos, salarios, pr, empleados
        salario_base=(dato.value)
        salario_base=int(salario_base)
        if salario_base>0:
            if salario_base>9999:
                imp=salario_base*0.30
            else:
                imp=salario_base*0.20
            impuestos=impuestos+imp
            pr=(salario_base*0.05)+(salario_base*0.03)
            salarios=salarios+salario_base+pr-imp
            empleados=empleados+1
            message2.value=empleados
            dato.clear()
        else:
            app.error("Error","El salario ingresado debe ser positivo")
    except ValueError:
        app.error("Error","Ingresa números")

def resultados():
    app.info(title="Resultados de calculos",text=f"Los impuestos a pagar son {impuestos} y los salarios {salarios}")

app = App(title="Sacar pagos de impuestos y salarios")
message = Text(app, text="Ingresa el salario base de un empleado")
dato = TextBox(app, width=20)
add_button = PushButton(app, text="Añadir salario base", command=sacar_edad)
add_button1 = PushButton(app, text="Calcular salarios e impuestos a pagar", command=resultados)
message1 = Text(app, text="Los empleados calculados hasta el momento son:")
message2 = Text(app, text=f"{empleados}")


app.display()