"""Two identical cyclically ordered RRRBBBBBBB laps; insert two indistinguishable-in-role but distinct neutral visits. Keep directed backbone and node identities. Detect whether the lap exchange extends to a successor-preserving map (permitted to exchange the Ns)."""
from itertools import combinations_with_replacement
from collections import Counter
word='RRRBBBBBBB'*2
stats=Counter();fixed=[]
for a,b in combinations_with_replacement(range(20),2):
    C=[]
    for i in range(20):
        C.append(i%10)
        if i==a:C.append('N')
        if i==b:C.append('N')
    assert len(C)==22
    symmetric=C==C[11:]+C[:11]
    assert symmetric==(b==a+10)
    stats[symmetric]+=1
    if symmetric:fixed.append((a,b,word[a]+word[(a+1)%20]))
assert stats=={False:200,True:10};print(stats, 'symmetric transition gaps:',[x for x in fixed if x[2] in ('RB','BR')])
