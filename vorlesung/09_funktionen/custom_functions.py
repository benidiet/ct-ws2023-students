
counter = 0

def function1():
    """
    This function does something.

    Parameters:
        None
    
    Returns:
        (int): a value
    """
    return 5

def function2(n):
    """
    This function does something.

    Parameters:
        n (int): unsigned integer
    
    Returns: 
        None
    """
    for i in range(n):
        print("-", end = "")


def function3(a):
    """
    This function does something.

    Parameters:
        a (int): integer
    
    Returns:
        (int): result
    """
    return 2 * a

def function4(a, b):
    """
    This function does something.

    Parameters:
        a (int): integer
        b (int): another integer

    Returns:
        (int): result
    """
    return a * b

def function5():
    """
    This function does something.

    Parameters:
        None
    
    Returns:
        (int): result
    """
    global counter
    counter += 1
    return counter


def function6(text):
    """
    This function does something.

    Parameters:
        text (String): A string
    
    Returns:
        (String): result
    """
    dic = {}
    for i in text:
        if i in dic:
            dic[i] = dic[i]+1
        else:
            dic[i] = 1
    result = ""

    for i in text:
        if dic[i] > 1:
            i = i.upper()
        result = result + i
    return result
