"""Classify residual failures after the 8-step guard passes, by minimum Hall-deficient set on either side and by how isolated vertices lost their last neighbors. Compare full 118 unordered 3+7 controls."""
from itertools import combinations
from ramsey_strip_guard_rule import ps,N,s,t,full,fill,Counter,leaves
C=Counter();origin=Counter();whole=Counter();examples={}
for p in ps:
    L=leaves(p);gs=[(v,w) for d,v,w in L if d==8]
    for q in ps:
        if not set(p).isdisjoint(q):continue
        rem=frozenset(full-set(p)-set(q)-{s,t});ok=fill(rem);iso={x for x in rem if not (N[x]&rem)};witness=None
        if not ok:
            for k in range(1,5):
                for U in combinations(sorted(rem),k):
                    if len({v<15 for v in U})!=1:continue
                    V=set.union(*(N[x]&rem for x in U))
                    if len(V)<k:witness=(U,sorted(V));break
                if witness:break
            assert witness
        kind=(len(iso),len(witness[0]) if witness else 0);whole[kind]+=int(p<q)
        if len(gs)!=1:continue
        v,w=gs[0];strands=v not in q and w in q;C[strands,ok,kind]+=1
        if not strands and not ok:
            examples.setdefault(kind,(p,q,sorted(rem),witness));origin[tuple(sorted(sum(y in (s,*p,t) for y in N[x]) for x in iso))]+=1
print('strands,closes,(isolates,min Hall size):',C,'unstranded isolate neighbors already used on first half:',origin,'all unordered:',whole);print('examples:',examples)
from ramsey_strip_unmirrored_holdout import groups
wider=Counter();sample=None
for (length,_),paths in groups.items():
    for p,q in combinations(paths,2):
        if not set(p).isdisjoint(q):continue
        rem=frozenset(full-{s,t}-set(p)-set(q));ok=fill(rem);iso=any(not N[x]&rem for x in rem);k=0 if ok else 1
        if not ok and not iso:
            k,U,V=min((len(U),U,tuple(sorted(V))) for side in (True,False) for n in range(2,len(rem)//2+1) for U in combinations(sorted(v for v in rem if (v<15)==side),n) for V in [set.union(*(N[v]&rem for v in U))] if len(V)<n)
            if sample is None:sample=(length,U,V)
        wider[length,k]+=1
print('wider by length,minimum obstruction (0=closes):',wider,'example',sample)
