#estructura de un nodo
class Nodo:
    def __init__(self,numero):
        #valor q tendra el nodo
        self.numero = numero
        #apunta al siguiente nodo
        self.siguiente = None

        #clase q va a administrar todos los nodos
class ListasEnlazadas:
      def __init__(self):
          self.cabeza = None
      def Insertar_Nodo_al_Inicio(self,numero):
              nuevo_nodo = Nodo(numero)
              if(self.cabeza == None):
                  self.cabeza = Nodo(numero)
                  return
              nuevo_nodo.siguiente = self.cabeza

              self.cabeza = nuevo_nodo

      def Insertar_Nodo_al_Final(self,numero):
          nuevo_nodo = Nodo(numero)
          if(self.cabeza == None):
              self.cabeza = Nodo(numero)
              return
          actual = self.cabeza
          while(actual.siguiente):
              actual = actual.siguiente

          actual.siguiente = nuevo_nodo

      def Eliminar_Nodo_al_Inicio(self):
          #si la lista esta vacia no hay nada q eliminar
          if(self.cabeza == None):
              print("La lista esta vacia")
              return
          #la cabeza pasa a ser el segundo nodo
          self.cabeza = self.cabeza.siguiente

      def Eliminar_Nodo_al_Final(self):
          #si la lista esta vacia no hay nada q eliminar
          if(self.cabeza == None):
              print("La lista esta vacia")
              return
          #si solo hay un nodo, la lista queda vacia
          if(self.cabeza.siguiente == None):
              self.cabeza = None
              return
          actual = self.cabeza
          #nos paramos en el penultimo nodo
          while(actual.siguiente.siguiente):
              actual = actual.siguiente

          actual.siguiente = None

      def Imprimir_ListaEnlazada(self):
          actual = self.cabeza

          while(actual):
              print(actual.numero, "->", end=" ")
              actual = actual.siguiente
          print("None")

Mi_lista = ListasEnlazadas()
Mi_lista.Insertar_Nodo_al_Inicio(5)
Mi_lista.Insertar_Nodo_al_Inicio(4)
Mi_lista.Insertar_Nodo_al_Inicio(8)
Mi_lista.Insertar_Nodo_al_Inicio(9)
Mi_lista.Insertar_Nodo_al_Inicio(1)
Mi_lista.Insertar_Nodo_al_Inicio(3)
Mi_lista.Imprimir_ListaEnlazada()

Mi_lista.Eliminar_Nodo_al_Final()
Mi_lista.Eliminar_Nodo_al_Inicio()
Mi_lista.Imprimir_ListaEnlazada()
