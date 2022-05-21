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
        """Adding new data in linkedlist.
            Args:
                data: A String to save on linked list
        """

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
        """
            Find node in list 
        """

        temp_node = self.head

        while temp_node != None:
            if temp_node.data == data:
                return temp_node
            
            temp_node = temp_node.next

        return None

    def print_reverse(self) -> str:
        """
            Print list on reverse
        """
        result = ""
        temp_node = self.end

        while temp_node != None:
            result += temp_node.data + ","
            temp_node = temp_node.prev
        
        return result
        

if __name__ == "__main__":
    ''' Manejo de la lista '''
    list_double = double_linked() # Crear una lista
    list_double.append("Python") # append para agregar datos a la lista
    list_double.append("JavaScript")
    list_double.append("Java")

    print("Lista completa :  " , str(list_double))
    print("Nodo head :  " , str(list_double.head.data))
    print("Nodo siguiente :  " , str(list_double.head.next.data))
    print("Nodo siguiente del siguiente :  " , str(list_double.head.next.next.data))
    print("Nodo previo del siguiente :  " , str(list_double.head.next.prev.data))
    print("Nodo antepenúltimo :  " , str(list_double.end.prev.data))
    print("Nodo end :  " , str(list_double.end.data))