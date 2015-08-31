"""
Shows how all logic gates can be implemented in terms of the NAND-gate: The
NOT-AND gate.

Written and put in the public domain by Christian Stigen Larsen.
"""

def truth(op):
    """Prints truth table for an operator."""
    for x in (0,1):
        for y in (0,1):
            print("%s(%d,%d) ==> %d" % (op.__name__, x, y, op(x,y)))

def NAND(x,y):
    """
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
        not(0) ==> 1
        not(1) ==> 0

    By looking at the NAND table, we see that we are interested in the outputs
    that will result in 0 and 1. The two last rows have this property, and we
    then notice that in those cases, the inputs are equal. We get

        not(x) := nand(x,x)
        not(0) ==> nand(0,0) ==> 1
        not(1) ==> nand(1,1) ==> 0

    An alternative is NOT(x) := NAND(x,x) which I think is more elegant
    (thinking about actual circuits, we could just connect the two NAND inputs
    to the same wire).
    """
    return NAND(x,x)

def AND(x,y):
    """
    The truth table is:

        and(0,0) ==> 0
        and(0,1) ==> 0
        and(1,0) ==> 0
        and(1,1) ==> 1

    But NAND is "not-and", so we can just reverse the result from NAND:

        and(x,y) := not(nand(x,y))
    """
    return NOT(NAND(x,y))

def OR(x,y):
    """
    This gate is a bit more tricky. The truth table is:

        or(0,0) ==> 0
        or(0,1) ==> 1
        or(1,0) ==> 1
        or(1,1) ==> 1

    This is almost the same as the NAND. I don't have a good pedagogical way of
    showing this, but we don't have many primitives, and AND is just NAND
    reversed. So what happens if we negate both inputs to NAND?

        >>> truth(lambda x,y: NAND(NOT(x), NOT(y)))
        <lambda>(0,0) ==> 0
        <lambda>(0,1) ==> 1
        <lambda>(1,0) ==> 1
        <lambda>(1,1) ==> 1

    Hey, this is the OR operator!

        OR(x,y) := NAND(NOT(x), NOT(y))
    """
    return NAND(NOT(x), NOT(y))

def XOR(x,y):
    """
    >>> truth(lambda x,y: AND(OR(x,y), NAND(x,y)))
    <lambda>(0,0) ==> 0
    <lambda>(0,1) ==> 1
    <lambda>(1,0) ==> 1
    <lambda>(1,1) ==> 0
    """
    return AND(OR(x,y), NAND(x,y))

def EQ(x,y):
    """
    Looking at XOR, this would be its negation.
    """
    return NOT(XOR(x,y))
