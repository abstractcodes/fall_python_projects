class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        
           
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        # adds an item to list at the beginning
        temp = DLinkedListNode(item, self.__head, None)
        if self.__head != None:
            self.__head.setPrevious(temp)
            temp.setNext(self.__head)
        else:
            self.__tail = temp
        self.__head = temp
        self.__size += 1
        
    def remove(self, item):
        # search for the item and remove it
        # the method assumes the item exists
        current = self.__head
        previous = None
        found = False
        index = 0
        while not found and index < self.__size:
            index += 1
            if current.getData() ==  item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found == True:
            if previous == None:
                self.__head = current.getNext()
            else:
                previous.setNext(current.getNext())
            if (current.getNext() != None):
                current.getNext().setPrevious(previous)
            else:
                self.__tail=previous
            self.__size -= 1
        
    def append(self, item):
    # adds the item to the end of the list
    # must traverse the list to the end and add item
        temp = DLinkedListNode(item, None, None)
        if (self.__head == None):
            self.__head = temp
        else:
            self.__tail.setNext(temp)
        temp.setPrevious(self.__tail)
        self.__tail= temp
        self.__size += 1

        
    def insert(self, pos, item):
        # Insertion at beginning
        new_node = DLinkedListNode(item , None, None)
        if self.__size == 0:
            self.__head = new_node
        else:
            if pos == 0:
                temp = self.__head
                temp.setPrevious(new_node)
                new_node.setNext(temp)
                self.__head = new_node
            # Insertion at end
            elif pos == self.__size + 1:
                temp = self.__tail
                temp.setNext(new_node)
                new_node.setPrevious(temp)
                self.__tail = new_node
            # Insertion at a position
            else:
                temp = self.__head.getNext()
                before = self.__head
                for index in range(1,pos):
                    temp = temp.getNext()
                    before = before.getNext()
                before.setNext(new_node)
                new_node.setNext(temp)
                temp.setPrevious(new_node)
                new_node.setPrevious(before)
        self.__size += 1

    def pop1(self):
        if self.__head.getNext() != None:
            current = self.__head.getNext()
            before = self.__head
            while current.getNext() is not None:
                current = current.getNext()
                before = before.getNext()
            element = current.getData()
            before.setNext(None)   
            current.setPrevious(None)
        else:
            current = self.__head
            element = current.getData()
            current.setNext(None)
            current.setPrevious(None)
            self.__head = None
        return element

    
    def pop(self, pos=None):
        # TODO:
        # Hint - incorporate pop1 when no pos argument is given
        # self.__head == None or self.__size == 0 that means no element.
        # if one element is there the self.__head should become none
        # if last two elements are there the self.__tail shoule become none
        # if two elements are there then self.__head should become the next element
        if self.__size == 0:
            raise Exception("The linked list is empty")
        if pos == None:
            element = self.pop1()
        elif pos >=0 and pos <= self.__size:
            if pos == 0:
                current = self.__head
                self.__head = current.getNext()
                current.setNext(None)
                self.__head.setPrevious(None)
            elif pos == self.__size-1:
                element = self.pop1()
            else:
                current = self.__head.getNext()
                before = self.__head
                for index in range(1,pos):
                    current = current.getNext()
                    before = before.getNext()
                before.setNext(current.getNext())
                current.getNext().setPrevious(before)
                current.setNext(None)
                current.setPrevious(None)
                element = current.getData()
        self.__size -= 1
        return element
            

        
    def searchLarger(self, item):
        # TODO:
        temp = self.__head
        position_of_element = 0
        found = False
        while not found:
            if temp.getData() > item:
                found = True
            else:
                position_of_element += 1
                temp = temp.getNext()
        if found == True:
            return position_of_element
        else:
            return -1
        
    def getSize(self):
        return self.__size
    
    def getItem(self, pos):
        temp = self.__head
        if pos < 0:
            pos = self.__size + pos
        if pos >= 0 and pos <= self.getSize(): 
            for index in range(pos+1):
                if index == pos:
                    return temp.getData()
                temp = temp.getNext()
        else:
            raise Exception("index out of range")
        
    def __str__(self):
        current = self.__head
        string = ''
        while current != None:
            string = string + str(current.getData())+' '
            current = current.getNext()
        return string


def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World ")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"
        
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)   
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0) 
    print(str(int_list2))
    is_pass = (str(int_list2) == "9 8 7 6 5 4 ")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    print(str(int_list2))
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12 ")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    print(str(int_list2))
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12 ")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False
        else:
            print("True")
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test" 

    int_list.insert(7,801) 

        
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"  
            
            
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

                
if __name__ == '__main__':
    test()
