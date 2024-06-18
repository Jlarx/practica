pedidos=[]

def Registrate():
    nombre=input("Ingrese nombre y apellido: ")
    try:
        cli_5kg=int(input("Cant. de 5kg: "))
    except ValueError:
        print("Ingrese numeros ")
        return
    pedido={
        "cliente":nombre,
        "cli_5kg":cli_5kg
    }
    pedidos.append(pedido)
    with open ("yepaaaa.txt", "a") as file:
        file.write(f"{nombre},{cli_5kg}\n")
        print("Pedido registrado con exito")

def listar():
    try:
        with open("yepaaaa.txt","r") as file:
            lines=file.readlines()
            if not lines:
                print("No hay pedidos registrados")
                return
            for i, line in enumerate(lines,start=1):
                nombre,cli_5kg=line.strip().split(",")
                print(f"pedido {i}")
                print(f"nombre {nombre}")
                print(f"cli_5kg: {cli_5kg}")
    except FileNotFoundError:
        print("No hay pedidos registrados")

def Rutas():
    sectores=["la granja", "san bernardo"]
    print("sectores disponibles")
    for i,sector in enumerate(sectores,start=1):
        print(f"{i}.{sector}")
    try:
        opc=int(input("seleccione numero del sector"))
        if opc<1 or opc>len(sectores):
            print("opcion no registrado")
            return
    except ValueError:
        print("ingrese un numero")
        return
    sector_seleccionado=sectores[opc-1]

    try:
        with open("yepaaaa.txt","r")as file:
            lines=file.readlines()
            pedido_filtrado=[line for line in lines if line.strip().split(",")[2]==sector_seleccionado]
            if not pedido_filtrado:
                print(f"no hay pedido en {sector_seleccionado}")
                return
            
            with open(f"hoja_ruta_{sector_seleccionado}.txt","w")as ruta_file:
                for pedido in pedido_filtrado:
                    ruta_file.write(pedido)
            print(f" hoja ruta {sector_seleccionado} impresa")
    except FileNotFoundError:
        print("pedido no registrado")    


def salir():
    print("Muchas gracias por usar nuestro programa :) ")

def menu():
    while True:
        print("1) Registrar Pedidos")
        print("2) Listar Pedidos")
        print("3) Rutas Disponibles")
        print("4) Salir")
        try:
            opc=int(input("Ingrese un numero del 1-4\n"))
            if opc==1:
                Registrate()
            elif opc==2:
                listar()
            elif opc==3:
                Rutas()
            elif opc==4:
                salir()
        except ValueError:
            print("Ingrese un numero del 1-4\n")
menu()