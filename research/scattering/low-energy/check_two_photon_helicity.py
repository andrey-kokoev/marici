"""All two-photon helicity pairs: physical rotation/exchange and conditional J=1 exclusion."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path
import check_three_photon_helicity as three

pair=three.pair;measure=three.measure;phase=three.phase;cm=three.cm;x=three.x;F=three.F;ROOT=three.ROOT;HOME=three.HOME
CONTRACT=HOME/'contracts/two-photon-helicity.v1.json'
PROOF=HOME/'TWO-PHOTON-HELICITY.md'
RESULT=HOME/'results/two-photon-helicity.v1.json'
mm,adj,eye=phase.mm,phase.adj,phase.eye


def transpose(A):return [list(row) for row in zip(*A)]
def outer(a,b):return [[v*w for w in b] for v in a]
def frobenius(A):return sum((v.conjugate()*v for row in A for v in row),F())
def sub(A,B):return x.add(A,phase.scale(F(-1),B))
def act_tensor(R,B):return mm(mm(R,B),transpose(R))
def helicity_pair(n,t,h1,h2):
    assert len(n)==len(t)==3 and h1 in (-1,1) and h2 in (-1,1)
    assert all(v==v.conjugate() for v in n+t)
    assert three.dot(n,n)==three.dot(t,t)==F(1) and three.dot(n,t)==F()
    s=three.cross(n,t)
    e1=[(a+phase.IM*h1*b)/phase.SQ2 for a,b in zip(t,s)]
    e2=[(a-phase.IM*h2*b)/phase.SQ2 for a,b in zip(t,s)]
    assert three.cross(n,e1)==three.times(-phase.IM*h1,e1)
    assert three.cross(three.times(F(-1),n),e2)==three.times(-phase.IM*h2,e2)
    assert three.hermitian(e1,e1)==three.hermitian(e2,e2)==F(1)
    B=outer(e1,e2);assert frobenius(B)==F(1)
    return B

def equal_helicity_section(n,h):
    assert h in (-1,1) and len(n)==3 and all(v==v.conjugate() for v in n)
    assert three.dot(n,n)==F(1)
    nx,ny,nz=n
    C=[[F(),-nz,ny],[nz,F(),-nx],[-ny,nx,F()]]
    return [[(F(int(i==j))-n[i]*n[j]+phase.IM*h*C[i][j])/2 for j in range(3)] for i in range(3)]

def validate_contract(c):
    assert c['schema']=='marici.scattering.two-photon-helicity.v1'
    assert c['helicity_pairs']==[[1,1],[1,-1],[-1,1],[-1,-1]]
    assert c['continuous_exclusion_scope']=='SO3_total_J1_to_isolated_two_real_photons_without_extra_records'
    for key in ('source_triplet_identified_with_physical_total_J1','full_continuous_source_rotation_licensed',
                'physical_electron_positron_preparation_bound','charge_conjugation_rule_bound',
                'native_joint_emission_operation_licensed','full_Lorentz_intertwiner_constructed',
                'full_Fock_wavepacket_constructed','contact_generator_constructed',
                'finite_native_symmetry_alone_excludes_triplet_two_photons','branching_ratio_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=three.build();assert parent==json.loads(three.RESULT.read_text(encoding='utf-8')),'stale three-photon audit'
    n=[F(),F(),F(1)];t=[F(1),F(),F()]
    R90=[[F(),F(-1),F()],[F(1),F(),F()],[F(),F(),F(1)]]
    Ry180=[[F(-1),F(),F()],[F(),F(1),F()],[F(),F(),F(-1)]]
    a=F(1)/phase.SQ2;R45=[[a,-a,F()],[a,a,F()],[F(),F(),F(1)]]
    group,_,spin=phase.source_group();native=[phase.spatial(phase.from_spin(spin,q)) for q in sorted(group)]
    assert R90 not in native and R45 not in native
    determinants={};frame_phases={};rotation_cases=0;exchange_cases=0
    for h1,h2 in c['helicity_pairs']:
        key=f'{h1},{h2}';B=helicity_pair(n,t,h1,h2)
        flipped=helicity_pair(three.times(F(-1),n),t,h2,h1)
        assert flipped==transpose(B);exchange_cases+=1
        phases=[]
        for R,co,si in ((R45,a,a),(R90,F(),F(1))):
            character=(co-phase.IM*h1*si)*(co+phase.IM*h2*si)
            reframed=helicity_pair(n,cm.act(R,t),h1,h2)
            assert reframed==phase.scale(character,B)==act_tensor(R,B)
            phases.append(character.encoded())
        frame_phases[key]=phases
        character=F(1 if h1==h2 else -1)
        A=sub(R90,phase.scale(character,eye(3)))
        G=mm(A,adj(A))
        if h1==h2:
            # Rotation about the ray leaves only m=0; Bose exchange kills it.
            exchange=sub(Ry180,eye(3));G=x.add(G,mm(exchange,adj(exchange)))
            assert B==equal_helicity_section(n,h1)
            assert act_tensor(Ry180,B)==transpose(B)
        determinant=cm.determinant(G)
        assert determinant==F(48 if h1==h2 else 16)
        determinants[key]=str(determinant.v[0])
        for R in native+[R45,R90]:
            nr,tr=cm.act(R,n),cm.act(R,t)
            assert helicity_pair(nr,tr,h1,h2)==act_tensor(R,B);rotation_cases+=1
    # Same-helicity product has a frame-independent global tensor expression.
    section_cases=0
    directions=[[F(int(i==j)*sign) for i in range(3)] for j in range(3) for sign in (-1,1)]
    directions.append([F(Q(-1,3)),F(Q(-2,3)),F(Q(2,3))])
    for direction in directions:
        for h in (-1,1):
            B=equal_helicity_section(direction,h)
            assert frobenius(B)==F(1) and adj(B)==B and mm(B,B)==B
            assert equal_helicity_section(three.times(F(-1),direction),h)==transpose(B)
            for R in native+[R45,R90]:
                assert equal_helicity_section(cm.act(R,direction),h)==act_tensor(R,B)
                section_cases+=1
    # Photon completion of the finite native quadrupole code; the scalar Gram
    # is unchanged since the full polarization section has pointwise norm one.
    variables=[measure.var(i) for i in range(3)]
    quadrupoles=[measure.scale(phase.root(6),measure.mul(variables[(i+1)%3],variables[(i+2)%3])) for i in range(3)]
    profiles=[measure.const(1)]+quadrupoles
    gram=[[pair.sphere_integral(measure.mul(measure.conj(p),q)) for q in profiles] for p in profiles]
    assert gram==eye(4)
    for R in native:
        for j,p in enumerate(quadrupoles):
            assert pair.pullback(p,R)==measure.add(*(measure.scale(R[k][j],quadrupoles[k]) for k in range(3)))
    moved=pair.pullback(quadrupoles[2],R45)
    assert all(pair.sphere_integral(measure.mul(measure.conj(p),moved))==F() for p in profiles)
    assert pair.sphere_integral(measure.mul(measure.conj(moved),moved))==F(1)
    # With continuous spin0+spin1 input, rotations leave singlet mixing free.
    Ps=[[F(int(i==j==0)) for j in range(4)] for i in range(4)]
    Pt=sub(eye(4),Ps);weights=[]
    for a,b in ((Q(1),Q()),(Q(3,5),Q(4,5)),(Q(),Q(1))):
        two_gram=phase.scale(F(a*a),Ps)
        three_gram=x.add(phase.scale(F(b*b),Ps),Pt)
        assert x.add(two_gram,three_gram)==eye(4)
        weights.append({'singlet_two_probability':str(a*a),'singlet_three_probability':str(b*b),
                        'triplet_two_probability':'0','triplet_three_probability':'1'})
    refused=[]
    for name in ('erase_mixed_helicity_stabilizer_phase','erase_equal_helicity_Bose_constraint',
                 'promote_finite_triplet_to_continuous_J1','claim_source_total_spin_identification','infer_unique_branching'):
        try:
            if name=='erase_mixed_helicity_stabilizer_phase':assert frame_phases['1,-1'][1]==F(1).encoded()
            elif name=='erase_equal_helicity_Bose_constraint':assert cm.determinant(mm(sub(R90,eye(3)),adj(sub(R90,eye(3)))))!=F()
            else:
                bad=copy.deepcopy(c)
                key={'promote_finite_triplet_to_continuous_J1':'finite_native_symmetry_alone_excludes_triplet_two_photons',
                     'claim_source_total_spin_identification':'source_triplet_identified_with_physical_total_J1',
                     'infer_unique_branching':'branching_ratio_derived'}[name]
                bad[key]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported two-photon promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((three.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_two_photon_helicity.py'))
    return {'schema':'marici.scattering.two-photon-helicity-receipt.v1','status':'pass',
        'scope_verdict':'physical_relative_two_photon_helicity_and_conditional_total_J1_exclusion_not_native_spin_binding',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'helicity_pairs':c['helicity_pairs'],'rotation_cases':rotation_cases,'exchange_cases':exchange_cases,
        'frame_independent_section_rotation_cases':section_cases,'frame_change_characters_45_and_90':frame_phases,
        'spin1_reference_constraint_Gram_determinants':determinants,
        'conditional_continuous_total_J1_two_photon_intertwiner_rank':0,
        'equal_helicity_singlet_relative_states_constructed':True,
        'conditional_native_pair_two_photon_finite_rotation_isometry_constructed':True,
        'finite_code_profile_Gram':x.encoded(gram),'physical_quadrupole_45_degree_leakage_squared_norm':'1',
        'continuous_spin0_plus_spin1_sector_weight_examples':weights,
        'source_triplet_identified_with_physical_total_J1':False,'full_continuous_source_rotation_licensed':False,
        'physical_electron_positron_preparation_bound':False,'charge_conjugation_rule_bound':False,
        'native_joint_emission_operation_licensed':False,'full_Lorentz_intertwiner_constructed':False,
        'full_Fock_wavepacket_constructed':False,'contact_generator_constructed':False,
        'finite_native_symmetry_alone_excludes_triplet_two_photons':False,'branching_ratio_derived':False,
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],
        'analytic_argument_machine_formalized':False,'new_live_proposition_admitted':False,
        'C12_protocol_renewed':False,'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale two-photon helicity'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','helicity_pairs','rotation_cases','frame_independent_section_rotation_cases',
        'spin1_reference_constraint_Gram_determinants','conditional_continuous_total_J1_two_photon_intertwiner_rank',
        'conditional_native_pair_two_photon_finite_rotation_isometry_constructed',
        'source_triplet_identified_with_physical_total_J1','branching_ratio_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
