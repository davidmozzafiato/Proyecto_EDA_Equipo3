class Node():
    def __init__(self,data : str):
        self.data : str = data
        self.next : Node = None
        self.prev : Node = None
class double_linked():
    def __init__(self):
        self.head : Node = None
        self.end  : Node = None
    def append(self,data: str):
        new_node = Node(data)
        if self.end != None:
            new_node.prev = self.end
            self.end.next = new_node
            self.end = new_node
            return
        self.head = new_node
        self.end  = new_node
    def __str__(self):
        result = ""
        temp_node = self.head
        while temp_node != None:
            result += temp_node.data + ","
            temp_node = temp_node.next
        return result
    def find(self,data : str) -> Node:
        temp_node = self.head
        while temp_node != None:
            if temp_node.data == data:
                return temp_node
            temp_node = temp_node.next
        return None
    def print_reverse(self) -> str:
        result = ""
        temp_node = self.end
        while temp_node != None:
            result += temp_node.data + ","
            temp_node = temp_node.prev
        return result
if __name__ == "__main__":
    # NOTE: Líneas para experimentar con las funciones este archivo sirve para controlar las listas del juego y que sean circulares ya queeee
    '''
    # NOTE: Manejo de la lista
    list_double = double_linked() # Crear una lista
    list_double.append("Python") # append para agregar datos a la lista
    list_double.append("JavaScript")
    list_double.append("Java")
    # NOTE: Nodos head
    print("NODOS HEAD")
    Nodo = list_double.head
    print("Nodo actual:           " , str(Nodo.data))
    Nodo = Nodo.next
    print("Nodo siguiente:        " , str(Nodo.data))
    Nodo = Nodo.next
    print("Nodo * del siguiente:  " , str(Nodo.data))
    if Nodo == list_double.end:
        print('Has llegado al final de la lista')
        Nodo = Nodo = list_double.head
    print("Nodo * del siguiente:  " , str(Nodo.data))
    Nodo = Nodo.next
    print("Nodo siguiente:        " , str(Nodo.data))
    Nodo = Nodo.next
    print("Nodo * del siguiente:  " , str(Nodo.data))
    # NOTE: Nodos end
    print("NODOS END")
    Nodo = list_double.end
    print("Nodo actual:           " , str(Nodo.data))
    Nodo = Nodo.prev
    print("Nodo siguiente:        " , str(Nodo.data))
    Nodo = Nodo.prev
    print("Nodo * del siguiente:  " , str(Nodo.data))
    if Nodo == list_double.head:
        print('Has llegado al final de la lista')
        Nodo = Nodo = list_double.end
    print("Nodo * del siguiente:  " , str(Nodo.data))
    Nodo = Nodo.prev
    print("Nodo siguiente:        " , str(Nodo.data))
    Nodo = Nodo.prev
    print("Nodo * del siguiente:  " , str(Nodo.data))
    '''
#           /^\/^\
#         _|__|  O|
#\/     /~     \_/ \
# \____|__________/  \
#        \_______      \
#                `\     \                 \
#                  |     |                  \
#                 /      /                    \
#                /     /                       \\
#              /      /                         \ \
#             /     /                            \  \
#           /     /             _----_            \   \
#          /     /           _-~      ~-_         |   |
#         (      (        _-~    _--_    ~-_     _/   |
#          \      ~-____-~    _-~    ~-_    ~-_-~    /
#            ~-_           _-~          ~-_       _-~
#               ~--______-~                ~-___-~