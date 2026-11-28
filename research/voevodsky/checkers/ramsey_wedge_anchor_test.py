"""Test every triple as a common anchor; also seek irreducible anchor-free certificates."""
from itertools import combinations
from random import Random
from pathlib import Path
import json
from pysat.solvers import Solver
from ramsey_wedge_region_core import setup


def audit():
    corners,v,base,top,groups,names,clauses=setup();out=[]
    for s,t,u in [('*00','**1','*1*'),('**0','*01','*11')]:
        fixed=[[-v[frozenset((s,p))]] for p in (t,u)];anchors=[];spread=None;tried=0;best=None
        with Solver(name='cadical195',bootstrap_with=base+fixed+clauses) as sl:
            for tri in combinations(corners,3):
                inside=[i for i in groups if set(tri)<=set(names[i])];outside=[i for i in groups if i not in inside];assert len(inside)==10
                anchors.append(dict(triple=tri,alone_excludes=not sl.solve(assumptions=inside),without_excludes=not sl.solve(assumptions=outside)))
            rng=Random(4354)
            for trial in range(40):
                tried+=1;ids=list(groups);rng.shuffle(ids);assert not sl.solve(assumptions=ids);core=set(sl.get_core());order=[i for i in ids if i in core]
                for i in order:
                    if not sl.solve(assumptions=sorted(core-{i})):core.remove(i)
                shared=set.intersection(*(set(names[i]) for i in core))
                if best is None or len(shared)<len(best['intersection']):
                    assert all(sl.solve(assumptions=sorted(core-{i})) for i in core);best=dict(intersection=sorted(shared),regions=[names[i] for i in sorted(core)])
                if not shared:
                    assert all(sl.solve(assumptions=sorted(core-{i})) for i in core);spread=[names[i] for i in sorted(core)];break
        out.append(dict(wedge=[s,t,u],anchors=anchors,empty_intersection_certificate=spread,trials=tried,smallest_observed_intersection=best));print(s,'sufficient',[r['triple'] for r in anchors if r['alone_excludes']],'necessary',[r['triple'] for r in anchors if not r['without_excludes']],'spread',len(spread or []),'tries',tried,'best',best['intersection'],len(best['regions']),flush=True)
    (Path(__file__).resolve().parents[1]/'results/ramsey_wedge_anchor_test.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
