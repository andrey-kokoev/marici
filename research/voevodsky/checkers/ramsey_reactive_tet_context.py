"""Context test: globally resolved pure responder functions, once per role identity."""
from itertools import combinations,product
from pathlib import Path
from collections import Counter
import json

# (red index, blue index), labels fixed in the join.  N is a responder only.
AB=frozenset({(2,1),(2,2)});base=frozenset({(1,2)});universe=sorted(AB|base)

def role(side,i):
    def bind(links):
        incident=frozenset(e for e in links if e[side]==i)
        def resolved(full):
            if i==1:return frozenset() # neutral: no positive reply to negation
            if side==0:return incident if AB<=full else frozenset()
            return incident & base
        return resolved
    return bind

def resolve(parts,override=None):
    net=frozenset.union(*parts);full=net if override is None else override
    # Merge all incident bindings at each named responder before resolution.
    keys={(side,e[side]) for e in net for side in (0,1)};positive=[set(),set()]
    for side,i in keys:positive[side].update(role(side,i)(net)(full))
    return tuple(map(frozenset,positive))

def combine(a,b):return tuple(x|y for x,y in zip(a,b))
def final(pos):return not all(pos)
def run():
    regions=[frozenset(c) for k in range(4) for c in combinations(universe,k)];counts=Counter()
    for a,b in product(regions,repeat=2):
        u=a|b;exact=resolve([a,b]);assert exact==resolve([b,a])==resolve([u,u]);counts['joins']+=1
        if final(combine(resolve([a]),resolve([b])))!=final(exact):counts['local_or_decision_errors']+=1
        assert combine(resolve([a],u),resolve([b],u))==exact # reference equality, not execution plan
    a=base|{(2,1)};b=frozenset({(2,2)});w=[resolve([a]),resolve([b]),resolve([a,b])];assert [final(x) for x in w]==[True,True,False]
    out=dict(scope='Synthetic joint responder: R2 needs both named incidences; B2 replies positively on (1,2); neutral responders at position 1. Exterior-aware projections are compared extensionally. No time or source-law claim.',counts=counts,regions=[sorted(a),sorted(b)],terminal_positive=[list(map(sorted,v)) for v in w]);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_reactive_tet_context.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
