"""Exact edge-hinge kinematics for draft EF1; no native dynamics asserted."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3];HOME=Path(__file__).resolve().parent
CONTRACT=HOME/'contracts/edge-face-annihilation-conjecture.v1.json'
PROOF=HOME/'EDGE-FACE-ANNIHILATION-CONJECTURE.md'
RESULT=HOME/'results/edge-face-hinge.v1.json'
BASE=ROOT/'research/voevodsky'
sys.path.insert(0,str(BASE/'checkers'))
from check_proton_merkle_reassembly import POINTS


def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(k,a):return tuple(k*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mean(vs):return tuple(sum(v[i] for v in vs)/len(vs) for i in range(3))
def mm(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def tr(A):return list(map(list,zip(*A)))
def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def encode(A):return [[str(x) for x in row] for row in A]
def boundary(chain):
    out={}
    for cell,value in chain.items():
        for i in range(len(cell)):
            f=cell[:i]+cell[i+1:];out[f]=out.get(f,0)+(-1)**i*value
    return {f:v for f,v in out.items() if v}
def first_hit_fraction(normalized_travel):
    # Assumed constant-speed, finite-duration, absorbing-boundary toy law.
    assert normalized_travel>=0
    return min(Q(1),normalized_travel)

def validate_contract(c):
    assert c['schema']=='marici.scattering.edge-face-annihilation-conjecture.v1'
    assert c['status']=='proposed_explanatory_conjecture_not_test_ready'
    assert c['draft_id']=='EF1'
    assert ROOT/c['source_points']==BASE/'checkers/check_proton_merkle_reassembly.py'
    assert ROOT/c['existing_belt_receipt']==BASE/'results/three_tetrahedron_belt.json'
    for key in ('native_rotation_generator_constructed','finite_capture_probability_derived',
                'static_face_alignment_has_positive_angular_measure','outgoing_photon_factorization_constructed',
                'physical_species_binding_supplied','ratio_372_predicted','live_proposition_inventory_changed',
                'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    P={k:tuple(map(Q,v)) for k,v in POINTS.items()};M=mean([P['A'],P['B']])
    axis=sub(P['B'],P['A']);a,b=sub(P['C'],M),sub(P['D'],M)
    assert all(dot(sub(P[k],P[j]),sub(P[k],P[j]))==8 for j in P for k in P if j!=k)
    assert dot(a,axis)==dot(b,axis)==0
    G=[[dot(a,a),dot(a,b)],[dot(b,a),dot(b,b)]];assert G==[[6,2],[2,6]]
    assert det2(G)==32 and dot(a,b)/dot(a,a)==Q(1,3)
    plus=[[Q(),Q(-1)],[Q(1),Q(2,3)]];minus=[[Q(2,3),Q(1)],[Q(-1),Q()]]
    I=[[Q(1),Q()],[Q(),Q(1)]]
    assert mm(plus,minus)==mm(minus,plus)==I
    for R in (plus,minus):assert det2(R)==1 and mm(mm(tr(R),G),R)==G
    def at(coeff):return add(M,add(scale(coeff[0],a),scale(coeff[1],b)))
    def placement(R):return {P['A'],P['B'],at([R[0][0],R[1][0]]),at([R[0][1],R[1][1]])}
    initial=set(P.values());pos=placement(plus);neg=placement(minus)
    assert initial&pos=={P[k] for k in 'ABD'} and initial&neg=={P[k] for k in 'ABC'}
    P['e']=at([Q(2,3),Q(-1)])
    assert P['e']==sub(scale(2,mean([P[k] for k in 'ABC'])),P['D'])
    assert neg=={P[k] for k in 'ABCe'}
    # A generic non-overlapping placement: pi rotation. The common edge is
    # the only intersection, separated by the plane normal to a+b.
    opposite=placement([[Q(-1),Q()],[Q(),Q(-1)]]);normal=add(a,b)
    assert initial&opposite=={P['A'],P['B']}
    assert all(dot(normal,sub(x,M))>=0 for x in initial)
    assert all(dot(normal,sub(x,M))<=0 for x in opposite)
    assert all(dot(normal,sub(P[k],M))>0 for k in 'CD')
    def volume(t):
        x,y,z,w=[P[k] for k in t]
        return dot(sub(y,x),cross(sub(z,x),sub(w,x)))/6
    pair=[tuple('ABCD'),tuple('ABCe')];belt=[tuple('ABDe'),tuple('BCDe'),tuple('ACDe')]
    def oriented(ts):return {t:(1 if volume(t)>0 else -1) for t in ts}
    assert boundary(oriented(pair))==boundary(oriented(belt))
    assert len(boundary(oriented(pair)))==6
    assert sum(abs(volume(t)) for t in pair)==sum(abs(volume(t)) for t in belt)==Q(16,3)
    assert all(abs(volume(t))==Q(16,9) for t in belt)
    owner=json.loads((ROOT/c['existing_belt_receipt']).read_text(encoding='utf-8'))
    assert owner['verification_passed'] is True
    assert {k:tuple(map(Q,owner['coordinates'][k])) for k in P}==P
    controls=[]
    for key in ('native_rotation_generator_constructed','finite_capture_probability_derived',
                'static_face_alignment_has_positive_angular_measure','outgoing_photon_factorization_constructed',
                'ratio_372_predicted','C12_protocol_renewed','physical_outcomes_admitted'):
        bad=copy.deepcopy(c);bad[key]=True
        try:validate_contract(bad)
        except AssertionError:controls.append(key)
        else:raise AssertionError('unsupported promotion accepted: '+key)
    paths={CONTRACT,PROOF,Path(__file__),HOME/'test_edge_face_hinge.py',ROOT/c['source_points'],
           ROOT/c['existing_belt_receipt'],BASE/'checkers/check_three_tetrahedron_belt.py',
           BASE/'three-tetrahedron-belt.md',BASE/'simplicial-recombination-particle-interactions.md',
           BASE/'dimensional-resolution-simplex-interaction.md'}
    return {'schema':'marici.scattering.edge-face-hinge-receipt.v1','status':'pass',
        'scope_verdict':'exact_hinge_geometry_only_explanatory_conjecture_untested',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'draft_id':'EF1','draft_status':c['status'],'perpendicular_gram':encode(G),
        'dihedral_cosine':'1/3','rotation_plus':encode(plus),'rotation_minus':encode(minus),
        'reflected_apex':[str(x) for x in P['e']],
        'face_contacts':['ABD at +alpha','ABC at -alpha'],
        'nonoverlapping_hinge_interval':'[alpha,2*pi-alpha]','angular_width':'2*pi-2*alpha',
        'pair_and_belt_total_volume':'16/3','belt_cell_volumes':['16/9']*3,
        'same_oriented_outer_boundary_verified':True,'owner_receipt_inspected_not_replayed':True,
        'analytic_measure_and_first_hit_argument_machine_formalized':False,
        'native_rotation_generator_constructed':False,'finite_capture_probability_derived':False,
        'outgoing_photon_factorization_constructed':False,'physical_species_binding_supplied':False,
        'ratio_372_predicted':False,'historical_ancestor_freshness_claimed':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,
        'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'unsupported_promotions_refused':controls}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale edge-face hinge audit'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','scope_verdict','draft_status','dihedral_cosine','angular_width',
                                     'native_rotation_generator_constructed','ratio_372_predicted','unsupported_promotions_refused')}))


if __name__=='__main__':main()
