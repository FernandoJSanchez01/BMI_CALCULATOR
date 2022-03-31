with open ("poemas.txt","w") as archivo:
     archivo.write("Fernando estuvo aqui")


with open("poemas.txt", "r") as value:
     for i in value:
          print("==Esto fue lo que se escribio")
          print(i)