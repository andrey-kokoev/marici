"""EF1-B: retained classical CM completion of geometric null seed momenta."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import permutations
import json
from pathlib import Path
import check_normal_direction_contact as contact

phase=contact.phase;x=phase.x;F=x.F;ROOT=contact.ROOT;HOME=contact.HOME
CONTRACT=HOME/'contracts/cm-separation-map.v1.json'
PROOF=HOME/'CM-SEPARATION-MAP.md'
RESULT=HOME/'results/cm-separation-map.v1.json'
mm,adj,eye=x.mm,x.adjoint,x.eye
ETA=[[F((1 if i==0 else -1) if i==j else 0) for j in range(4)] for i in range(4)]


def dot(a,b):return sum((v*w for v,w in zip(a,b)),F())
def mink(a,b):return a[0]*b[0]-dot(a[1:],b[1:])
def total(vectors):return [sum((p[i] for p in vectors),F()) for i in range(4)]
def act(A,v):return [row[0] for row in mm(A,[[a] for a in v])]
def determinant(A):
    out=F();n=len(A)
    for perm in permutations(range(n)):
        term=F((-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n)))
        for i,j in enumerate(perm):term=term*A[i][j]
        out=out+term
    return out

def rest_boost(K,s):
    assert x.positive(s) and s*s==mink(K,K) and x.positive(K[0])
    A=K[0];q=K[1:];B=eye(4);B[0][0]=A/s
    for i in range(3):
        B[0][i+1]=B[i+1][0]=-q[i]/s
        for j in range(3):B[i+1][j+1]=F(int(i==j))+q[i]*q[j]/(s*(A+s))
    return B

def complete(seeds,M,s):
    assert x.positive(M) and all(x.positive(k[0]) and mink(k,k)==F() for k in seeds)
    K=total(seeds);assert x.positive(mink(K,K)),'null/parallel seed total cannot complete to a massive CM state'
    B=rest_boost(K,s);inverse=rest_boost([K[0]]+[-v for v in K[1:]],s)
    assert mm(mm(adj(B),ETA),B)==ETA and determinant(B)==F(1)
    assert mm(B,inverse)==eye(4) and act(B,K)==[s,F(),F(),F()]
    scale=M/s;out=[[scale*v for v in act(B,k)] for k in seeds]
    assert total(out)==[M,F(),F(),F()]
    assert all(mink(p,p)==F() and x.positive(p[0]) for p in out)
    restored=[[v/scale for v in act(inverse,p)] for p in out]
    assert restored==seeds
    return out,{'seed_total':K,'seed_mass':s,'scale':scale,'boost':B,'inverse_boost':inverse}

def energy_fractions(weights):
    assert len(weights)==3 and all(w>0 for w in weights)
    S=sum(weights[i]*weights[j] for i in range(3) for j in range(i+1,3))
    return tuple(weights[i]*sum(weights[j] for j in range(3) if j!=i)/(2*S) for i in range(3))
def inverse_shape(energies):
    assert len(energies)==3 and sum(energies)==1 and all(0<e<Q(1,2) for e in energies)
    weights=tuple(1/(1-2*e) for e in energies)
    assert energy_fractions(weights)==tuple(energies)
    return tuple(w/weights[0] for w in weights)

def validate_contract(c):
    assert c['schema']=='marici.scattering.cm-separation-map.v1' and c['candidate_id']=='EF1-B'
    assert c['boost_scale_record_retained'] is True
    for key in ('source_native_separation_derived','physical_motion_implemented','quantum_separation_isometry_constructed',
                'normalizable_photon_output_constructed','unequal_seed_weights_source_selected',
                'contact_amplitudes_derived','branching_ratio_derived','EF1_N_refutation_reversed',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=contact.build();assert parent==json.loads(contact.RESULT.read_text(encoding='utf-8')),'stale normal-readout test'
    P={k:tuple(Q(v) for v in p) for k,p in parent['witness_coordinates'].items()}
    edge=[contact.normal(P,t) for t in ('ACE','BDF')]
    polynomials,D=contact.points_polynomial()
    n1,n2=[contact.pnormal(polynomials,t) for t in ('ACE','BDF')]
    assert contact.pa(*(contact.pm(v,v) for v in n1))==contact.pa(*(contact.pm(v,v) for v in n2))
    difference=contact.psub(n1,n2)
    expected=[contact.ps(-16,contact.pm([Q(),Q(1)],D)),
              contact.ps(-16,contact.pm([Q(),Q(),Q(1)],D)),
              contact.ps(16,contact.pm([Q(),Q(),Q(1)],D))]
    assert difference==expected
    face=[[Q(v) for v in n] for n in parent['face_three_normals']]
    L=F(Q(16,3))*phase.SQ2
    assert all(dot([F(v) for v in n],[F(v) for v in n])==L*L for n in edge+face)
    directions={name:[[F(v)/L for v in n] for n in ns] for name,ns in (('edge',edge),('face',face))}
    cases=[('edge_equal_area',directions['edge'],[Q(1),Q(1)],phase.SQ2),
           ('face_equal_area',directions['face'],[Q(1)]*3,F(3)),
           ('face_weight_sensitivity',directions['face'],[Q(1),Q(2),Q(1,3)],F(3))]
    group,_,spin=phase.source_group();rotations=[]
    for q in group:
        R=phase.spatial(phase.from_spin(spin,q))
        if R not in rotations:rotations.append(R)
    assert len(rotations)==12
    audits={};covariance=0
    for name,ns,weights,s in cases:
        seeds=[[F(w)]+[F(w)*v for v in n] for w,n in zip(weights,ns)]
        out,record=complete(seeds,F(1),s)
        doubled=[[2*v for v in k] for k in seeds]
        assert complete(doubled,F(1),2*s)[0]==out
        for order in permutations(range(len(seeds))):
            assert complete([seeds[i] for i in order],F(1),s)[0]==[out[i] for i in order]
        for R in rotations:
            RR=[[F(int(i==j)) if i==0 or j==0 else R[i-1][j-1] for j in range(4)] for i in range(4)]
            rotated=[act(RR,k) for k in seeds]
            assert complete(rotated,F(1),s)[0]==[act(RR,p) for p in out];covariance+=1
        if len(weights)==3:assert tuple(p[0] for p in out)==tuple(F(v) for v in energy_fractions(weights))
        audits[name]={'weights_in_common_area_units':[str(w) for w in weights],
            'seed_momenta':x.encoded(seeds),'completed_momenta':x.encoded(out),
            'retained_seed_total':[v.encoded() for v in record['seed_total']],
            'retained_seed_mass':s.encoded(),'retained_scale':record['scale'].encoded(),
            'retained_boost':x.encoded(record['boost']),'exact_inverse_verified':True}
    edge_expected=[[F(Q(1,2)),F(Q(-1,6)),F(Q(-1,3)),F(Q(1,3))],
                   [F(Q(1,2)),F(Q(1,6)),F(Q(1,3)),F(Q(-1,3))]]
    assert audits['edge_equal_area']['completed_momenta']==x.encoded(edge_expected)
    assert energy_fractions([Q(1),Q(2),Q(1,3)])==(Q(7,18),Q(4,9),Q(1,6))
    shape_tests=[]
    for a in range(1,9):
        for b in range(1,9):
            energies=(Q(a,18),Q(b,18),1-Q(a+b,18))
            if all(0<e<Q(1,2) for e in energies):
                inverse_shape(energies);shape_tests.append([str(v) for v in energies])
    assert shape_tests
    refused=[]
    for name in ('single_ray','parallel_rays','erase_boost_scale_record','claim_source_derivation','claim_spectrum_or_branching'):
        try:
            if name in ('single_ray','parallel_rays'):
                seed=[F(1),F(1),F(),F()];complete([seed]*(1 if name=='single_ray' else 2),F(1),F(1))
            else:
                bad=copy.deepcopy(c)
                key={'erase_boost_scale_record':'boost_scale_record_retained','claim_source_derivation':'source_native_separation_derived',
                     'claim_spectrum_or_branching':'branching_ratio_derived'}[name]
                bad[key]=name!='erase_boost_scale_record';validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported CM-map control: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((contact.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_cm_separation_map.py'))
    return {'schema':'marici.scattering.cm-separation-map-receipt.v1','status':'pass',
        'scope_verdict':'conditional_retained_classical_mass_shell_completion_not_emission_dynamics',
        'source_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(paths)},
        'candidate_id':'EF1-B','classical_CM_map_constructed':True,'mass_shell_and_total_momentum_verified':True,
        'boost_scale_record_retained':True,'source_rotation_covariance_cases':covariance,
        'two_equal_area_axis_polynomial_identity_verified':True,
        'examples':audits,'two_ray_witness_energy_fractions':['1/2','1/2'],
        'two_ray_witness_first_direction':['-1/3','-2/3','2/3'],
        'three_equal_area_energy_fractions':['1/3']*3,
        'three_weight_sensitivity_energy_fractions':['7/18','4/9','1/6'],
        'three_body_shape_inverse_rational_checks':len(shape_tests),
        'source_native_separation_derived':False,'physical_motion_implemented':False,
        'quantum_separation_isometry_constructed':False,'normalizable_photon_output_constructed':False,
        'unequal_seed_weights_source_selected':False,'contact_amplitudes_derived':False,
        'branching_ratio_derived':False,'EF1_N_refutation_reversed':False,'analytic_argument_machine_formalized':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,'high_energy_protocol_executed':False,
        'physical_outcomes_admitted':False,'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale CM separation map'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','classical_CM_map_constructed','two_ray_witness_first_direction',
        'three_weight_sensitivity_energy_fractions','source_rotation_covariance_cases',
        'three_body_shape_inverse_rational_checks','contact_amplitudes_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
