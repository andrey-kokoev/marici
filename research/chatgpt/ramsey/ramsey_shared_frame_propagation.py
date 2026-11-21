"""Derive forced edges from frame-only independence, degree and triangle constraints."""
from itertools import combinations
from collections import Counter
from ramsey_shared_frame_reconstruction import T,allowed,degree
E=[(i,j) for i,j in combinations(range(15),2) if j in allowed[i]]
bits={e:1<<i for i,e in enumerate(E)};allbits=(1<<len(E))-1
rules=[]
for i,d in enumerate(degree):rules.append((sum(b for e,b in bits.items() if i in e),d,d))
for t in combinations(range(15),3):
    es=list(combinations(t,2))
    if all(e in bits for e in es):rules.append((sum(bits[e] for e in es),0,2))
clauses=set()
for k in range(1,7):
    for U in combinations(range(15),k):
        if k+max(1,6-len(set().union(*(set(T[i]) for i in U))))>=7:
            clauses.add(sum(bits.get(e,0) for e in combinations(U,2)))
minimal=[]
for c in sorted(clauses,key=lambda c:(c.bit_count(),c)):
    if not any(d&c==d for d in minimal):minimal.append(c)
rules.extend((c,1,c.bit_count()) for c in minimal)
def prop(y,n):
    while True:
        old=y,n
        for m,lo,hi in rules:
            used=(m&y).bit_count();free=m&~(y|n)
            if used>hi or used+free.bit_count()<lo:return None
            if used==hi:n|=free
            elif used+free.bit_count()==lo:y|=free
        if old==(y,n):return old
if __name__=='__main__':
    y,n=prop(0,0);print('edges',len(E),'clauses',Counter(c.bit_count() for c in minimal),'base',y.bit_count(),n.bit_count())
    for depth in range(20):
        old=y,n
        for e,b in bits.items():
            if b&(y|n):continue
            if prop(y|b,n) is None:n|=b
            elif prop(y,n|b) is None:y|=b
        y,n=prop(y,n);print('one-split pass',depth+1,'present',y.bit_count(),'absent',n.bit_count());
        if old==(y,n):break
    def refute(y,n,depth):
        state=prop(y,n)
        if state is None:return True
        if not depth:return False
        y,n=state
        return any(refute(y|b,n,depth-1) and refute(y,n|b,depth-1) for b in bits.values() if not (y|n)&b)
    for depth in (1,2):
        for b in bits.values():
            if (y|n)&b:continue
            if refute(y|b,n,depth):n|=b
            elif refute(y,n|b,depth):y|=b
        y,n=prop(y,n);print('extra split depth',depth,y.bit_count(),n.bit_count())
    u,v=prop(y|bits[0,10],n);print('conditioning a-X: present',[(i,j) for (i,j),b in bits.items() if b&u and not b&y], 'free',[e for e,b in bits.items() if not b&(u|v)])
    print('unfixed',[(T[i],T[j]) for (i,j),b in bits.items() if not (y|n)&b])
