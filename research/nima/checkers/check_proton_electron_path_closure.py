"""Positive path-resource closure trial for the 1836 comparison family.

Assumptions: each of 1836 unit-resource base channels repeats after a return;
return requires one designated selection at each of three uniform independent
routing stages of sizes 12,144,9. Trial selects no coefficient from mass data.
Electron closure multiplier is an explicit separate parameter. No files written.
"""
from fractions import Fraction as F
from itertools import product

routes=list(product(range(12),range(144),range(9)))
assert len(routes)==15552
accepted=sum(route==(0,0,0) for route in routes)
assert accepted==1
p=F(accepted,len(routes))
base=F(1836)
# Renewal equation C=base+p*C, sums nonnegative repeated traversal resource.
cost=base/(1-p)
assert cost==base+p*cost
first_extra=base*p
assert cost-base>first_extra>0
# This costs the counted repeated channels; routing stages are selection
# conditions here. Extra physical traversals of the routing stages would
# themselves need positive costs, not silently be counted as free operations.
print(f'Uniform designated-return fraction={p}')
print(f'First repeated-channel resource={first_extra}={float(first_extra):.12f}')
print(f'Resummed proton/electron ratio with uncorrected electron={float(cost):.12f}')
print(f'Tail={float(cost-base):.12f}')

# Ratio when both sectors have renewal corrections.
def ratio(pp,pe): return base*(1-pe)/(1-pp)
assert ratio(p,F(0))==cost
assert ratio(p,p)==base
assert ratio(p,p/2)<cost
print(f'Equal proton/electron return fractions: ratio={ratio(p,p)}')
print(f'Electron return fraction p/2: ratio={float(ratio(p,p/2)):.12f}')
# Rounded empirical target is used only after predictions above.
target=F('1836.152673')
required=1-base/target
assert required>p
print(f'Target diagnostic with uncorrected electron: required return fraction={float(required):.12g}')
print(f'Trial minus rounded target={float(cost-target):.12f}')
print('Exact positive-resource identities passed; specified routing trial undershoots target.')
