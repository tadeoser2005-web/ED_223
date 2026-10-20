from collections import deque

def menu_cola():
    cola = deque(["carlos","carlo","sergi"])
    while True:
        print("\nMenu")
        print("1. insertar")
        print("2. borrar")
        print("3. listar")
        print("4. salir")
        op = int(input("Ingrese su opcion: "))
        if op == 1:
            cola.append(input("Ingrese el nombre: "))
        elif op == 2:
          if len(cola) > 0:
            print("salio:", cola.popleft())
          else:
            print("no existe")
        elif op == 3:
            if len(cola) > 0:
                print(cola)
            else:
                print("la cola esta vacia")
        elif op == 4:
            break
        else:
            print("opcion invalida")
while True:
    menu_cola()
