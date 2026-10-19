"""Conservative conditional extraction on a prepared joint256-slot bank.

Joint preparation and physical control are NOT supplied by this module. The
normalization follows the source sewing metric; this is not the unscaled
bilinear composition recipe or the prior20-coordinate exchange.
"""
from clifford_comparison_bank import algebra,memory

ZERO4=(0,)*4
_BASIS=memory.basis(16)
PRODUCT_COLUMNS=tuple(algebra.multiply(memory.readout(_BASIS[i]),memory.readout(_BASIS[j]))
                      for i in range(16) for j in range(16))


def product_readout(joint):
    if len(joint)!=256:
        raise ValueError('Prepared joint256-slot bank required')
    out=ZERO4
    for coefficient,value in zip(joint,PRODUCT_COLUMNS):
        if coefficient:
            out=memory.add(out,memory.scale(value,coefficient))
    return out


def readout(joint):
    return memory.scale(product_readout(joint),algebra.F(1,2))


def lift(value):
    return tuple(sum(a*b for a,b in zip(value,column))/2 for column in PRODUCT_COLUMNS)


def exchange(carrier,joint):
    if len(carrier)!=4 or len(joint)!=256:
        raise ValueError('Four carrier and256 joint-bank coordinates required')
    observed=readout(joint)
    remainder=memory.sub(joint,lift(observed))
    return observed,memory.add(lift(carrier),remainder)


def tensor(right,left):
    if len(right)!=16 or len(left)!=16:
        raise ValueError('Two16-slot operand banks required')
    return tuple(a*b for a in right for b in left)
