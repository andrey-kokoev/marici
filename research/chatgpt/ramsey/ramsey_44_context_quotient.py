"""Exact (4,4) continuation languages for complete labeled old graphs.
Contexts add exactly d fresh vertices, with all new incident edges colored.
A signature is a bitset of rejected context assignments, not an edge encoding.
"""
from itertools import combinations
from collections import Counter


def quotient(n,d):
    old=list(combinations(range(n),2));new=[e for e in combinations(range(n+d),2) if e not in old];nc=1<<len(new)
    allbits=(1<<nc)-1
    red=[sum(1<<j for j in range(nc) if j>>i&1) for i in range(len(new))];patterns=[];internal=[]
    for t in combinations(range(n+d),4):
        edges=list(combinations(t,2));om=sum(1<<old.index(e) for e in edges if e in old)
        if all(e in old for e in edges):internal.append(om);continue
        r=b=allbits
        for e in edges:
            if e in new:r &= red[new.index(e)]; b &= allbits^red[new.index(e)]
        patterns.append((om,r,b))
    classes=Counter()
    for g in range(1<<len(old)):
        if any((g&m) in (0,m) for m in internal):continue
        sig=0
        for m,r,b in patterns:
            if g&m==m:sig|=r
            if not g&m:sig|=b
        classes[sig]+=1
    return sum(classes.values()),len(classes),max(classes.values())

if __name__=='__main__':
    for n in (2,3,4,5):print(n,'(valid colorings, languages, largest class):',*[quotient(n,d) for d in (1,2)])
