"""Seek strict best-cut failures on planes of the four-bit profile cube. Small coordinate support suffices: unused coordinates cannot change the cuts."""
from itertools import combinations
from functools import reduce
from operator import xor
from random import Random

def trial(n):
    free=[j for j in range(n) if j and j&(j-1)];P={sum(1<<i for i,x in enumerate(free) if x in q):q for q in combinations(range(n),4) if reduce(xor,q)==0};B=sorted(P);hs=range(1,1<<len(free));cuts={h:sum(1<<i for i,b in enumerate(B) if (b&h).bit_count()%2) for h in hs};rng=Random(38)
    def strict(m,cert=False):
        if not m:return False
        r={h:m&~c for h,c in cuts.items()};lo=min(x.bit_count() for x in r.values());top=[h for h in hs if r[h].bit_count()==lo];finish=lambda h:next((k for k,c in cuts.items() if not r[h]&~c),None)
        if not lo or any(finish(h) for h in top):return False
        pair=next(((h,finish(h)) for h in hs if finish(h)),None)
        if not pair:return False
        return (top,lo,pair) if cert else True
    for _ in range(10000):
        a,b,h=rng.sample(list(hs),3);ok=cuts[a]|cuts[b];rest=ok&~cuts[h];pool=[i for i in range(len(B)) if rest>>i&1];m=ok&cuts[h]
        for i in rng.sample(pool,min(len(pool),rng.randint(3,7))):m|=1<<i
        if not strict(m):continue
        for i in range(len(B)):
            if strict(m&~(1<<i)):m&=~(1<<i)
        top,lo,pair=strict(m,True);bs=[v for i,v in enumerate(B) if m>>i&1];print('profiles used',n,'free',free,'directions',bs,'planes',[P[v] for v in bs]);print('best first cuts:',top,'cover',len(bs)-lo,'of',len(bs));print('optimal pair:',pair,'individual cover',[sum((h&v).bit_count()%2 for v in bs) for h in pair]);
        for h in top:
            rem=[v for v in bs if (v&h).bit_count()%2==0];odd=next(q for k in range(3,len(rem)+1,2) for q in combinations(rem,k) if reduce(xor,q)==0);print('best bit',h,'leaves odd dependency',odd)
        # Realize exactly these constraints in a partial three-row table. Reserve one
        # (row pair, base XOR) per plane so different planes create no extra conflicts.
        used=set();cells=[]
        def place(i):
            if i==len(bs):return True
            q=P[bs[i]]
            for r,s in combinations(range(3),2):
                for y in q[1:]:
                    x=q[0];key=(r,s,x^y)
                    if key in used:continue
                    z,w=sorted(set(q)-{x,y});used.add(key);cells.append((r,s,x,y,z,w))
                    if place(i+1):return True
                    used.remove(key);cells.pop()
            return False
        assert place(0);print('partial table (row pair, blue column pair, red column pair):',cells)
        return bs,free,pair,top,P
if __name__=='__main__':
    for n in range(10,17):
        if trial(n):break
