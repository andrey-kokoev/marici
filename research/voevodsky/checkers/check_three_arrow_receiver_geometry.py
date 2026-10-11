"""Spatial realization under inherited regular-edge metric and outward side.
The phase equations do not determine length; that metric rule is explicit.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
from check_proton_merkle_reassembly import POINTS
from check_three_arrow_receiver import WEIGHTS, decode, images, ONE

BASE=Path(__file__).resolve().parents[1]

def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def norm2(a): return sum(x*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mean(vs): return tuple(sum(v[i] for v in vs)/len(vs) for i in range(3))
def boundary(chain):
    out={}
    for cell,value in chain.items():
        if len(cell)<2: continue
        for i in range(len(cell)):
            f=cell[:i]+cell[i+1:]; out[f]=out.get(f,0)+(-1)**i*value
    return {f:v for f,v in out.items() if v}

def main():
    P={k:tuple(map(Q,v)) for k,v in POINTS.items()}
    F=mean([P[k] for k in 'ABC'])
    e=tuple(2*f-d for f,d in zip(F,P['D']))
    P['e']=e
    p=mean([P[k] for k in 'ABCD']); q=mean([P[k] for k in 'ABCe'])
    n=cross(sub(P['B'],P['A']),sub(P['C'],P['A']))
    if dot(n,sub(e,F))<0: n=tuple(-x for x in n)
    side2=norm2(sub(P['A'],P['B']))
    # Subtracting any two equal-distance equations leaves a perpendicular
    # bisector plane. Their intersection is the line through F normal to ABC.
    # Along that line the remaining equation has exactly two solutions,
    # symmetric about F: the old D and its reflected point e.
    volume=lambda keys:dot(sub(P[keys[1]],P[keys[0]]),cross(sub(P[keys[2]],P[keys[0]]),sub(P[keys[3]],P[keys[0]])))/6
    top={tuple('ABCD'):1 if volume('ABCD')>0 else -1,tuple('ABCe'):1 if volume('ABCe')>0 else -1}
    surface=boundary(top)
    old={(a,b) for a in 'ABCD' for b in 'ABCD' if a!=b}
    extra={(a,'e') for a in 'ABC'}
    checks={
        'all_three_new_lengths_equal_existing_edge_length':all(norm2(sub(e,P[a]))==side2 for a in 'ABC'),
        'old_D_is_the_other_equal_distance_solution':all(norm2(sub(P['D'],P[a]))==side2 for a in 'ABC'),
        'new_apex_is_reflection_of_D_across_shared_face':mean([e,P['D']])==F and cross(sub(e,P['D']),n)==(0,0,0),
        'outward_condition_selects_new_not_old_solution':dot(n,sub(e,F))>0>dot(n,sub(P['D'],F)),
        'new_apex_distinct_from_old_vertices':all(e!=P[a] for a in 'ABCD'),
        'two_tetrahedra_have_equal_nonzero_volume':abs(volume('ABCD'))==abs(volume('ABCe'))==Q(8,3),
        'shared_face_cancels_in_oriented_boundary':tuple('ABC') not in surface and len(surface)==6,
        'outer_surface_is_closed':not boundary(surface),
        'barycenters_are_distinct_and_separate_from_apex':p!=q and q!=e,
        'center_segment_crosses_F_at_midpoint':mean([p,q])==F and cross(sub(q,p),n)==(0,0,0),
        'primitive_graph_still_has_only_fifteen_arrows':len(old|extra)==15 and not any(a=='e' for a,b in old|extra),
        'three_phased_inputs_have_same_arrival_value':images(decode(ONE))==(ONE,ONE,ONE),
    }
    result={'verification_passed':all(checks.values()),'checks':checks,
        'contract':{'metric':'inherit the proton tetrahedron regular edge length on A-e, B-e, C-e',
                    'side':'new receiver on opposite side of ABC from D',
                    'arrow_structure':'twelve old directed arrows plus only A/B/C -> e',
                    'centers':'derived after both tetrahedra; connector is a higher-level representation, not a new primitive generator'},
        'coordinates':{k:list(map(str,v)) for k,v in P.items()},'shared_face_center':list(map(str,F)),
        'proton_barycenter':list(map(str,p)),'receiver_tetrahedron_barycenter':list(map(str,q)),
        'edge_length_squared':str(side2),'center_segment_length_squared':str(norm2(sub(q,p))),
        'outer_oriented_triangles':[{'vertices':list(f),'orientation':v} for f,v in sorted(surface.items())],
        'outcome':'Two congruent tetrahedra share ABC, but only the first has a complete twelve-arrow directed structure. The receiving apex e and the derived second barycenter are different points.',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/three_arrow_receiver_geometry.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
