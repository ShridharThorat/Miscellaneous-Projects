def ERROR_check(a: int) -> ValueError:
    if a not in [0, 1]:
        raise ValueError("Inputs must be 0 or 1")
    else:
        return False # i.e no error
    
def NAND_gate(a: int, b: int) -> int:
    """Return the result of a NAND gate for two binary inputs

    #### Args:
        a (int): a single binary number
        b (int): a single binary number

    #### Returns:
        int: 0 if both inputs are 1, 1 otherwise
    """
    ERROR_check(a)
    ERROR_check(b)
    if a == 1 and b == 1:
        return 0
    else:
        return 1

def NOT_gate(a: int) -> int:
    """Return the result of a NOT gate for a single binary input

    #### Args:
        a (int): a single binary number

    #### Returns:
        int: 0 if input is 1 and 1 if input is 0
    """
    ERROR_check(a)
    if a == 1:
        return 0
    elif a == 0:
        return 1


def AND_gate(a: int, b: int) -> int:
    """Return the result of an AND gate for two binary inputs

    #### Args:
        a (int): a single binary number
        b (int): a single binary number

    #### Returns:
        int: 1 if both inputs are 1, 0 otherwise
    """
    ERROR_check(a)
    ERROR_check(b)
    
    if a == 1 and b == 1:
        return 1
    else:
        return 0
    
def OR_gate(a: int, b: int) -> int:
    """Return the result of an OR gate for two binary inputs

    #### Args:
        a (int): a single binary number
        b (int): a single binary number

    #### Returns:
        int: 1 if a or b are 1, 0 otherwise
    """
    ERROR_check(a)
    ERROR_check(b)
    if a == 0 and b == 0:
        return 0
    else:
        return 1

def XOR_gate(a: int, b: int) -> int:
    """Return the result of an XOR gate for two binary inputs

    #### Args:
        a (int): a single binary number
        b (int): a single binary number

    #### Returns:
        int: 1 if a or b are 1, 0 otherwise
    """
    ERROR_check(a)
    ERROR_check(b)
    
    if (a==1 and b==1) or (a==0 and b==0):
        return 0
    else:
        return 1

print(ERROR_check(1))