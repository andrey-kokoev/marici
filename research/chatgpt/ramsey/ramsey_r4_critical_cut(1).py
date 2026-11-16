#!/usr/bin/env python3
"""An exact graph-theoretic 10-versus-9 cut obstruction for the sole r4 profile
not already excluded by the singleton shadow or no-degree Hall+triangle system.
Only uses support overlap, 5-way Hall obligations and the degree equations.
"""
from itertools import combinations
from collections import Counter
from ramsey_fractional_witness_certificate import support_classes

m=support_classes(4)[0][17]
label=lambda x:''.join(str(i) for i in range(6) if x>>i&1)
labels=tuple(map(label,m));idx={x:i for i,x in enumerate(labels)}
A=('0','1','01','012','013','14','05')
B=('2','3','4','34','234','5','25','35','245')
assert set(A).isdisjoint(B) and set(A)|set(B)==set(labels)
# Each tuple of T-vertices below is deficient in its common S-neighborhood.
# Its internal possible red edges form one nonempty obligation, with no edge
# shared by another obligation. This is a statement about all red graphs, not
# an assumed edge-selection pattern.
W=(('2','5','25'),('3','4','34'),('3','5','35'),
   ('2','3','34','234'),('4','5','25','245'),
   ('2','234','25','35','245'),('3','34','234','25','35'),
   ('3','34','234','35','245'),('4','34','234','35','245'),
   ('34','234','5','35','245'))
def possible_edges(xs):
 return {tuple(sorted((x,y))) for x,y in combinations(xs,2)
         if not(m[idx[x]] & m[idx[y]])}
all_obligation_edges=[]
for U in W:
    union=0
    for x in U:union |= m[idx[x]]
    assert union.bit_count()<len(U),U
    E=possible_edges(U)
    assert E
    assert all(not E.intersection(F) for F in all_obligation_edges)
    all_obligation_edges.append(E)
assert len(W)==10
EA=possible_edges(A)
assert len(EA)==4
D_A=sum(6-m[idx[x]].bit_count() for x in A)
D_B=sum(6-m[idx[x]].bit_count() for x in B)
assert (D_A,D_B)==(28,38)
# For ANY red graph with prescribed degrees, writing cross edges e(A,B),
# 2e(A)+e(A,B)=28, 2e(B)+e(A,B)=38. Thus e(B)-e(A)=5.
# E_A <= 4 implies e(B)<=9, while 10 disjoint Hall requirements imply e(B)>=10.
assert (D_B-D_A)//2+len(EA)==9
print('CUT EXACT: 10 edge-disjoint deficient-support requirements entirely inside B')
print('A',A,'B',B)
print('A possible red edges',sorted(EA))
print('degrees A',D_A,'B',D_B,'forced e(B)-e(A)',(D_B-D_A)//2)
print('e(B)>=10 from disjoint witness requirements; e(B)<=9 from degrees and overlap')
print('Contradiction. With relaxed witness slack delta, 10(1-delta)<=9, so delta>=1/10.')
