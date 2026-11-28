"""Construct common quartets on the 5/10 square and its reflection; cycles only for replay."""
from itertools import combinations, permutations
from ramsey_pentagon_selector import charts,path
from ramsey_inherited_swap_selector import D
import json


def build(sq):
    U=set().union(*sq);W=set(range(1,11))-U;f,=set.intersection(*map(set,sq));mov=U-{f}
    for x,z in combinations(sorted(mov),2):
        u,v=x-1,z+1;Y=mov-{x,z}
        if any({x,z}<=set(r) for r in sq) or not {u,v}<=W:continue
        # Path forces p-u and v-q. If uv were red, the fifth site must close
        # p-u-v-q into a pentagon. A distance-two end link forbids this.
        p,q=u-1,v+1
        if not {p,q}<=W:continue
        middle,=W-{p,u,v,q};ends=[i for i in (p,q) if abs(i-middle)==2]
        if len(ends)!=1:continue
        S={ends[0],middle};a,={p,q}-S
        if any(abs(i-j)==1 for i in Y|{f} for j in (u,v)) or any(abs(a-y)==1 for y in Y):continue
        for y,w in permutations(sorted(Y)):
            rs=[tuple(sorted(r)) for r in [S|{x},{z,y,a},S|{z},{x,w,a}]]
            yield dict(missed=(u,v),common_pair=sorted(S),remaining=a,rows=rs,red_pairs=[(rs[0],rs[1]),(rs[2],rs[3])])


def audit():
    seed=((1,4,7),(1,4,8),(2,4,7),(2,4,8));mirror=tuple(sorted(tuple(sorted(11-i for i in r)) for r in seed));out=[]
    for sq,_,cs in charts():
        if sq not in (seed,mirror):continue
        proposals=list(build(sq));assert len(proposals)==2
        for choice in proposals:
            rs=choice['rows']
            for c in cs:
                E=path|c|{(i,11+j) for j,r in enumerate(sq) for i in r}|{(i,15+j) for j,r in enumerate(rs) for i in r}|{(11+i,15+j) for i,r in enumerate(sq) for j,s in enumerate(rs) if set(r).isdisjoint(s)}|{(15,16),(17,18)}
                assert not any(all(p in E for p in combinations(q,2)) for q in combinations(range(1,19),3))
                assert not any(all(p not in E for p in combinations(q,2)) for q in combinations(range(1,19),7))
                for p in [(15,16),(17,18)]:assert any(all(e not in E-{p} for e in combinations(q,2)) for q in combinations(range(1,19),7))
        out.append(dict(square=sq,cycles_checked=len(cs),proposals=proposals))
    assert len(out)==2;(D/'ramsey_shared_quartet_from_labels.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':audit()
