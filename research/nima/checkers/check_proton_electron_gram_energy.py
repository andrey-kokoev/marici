"""Conditional Gram-energy test of the 1836 comparison family.

Arrow (i,j) is represented by e_j-e_i; state i by e_i. Comparison pairs
use tensor-product norms. This is an explicit model choice, not a mass law.
G has diagonal 12 and offdiagonal 1. Writes no files.
"""
from fractions import Fraction as F
from itertools import product

G=tuple(tuple(F(12 if i==j else 1) for j in range(4)) for i in range(4))
E=[(i,j) for i in range(4) for j in range(4) if i!=j]
basis=[tuple(F(k==i) for k in range(4)) for i in range(4)]
def inner(x,y):
    return sum(x[i]*G[i][j]*y[j] for i in range(4) for j in range(4))
def arrow(i,j): return tuple(basis[j][k]-basis[i][k] for k in range(4))
arrow_norms=[inner(arrow(i,j),arrow(i,j)) for i,j in E]
state_norms=[inner(x,x) for x in basis]
assert set(arrow_norms)=={F(22)}
assert set(state_norms)=={F(12)}
arrow_block=sum(a*b for a,b in product(arrow_norms,repeat=2))
state_block=sum(a*b for a,b in product(state_norms[1:],repeat=2))
assert arrow_block==144*22**2 and state_block==9*12**2
# Divide total energy by the energy of one outer-arrow/arrow-pair channel.
ratio=sum(arrow_norms)*(arrow_block+state_block)/F(22**3)
assert ratio==12*(144+9*F(12,22)**2)
assert ratio==F(212976,121)
print('Outer edge Gram energy:22 for every directed edge, including all rooted orbits.')
print('State Gram energy:12 for every state.')
print(f'Tensor comparison energies: arrow block={arrow_block}, state block={state_block}.')
print(f'Total / one outer-arrow+arrow-pair channel={ratio}={float(ratio):.12f}')
print('Separately unit-normalizing every primitive gives1836 by construction.')
print('To equalize raw pair energies, state-pair block needs multiplier121/36.')
assert F(22**2,12**2)==F(121,36)
# Directed labels reverse into the same ray up to sign in this realization.
assert arrow(1,0)==tuple(-x for x in arrow(0,1))
# A trace over labelled channels sums energies. A coherent sum differs:
summed=tuple(sum(arrow(i,j)[k] for i,j in E) for k in range(4))
assert summed==(0,0,0,0) and inner(summed,summed)==0
print('Coherent sum of all directed edge vectors=0; incoherent energy sum=264.')
print('Exact Gram-energy checks passed; electron reference assignment remains hypothetical.')
