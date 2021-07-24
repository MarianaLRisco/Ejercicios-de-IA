arr = [[11, 10, 13],[9, 0, 16],[17, 15, 30]]

i= 0
for lista in arr:
    if(0 in lista):
        j = lista.index(0)
        pos_hueco = arr[i][j]
    i+=1
print(pos_hueco)

accs=list()
if pos_hueco not in (arr[0][0],arr[0][1],arr[0][2]):
   accs.append("Mover hueco arriba")
if pos_hueco not in (arr[0][0],arr[1][0],arr[2][0]): 
   accs.append("Mover hueco izquierda")
if pos_hueco not in (arr[2][0],arr[2][1],arr[2][2]): 
   accs.append("Mover hueco abajo")
if pos_hueco not in (arr[0][2],arr[1][2],arr[2][2]):
   accs.append("Mover hueco derecha")   

print(accs)