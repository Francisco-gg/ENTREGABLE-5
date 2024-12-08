
print("=== Bienvenido al programa interactivo de Python ===")

numero_entero = 10        
numero_flotante = 3.14    
cadena = "¡Hola, usuario!"  

suma = numero_entero + numero_flotante
multiplicacion = numero_entero * numero_flotante

print("\nOperaciones Matemáticas:")
print(f"La suma de {numero_entero} y {numero_flotante} es: {suma}")
print(f"La multiplicación de {numero_entero} y {numero_flotante} es: {multiplicacion}")

nombre = input("\n¿Cómo te llamas? ")  
mensaje_personalizado = cadena + " Me alegra conocerte, " + nombre + "!"

print(mensaje_personalizado)

print("\nVamos a realizar una operación con números que tú elijas:")
print("Que operacion quieres realizar: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
odd = int(input("Elije una opcion: "))

match odd:
    case 1:
        print("Ingrese dos numeros porfavor")

        x = int(input("Primer numero: "))
        y = int(input("Segundo numero: "))

        resultado = x + y

        print(f"El resultado de la operacion {x}+{y} es: {resultado}")
    case 2:
        print("Ingrese dos numeros porfavor")

        x = int(input("Primer numero: "))
        y = int(input("Segundo numero: "))

        resultado = x - y

        print(f"El resultado de la operacion {x}-{y} es: {resultado}")
    case 3:
        print("Ingrese dos numeros porfavor")

        x = int(input("Primer numero: "))
        y = int(input("Segundo numero: "))

        resultado = x * y

        print(f"El resultado de la operacion {x}x{y} es: {resultado}")
    case 4:
        print("Ingrese dos numeros porfavor")

        x = int(input("Primer numero: "))
        y = int(input("Segundo numero: "))

        while x==0 or y==0:
            print("Ambos numeros deben diferir de cero")
            print("Ingrese los numeros nuevamente")
            x = int(input("Primer numero: "))
            y = int(input("Segundo numero: "))

        resultado = x / y

        print(f"El resultado de la operacion {x}/{y} es: {resultado}")

print("Adivine el numero")

numero_mio= int(input("Ingrese un nuemero: "))
numero_adivinar=50

while numero_mio!=numero_adivinar:
    print("Te equivocaste")
    if numero_mio<numero_adivinar:
        print("Su numero es menor")
        numero_mio= int(input("Ingrese un numero: ")) 
    elif numero_mio>numero_adivinar:
        print("Su numero es mayor")   
        numero_mio= int(input("Ingrese un numero: ")) 


print("Ahora, ingresa un número, y te diré si es par o impar\n")

numero_par_impar=int(input("Ingresa el numero: "))

if numero_par_impar%2==0:
    print("El numero es par\n")
else:
    print("El numero es impar\n")
    
lista_numeros = [2,4,6,8,10]

print("A continuación, los cuadrados correspondientes a los números de una lista\n")

for numero in lista_numeros:
    cuadrado = numero*numero
    print(f"El cuadrado de {numero} es: {cuadrado}")

print("\nAhora va a ingresar una seria de datos")
print("\nHasta que cumpla con una condicion")

meta=0

while meta!=3:
    name=input("Ingrese un nombre: ")
    l_name=input("Ingrese un apellido: ")
    meta=meta+1

print("Le presentaré una serie de personas que quizá conozca")
print("Como en facebook :V")

lista_personas={"Luisardo", "Maria", "Gerardo"}

for persona in lista_personas:
    x=1
    print(f"Persona {x}: {persona}")
    x=x+1

mi_lista=[];

print("Tiene una lista a su disposicion")
print("Proceda a llenarla del siguiente modo: ")
print("Elemento, elemento, elemento...")

elemento=input("Ingrese aqui los elementos: ")

mi_lista=elemento.split(",")

print("Su lista: ", mi_lista)


