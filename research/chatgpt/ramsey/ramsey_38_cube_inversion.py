"""Catalogue witness 1499, laid out as three centrally inverted layers."""
from itertools import combinations
s=b'ZHoWM_JOdGsOADs?CeG@U?OM_aAG?G_XCI?LgCC_@YC?g?FC_aEO?DPbA`?G'
b=''.join(f'{v-63:06b}' for v in s[1:]);pairs=[(0,21),(1,22),(2,10),(3,5),(4,24),(6,26),(7,23),(8,25),(9,11),(13,18),(14,19),(15,17),(16,20)]
layout=[x for x,y in pairs]+[12]+[y for x,y in reversed(pairs)]
def sign(i,j):
    u,v=sorted((layout[i],layout[j]));return u!=v and b[v*(v-1)//2+u]=='1'
assert sorted(layout)==list(range(27));ind=[0]
for j in range(27):
    p=sum(1<<i for i in range(j) if sign(i,j));assert p in ind
    ind += [m|1<<j for m in ind if not p&m]
assert max(m.bit_count() for m in ind)==7
assert all(sign(i,j)==sign(26-i,26-j) for i,j in combinations(range(27),2))
for z in range(3):print([layout[9*z+i:9*z+i+3] for i in (0,3,6)])
