def write_py(name, parameters, statements):
    '''
    write_py - to write python statements into a new file.
    Parameters:-
    name - name of the new function.
    parameters - containing arguments which will be taken by the nw function.
    statements - list of statements for the function.
    return - none
    '''
    assert name != 'a3'
    #with as block used for opening file
    with open(name+".py","w") as written_file:
        written_file.write("def "+name+"(")
        # writing parameters within the new funciton.
        for elements in range(len(parameters)):
            if len(parameters) > 1 and elements < len(parameters) - 1:
                written_file.write(parameters[elements]+", ")
            elif len(parameters) == 1 or len(parameters) -1 == elements:
                written_file.write(parameters[elements])
            else:
                written_file.write("")
        written_file.write("):"+"\n")
        # writing statments within the new function
        for elements in statements:
            written_file.write("\t"+elements)
            written_file.write("\n")
            if ":" in elements:
                written_file.write("\t")
    written_file.close()

def fixed_bubble(size):
    '''
    fixed_bubble - implementing bubble sort by compare and swap algorithm by using write_py 
    to be written as separate function.
    Parameters:-
    size - contains the size of the list to be sorted
    returns - none
    '''
    # list_of_statements to save the statements for the new function.
    list_of_statements = []
    for bubble in range(0, size):
        if bubble < size - 1:
            list_of_statements.append("# bubble "+str(bubble))
        for index in range(0, size - bubble - 1):
            list_of_statements.append("if a_list["+str(index)+"] > a_list["+str(index + 1)+"]:")
            list_of_statements.append("a_list["+str(index)+"], a_list["+str(index + 1)+"] = a_list["+str(index + 1)+"], a_list["+str(index)+"]")
    list_of_statements.append("return a_list")
    write_py("bubble"+str(size),["a_list"],list_of_statements)

def flip(flip_string):
    '''
    flip - to flip the character ">" to "<" and vice versa.
    flip_strings - charcaters "<" or ">".
    returns - flipped strings which is ">" or "<".
    '''
    if flip_string == ">":
        return "<"
    else:
        return ">"

def greatest_power_of_two_less_than(number = int):
    '''
    greatest_power_of_two_less_than - to get upper end and lower end of lists.
    number - integer number
    returns - the required number length for upper end and lower end of strings which.
    '''
    # index for power of two.
    index = 1
    running = True
    while running:
        index *= 2
        if index >= number:
            index  = index//2
            running = False
    return index

# for implementing bitonic sort.

def bitonic_sort(a_list, start, end, direction):
    '''
    bitonic_sort - implementing the sorting algorithm by using recursive technique.
    parameters: -
    a_list - which contains the list to be sorted.
    start - starting index of the list.
    end - ending element of the list.
    holder - default value for storing items in the list.
    direction -  which contains character ">" or "<".
    returns - none
    '''
    # split list in half and recursively call itself on both halves.
    # split the list in middle.
    if end - start <= 1:
        return 
    middle = (start + end) // 2
    bitonic_sort(a_list, start, middle, direction)
    bitonic_sort(a_list, middle, end, flip(direction))
    bitonic_merge(a_list, start, end, direction)

def bitonic_merge(some_list, start_index, end_index, original_direction):
    '''
    bitonic_merge - implementing the sorting algorithm and merging it by recursive technique.
    parameters: -
    some_list - which contains the list.
    start_index - starting index of the list.
    end_index - ending element of the list.
    original_direction - which contains the original direction "<" or ">".
    holder - default value for storing items in the list.
    returns - none
    '''
    # merge the lists with the original direction which is ">" or "<".
    if end_index - start_index <= 1:
        return 
    distance = greatest_power_of_two_less_than(end_index - start_index)
    middle_index = end_index - distance
    for each_index in range(start_index , middle_index):
        if original_direction == "<":
            if some_list[each_index] < some_list[each_index + distance]:
                some_list[each_index] = some_list[each_index + distance]
        else:
            if some_list[each_index] > some_list[each_index + distance]:
                some_list[each_index] = some_list[each_index + distance]
    bitonic_merge(some_list, start_index, middle_index, original_direction)
    bitonic_merge(some_list, middle_index, end_index, original_direction)

# for implementing fixed bitonic.

def fixed_sort(a_list, start, end, direction):
    '''
    fixed_sort - implementing the sorting algorithm by using recursive technique and storing additional elements.
    parameters: -
    a_list - which contains the list to be sorted.
    start - starting index of the list.
    end - ending element of the list.
    holder - default value for storing items in the list.
    direction -  which contains character ">" or "<".
    returns - none
    '''
    # split list in half and recursively call itself on both halves.
    # split the list in middle.
    if end - start <= 1:
        return 
    middle = (start + end) // 2
    fixed_sort(a_list, start, middle, direction)
    fixed_sort(a_list, middle, end, flip(direction))
    fixed_merge(a_list, start, end, direction)

def fixed_merge(some_list, start_index, end_index, original_direction):
    '''
    bitonic_merge - implementing the sorting algorithm and merging it by recursive technique.
    parameters: -
    some_list - which contains the list.
    start_index - starting index of the list.
    end_index - ending element of the list.
    original_direction - which contains the original direction "<" or ">".
    holder - default value for storing items in the list.
    returns - none
    '''
    if end_index - start_index <= 1:
        return 
    distance = greatest_power_of_two_less_than(end_index - start_index)
    middle_index = end_index - distance
    for each_index in range(start_index , middle_index):
        if original_direction == "<":
            if some_list[each_index] < some_list[each_index + distance]:
                some_list[each_index] = some_list[each_index + distance]
        else:
            if some_list[each_index] > some_list[each_index + distance]:
                some_list[each_index] = some_list[each_index + distance]
        # appening new list items in the list which is indexes and direction.
        some_list.append([each_index,each_index+distance,original_direction])
    fixed_merge(some_list, start_index, middle_index, original_direction)
    fixed_merge(some_list, middle_index, end_index, original_direction)

def bitonic(a_list):
    '''
    bitonic - calling bitonic sorting algorithm
    a_list - list to be sorted
    returns - none
    '''
    # calling bitonic sort but with holder being none.
    bitonic_sort(a_list,  start = 0, end = len(a_list), direction = ">")


def fixed_bitonic(size):
    '''
    fixed_bitonic - function to write bitonic sort in a different python file using write_py.
    size - size of the list tobe sorted using bitonic sort.
    returns - none.
    '''
    # a_list to store the indexes for the list of statements which will be writing the bitonic function in new file.
    a_list = [] 
    for index in range(size):
        a_list.append(index)
    # calling bitonic sort but with holder being true.
    fixed_sort(a_list, start = 0, end = size, direction = ">")
    list_of_statements = []
    for elements in a_list:
        # isinstance sed to take out those elements form the list.
        if isinstance(elements, list) == True:
            list_of_statements.append("if a_list["+str(elements[0])+"]"+ elements[2] +"a_list["+str(elements[1])+"]:")
            list_of_statements.append("a_list["+str(elements[0])+"], a_list["+str(elements[1])+"] = a_list["+str(elements[1])+"], a_list["+str(elements[0])+"]")
    list_of_statements.append("return a_list")
    # writing it as a new file using write_py.
    write_py("bitonic"+str(size),["a_list"],list_of_statements)