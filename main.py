from flask import Flask

app = Flask(__name__)

# CALCULADORA en FLASK:

@app.route("/suma")
def sumar():
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un numero: "))
    suma = a+b
    return f"<h1><center> La suma de {a} + {b} es: {suma} </center></h1>"

@app.route("/resta")
def restar():
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un numero: "))
    resta = a-b
    return f"<h1><center> La resta de {a} - {b} es: {resta} </center></h1>"

@app.route("/multiplicar")
def multiplicacion():
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un numero: "))
    mult = a*b
    return f"<h1><center> La multiplicación de {a} x {b} es: {mult} </center></h1>"

@app.route("/division")
def dividir():
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un numero: "))
    division = a//b
    return f"<h1><center> La división de {a} / {b} es: {division} </center></h1>"
    
app.run(host='localhost', port=3000, debug=True)
