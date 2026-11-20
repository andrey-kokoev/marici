"""Proper RBNN transport: V4 on the tetrahedron, Q8 on a sign-sensitive lift. Test reversible, rotation-equivariant directed edge lifts; also test an explicit flat but non-equivariant vertex gauge. No interpretation of a lift sign as a Ramsey color."""
from itertools import permutations, product
V=range(4);E=list(permutations(V,2));Q=[s*a for a in range(1,5) for s in (1,-1)] # 1,i,j,k
pos=[[1,2,3,4],[2,-1,4,-3],[3,-4,-1,2],[4,3,-2,-1]]
def mul(a,b):return (1 if a*b>0 else -1)*pos[abs(a)-1][abs(b)-1]
def inv(a):return a if abs(a)==1 else -a
def conj(g,a):return mul(mul(g,a),inv(g))
# Identify vertices with V4=Q8/{+1,-1}; left multiplication by an axis is the half-turn crossing the edge.
def axis(a,b):return abs(mul(b+1,inv(a+1)))
for a,b in E:
    h=axis(a,b);assert abs(mul(h,a+1))==b+1 and abs(mul(h,b+1))==a+1
    for t in [h,-h]:assert conj(h,t)==t and inv(t)!=t
# All six orientation choices for the unordered edges, imposing inverse on reversal.
und=[(a,b) for a,b in E if a<b];hist={};equivariant=0
for signs in product([1,-1],repeat=6):
    t={(a,b):s*axis(a,b) for (a,b),s in zip(und,signs)};t.update({(b,a):inv(v) for (a,b),v in list(t.items())})
    minus=sum(mul(t[c,a],mul(t[b,c],t[a,b]))==-1 for a,b,c in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]);hist[minus]=hist.get(minus,0)+1
    if all(t[abs(mul(g,a+1))-1,abs(mul(g,b+1))-1]==conj(g,v) for g in range(1,5) for (a,b),v in t.items()):equivariant+=1
assert hist=={0:8,2:48,4:8} and not equivariant
print('64 reversible lifts; negative-face counts:',hist,'; equivariant under even V4 translations:',equivariant)
