#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    Asks for specific functionality of the website.
    Inputs: None
    Returns: choice which includes = , > ,< , and q
    '''
    get_input = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
    if get_input == "=" or get_input == ">" or get_input == "<" or get_input == "q":
        return get_input
    else:
        raise Exception("Invalid entry.")

def goToNewSite(current, bck, fwd):
    '''
    Asks for new webpage address.
    Inputs: We have the current webpage, a stack containing the web address to go back to, a stack containing the web address to go forward to.
    Returns: the new webpage.
    '''   
    get_webpage = input("URL: ")
    fwd.clear()
    if bck.isEmpty() or bck.peek() != current:
        bck.push(current)
    bck.push(get_webpage)
    return get_webpage
    
def goBack(current, bck, fwd):
    '''
    Access the previous webpage from the backward stack.
    Inputs: We have the current webpage, a stack containing the web address to go back to, a stack containing the web address to go forward to.
    Returns: previous web address if present or else the current one.
    '''    
    #delete pass and write your code here
    if bck.size() > 1:
        try:
            push_forward = bck.pop()
        except:
            print("Cannot go Back")
        else:
            fwd.push(push_forward)
            current = bck.peek()
    else:
        print("Cannot go Back")        
    '''
    if bck.size() <= 1:
        print("Cannot go back")
    else:
        fwd.push(bck.peek())
        bck.pop()
        current = bck.peek()'''
        
    return current

def goForward(current, bck, fwd):
    '''
    Access the next webpage from the forward stack.
    Inputs: We have the current webpage, a stack containing the web address to go back to, a stack containing the web address to go forward to.
    Returns: next web address if present or else the current one.
    '''    
    #delete pass and write your code here
    try:
        current = fwd.pop()
    except:
        print ("Cannot go forward")
    else:
        bck.push(current)

        
    return current
    

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    # putting the home in fwd stack
    #     
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True  
    forward.show()
    back.show()        
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    