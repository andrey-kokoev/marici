"""Plane-normal helicity cocycle and a conditional three-photon rotation code."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import permutations,product
import json
from pathlib import Path
import check_native_pair_intertwiner as pair

measure=pair.measure;cm=pair.cm;phase=pair.phase;x=pair.x;F=pair.F;ROOT=pair.ROOT;HOME=pair.HOME
CONTRACT=HOME/'contracts/three-photon-helicity.v1.json'
PROOF=HOME/'THREE-PHOTON-HELICITY.md'
RESULT=HOME/'results/three-photon-helicity.v1.json'


def dot(a,b):return sum((v*w for v,w in zip(a,b)),F())
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def hermitian(a,b):return dot([v.conjugate() for v in a],b)
def times(c,v):return [c*a for a in v]
def decode_matrix(A):return [[F(tuple(Q(v) for v in a)) for a in row] for row in A]
def direction(p):return [v/p[0] for v in p[1:]]
def tensor3(vectors):return [vectors[0][i]*vectors[1][j]*vectors[2][k] for i,j,k in product(range(3),repeat=3)]
def sign(order):return (-1)**sum(order[i]>order[j] for i in range(3) for j in range(i+1,3))

def helicity_frame(momenta,N,h):
    assert len(momenta)==3 and len(N)==3 and all(len(p)==4 for p in momenta)
    assert all(v==v.conjugate() for p in momenta for v in p) and all(v==v.conjugate() for v in N)
    assert h in (-1,1) and dot(N,N)==F(1)
    assert all(x.positive(p[0]) and cm.mink(p,p)==F() for p in momenta)
    spatial=[p[1:] for p in momenta];assert cm.total(momenta)[1:]==[F()]*3
    oriented=cross(spatial[0],spatial[1]);assert x.positive(dot(oriented,N))
    assert cross(oriented,N)==[F()]*3
    out=[]
    for p in momenta:
        n=direction(p);assert dot(n,n)==F(1) and dot(N,n)==F()
        t=cross(N,n);eps=[(a+phase.IM*h*b)/phase.SQ2 for a,b in zip(t,N)]
        assert dot(n,eps)==dot(eps,eps)==F() and hermitian(eps,eps)==F(1)
        assert cross(n,eps)==times(-phase.IM*h,eps)
        out.append(eps)
    return out

def rotate(momenta,R):return [[p[0]]+cm.act(R,p[1:]) for p in momenta]
def gauge(n):return (F(1)+phase.IM*n[0])/(F(1)-phase.IM*n[0])

def validate_contract(c):
    assert c['schema']=='marici.scattering.three-photon-helicity.v1'
    assert c['gauge']=='oriented_plane_normal_Coulomb_helicity_frame'
    assert c['scope']=='fixed_total_momentum_relative_three_photon_spatial_rotations'
    for key in ('physical_electron_positron_preparation_bound','native_continuous_rotation_licensed',
                'native_joint_emission_operation_licensed','charge_conjugation_rule_bound',
                'full_Lorentz_intertwiner_constructed','full_Fock_wavepacket_constructed',
                'two_photon_helicity_audit_performed_by_this_checker','contact_generator_constructed',
                'spectrum_selected_by_native_dynamics','branching_ratio_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=pair.build();assert parent==json.loads(pair.RESULT.read_text(encoding='utf-8')),'stale pair audit'
    classical=json.loads(cm.RESULT.read_text(encoding='utf-8'))
    baseline=decode_matrix(classical['examples']['face_equal_area']['completed_momenta'])
    N=times(F(2)/phase.SQ3,cross(direction(baseline[0]),direction(baseline[1])))
    group,_,spin=phase.source_group();rotations=[phase.spatial(phase.from_spin(spin,q)) for q in sorted(group)]
    a=F(1)/phase.SQ2;rotations.append([[a,-a,F()],[a,a,F()],[F(),F(),F(1)]])
    y=[measure.var(i) for i in range(3)]
    A=measure.mul(measure.mul(measure.add(y[0],measure.scale(F(-1),y[1])),
                              measure.add(y[1],measure.scale(F(-1),y[2]))),
                  measure.add(y[2],measure.scale(F(-1),y[0])))
    Z=measure.inner(A,A);assert 840*Z==F(1)
    gram=[[F() for _ in range(4)] for _ in range(4)];gram[0][0]=840*Z
    for i in range(3):
        for j in range(3):gram[i+1][j+1]=F(3)*pair.sphere_integral(measure.mul(y[i],y[j]))
    assert gram==phase.eye(4)
    # N_x*N_y is gauge-independent and even under photon permutations.
    plus=measure.scale(phase.SQ3/phase.SQ2,measure.add(y[0],y[1]))
    minus=measure.scale(phase.SQ3/phase.SQ2,measure.add(y[0],measure.scale(F(-1),y[1])))
    density_gap=measure.add(measure.mul(plus,plus),measure.scale(F(-1),measure.mul(minus,minus)))
    coherence_gap=pair.sphere_integral(measure.mul(measure.mul(y[0],y[1]),density_gap))
    assert coherence_gap==F(Q(2,5))
    permutation_cases=0;rotation_cases=0;gauge_cases=0;old_profile_failures=0
    for name in ('face_equal_area','face_weight_sensitivity'):
        momenta=decode_matrix(classical['examples'][name]['completed_momenta'])
        ys=[F(1)-2*p[0] for p in momenta];Aval=measure.evaluate(A,ys)
        for h in (-1,1):
            eps=helicity_frame(momenta,N,h);section=tensor3(eps)
            assert hermitian(section,section)==F(1)
            G=gauge(direction(momenta[0]));assert G*G.conjugate()==F(1)
            for order in permutations(range(3)):
                parity=sign(order);mom=[momenta[i] for i in order];Np=times(F(parity),N)
                epsp=helicity_frame(mom,Np,h);expected=[eps[i] for i in order]
                assert epsp==[times(F(parity),v) for v in expected]
                new_section=tensor3(epsp);permuted_section=tensor3(expected)
                assert new_section==times(F(parity),permuted_section)
                Ap=measure.evaluate(A,[ys[i] for i in order]);assert Ap==parity*Aval
                assert times(Ap,new_section)==times(Aval,permuted_section)
                for j in range(3):assert times(phase.SQ3*Np[j],new_section)==times(phase.SQ3*N[j],permuted_section)
                if parity<0:
                    assert new_section!=permuted_section;old_profile_failures+=1
                # A nontrivial ordered gauge transition: product section G -> G'.
                Gp=gauge(direction(mom[0]));assert Gp*Gp.conjugate()==F(1)
                cocycle=F(parity)*Gp/G
                assert times(Gp,new_section)==times(cocycle,times(G,permuted_section))
                assert times(Ap/Gp,times(Gp,new_section))==times(Aval,permuted_section)
                for j in range(3):
                    assert times(phase.SQ3*Np[j]/Gp,times(Gp,new_section))==times(phase.SQ3*N[j],permuted_section)
                gauge_cases+=1;permutation_cases+=1
            for R in rotations:
                inverse=phase.adj(R);pre=rotate(momenta,inverse);Npre=cm.act(inverse,N)
                pre_eps=helicity_frame(pre,Npre,h)
                transported=[cm.act(R,v) for v in pre_eps]
                assert transported==eps
                for j in range(3):
                    acted=times(phase.SQ3*Npre[j],tensor3(transported))
                    coefficient=sum((R[k][j]*phase.SQ3*N[k] for k in range(3)),F())
                    assert acted==times(coefficient,section)
                rotation_cases+=1
    refused=[]
    for name in ('erase_odd_permutation_phase','reuse_even_scalar_code_unchanged','claim_full_Lorentz',
                 'identify_native_pair_with_physical_preparation','infer_branching_from_intertwiner'):
        try:
            if name in ('erase_odd_permutation_phase','reuse_even_scalar_code_unchanged'):
                assert old_profile_failures==0
            else:
                bad=copy.deepcopy(c)
                key={'claim_full_Lorentz':'full_Lorentz_intertwiner_constructed',
                     'identify_native_pair_with_physical_preparation':'physical_electron_positron_preparation_bound',
                     'infer_branching_from_intertwiner':'branching_ratio_derived'}[name]
                bad[key]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported helicity promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((pair.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_three_photon_helicity.py'))
    return {'schema':'marici.scattering.three-photon-helicity-receipt.v1','status':'pass',
        'scope_verdict':'conditional_native_pair_to_relative_three_photon_rotation_isometry_not_emission',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'helicities_checked':[-1,1],'permutation_cases':permutation_cases,'rotation_cases':rotation_cases,
        'gauge_transition_cases':gauge_cases,'odd_permutation_section_cocycle':'sign(permutation)',
        'rephased_section_cocycle':'sign(permutation)*G(permuted_p)/G(p)',
        'unchanged_even_scalar_code_reuse_failures':old_profile_failures,
        'singlet_profile':'sqrt(840)*Vandermonde(y)','triplet_profiles':'sqrt(3)*oriented_plane_normal_components',
        'conditional_relative_three_photon_rotation_intertwiner_constructed':True,
        'conditional_native_pair_to_relative_three_photon_isometry_constructed':True,
        'profile_Gram':x.encoded(gram),'singlet_normalization_squared':'840','triplet_normalization_squared':'3',
        'triplet_coherent_NxNy_expectation_gap':'2/5',
        'physical_electron_positron_preparation_bound':False,'native_continuous_rotation_licensed':False,
        'native_joint_emission_operation_licensed':False,'charge_conjugation_rule_bound':False,
        'full_Lorentz_intertwiner_constructed':False,'full_Fock_wavepacket_constructed':False,
        'two_photon_helicity_audit_performed_by_this_checker':False,'contact_generator_constructed':False,
        'spectrum_selected_by_native_dynamics':False,'branching_ratio_derived':False,
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],
        'analytic_argument_machine_formalized':False,'new_live_proposition_admitted':False,
        'C12_protocol_renewed':False,'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale three-photon helicity'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','permutation_cases','rotation_cases','gauge_transition_cases',
        'odd_permutation_section_cocycle','conditional_native_pair_to_relative_three_photon_isometry_constructed',
        'unchanged_even_scalar_code_reuse_failures','contact_generator_constructed','hostile_controls_refused')}))


if __name__=='__main__':main()
