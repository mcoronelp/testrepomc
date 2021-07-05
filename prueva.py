character_name = "Ana"
character_age = "70"
print("There once was a man named " + character_name + ", ")
print("he was 70 years old. ")
print("que tal " + character_name + ", ")
print("but didn't like being 70.")
print("Habia una mujer de nombre " + character_name + ", ")

phrase = "Giraffe Academy"
print(phrase.replace("Giraffe","Manuel"))
print(10 % 10)

print(3+1)
print(round(4.4))

print(0.0000000000000000000001)

print(True > False)
print(False > True)
character_number = 4
character_number2 = 4

print({character_number + character_number2})
print((2 * 3) + 5)
print(3 * 5 + 2)
print(9 % 6 % 2)
print(2 * 3 % 5)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

print(16.99 + 2.9 + 7.9)

saludo = "holi"
cliente = "maria"
mensaje = "tu saldo es de"
monto = "245 US$"
print(saludo, cliente, mensaje, monto)

x = float(-1)
y = (3 * (x % 3)) + (- 2 * (x % 2)) + 3 * x - (1)

# escribe tu código aquí.
print("y =", float(y))

a = "1"
b = '2'

print(a + b)

a = 10
b = 10
a /= 2 * b
print(a)

a = 2
b = 3
a += 1 + b
print(a)

var = 9
var += 1
print(var)

# HOLA QUE TAL COMO ESTAN, ESTA ES UNA PRUEBA PARA INSERTAR UN COMENTARIO.


#cateto_a = float(input("Ingresa la longitud del primer cateto: "))
#cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
#print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))

#nombre = input("ingresa tu nombre: ")
#apellido = input("ingresa tu apellido: ")
#print("tu nombre completo es: " + nombre, apellido)

#var_a = float(input("ingresa valor para a: "))
#var_b = float(input("ingresa valor para b: "))
#x = float(input("ingresa x: "))
#print("la regresion lineal es: ", "y =" + str(var_a + var_b * x))


#hora = int(input("Hora de inicio (horas): "))
#min = int(input("Minuto de inicio (minutos): "))
#dura = int(input("Duración del evento (minutos): "))
#dif_min = 60 - min
#min_sig = dura - dif_min
#dif_hora = int((min + dif_min)/60)
#print(hora + dif_hora, ":", min_sig)

#hora = int(input("Hora de inicio (horas): "))
#min = int(input("Minuto de inicio (minutos): "))
#dura = int(input("Duración del evento (minutos): "))
#var_min1 = 60 - min
#var_hora1 = (min + var_min1)/60
#var_minf = (dura % 60) - var_min1
#var_horaf = int(dura/60) + var_hora1
#var_hfinal = int(24 - hora + var_horaf)
#print(var_hfinal,":",var_minf)

#var_1 = round((hora % 24) + (dura // 60))
#var_2 = dura % 60 - (60 - min)
#print(var_1,":",var_2)

#MODULO 3

#print( 1 == 2)

#SELECT type, SUM(calories)
#AS total_calories
#FROM exercise_logs
#GROUP BY type;

#SELECT author, AVG(words)
#AS total_words
#FROM books
#GROUP BY author
#HAVING total_words > 150000

#n = int(input("ingrese un numero: "))
#print(str(n >= 100))

#j = int(input("ingresa un numero mayor a 10: "))
#if j > 10:
   # print(j>10)
#else :
    #print("vuelve a introducir un número mayor a 10.")

# lee tres números
#numero1 = int(input("Ingresa el primer número:"))
#numero2 = int(input("Ingresa el segundo número:"))
#numero3 = int(input("Ingresa el tercer número:"))

# verifica cuál de los números es el mayor
# y pásalo a la variable de mayor número

#numeroMayor = max(numero1,numero2,numero3)

# imprimir el resultado
#print("El número más grande es:", numeroMayor)

#var1 = input("ingresa nombre de planta: ")

#if var1 == "Espatifilo":
 #   print("Sí, ¡El " + var1 + " es la mejor planta de todos los tiempos!")
#elif var1 == "espatifilo":
 #   print("No, ¡quiero un gran Espatifilo!")
#else:
 #   print("¡Espatifilo! !No " + var1 + "!")


ingreso = float(input("Ingrese el ingreso anual: "))
impuesto1 = round(float((ingreso * 0.18) - 556.20),0)
impuesto2 = round(float(14839.2 + ((ingreso - 85528) * 0.32)),0)
#si el impuesto resulta negativo debe salir 0.0

if ingreso > 85528:
        impuesto = impuesto2
else:
    if impuesto1 < 0:
        impuesto = float(0.0)
    else:
        impuesto = impuesto1

print("El impuesto es: ", impuesto, "pesos")

#Ejercicio 2 años bisiestos / años comunes

año = int(input("Introduzca un año: "))

if año <= 1582:
    print("No está dentro del periodo gregoriano.")
elif (año%4)>0:
    print("Año común.")
elif (año%100)>0:
    print("Año bisiesto.")
elif (año%400)>0:
    print("Año común.")
else:
    print("Año bisiesto.")


# Almacenaremos el número más grande actual aquí
numeroMayor = -999999999
# Ingresa el primer valor
numero = int(input ("Introduzca un número o escriba -1 para detener:"))
# Si el número no es igual a -1, continuaremos
while numero != -1:
    # ¿Es el número más grande que el número más grande?
    if numero > numeroMayor:
        # Sí si, actualiza el mayor númeroNúmero
        numeroMayor = numero
    # Ingresa el siguiente número
    numero = int (input("Introduce un número o escribe -1 para detener:"))
# Imprimir el número más grande
print("El número más grande es:", numeroMayor)

numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero = int(input("ingrese un numero: "))
while numero != numeroSecreto:
    print("jaja estas atrapado en mi ciclo")
    numero = int(input("ingrese un numero: "))

numero == numeroSecreto
print("Bien hecho, muggle. Eres libre ahora")

for i in range(3, 10, 4):
    print("El valor de i es actualmente", i)

pow = 1
for exp in range(16):
    print ("2 a la potencia de", exp, "es", pow)
    pow *= 2

#INGRESAR UNA CANTIDAD DE HORAS Y QUE ARROJE LA HORA SIGUIENTE

H = int(input("ingresar hora: ")) #horas de 0 a 23
M = int(input("ingresar minutos: ")) #minutos de 0 a 59
TT = int(input("ingresar tiempo transurrido: ")) #tiempo que estuvieron en reunion

min = (M + TT)%60
hor = (((H*60) + (M + TT))//60)%24

print(hor,min,sep=":")

