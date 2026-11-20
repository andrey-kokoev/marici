"""Compare next partitions using the entry's unconsumed block. No global map or square is used to define the test. One branch retains that block, the other reroutes it."""
from itertools import combinations
X=list(combinations(range(1,5),2));P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6]
for entry,exit in ((16,7),(17,4)):
    fan=P[0];e=P[exit];partition=T[entry-15];unused,=[p for p in partition if set(p).isdisjoint(e) and p!=fan]
    # The fan and marked pair each donate one label to the selected exit block.
    assert len(set(fan)&set(e))==1
    options=[j for j,t in enumerate(T,15) if e in t and j!=29]
    print('entry',entry,'exit',exit,'untouched block',[X[i] for i in unused])
    for j in options:print(' next',j,'retains untouched block',unused in T[j-15],'shared blocks with entry',len(set(partition)&set(T[j-15])))
    assert sorted(unused in T[j-15] for j in options)==[False,True]
