"""All normalized encodings of the four benchmark distances and the unique difficult query."""
from itertools import product
from collections import Counter
from ramsey_simplex_complement_routes import layer,phase,orders,W
from ramsey_mutual_repair_conjecture import sevens
from ramsey_39_cyclic_constructor import graph
M=35;target={1,7,11,16};hist=Counter();example={}
for v in product(range(M),repeat=3):
    w=(0,)+v;d=[(w[(i+1)%4]-w[i])%M for i in range(4)]
    if {min(a,M-a) for a in d}!=target:continue
    S={0};r=0
    while len(S)<M:S={(a+b)%M for a in S for b in w};r+=1
    hist[r+3]+=1;example.setdefault(r+3,w)
print('first all-order depths',hist,'examples',example)
A=graph(tuple(target));witnesses=[m for m in sevens(A,((1<<35)-1)^1,8) if m&A[0]==1<<7];print('forced sevens',len(witnesses),'first eight',[i for i in range(35) if witnesses[0]>>i&1]);
for n in (7,8):
    reps=[(x,orders(x,1)) for x in layer(n) if phase(x)==0 and x[1]];print(n,'0->7 reps',reps)
