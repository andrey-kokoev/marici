"""Ideal passive factorization of the conditional260-mode extraction.

Four64-mode signed Walsh routers, four swaps and inverse routing. Balanced
couplers/sign phases are declared ideal controls, NOT calibrated apparatus.
The input joint bank is still an explicitly prepared resource.
"""
from fractions import Fraction
from joint_bank_extraction import PRODUCT_COLUMNS

GROUPS=tuple(tuple((index,1 if column[row]>0 else -1)
                   for index,column in enumerate(PRODUCT_COLUMNS) if column[row])
             for row in range(4))


def hadamard64(values):
    if len(values)!=64:
        raise ValueError('Exactly64 routed amplitudes required')
    out=[Fraction(value) for value in values]
    stride=1
    while stride<64:
        for base in range(0,64,2*stride):
            for offset in range(stride):
                i,j=base+offset,base+offset+stride
                a,b=out[i],out[j]
                out[i],out[j]=a+b,a-b
        stride*=2
    # Six normalized balanced layers: (sqrt(2))^6=8 exactly.
    return tuple(value/8 for value in out)


def route(bank):
    if len(bank)!=256:
        raise ValueError('Prepared256-mode joint bank required')
    blocks=[hadamard64(tuple(sign*bank[index] for index,sign in group)) for group in GROUPS]
    return tuple(block[0] for block in blocks)+tuple(value for block in blocks for value in block[1:])


def unroute(routed):
    if len(routed)!=256:
        raise ValueError('Complete256-mode router output required')
    result=[0]*256
    for row,group in enumerate(GROUPS):
        block=(routed[row],)+tuple(routed[4+63*row:4+63*(row+1)])
        restored=hadamard64(block)
        for (index,sign),value in zip(group,restored):
            result[index]=sign*value
    return tuple(result)


def extract(carrier,bank):
    if len(carrier)!=4:
        raise ValueError('Four carrier modes required')
    routed=route(bank)
    new_carrier=routed[:4]
    swapped=tuple(carrier)+routed[4:]
    return new_carrier,unroute(swapped)


def router_layers():
    return tuple(tuple((base+offset,base+offset+stride)
                       for base in range(0,64,2*stride) for offset in range(stride))
                 for stride in (1,2,4,8,16,32))
