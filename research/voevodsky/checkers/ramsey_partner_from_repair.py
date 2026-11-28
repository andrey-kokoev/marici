"""Complete one required red pair directly; check labeled edges against exhaustive two-link repairs."""
from itertools import combinations,permutations
from collections import defaultdict,Counter
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import D
from ramsey_two_repairs_opposite import run
import json


def audit():
    reference=defaultdict(set)
    for sq,c,rs in run():
        options=[p for p in combinations(rs,2) if set(p[0]).isdisjoint(p[1]) and all(set(r)&set(p[0]+p[1]) for r in sq)]
        matching,=[(p,q) for p,q in combinations(options,2) if set(p).isdisjoint(q)]
        for p,q in permutations(matching):reference[sq,c,p].add(q)
    hist=Counter();kinds=Counter();examples={}
    for sq,_,cs in charts():
        U=set().union(*sq);f,=set.intersection(*map(set,sq));mov=U-{f};W=set(range(1,11))-U
        for X in combinations(sorted(mov),2):
            if any(set(X)<=set(r) for r in sq):continue
            edge=(X[0]-1,X[1]+1);Y=mov-set(X)
            if not set(edge)<=W or any(abs(i-j)==1 for i in edge for j in Y):continue
            for c in cs:
                if edge in c:continue
                K=W-set(edge);ab,=[e for e in combinations(sorted(K),2) if e in c];h,=K-set(ab)
                for x,z in permutations(X):
                    fx=x-1 if x<z else x+1;fz=z+1 if x<z else z-1
                    for k,a in permutations(ab):
                        for y,w in permutations(sorted(Y)):
                            if abs(y-a)==1:continue
                            pair=lambda *ss:tuple(sorted(tuple(sorted(s)) for s in ss));base=pair((x,h,k),(z,y,a));out={};clear=all(abs(f-v)!=1 for v in edge)
                            if abs(k-w)!=1:
                                out['keep x, switch outside pair']=pair((x,h,a),(z,w,k))
                                if clear and tuple(sorted((k,fz))) in c:out['switch x and outside pair']=pair((z,h,a),(x,w,k))
                            if clear and abs(w-a)!=1:out['switch x, keep outside pair']=pair((z,h,k),(x,w,a))
                            assert set(out.values())==reference.pop((sq,tuple(sorted(c)),base),set());hist[len(out)]+=1;kinds.update(out.keys());examples.setdefault(len(out),dict(square=sq,cycle=sorted(c),installed=base,partners=out))
    assert not reference and sum(k*v for k,v in hist.items())==552;res=dict(by_partner_count=hist,partner_types=kinds,examples=examples);print(hist,kinds);print(examples.get(3));(D/'ramsey_partner_from_repair.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':audit()
