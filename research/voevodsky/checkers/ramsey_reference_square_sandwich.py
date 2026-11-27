"""Exact trial in Cl(2,0). Relations carry invertible sandwich actions, not updates."""
from itertools import product
from pathlib import Path
import json
# Blade mask order: 1, e1, e2, e12. All representatives here are unit blades.
def mul(a,b):
    s,x=a;t,y=b
    return s*t*(-1 if x&2 and y&1 else 1),x^y

def inv(a):return (a[0]*mul(a,a)[0],a[1])

def image(g,x):return mul(mul(g,x),inv(g))

def audit(square):
    a,b,c,d=square # a:R2->B2, b:R2->B3, c:R3->B2, d:R3->B3
    if d is None:return 'undefined'
    # Same endpoints R2 and R3, two ways to compare their frames.
    p=mul(inv(c),a);q=mul(inv(d),b)
    return tuple(image(p,(1,i))==image(q,(1,i)) for i in (1,2))

def main():
    I=(1,0);G=[(1,x) for x in range(4)];outside={}
    for d in [None,*G,(-1,0)]:outside[str(d)]=audit([I,I,I,d])
    assert outside[str(None)]=='undefined' and outside[str((-1,0))]==(True,True)
    counts={}
    for square in product(G,repeat=4):
        k=str(audit(square));counts[k]=counts.get(k,0)+1
    assert set(counts.values())=={64}
    # If every link is derived from immutable vertex frames, both routes telescope.
    for r,s,b,c in product(G,repeat=4):
        edge=lambda x,y:mul(y,inv(x));assert audit([edge(r,b),edge(r,c),edge(s,b),edge(s,c)])==(True,True)
    out=dict(scope='Trial using basis vector probes and unit-blade sandwich maps, not an assumed Ramsey source law.',opposite_edge_controls=outside,all_link_assignments=counts,vertex_frame_assignments=256)
    p=Path(__file__).resolve().parents[1]/'results/ramsey_reference_square_sandwich.json';p.write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()
