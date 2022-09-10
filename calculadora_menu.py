# Calculadora con menu

from math import log

print("---------------------------")
print("----Calculadora-menu--------")

# input
bandera=False
x=float(input("Dame el valor del numero x: "))
y=float(input("Dame el valor del numero y: "))

print("\nDame la opcion que deseas realizar:\n")
#Se despliega el menu para selepcionar la opcion que deseas realizar:
print("1.sumar(el primero mas el segundo)")
print("2.restar(el primero menos el segundo)")
print("3.multiplicar(el primero por el segundo)")
print("4.dividir(el primero entre el segundo)")
print("5.Potencia(el primero a la potencia de el segundo)")
print("6. Logaritmo(logaritmo del primero )")
opcion=int(input("\nDame la opcion:"))

# processing
if(opcion==1):
    z=x +y
    print(x,"+",y)
elif(opcion== 2):
    z= x -y
    print(x,"-",y)
elif(opcion== 3):
    z= x * y
    print(x,"*",y)
elif(opcion== 4 and y!=0):
    z= x / y
    print(x,"/",y)
elif(opcion== 4 and y==0):
    print("El dominador es igual a cero y")
    print("No se puede realizar la divicion")
    bandera = True
elif(opcion== 5):
    z = pow(x,y)
    print(x, "^",y)
elif(opcion==6 and x>0):
    z= log(x)
    print("Logaritmo de" , x)
elif (opcion==6 and x<=0):
    print(" el  valor de x es menor o igual a cero y")
    print("No se puede calcular el logaritmo.")
    bandera= True
else:
    print("Opcion no valida")

# se escribe el logaritmo con otra condicion

if(opcion<7 and bandera ==False):
    print("Resultado:", z)








  

