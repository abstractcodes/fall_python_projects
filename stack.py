#----------------------------------------------------
# Stack implementation #2 
# (Top of stack corresponds to back of list)
# 
# Author: CMPUT 175 team
# Updated by:
#----------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def pop(self):
        if self.isEmpty() == False:       
            return self.items.pop()
        else:
            raise Exception('Stack is empty cannot pop an element')
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def peek(self):
        if self.isEmpty() == False:      
            return self.items[len(self.items)-1]
        else:
            raise Exception('The stack is empty cannot peek') 
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        #TO DO: complete method according to updated ADT
        self.items = []    


OPENS = "({[<"
CLOSES = ")}]>"
def check_brackets_stack(string):
    # Returns True if brackets in string are matched correctly,
    # returns False if they're mismatched
    stack = Stack()
    for character in string:
        if character in OPENS:
            stack.push(character)
        elif character in CLOSES:
            opening = OPENS[CLOSES.index(character)]
            if stack.size() > 0 and stack.peek() == opening:
                stack.pop()
            else:
                stack.push(character)
                break
    if stack.isEmpty():
        return True
    else:
        return False

print(check_brackets_stack("[Rishit is a goo goo](1+1)[][[[[[[[[]]]]]]]]"))


# recursive

def check_brackets_recursive(string, index, opened):
    # Returns True if brackets in string are matched correctly,
    # returns False if they're mismatched
    while index < len(string):
        character = string[index]
        index = index + 1
        if character in OPENS:
            index, result = check_brackets_recursive(string, index, character)

            if not result:
                return index, result
        elif character in CLOSES:
            opening = OPENS[CLOSES.index(character)]
            if opened == opening:
                return index, True
            else:
                return index, False
    if opened is None:
        return index, True
    else:
        return index, False

def check_brackets_callstack(string):
    index, result = check_brackets_recursive(string, 0, None)
    return result

print(check_brackets_callstack("[Rishit is a goo goo](1+1)[][[[[[[[[]]]]]]]]"))