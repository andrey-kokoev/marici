"""Compare signed electron Pauli-commutator axes with proton directed edge displacements in the documented common tetrahedral frame. Test all port permutations within each fixed source face."""
from itertools import permutations,product,combinations
from fractions import Fraction as F
from pathlib import Path
import json
D=Path(__file__).resolve().parent;load=lambda f:json.loads((D.parents[1]/f).read_text());pts=dict(A=(1,1,1),B=(1,-1,-1),C=(-1,1,-1),D=(-1,-1,1))
def cross(a,b):return tuple(a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3] for i in range(3))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def run():
    spin=load('voevodsky/results/electron_tetrahedral_spinor_store.json');n=[tuple(3*F(v) for u,v in w) for w in spin['normals']];faces=[set(pts)-{next(s for s,v in pts.items() if tuple(-x for x in v)==u)} for u in n];geo=load('nima/results/twelve-triangle-positive-geometry.json')['triangles_and_transports'];ports=[[z['outer_arrow'] for z in geo if set(z['triangle'][0][2:])==f] for f in faces];vec=lambda e:tuple(y-x for x,y in zip(pts[e[0]],pts[e[1]]));pairs=list(permutations(range(4),2));axes=[cross(n[i],n[j]) for i,j in pairs];correct=[next(e for e in ports[i] if set(e)==faces[i]&faces[j]) for i,j in pairs];assert list(map(vec,correct))==axes
    marks=['AB','AC','AD','BC','BD','CD'];layouts=[sum((list(b) for b in choice),[]) for choice in product(*(permutations(w) for w in ports))];tests={}
    for num in (1,2):
        for es in combinations(marks,num):
            sig=lambda u:tuple(dot(u,vec(e)) for e in es);ref=list(map(sig,axes));tests[' '.join(es)]=sum(all(sig(vec(e))==r for e,r in zip(q,ref)) for q in layouts)
    return dict(crossings=list(zip(pairs,correct)),layout_count=len(layouts),surviving=tests)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_crossing_axis_scramble.json').write_text(json.dumps(out)+'\n')
