"""Retained three-witness cone: exact incidence, recovery and hostile.
Formal higher coherence is checked separately in ThreeWitnessRetainedCone.agda.
"""
from dataclasses import dataclass,replace
from fractions import Fraction as F
from itertools import combinations,permutations
from pathlib import Path
import hashlib,json
from check_charge_mass_recoil_triangle import direct,scale,impulse
ROOT=Path(__file__).resolve().parents[1]

@dataclass(frozen=True)
class Context:
    q1:F; q2:F; m1:F; m2:F; kernel:tuple

@dataclass(frozen=True)
class Comparison:
    left:tuple; right:tuple

@dataclass(frozen=True)
class Packet:
    context:Context
    ab:Comparison
    bc:Comparison
    ac:Comparison
    # Retain both face routes, not just a shared scalar.
    face_routes:tuple=(('ab','bc'),('ac',))

@dataclass(frozen=True)
class View:
    slot:int
    whole:Packet

def execute(route,c):
    a,b=direct(c.q1,c.q2,c.m1,c.m2,c.kernel)
    named={'A':scale(c.m1,a),'B':scale(-c.m2,b),'C':impulse(c.q1,c.q2,c.kernel)[0]}
    value=named[route[0]]
    for token in route[1:]:
        if token=='unit-x':value=(value[0]+1,)+value[1:]
        elif token!='identity':raise ValueError('unsupported route operation')
    return value

def validate(p):
    c=p.context
    for w in (p.ab,p.bc,p.ac):
        if execute(w.left,c)!=execute(w.right,c):return False
    return (p.face_routes==(('ab','bc'),('ac',))
            and execute(p.ab.right,c)==execute(p.bc.left,c)
            and execute(p.ab.left,c)==execute(p.ac.left,c)
            and execute(p.bc.right,c)==execute(p.ac.right,c))

def focus(v):
    return v.whole if v.slot==0 else (v.whole.ab,v.whole.bc,v.whole.ac)[v.slot-1]

def move(v,target):return View(target,v.whole)
def route(v,path):
    assert v.slot==path[0]
    for target in path[1:]:v=move(v,target)
    return v

def boundary(simplex):
    return {simplex[:i]+simplex[i+1:]:(-1)**i for i in range(len(simplex))}

def main():
    src=ROOT/'agda/ThreeWitnessRetainedCone.agda'
    proof=json.loads((ROOT/'results/agda-ThreeWitnessRetainedCone.json').read_text(encoding='utf-8-sig'))
    assert proof['passed'] and proof['ignore_interfaces'] and proof['inputs_stable_during_check']
    assert proof['source_sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
    c=Context(F(1),F(-2),F(2),F(3),(F(1),F(2),F(-1)))
    p=Packet(c,Comparison(('A',),('B',)),Comparison(('B',),('C',)),Comparison(('A',),('C',)))
    other=replace(p,bc=Comparison(('B',),('C','identity')))
    assert validate(p) and validate(other) and p!=other
    assert p.ab==other.ab and p.ac==other.ac
    views=[View(i,p) for i in range(4)]
    assert all(v.whole==p for v in views)
    assert all(View(i,p)!=View(i,other) for i in range(4))
    assert focus(View(1,p))==focus(View(1,other))  # Focus alone loses history.
    for i,j in combinations(range(4),2):
        assert move(move(views[i],j),i)==views[i]
    faces=list(combinations(range(4),3))
    for i,j,k in faces:
        assert route(views[i],(i,j,k))==route(views[i],(i,k))
    assert route(views[0],(0,1,2,3))==route(views[0],(0,2,3))==route(views[0],(0,1,3))==route(views[0],(0,3))
    controls=0
    for path in permutations(range(4)):
        assert route(views[path[0]],path)==views[path[-1]];controls+=1
    simplices=[list(combinations(range(4),k)) for k in range(5)]
    assert list(map(len,simplices))==[1,4,6,4,1]
    for level in simplices[2:]:
        for simplex in level:
            total={}
            for face,s in boundary(simplex).items():
                for edge,t in boundary(face).items():total[edge]=total.get(edge,0)+s*t
            assert all(v==0 for v in total.values())
    # A reversible twist of ONE apex link keeps the numerical readout and all
    # cell counts, but changes which retained history reaches a focused view.
    def twist(v,target):
        body=v.whole
        if {v.slot,target}=={0,1}:
            assert body in (p,other)
            body=other if body==p else p
        return View(target,body)
    for body in (p,other):
        for i,j in combinations(range(4),2):
            v=View(i,body)
            assert twist(twist(v,j),i)==v
            assert execute(twist(v,j).whole.bc.right,c)==execute(v.whole.bc.right,c)
    failed=[]
    for i,j,k in faces:
        if twist(twist(views[i],j),k)!=twist(views[i],k):failed.append((i,j,k))
    assert failed==[(0,1,2),(0,1,3)] and (1,2,3) not in failed
    bad=replace(p,bc=Comparison(('B',),('C','unit-x')))
    assert not validate(bad)
    # Lossless packaging of data cannot certify its original physical claim.
    for i,j,k in faces:
        assert route(View(i,bad),(i,j,k))==route(View(i,bad),(i,k))
    result=dict(schema='marici.nima.three-witness-retained-cone.v1',status='pass',
        classification='checked retained-presentation cone, not physical dynamics',
        obligation='attachment transport and route/coherencer compatibility',
        augmented_simplex_counts=[1,4,6,4,1],apex='the complete retained comparison packet',
        edge_count=6,face_count=4,full_order_route_controls=controls,
        formal='Safe Cubical proof constructs three lossless pointed views, six paths, a WG horn and its completed fourth face/interior; it recovers the original packet and supplied original triangle face.',
        numeric_fixture='The previous charge-mass-recoil example, including three actual route comparisons. This Python fixture is not a formal Agda encoding of physical charge or mass.',
        hostile={'all_edges_remain_invertible':True,'numerical_readouts_unchanged':True,
                 'original_witness_view_triangle_still_commutes':True,
                 'failed_apex_faces':failed,'reason':'one apex adapter changes the retained packet instead of preserving it'},
        invalid_input_control='An invalid original comparison can still be transported coherently as data; input validation rejects it. The formal PathWitnessTriangle specialization requires an actual original face proof.',
        conclusion='The backbone is constructible after adjoining the retained whole and specifying lossless views. Pairwise comparison counts alone do not force the apex, faithful transport or filler.',
        scope='A structural, path-coherent presentation cone. No independent geometric tetrahedron, particle dynamics or physical-time vertex is derived.')
    (ROOT/'results/three-witness-retained-cone.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
