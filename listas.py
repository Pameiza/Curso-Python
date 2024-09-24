nombres=["Diego","Gaspar","Pame","Agustin","Brisa","Cristian","Camila","Franco","Emanuel"]
ultimo_nombre = nombres[-1]
print (ultimo_nombre)

nombres[0] = "Diego"
print(nombres)

nombres = ["Diego","Gaspar","Pame","Agustin","Brisa","Cristian","Camila","Franco","Emanuel"]
print(len(nombres))

nombres.append("Juan")
print(nombres)

nombres.remove("Diego")
print(nombres)

nombres = ["Diego","Gaspar","Pame"]
nombre = "Pame"
if nombre in nombres:
    print(f"{nombre} esta en la lista-presente")
else:
    print(f"{nombre} no esta en la lista")

nombres = ["Diego","Gaspar","Pame","Agustin","Brisa","Cristian","Camila","Franco","Emanuel"]
nombres.sort()
print(nombres)
