"""Smallest carrier on which a comparison can close a rectangle. No update schedule.
Bits enumerate incidences of a complete static realization, not stored role values.
"""
from itertools import product
from pathlib import Path
import json

edges=('R2:B2','R2:B3','R3:B2','R3:B3')
# An immutable reference to a pure, unresolved comparison at R2:B2.
def reference(rule):
    def bind(target):
        def continuation(net):return rule(net,target)
        return continuation
    return bind(edges[0])

def incident(net,target):return target in net and edges[1] in net

def both_ends(net,target):return incident(net,target) and edges[2] in net

def closed(net,target):return both_ends(net,target) and edges[3] in net

def run():
    states=[frozenset(e for e,b in zip(edges,bits) if b) for bits in product(range(2),repeat=4)];out={}
    for name,rule in [('same_role',incident),('both_endpoint_stars',both_ends),('closed_comparison',closed)]:
        ref=reference(rule);essential=[e for e in edges if any(ref(s)!=ref(s^{e}) for s in states)]
        # Test sufficiency rather than inferring it solely from a witness.
        for a,b in product(states,repeat=2):
            if a.intersection(essential)==b.intersection(essential):assert ref(a)==ref(b)
        out[name]=essential
    assert list(map(len,out.values()))==[2,3,4]
    a=frozenset(edges[:3]);b=frozenset(edges);assert a.intersection(edges[:3])==b.intersection(edges[:3]) and reference(closed)(a)!=reference(closed)(b)
    path=Path(__file__).resolve().parents[1]/'results/ramsey_immutable_reference_scope.json';path.write_text(json.dumps(dict(scope='Conditional on three declared response laws; each is evaluated only on a full realization. N still supplies its stipulated terminal response, so this control uses non-neutral bindings.',minimal_incidence_sets=out,open_square=sorted(a),closed_square=sorted(b)),indent=2)+'\n');print(out)

if __name__=='__main__':run()
