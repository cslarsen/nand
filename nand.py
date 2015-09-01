"""
Shows how all logic gates can be implemented in terms of the NAND-gate: The
NOT-AND gate.

Written and put in the public domain by Christian Stigen Larsen.
"""

def truth(op):
    """Prints truth table for an operator.

    For example, we can write

        >>> truth(NAND)
        NAND(0,0) ==> 1
        NAND(0,1) ==> 1
        NAND(1,0) ==> 1
        NAND(1,1) ==> 0
    """
    for x in (0,1):
        for y in (0,1):
            print("%s(%d,%d) ==> %d" % (op.__name__, x, y, op(x,y)))

def NAND(x,y):
    """
    This is our primitive. We'll simply define this by hand. The truth table
    is:

        nand(0,0) ==> 1
        nand(0,1) ==> 1
        nand(1,0) ==> 1
        nand(1,1) ==> 0
    """
    if (x,y) == (0,0): return 1
    if (x,y) == (0,1): return 1
    if (x,y) == (1,0): return 1
    if (x,y) == (1,1): return 0

def NOT(x):
    """
    Negates its input. The truth table is thus:

        not(0) ==> 1
        not(1) ==> 0

    We want to implement this in terms of NAND. Looking at NAND's truth table,
    we see that the top and bottom rows give the right output. What's special
    about the inputs for these rows is that they're equal. Therefore we can
    simply state

        not(x) := nand(x,x)
    """
    return NAND(x,x)

def AND(x,y):
    """
    AND is the negation of NAND, so we can straight out write

        and(x,y) := not(nand(x,y))
    """
    return NOT(NAND(x,y))

def OR(x,y):
    """
    This gate is a bit more tricky. We'll start by writing out the truth table
    alongside NAND:

        or(0,0) ==> 0    nand(0,0) ==> 1
        or(0,1) ==> 1    nand(0,1) ==> 1
        or(1,0) ==> 1    nand(1,0) ==> 1
        or(1,1) ==> 1    nand(1,1) ==> 0

    We clearly see that if we could flip the NAND *outputs* vertically, we'd
    get the OR operator. We can't simply negate NAND's output (that would
    give us AND), but if we negate the *inputs*, we will be able to do exactly
    that:

        nand(not(x), not(y)) gives
        (x,y) = (0,0) ==> nand(1,1) ==> 0
        (x,y) = (0,1) ==> nand(1,0) ==> 1
        (x,y) = (1,0) ==> nand(0,1) ==> 1
        (x,y) = (1,1) ==> nand(0,0) ==> 1

    So, we get

        or(x,y) := nand(not(x), not(y))
    """
    return NAND(NOT(x), NOT(y))

def XOR(x,y):
    """
    The exclusive-or truth table is

        xor(0,0) ==> 0
        xor(0,1) ==> 1
        xor(1,0) ==> 1
        xor(1,1) ==> 0

    By juxtapositioning OR and NAND, as shown above, we see that their outputs
    are

         x,y   OR   NAND  XOR
         0 0    0     1     0
         0 1    1     1     1
         1 0    1     1     1
         1 1    1     0     0

    So, if we AND the OR and NAND results together, we'll get XOR:

        xor(x,y) := and(or(x,y), nand(x,y))
    """
    return AND(OR(x,y), NAND(x,y))

def EQ(x,y):
    """
    The equals operator (is x == y?) is actually the negation of the XOR, as
    can be seen in XOR truth table. We simply write out

        eq(x,y) := not(xor(x,y))
    """
    return NOT(XOR(x,y))
