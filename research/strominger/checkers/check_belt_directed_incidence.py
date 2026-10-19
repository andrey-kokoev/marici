"""Source-bound directed-incidence test; no sign-fitted radial directions."""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations, product
from collections import defaultdict
import hashlib,json
from assemble_real_complex_arrows import run, ROOT

BASE=ROOT/'research/strominger'
hashes={}
def read(p):
    raw=(ROOT/p).read_bytes();hashes[p]=hashlib.sha256(raw).hexdigest()
    return json.loads(raw)
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def mean(vs):return tuple(sum(v[i] for v in vs)/len(vs) for i in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sign(x):return (x>0)-(x<0)
def parity(xs):return (-1)**sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))
def addcell(chain,cell,c):
    key=tuple(sorted(cell));chain[key]+=c*parity([key.index(x) for x in cell])
def clean(c):return {k:v for k,v in c.items() if v}
def boundary(chain):
    out=defaultdict(int)
    for cell,c in chain.items():
        for i in range(len(cell)):addcell(out,cell[:i]+cell[i+1:],c*(-1)**i)
    return clean(out)
def push(chain,perm):
    out=defaultdict(int)
    for cell,c in chain.items():addcell(out,tuple(perm[x] for x in cell),c)
    return clean(out)
def enc(chain):return [[list(k),v] for k,v in sorted(chain.items())]

def main():
    read('research/strominger/inputs/belt-directed-incidence-protocol-v1.json')
    source=read('research/strominger/inputs/neutron-real-complex-arrows.json')
    prior=read('research/strominger/results/neutron-real-complex-assembly.json')
    geometry=read('research/voevodsky/results/four_six_center_cones.json')
    opposite=read('research/voevodsky/results/opposite_branch_belt_store.json')
    current=run(source)
    assert all(current[k]==prior[k] for k in ('decoded_source','geometry','cycle'))
    points={k:tuple(map(F,v)) for k,v in geometry['belt_scaled_coordinates'].items()}
    # Original arrow chart (r,a,b) -> stored belt chart (b,r,a).
    convert=lambda p:(F(p[2]),F(p[0]),F(p[1]))
    vertices=current['cycle']['geometry']['vertices'];lookup={v:k for k,v in points.items()}
    labels=[lookup[convert(v)] for v in vertices]
    generated=[tuple(labels[i] for i in face) for face in current['cycle']['geometry']['carrier_facets']]
    faces=[tuple(f) for f in geometry['belt_faces']]
    assert {frozenset(f) for f in generated}=={frozenset(f) for f in faces}
    assert all(dot(mean([points[k] for k in f]),cross(sub(points[f[1]],points[f[0]]),sub(points[f[2]],points[f[0]])))>0 for f in generated)
    A=[[F(x) for x in row] for row in current['decoded_source']['generators'][0]['matrix']]
    def advance(v):
        p=(v[1],v[2],v[0]);q=tuple(sum(a*x for a,x in zip(row,p)) for row in A)
        return (q[2],q[0],q[1])
    perm={k:lookup[advance(v)] for k,v in points.items()}
    wanted=opposite['face_signs'];assert len(wanted)==6 and set(wanted)=={-1,1}
    rows=[]
    for i,f in enumerate(faces):
        vs=[points[k] for k in f];center=mean(vs)
        normal=cross(sub(vs[1],vs[0]),sub(vs[2],vs[0]))
        tetcenter=tuple(x*F(3,4) for x in center)
        ds={'global_outgoing':center,'global_incoming':neg(center),
            'constituent_outgoing':sub(center,tetcenter),
            'constituent_incoming':sub(tetcenter,center),
            'scheduled_centroid_chord':sub(advance(center),center),
            'upper_to_lower_axis':(F(0),F(-7,10),F(0))}
        beta={k:-dot(d,normal) for k,d in ds.items()}
        # Small centroid-edge triangles have exactly 1/3 this area bivector.
        assert all(cross(sub(vs[j],center),sub(vs[(j+1)%3],center))==tuple(x/3 for x in normal) for j in range(3))
        rows.append({'face':list(f),'expected':wanted[i], 'pairings':{k:str(v) for k,v in beta.items()},'signs':{k:sign(v) for k,v in beta.items()}})
    outputs={k:[r['signs'][k] for r in rows] for k in rows[0]['signs']}
    assert outputs['global_incoming']==[1]*6 and outputs['global_outgoing']==[-1]*6
    assert outputs['constituent_incoming']==[1]*6 and outputs['constituent_outgoing']==[-1]*6
    assert all(outputs[k]!=wanted for k in ('global_incoming','global_outgoing','constituent_incoming','constituent_outgoing'))
    # A common axial direction is a different contraction rule, not radial d.
    assert outputs['upper_to_lower_axis']==wanted
    internal=set()
    owners=defaultdict(list)
    tets=[]
    for i,f in enumerate(faces):
        tet=('O',)+f;tets.append(tet)
        for face in combinations(tet,3):owners[tuple(sorted(face))].append(i)
    internal={k for k,v in owners.items() if len(v)==2}
    def signed_chain(ss):
        c=defaultdict(int)
        for t,s in zip(tets,ss):addcell(c,t,s)
        return clean(c)
    c=signed_chain(wanted);b=boundary(c);seams={k:v for k,v in b.items() if k in internal}
    assert len(seams)==6 and all(abs(v)==2 for v in seams.values())
    assert boundary(b)=={}
    coherent=[ss for ss in product((-1,1),repeat=6) if not any(k in internal for k in boundary(signed_chain(ss)))]
    assert set(coherent)=={(-1,)*6,(1,)*6}
    # Existing geometry transition transports the WHOLE signed boundary,
    # including its nonzero seam record. This is not a WG identification.
    assert push(c,perm)==c and push(b,perm)==b and push(seams,perm)==seams
    assert boundary(push(c,perm))==push(boundary(c),perm)
    inverse={v:k for k,v in perm.items()}
    assert push(push(c,perm),inverse)==c
    # Exhaustive chain naturality and recovery, not merely the invariant mode.
    for ss in product((-1,1),repeat=6):
        cc=signed_chain(ss)
        assert boundary(push(cc,perm))==push(boundary(cc),perm)
        assert push(push(cc,perm),inverse)==cc
    # Source-domain audit: the retained WG uses the connected four-vertex
    # six-occurrence seed; the belt uses two disjoint three-cycles.
    agda=ROOT/'research/nima/agda/SeedJointParityResponse.agda'
    text=agda.read_text(encoding='utf-8')
    for e in ('AB','BC','CA','AD','DB','BA'):
        assert f'first-step {e} b = '+('not b' if e=='AB' else 'b') in text
        assert f'second-step {e} b = '+('not b' if e=='BA' else 'b') in text
    edges=source['arrow_families'][0]
    assert len({x for e in edges for x in e})==6
    assert not any([b,a] in edges for a,b in edges)
    checks={'source_assembler_replayed_in_memory':True,'all_six_faces_identified_in_original_geometry':True,
        'radial_rule_fails_alternation_on_all_eighteen_small_triangles_as_a_pattern':True,
        'axial_alternative_matches_but_changes_direction_contract':True,
        'six_internal_orientation_defects_retained':True,'all_64_signed_chains_transport_and_reverse':True,
        'only_uniform_signs_are_internal_seam_free':True,'WG_and_belt_occurrence_domains_are_not_identical':True}
    paths=[Path(__file__),ROOT/'research/strominger/checkers/assemble_real_complex_arrows.py',ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',ROOT/'research/voevodsky/checkers/evolve_relative_geometry_modes.py',ROOT/'research/voevodsky/checkers/check_directed_incidence_orientation.py',agda,ROOT/'research/nima/agda/SeedGeometricResponseState.agda',ROOT/'research/nima/agda/ActualSeedEndpointTable.agda']
    for p in paths:hashes[p.relative_to(ROOT).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    result={'status':'pass','checks':checks,'source_hashes':hashes,'expected_face_signs':wanted,'tested_sign_patterns':outputs,
        'face_pairings':rows,'internal_orientation_defects':enc(seams),'full_signed_boundary':enc(b),'native_vertex_permutation':perm,
        'claims':{'unchanged_radial_rule':'rejected: three of six faces mismatch for either uniform radial direction',
        'axial_contraction':'exact alternating signs from retained upper-to-lower rim axis, conditional on replacing radial direction by this common axis',
        'native_C3_defect_transport':'constructed: full chain boundary commutes and reverses on all 64 sign assignments',
        'WG_defect_attachment':'not established: no typed map from the four-vertex WG occurrence carrier to the six-vertex belt face/interface record is supplied or constructed',
        'WG_filler':'not established; retaining a nonzero signed boundary does not cancel it'},
        'scope':'No other-owner files written; no Agda compilation; finite source arithmetic and source-domain audit only.'}
    out=BASE/'results/belt-directed-incidence';out.mkdir(parents=True,exist_ok=True)
    (out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','checks':len(checks),'sign_patterns':outputs,'expected':wanted,'internal_defects':len(seams),'WG_attachment':'unestablished'}))
if __name__=='__main__':main()
