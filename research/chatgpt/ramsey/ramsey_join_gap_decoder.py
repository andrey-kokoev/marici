"""Generate all minimum quartet certificates by a cyclic gap rule, then verify."""
from itertools import combinations, combinations_with_replacement, product
from collections import Counter

n=13
reps=((0,2,4,6),(0,2,6,9),(0,3,6,9))
Q=[frozenset((x+d)%n for x in r) for r in reps for d in range(n)]

def triples(step):
    return {frozenset(step*x%n for x in (i,i+a,i+a+b))
            for i in range(n) for a,b,c in product(range(1,6),repeat=3) if a+b+c==n}

miss=[{j for j,b in enumerate(Q) if not a&b} for a in Q]
violations=[a&b|a&c|b&c for a,b,c in combinations_with_replacement(miss,3)]
B=set(range(n,2*n)); assert {next(iter(s)) for s in violations if len(s)==1}==B
expected={frozenset(offset+(i+j*step)%n for j in range(5)) for offset,step in [(0,5),(26,1)] for i in range(n)}
assert {frozenset(s) for s in violations if not s&B}==expected
certs={frozenset(a|B|{26+i for i in c}) for a,c in product(triples(5),triples(1))}
assert len(certs)==676 and all(all(s&t for t in expected) for s in certs)
# Classify the compact descriptions under the 52 affine graph symmetries.
perms=[[Q.index(frozenset((m*x+b)%n for x in q)) for q in Q] for m in (1,5,12,8) for b in range(n)]
todo=certs.copy();counts=Counter()
while todo:
    s=next(iter(todo));orbit={frozenset(p[i] for i in s) for p in perms};assert orbit<=todo
    counts[len(orbit)]+=1;todo-=orbit
print('minimum certificates:',len(certs),'symmetry classes by orbit size:',dict(sorted(counts.items())))
