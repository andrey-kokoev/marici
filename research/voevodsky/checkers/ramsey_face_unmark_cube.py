"""Forget five marked sites and their correspondence. Use only unlabeled H and abstract pocket types during search. Compare survivors with intact marking afterwards."""
from itertools import product,combinations
from functools import lru_cache
from collections import Counter
import json
from ramsey_face_pair_obstruction import bits,ind,CAT,D,decode
from ramsey_cube_construct35 import G,cells

def iso(a,b):
    n=len(a);order=sorted(range(n),key=lambda i:sum(x.bit_count()==a[i].bit_count() for x in b));p=[0]*n
    def go(k,used):
        if k==n:yield tuple(p);return
        i=order[k]
        for j,x in enumerate(b):
            if used>>j&1 or x.bit_count()!=a[i].bit_count() or any((a[i]>>v&1)!=(x>>p[v]&1) for v in order[:k]):continue
            p[i]=j;yield from go(k+1,used|1<<j)
    yield from go(0,0)
def rel(g,vs):return [sum(1<<j for j,y in enumerate(vs) if g[x]>>y&1) for x in vs]
def audit():
    z=cells.index('0**');f=G[34]&G[z];H=bits(((1<<35)-1)&~(G[z]|G[34]|1<<34|1<<z));a=rel(G,H);assert sum(x.bit_count() for x in a)==106;b=decode((CAT/'r35_13.g6').read_text().strip());types=[r for r in json.loads((D.parent/'ramsey_face_double_root.json').read_text())['marked'] if r['e']==53 and r['catalogue']];I=ind(a);S=set(I);tri=[s for s in I if s.bit_count()==3];six=[s for s in I if s.bit_count()==6];autos=list(iso(a,a));autb=list(iso(b,b));stats=[];passed=set();classes=set()
    @lru_cache(None)
    def miss(s):return sum(1<<j for j,v in enumerate(six) if not v&s)
    def feasible(ds,ms=0):return not ds or any(not miss(s)&ms and feasible(ds[1:],ms|miss(s)) for s in ds[0])
    def image(mask,p):return sum(1<<p[i] for i in bits(mask))
    for r in types:
        q,t=r['q'],r['t'];p=bits(8191^(q|t));stab=[h for h in autb if image(q,h)==q and image(t,h)==t];perms=[[p.index(h[i]) for i in p] for h in stab];counts=Counter();candidate_classes=set()
        def canon(ls):return (q,t,min(tuple(h[ls[i]] for i in pm) for pm in perms for h in autos))
        for ls in product(*[[j for j,v in enumerate(a) if v.bit_count()==4+sum(b[i]>>k&1 for k in p)] for i in p]):
            if len(set(ls))!=5 or any((a[ls[i]]>>ls[j]&1)!=(b[p[i]]>>p[j]&1) for i,j in combinations(range(5),2)):continue
            counts['structural']+=1;key=canon(ls);candidate_classes.add(key);mark=sum(1<<i for i in ls);ts=[s for s in tri if not s&mark];passed_sides=0
            for group in (q,t):
                ds=[]
                for v in bits(group):
                    req=sum(1<<h for i,h in zip(p,ls) if b[v]>>i&1);ds.append([s|req for s in ts if s|req in S]);
                if not feasible(sorted(ds,key=len)):break
                passed_sides+=1
            if passed_sides>=1:counts['first']+=1
            if passed_sides==2:counts['both']+=1;classes.add(key);passed.add((q,t,tuple(ls)))
        stats.append(dict(q=q,t=t,counts=counts,structural_orbits=len(candidate_classes)))
    # Only now use the true pocket and its colors to identify the known marking, via abstract isomorphisms.
    Q=G[34]&~f;T=G[z]&~f;P=bits(((1<<35)-1)&~(f|__import__('functools').reduce(int.__or__,(G[i] for i in bits(f)))));assert len(P)==13;true=set()
    for h in iso(b,rel(G,P)):
        h=[P[i] for i in h];q=sum(1<<j for j,v in enumerate(h) if Q>>v&1);t=sum(1<<j for j,v in enumerate(h) if T>>v&1);p=bits(8191^(q|t));ls=tuple(H.index(h[j]) for j in p)
        for g in autos:true.add((q,t,tuple(g[j] for j in ls)))
    orbit_results=[dict(q=q,t=t,sites=[H[i] for i in ls],known=(q,t,ls) in true) for q,t,ls in sorted(classes)];assert any(r['known'] for r in orbit_results);out=dict(core_aut=len(autos),pocket_aut=len(autb),stats=stats,passed=len(passed),survivor_orbits=orbit_results);print(out);(D.parent/'ramsey_face_unmark_cube.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
