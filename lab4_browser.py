#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------


def getAction():
    '''
    Asks for specific functionality of the website.
    Inputs: None
    Returns: choice which includes = , > ,< , and q
    '''
    continue_looping = False
    while not continue_looping:
        get_input = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
        if get_input == "=" or get_input == ">" or get_input == "<" or get_input == "q":
            continue_looping = True
        else:
            print("Invalid entry.")
    return get_input


def goToNewSite(current, pages):
    '''
    Asks for new webpage address.
    Inputs: We have the current index and the list containing the webpages.
    Returns: index of the new webpade address.
    '''   
    continue_looping = False
    # checks whether correct web address is entered or not.
    while not continue_looping:
        get_webpage = input("URL: ")
        if "." in get_webpage:
            continue_looping = True
    for i in range(current + 1,len(pages)):
        pages.pop()
    pages.append(get_webpage)
    current = pages.index(get_webpage)
    return current
    
def goBack(current, pages):
    '''
    Access the previous webpage from a list of web pages.
    Inputs: We have the current index and the list containing the webpages.
    Returns: index of the previous web page if present or else the current index.
    '''
    if current != 0:    
        previous_webpage = pages[current - 1]
        #pages.remove(pages[current])
        return pages.index(previous_webpage)
    else:
        print("Cannot go Back.")
        return current


def goForward(current, pages):
    '''
    Access the next webpage from a list of web pages.
    Inputs: We have the current index and the list containing the webpages.
    Returns: index of the previous web page if present or else the current index.
    '''    
    try:
        next_webpage = pages[current + 1]
    except:
        print("Cannot go Forward.")
        return current
    else:
        return pages.index(next_webpage)
   


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
        print(websites)
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    