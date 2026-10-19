"""Forward photon crossing, preparation cones and conditional dispersion positivity."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import combinations,permutations,product
import json
from pathlib import Path
import check_forward_photon_moments as mom

ir=mom.ir;F=ir.F;phase=ir.crossed.phase;ROOT=ir.ROOT;HOME=ir.HOME
CONTRACT=HOME/'contracts/forward-crossing-positivity.v1.json';PROOF=HOME/'FORWARD-CROSSING-POSITIVITY.md'
RESULT=HOME/'results/forward-crossing-positivity.v1.json'
LABELS=((1,1),(-1,-1),(1,-1),(-1,1));INDEX={h:i for i,h in enumerate(LABELS)}


def gamma(A):
    """(I tensor X) A^(T2) (I tensor X), in (++ , -- , +- , -+) order."""
    return [[A[INDEX[a,-d]][INDEX[c,-b]] for c,d in LABELS] for a,b in LABELS]


def add(A,B):return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def scale(c,A):return [[c*a for a in r] for r in A]
def crossed_sum(A,n):return add(A,scale((-1)**n,gamma(A)))
def trace(A):return sum((A[i][i] for i in range(4)),Q())
def trace_product(A,B):return sum((A[i][j]*B[j][i] for i in range(4) for j in range(4)),Q())
def outer(z):return [[a*b.conjugate() for b in z] for a in z]
def expectation(A,z):return sum((z[i].conjugate()*A[i][j]*z[j] for i in range(4) for j in range(4)),Q())
def product_state(a,b):return [a[0]*b[0],a[1]*b[1],a[0]*b[1],a[1]*b[0]]


def rational(v):
    if isinstance(v,(int,Q)):return Q(v)
    encoded=v.encoded();assert all(Q(x)==0 for x in encoded[1:]);return Q(encoded[0])


def determinant(A):
    n=len(A);out=Q()
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n));term=sign
        for i in range(n):term*=A[i][p[i]]
        out+=term
    return out


def is_psd(A):
    """Exact principal-minor test for rational/Gaussian-rational matrix controls."""
    assert all(A[i][j]==A[j][i].conjugate() for i in range(4) for j in range(4))
    return all(rational(determinant([[A[i][j] for j in ids] for i in ids]))>=0
               for k in range(1,5) for ids in combinations(range(4),k))


def restricted_even_safe(rho):
    """Exact dual condition for the real parity-even (D,O,M) PSD cut cone."""
    assert rational(trace(rho))==1 and is_psd(rho)
    real=(rho[0][1]+rho[1][0])/2
    return abs(rational(real))<=Q(1,4)


def conditional_dispersion_gate(n,N,k0,assumptions):
    """Hypothetical contour eligibility, NOT admission of physical/source assumptions."""
    assert isinstance(n,int) and isinstance(N,int) and isinstance(k0,int) and N>=0 and k0>=2
    assert n>=N,'subtraction coefficient remains independent'
    assert n<2*k0,'unsubtracted small-circle jet/moment not IR finite'
    for key in ('poles_and_forward_limit_accounted','regular_IR_matching_jet_and_cut_inventory',
                'large_arc_zero_at_n','global_cut_positive_at_same_scope',
                'jet_and_cut_same_scope','forward_crossing_and_Hermitian_analyticity'):
        assert assumptions.get(key) is True,key
    return True


def validate_contract(c):
    assert c['schema']=='marici.scattering.forward-crossing-positivity.v1'
    assert c['scope']=='forward_photon_crossing;conditional_dispersion_not_source_admission'
    assert c['gamma']=='Gamma(A)_(ab,cd)=A_(a,-d;c,-b)=(I tensor X)*A^(T2)*(I tensor X)'
    assert c['restricted_even_dual']=='Tr(rho)=1;rho>=0;abs(Re(rho_(++,--)))<=1/4'
    for key in ('forward_crossing_map_constructed','field_strength_crossing_checks_retained',
                'product_preparation_positive_crossed_sum_established','restricted_even_preparation_cone_characterized',
                'entangled_negative_even_moment_control_constructed','cut_free_local_matching_ambiguity_retained',
                'conditional_contour_assumptions_explicit','independent_dimensionful_couplings_retained'):
        assert c[key] is True,key
    for key in ('Gamma_is_positive_on_all_PSD_matrices','all_entangled_preparations_excluded',
                'restricted_cut_cone_is_all_UV_matrices','odd_crossing_has_universal_positive_bound',
                'global_dispersion_growth_assumptions_source_licensed','UV_fixed_order_spectral_positivity_derived',
                'leading_response_subtraction_count_is_quartic_growth_bound','finite_matching_fixed_or_bounded',
                'IR_subtracted_moments_automatically_positive','native_source_licensed',
                'physical_preparation_selected','physical_rates_or_branching_derived','UV_completion_constructed',
                'exact_scattering_operator_constructed','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=mom.build();assert parent==json.loads(mom.RESULT.read_text(encoding='utf-8')),'stale forward moments'
    units=[]
    for i,j in product(range(4),repeat=2):
        A=[[Q(int((a,b)==(i,j))) for b in range(4)] for a in range(4)]
        assert gamma(gamma(A))==A and trace(gamma(A))==trace(A);units.append(A)
    self_adjoint=0
    for A in units:
        for B in units:
            assert trace_product(A,gamma(B))==trace_product(gamma(A),B);self_adjoint+=1
    # Derive channel crossing in the existing transported field-strength frames.
    tensor_checks=0;sections=0;local_checks=0
    L2=[[Q(1,2),Q(-1),Q(),Q()],[Q(-1),Q(1,2),Q(),Q()],
        [Q(),Q(),Q(1,2),Q()],[Q(),Q(),Q(),Q(1,2)]]
    L3=[[Q((1 if i<2 else -1),2) if i==j else Q() for j in range(4)] for i in range(4)]
    assert gamma(L2)==L2 and gamma(L3)==scale(-1,L3)
    for E in (Q(1,4),Q(1,3)):
        s=4*E*E;ks=ir.crossed.kinematics(Q(1),Q(),E);cases=[]
        for i,out in enumerate(LABELS):
            for j,inc in enumerate(LABELS):
                cache=ir.crossed.tensor_cache(ks,ir.crossed.polarizations(inc+out,Q(1),Q()))
                sigmas=inc+tuple(-h for h in out);cases.append((i,j,cache,sigmas))
                for k,L in ((2,L2),(3,L3)):
                    value=sum((a*ir.power(z,k-2) for z,a in ir.crossed.tensor_terms(cache)),F())
                    assert value==F(s**k*L[i][j]);local_checks+=1
        for k,l in product(range(2,5),repeat=2):
            right=[[F() for _ in range(4)] for _ in range(4)];left=copy.deepcopy(right)
            for i,j,cache,sigmas in cases:
                coeff=ir.pair_log_coefficients(cache,sigmas,k,l)
                right[i][j]=coeff.get(tuple(F(s).encoded()),F())
                left[i][j]=coeff.get(tuple(F(-s).encoded()),F());sections+=1
                assert coeff.get(tuple(F().encoded()),F())==F()
            expected=scale(s**(k+l),mom.matrix(mom.pair_eigenvalues(k,l)))
            assert right==expected and left==scale((-1)**(k+l),gamma(right));tensor_checks+=1
    # Complex product-preparation identity, not an incoherent helicity average.
    I=phase.IM;spinors=((F(1),F()),(F(),F(1)),(F(1),F(1)),(F(1),I),(F(2),F(1)+I))
    vectors=((F(1),F(1),F(),F()),(F(1),I,F(2),F(1)-I),(F(),F(),F(1),I))
    product_checks=0
    for a,b in product(spinors,repeat=2):
        z=product_state(a,b);zc=product_state(a,(b[1].conjugate(),b[0].conjugate()))
        for v in vectors:
            A=outer(v)
            assert expectation(gamma(A),z)==expectation(A,zc);product_checks+=1
            assert rational(expectation(crossed_sum(A,2),z))>=0
    plus=[Q(1),Q(1),Q(),Q()];minus=[Q(1),Q(-1),Q(),Q()]
    rho=scale(Q(1,2),outer(plus));assert is_psd(rho) and not is_psd(gamma(rho))
    assert expectation(gamma(rho),minus)==-1
    rho_i=scale(Q(1,2),outer([F(1),I,F(),F()]))
    assert restricted_even_safe(rho_i) and not is_psd(gamma(rho_i))
    assert not restricted_even_safe(rho)
    identity=[[Q(int(i==j)) for j in range(4)] for i in range(4)]
    rho_mix=add(scale(Q(3,20),identity),scale(Q(2,5),rho))
    assert trace(rho_mix)==1 and is_psd(rho_mix) and not is_psd(gamma(rho_mix))
    assert is_psd(crossed_sum(rho_mix,2))  # entangled mixed control in the unrestricted even dual cone
    # Extremal rays generate exactly D>=|O|, M>=0; prove the preparation inequality's controls.
    cone_checks=0
    for D,O,M in ((Q(1),Q(1),Q()),(Q(1),Q(-1),Q()),(Q(),Q(),Q(1))):
        A=mom.matrix((D-O,D+O,M));K=crossed_sum(A,2)
        assert K==[[D+M,2*O,Q(),Q()],[2*O,D+M,Q(),Q()],
                   [Q(),Q(),D+M,Q()],[Q(),Q(),Q(),D+M]]
        for state in (rho,rho_i,outer([Q(1),Q(),Q(),Q()]),scale(Q(1,4),outer([Q(1)]*4))):
            value=rational(trace_product(state,K));x=rational((state[0][1]+state[1][0])/2)
            assert value==D+M+4*O*x
            if restricted_even_safe(state):assert value>=0
            cone_checks+=1
    tau=Q(1,2);polys=mom.eigen_polynomials({2:Q(1)})
    M2=mom.matrix([mom.moment(p,2,tau) for p in polys]);K2=crossed_sum(M2,2)
    negative=rational(expectation(K2,plus)/2);assert negative==Q(-37,3840)
    assert (M2[0][0]+M2[2][2])/(4*abs(M2[0][1]))==Q(63,200)
    assert rational(expectation(K2,[Q(1),Q(),Q(),Q()]))>0
    M3=mom.matrix([mom.moment(p,3,tau) for p in polys]);K3=crossed_sum(M3,3)
    assert K3[0][0]==Q(17,320) and K3[2][2]==Q(-17,320) and trace(K3)==0
    # Actual infinite spectral comparison: propagate the parent's certified eigenvalue boxes.
    boxes=parent['spectral_comparison']['eigenvalue_boxes']['2']
    lo={k:Q(v[0]) for k,v in boxes.items()};hi={k:Q(v[1]) for k,v in boxes.items()}
    # Bell-plus eigenvalue of M+Gamma(M) = (-minus+3*plus)/2 + mixed.
    spectral_box=[(-hi['minus']+3*lo['plus'])/2+lo['mixed'],(-lo['minus']+3*hi['plus'])/2+hi['mixed']]
    assert spectral_box[1]<0
    assumptions={key:True for key in ('poles_and_forward_limit_accounted','regular_IR_matching_jet_and_cut_inventory',
        'large_arc_zero_at_n','global_cut_positive_at_same_scope','jet_and_cut_same_scope','forward_crossing_and_Hermitian_analyticity')}
    assert conditional_dispersion_gate(2,2,2,assumptions)
    failed_gates=0
    for key in assumptions:
        try:conditional_dispersion_gate(2,2,2,{**assumptions,key:False})
        except AssertionError:failed_gates+=1
        else:raise AssertionError('missing contour assumption admitted')
    for n,N,k0 in ((2,3,2),(4,2,2)):
        try:conditional_dispersion_gate(n,N,k0,assumptions)
        except AssertionError:failed_gates+=1
        else:raise AssertionError('subtraction or IR gate bypassed')
    refused=[]
    for name in ('Gamma_is_positive_on_all_PSD_matrices','all_entangled_preparations_excluded',
                 'restricted_cut_cone_is_all_UV_matrices','odd_crossing_has_universal_positive_bound',
                 'global_dispersion_growth_assumptions_source_licensed','UV_fixed_order_spectral_positivity_derived',
                 'leading_response_subtraction_count_is_quartic_growth_bound','finite_matching_fixed_or_bounded'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported crossing promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((mom.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_forward_crossing_positivity.py'))
    return {'schema':'marici.scattering.forward-crossing-positivity-receipt.v1','status':'pass',
        'scope_verdict':'crossing_preparation_cones_and_conditional_contours_not_physical_matching_bounds',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'Gamma_matrix_unit_checks':len(units),'Gamma_self_adjoint_checks':self_adjoint,
        'field_crossing_matrix_checks':tensor_checks,'physical_helicity_section_checks':sections,
        'local_cut_free_counterterm_section_checks':local_checks,'complex_product_preparation_checks':product_checks,
        'restricted_cone_controls':cone_checks,'missing_contour_or_scope_controls_refused':failed_gates,
        'c0_only_tau_half_even_n2_Bell_plus':str(negative),
        'spectral_zero_subtraction_pi_squared_even_n2_Bell_plus_box':list(map(str,spectral_box)),
        'general_crossing_and_contour_arguments_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale forward crossing positivity'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','field_crossing_matrix_checks','complex_product_preparation_checks',
        'c0_only_tau_half_even_n2_Bell_plus','finite_matching_fixed_or_bounded','hostile_controls_refused')}))


if __name__=='__main__':main()
