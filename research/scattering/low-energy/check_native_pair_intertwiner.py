"""Native diagonal pair symmetry versus Bose scalar-coordinate output codes."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_relative_photon_measure as measure

cm=measure.cm;phase=cm.phase;x=cm.x;F=cm.F;ROOT=cm.ROOT;HOME=cm.HOME
CONTRACT=HOME/'contracts/native-pair-intertwiner.v1.json'
PROOF=HOME/'NATIVE-PAIR-INTERTWINER.md'
RESULT=HOME/'results/native-pair-intertwiner.v1.json'
mm,adj,eye=phase.mm,phase.adj,phase.eye
add,mul,power,scale=measure.add,measure.mul,measure.power,measure.scale


def conjugate(A):return [[v.conjugate() for v in row] for row in A]
def trace(A):return sum((A[i][i] for i in range(len(A))),F())
def double_factorial(n):
    out=1
    for i in range(n,0,-2):out*=i
    return out

def sphere_integral(p):
    out=F()
    for a,c in p.items():
        if any(k%2 for k in a):continue
        numerator=1
        for k in a:numerator*=double_factorial(k-1)
        out=out+c*Q(numerator,double_factorial(sum(a)+1))
    return out

def compose(p,images):
    out={}
    for a,c in p.items():
        term=measure.const(c)
        for k,v in zip(a,images):term=mul(term,power(v,k))
        out=add(out,term)
    return out

def pullback(p,R):
    variables=[measure.var(i) for i in range(3)]
    images=[add(*(scale(R[j][i],variables[j]) for j in range(3))) for i in range(3)]
    return compose(p,images)

def validate_contract(c):
    assert c['schema']=='marici.scattering.native-pair-intertwiner.v1'
    assert c['source_symmetry']=='diagonal_24_binary_tetrahedral_actions'
    assert c['output_action']=='scalar_coordinate_pullback_not_helicity_completed'
    assert c['pair_conventions_tested']==['U_tensor_U','U_tensor_conjugate_U']
    for key in ('physical_electron_positron_preparation_bound','physical_photon_helicity_intertwiner_constructed',
                'native_input_to_photon_isometry_constructed','finite_symmetry_selects_multiplicity',
                'two_ray_quadrupole_code_is_SO3_vector_intertwiner','contact_generator_constructed',
                'branching_ratio_derived','full_Fock_wavepacket_constructed','live_proposition_inventory_changed',
                'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=measure.build();assert parent==json.loads(measure.RESULT.read_text(encoding='utf-8')),'stale relative measure'
    owner_before={p:p.read_bytes() for p in (phase.STORE,phase.OWNER)}
    raw=json.loads(owner_before[phase.STORE])
    P=[[[phase.decode(z) for z in row] for row in B] for B in raw['face_projectors']]
    J=phase.scale(F(1)/phase.SQ2,[row for B in P for row in B])
    assert mm(adj(J),J)==eye(2)
    pair_encodings=[phase.tensor(J,J),phase.tensor(J,conjugate(J))]
    assert all(mm(adj(E),E)==eye(4) for E in pair_encodings)
    basis=[eye(2)]+phase.SIGMA
    C=[[B[i][j]/phase.SQ2 for B in basis] for i in range(2) for j in range(2)]
    epsilon=[[F(),F(1)],[F(-1),F()]]
    Csame=mm(phase.tensor(eye(2),epsilon),C)
    assert mm(adj(C),C)==mm(adj(Csame),Csame)==eye(4)
    quats,_,spin=phase.source_group();average=[[F() for _ in range(4)] for _ in range(4)]
    variables=[measure.var(i) for i in range(3)]
    quadrupoles=[scale(phase.root(6),mul(variables[(i+1)%3],variables[(i+2)%3])) for i in range(3)]
    two_profiles=[measure.const(1)]+quadrupoles
    gram2=[[sphere_integral(mul(measure.conj(a),b)) for b in two_profiles] for a in two_profiles]
    assert gram2==eye(4)
    assert all(pullback(p,phase.scale(F(-1),eye(3)))==p for p in two_profiles)
    rotation_cases=0;triplet_character_norm=F()
    for q in sorted(quats):
        U=phase.from_spin(spin,q);R=phase.spatial(U)
        D=phase.blockdiag([[[F(1)]],R])
        Vsame=phase.tensor(U,U);Vconjugate=phase.tensor(U,conjugate(U))
        assert mm(mm(adj(Csame),Vsame),Csame)==D
        assert mm(mm(adj(C),Vconjugate),C)==D
        average=x.add(average,phase.scale(F(Q(1,24)),Vconjugate))
        triplet_character_norm=triplet_character_norm+trace(R)*trace(R)/24
        images=[mm(mm(U,B),adj(U)) for B in P];perm=[P.index(B) for B in images]
        T=[[U[i%2][j%2] if i//2==perm[j//2] else F() for j in range(8)] for i in range(8)]
        TJ=mm(T,J);assert TJ==mm(J,U)
        assert phase.tensor(TJ,TJ)==mm(pair_encodings[0],Vsame)
        assert phase.tensor(TJ,conjugate(TJ))==mm(pair_encodings[1],Vconjugate)
        for j,p in enumerate(quadrupoles):
            assert pullback(p,R)==add(*(scale(R[i][j],quadrupoles[i]) for i in range(3)))
        rotation_cases+=1
    assert triplet_character_norm==F(1)
    invariant=mm(mm(adj(C),average),C)
    assert invariant==[[F(int(i==j==0)) for j in range(4)] for i in range(4)]
    assert trace(average)==F(1) and mm(average,average)==average
    # The scalar-coordinate center is +1. A lone native spinor has center -1.
    center=phase.from_spin(spin,(Q(-1),Q(),Q(),Q()))
    assert center==phase.scale(F(-1),eye(2))
    assert phase.tensor(center,center)==eye(4)
    # Three-body Bose vector: odd shape polynomial times odd plane normal.
    y=variables
    A=mul(mul(add(y[0],scale(F(-1),y[1])),add(y[1],scale(F(-1),y[2]))),add(y[2],scale(F(-1),y[0])))
    Z=measure.inner(A,A);assert Z==F(Q(1,840))
    from itertools import permutations
    for order in permutations(range(3)):
        sign=(-1)**sum(order[i]>order[j] for i in range(3) for j in range(i+1,3))
        assert measure.permute(A,order)==scale(F(sign),A)
    C2=F(2520);assert C2*Z/3==F(1)
    # Exact degree-two sphere cubature witnesses the Haar moment inputs.
    axes=[[F(sign*int(i==j)) for i in range(3)] for j in range(3) for sign in (-1,1)]
    first=[sum((v[i] for v in axes),F())/6 for i in range(3)]
    second=[[sum((v[i]*v[j] for v in axes),F())/6 for j in range(3)] for i in range(3)]
    assert first==[F()]*3 and second==phase.scale(F(Q(1,3)),eye(3))
    gram3=[[F() for _ in range(4)] for _ in range(4)];gram3[0][0]=measure.simplex_integral(measure.const(1))
    for i in range(3):
        for j in range(3):gram3[i+1][j+1]=C2*Z*second[i][j]
    assert gram3==eye(4)
    # Proper reference-triangle permutations flip its normal exactly when odd.
    rays=[[F(1),F(),F()],[F(Q(-1,2)),phase.SQ3/2,F()],[F(Q(-1,2)),-phase.SQ3/2,F()]]
    for order in permutations(range(3)):
        sign=(-1)**sum(order[i]>order[j] for i in range(3) for j in range(i+1,3))
        S=[[rays[order[0]][i],(2*rays[order[1]][i]+rays[order[0]][i])/phase.SQ3,F(sign*int(i==2))] for i in range(3)]
        assert mm(adj(S),S)==eye(3) and cm.determinant(S)==F(1)
        assert all(cm.act(S,rays[i])==rays[order[i]] for i in range(3))
    sector_examples=[]
    for a,b in ((Q(1),Q()),(Q(3,5),Q(4,5)),(Q(4,5),Q(3,5)),(Q(),Q(1))):
        assert x.add(phase.scale(F(a*a),gram2),phase.scale(F(b*b),gram3))==eye(4)
        sector_examples.append([str(a*a),str(b*b)])
    # A nonnative continuous rotation takes the two-ray triplet out of its code.
    a=F(1)/phase.SQ2
    R45=[[a,-a,F()],[a,a,F()],[F(),F(),F(1)]]
    moved=pullback(quadrupoles[2],R45)
    assert all(sphere_integral(mul(measure.conj(p),moved))==F() for p in two_profiles)
    leakage=sphere_integral(mul(measure.conj(moved),moved));assert leakage==F(1)
    # Coherent two-body code has a phase-sensitive bounded observable.
    plus=scale(a,add(two_profiles[0],two_profiles[1]));minus=scale(a,add(two_profiles[0],scale(F(-1),two_profiles[1])))
    gap=sphere_integral(mul(two_profiles[1],add(mul(plus,plus),scale(F(-1),mul(minus,minus)))))
    assert gap==F(2)
    refused=[]
    for name in ('discard_pair_triplet','identify_lone_spinor_with_center_even_target','promote_finite_code_to_SO3',
                 'infer_multiplicity_from_diagonal_symmetry','promote_scalar_code_to_photon_intertwiner'):
        try:
            if name=='discard_pair_triplet':assert invariant==eye(4)
            elif name=='identify_lone_spinor_with_center_even_target':assert center==eye(2)
            elif name=='promote_finite_code_to_SO3':assert leakage==F()
            else:
                bad=copy.deepcopy(c)
                key={'infer_multiplicity_from_diagonal_symmetry':'finite_symmetry_selects_multiplicity',
                     'promote_scalar_code_to_photon_intertwiner':'physical_photon_helicity_intertwiner_constructed'}[name]
                bad[key]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported pair-intertwiner promotion: '+name)
    assert all(p.read_bytes()==b for p,b in owner_before.items())
    phase_receipt=json.loads(phase.RESULT.read_text(encoding='utf-8'))
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((measure.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_native_pair_intertwiner.py'))
    return {'schema':'marici.scattering.native-pair-intertwiner-receipt.v1','status':'pass',
        'scope_verdict':'diagonal_native_pair_to_Bose_scalar_coefficients_not_physical_helicity_emission',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'native_group_cases':rotation_cases,'pair_decomposition':'one_singlet_plus_one_irreducible_triplet',
        'pair_invariant_rank':1,'lone_spinor_center_even_intertwiner_rank':0,
        'conjugate_pair_Clebsch_Gordan_matrix':x.encoded(C),'same_pair_Clebsch_Gordan_matrix':x.encoded(Csame),
        'raw_pair_encoding_Gram_verified':True,'raw_pair_intertwining_verified':True,
        'two_output_Bose_scalar_profile_Gram':x.encoded(gram2),'three_output_Bose_scalar_profile_Gram':x.encoded(gram3),
        'three_body_Vandermonde_squared_norm':'1/840','three_body_vector_normalization_squared':'2520',
        'two_output_coherent_observable_gap':'2','two_output_quadrupole_45_degree_leakage_squared_norm':'1',
        'native_pair_to_Bose_scalar_coefficient_isometries_constructed':True,
        'counterexample_sector_probabilities':sector_examples,
        'scalar_profile_only_pair_intertwiner_max_rank':1,'finite_symmetry_selects_multiplicity':False,
        'physical_electron_positron_preparation_bound':False,'physical_photon_helicity_intertwiner_constructed':False,
        'native_input_to_photon_isometry_constructed':False,'contact_generator_constructed':False,
        'branching_ratio_derived':False,'full_Fock_wavepacket_constructed':False,
        'owner_producer_hash_matches_current':phase_receipt['owner_producer_hash_matches_current'],
        'owner_files_unchanged':True,'analytic_argument_machine_formalized':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,'high_energy_protocol_executed':False,
        'physical_outcomes_admitted':False,'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale native pair intertwiner'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','native_group_cases','pair_decomposition','pair_invariant_rank',
        'native_pair_to_Bose_scalar_coefficient_isometries_constructed','three_body_Vandermonde_squared_norm',
        'two_output_quadrupole_45_degree_leakage_squared_norm','finite_symmetry_selects_multiplicity',
        'physical_photon_helicity_intertwiner_constructed','owner_producer_hash_matches_current','hostile_controls_refused')}))


if __name__=='__main__':main()
