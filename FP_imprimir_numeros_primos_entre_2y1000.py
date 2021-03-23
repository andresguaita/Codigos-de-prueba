#Imprimir todos los números primos entre 2 y 1.000
#inclusive.

print("Los numeros primos entre 2 y 1000 son : \n",)

for num in range(2, 1000 + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
