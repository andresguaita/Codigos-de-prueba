def insercion(arr):
  
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
       #Mueve los elementos de arr [0..i-1], que son mayores que la "key",
       #a una posición por delante de su posición actual
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr
  
  
# Recorre todo el vector y lo imprime
arr = [12, 11, 13, 5, 6]
print(arr)
insercion(arr)
print (arr)
  
