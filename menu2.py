def menu_pila():
    pila = ["carlos", "carlo", "sergi"]
    while True:
        print("\nMenu")
        print("1. insertar")
        print("2. borrar")
        print("3. listar")
        print("4. salir")
        op = int(input("Ingrese su opcion: "))
        if op == 1:
            pila.append(input("Ingrese el nombre: "))
        elif op == 2:
            if len(pila) > 0:
                print("salio:", pila.pop(0))
            else:
                print("no existe")
        elif op == 3:
            if len(pila) > 0:
                print(pila)
            else:
                print("la pila esta vacia")
        elif op == 4:
            break
        else:
            print("opcion invalida")


while True:
    menu_pila()
