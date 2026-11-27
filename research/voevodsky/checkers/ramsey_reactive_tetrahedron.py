"""Local carrier test; no rule for the graph-wide absence computeds is assumed."""
from itertools import permutations
from fractions import Fraction
import json
from pathlib import Path


def run():
    # Candidate binding of the as-yet unnamed vertices.  Keep outputs callable.
    names=('R','B','RorN','BorN');coords=dict(zip(names,[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]));mid=lambda a,b:tuple((Fraction(x)+y)/2 for x,y in zip(a,b));pairs=[(('R','B'),('RorN','BorN')),(('R','RorN'),('B','BorN')),(('R','BorN'),('B','RorN'))];req={('R','BorN'),('B','RorN')}
    out=[]
    for (a,b),(c,d) in pairs:
        center=mid(mid(coords[a],coords[b]),mid(coords[c],coords[d]));edges=[k for k in req if set(k) in ({a,b},{c,d})];out.append(dict(edges=[[a,b],[c,d]],center=list(map(str,center)),admitted_requests=sorted(edges)))
    assert len({tuple(q['center']) for q in out})==1 and [len(q['admitted_requests']) for q in out]==[0,0,2]
    sym=[]
    for p in permutations(names):
        m=dict(zip(names,p));
        if {(m[a],m[b]) for a,b in req}==req:sym.append(p)
    assert len(sym)==2
    result=dict(candidate_binding=names,pairings=out,typed_request_symmetries=sym,scope='Equality of geometric centers and admissibility of local requests, not equality of terminal values or a derivation of the two responder roles.');print(result);(Path(__file__).resolve().parents[1]/'results/ramsey_reactive_tetrahedron.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':run()
