"""After twin-slot elimination, isolate which constraints force the eight-cycle."""
from ramsey_root_gate import bits,T,degree,base
from itertools import combinations
V=[i for i in range(15) if i not in (10,11,14)];E={e:b for e,b in bits.items() if set(e)<=set(V)};mask=sum(E.values());rules=[]
for i in V:
    d=degree[i]-int(i<6);rules.append((sum(b for e,b in E.items() if i in e),d,d))
for U in combinations(V,3):
    if all(e in E for e in combinations(U,2)):rules.append((sum(E[e] for e in combinations(U,2)),0,2))
# All singleton point clauses on core edges.
seed=sum(set(m for m,l,h in base if l==1 and m.bit_count()==1 and m&mask));print('seed',[(T[i],T[j]) for (i,j),b in E.items() if b&seed])
def close(y,n):
    while True:
        old=y,n
        for m,l,h in rules:
            f=m&~(y|n);a=(y&m).bit_count()
            if a>h or a+f.bit_count()<l:return None
            if a==h:n|=f
            elif a+f.bit_count()==l:y|=f
        if old==(y,n):return old

def models(y,n):
    state=close(y,n)
    if state is None:return
    y,n=state;f=mask&~(y|n)
    if not f:yield y;return
    b=f&-f;yield from models(y|b,n);yield from models(y,n|b)
if __name__=='__main__':
    S=list(models(seed,0));print('core models',len(S));y,n=close(seed,0);print('direct closure',y.bit_count(),n.bit_count(),'free',len(E)-(y|n).bit_count());print('residual',[(T[i],T[j]) for (i,j),b in E.items() if not (y|n)&b]);print('core-only positive clauses failing in some models:',sum(1 for m,l,h in base if m&~mask==0 and l==1 and any(not s&m for s in S)))
