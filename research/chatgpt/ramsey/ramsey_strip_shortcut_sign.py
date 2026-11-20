"""Predict type without constructing a 22-vertex graph. Clamp one alternation on the traversed incidence cycle, then take a signed residual minor. Validate type labels by all 288 matchings. Compare the changed permutation cycles for same-alternation long/short unique completions."""
from ramsey_strip_shortcut_normal_forms import data,shortcuts,r,edges,fill,orbits,Counter
from ramsey_strip_witness_orbits import D,M
from itertools import combinations
from functools import lru_cache

def sign(u):return (-1)**sum((i-k)*(j-l)<0 for (i,j),(k,l) in combinations(u,2))
assert {(k,sign(u)) for u,k in orbits.items()}=={(1,1),(2,-1)}
def minor(rows,cols):
 if not rows:return 1
 i,*tail=rows;return sum((-1)**j*minor(tail,cols[:j]+cols[j+1:]) for j,v in enumerate(cols) if D[i] in M[v])
@lru_cache(None)
def packet(w):
 p=data[w]['path'];c=p+[r[x] for x in p[-2:0:-1]];base={(i,j-15) for i,j in (edges(c[k],c[k+1]) for k in range(0,len(c),2))};L=sorted(set(range(15))-{i for i,j in base});R=sorted(set(range(15))-{j for i,j in base});pref=sign(base|set(zip(L,R)));det=pref*minor(L,R);full=[base|{(i,j-15) for i,j in ex} for ex in fill(set(range(30))-set(c))];return det,full

def diff(a,b):
 p=dict(a);inv={j:i for i,j in b};todo=set(p);cs=[]
 while todo:
    x=min(todo);n=0
    while x in todo:todo.remove(x);n+=1;x=inv[p[x]]
    if n>1:cs.append(n)
 return tuple(sorted(cs))
h=Counter()
for w in data:
 for _,v in shortcuts(w):
    d,a=packet(w);e,b=packet(v)
    if len(a)==len(b)==1:
        cs=diff(a[0],b[0]);assert (d,e)==(sign(a[0]),sign(b[0])) and d*e==(-1)**sum(k-1 for k in cs);h[len(w),d,e,cs]+=1
print('length, long/short signed minor, relative permutation cycles:',h)
