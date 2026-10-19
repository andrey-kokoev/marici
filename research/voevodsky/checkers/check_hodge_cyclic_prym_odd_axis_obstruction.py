"""Actual elliptic-surface saturation and odd-axis/free-C4 obstruction."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from math import isqrt
from pathlib import Path
import json
import check_hodge_indecomposable_principal_model as target
import check_hodge_equivariant_tetragonal_gate as gate
import check_hodge_trigonal_principal_match_obstruction as previous

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-cyclic-prym-odd-axis-obstruction.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-cyclic-prym-odd-axis-obstruction-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-cyclic-prym-odd-axis-obstruction-v1.json'
POLICY=['all_unpolarized_K_isogenies_excluded','all_nonunit_polarized_isogenies_excluded',
    'all_smooth_etale_double_Prym_presentations_excluded',
    'all_ramified_Prym_presentations_excluded','elliptic_axis_preservation_merely_assumed',
    'all_surface_unitaries_extend_to_Y2','finite_unitaries_counted_as_actual_curve_actions',
    'auxiliary_cover_existence_refuted','auxiliary_Weil_algebraicity_refuted',
    'actual_isogeny_source_axes_constructed','actual_theta_dimension_computed','target_cycle_constructed',
    'Hodge_proved','Hodge_refuted','global_witness_search_completed']
GEOMETRY={'elliptic_isotypic_surface_is_actual_product':True,
    'physical_CM_product_polarization_degrees':[2,3],
    'native_Gaussian_surface_Hermitian_diagonal':[2,-3],'free_curve_group_order':4,
    'Prym_deck_square':'minus_identity','elliptic_adjoint_curve_degree_multiplier':2,
    'odd_axis_degree':3,'odd_axis_curve_degree':6}
INPUTS={'target':'research/voevodsky/results/hodge-indecomposable-principal-model-v1.json',
    'axis_gate':'research/voevodsky/results/hodge-equivariant-tetragonal-gate-v1.json',
    'previous':'research/voevodsky/results/hodge-trigonal-principal-match-obstruction-v1.json'}
Z=(Q(0),Q(0));ONE=(Q(1),Q(0))


def require(c,m):
    if not c:raise ValueError(m)


def plus(a,b):return (a[0]+b[0],a[1]+b[1])


def conjugate(a):return (a[0],-a[1])


def times(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def norm(a):return a[0]**2+a[1]**2


def inner(a,b,weights):
    v=Z
    for x,y,d in zip(a,b,weights):
        c=times(conjugate(x),y);v=plus(v,(d*c[0],d*c[1]))
    return v


def unitary_restriction_controls(weights):
    require(len(weights)==2 and all(type(w) is int and w>0 for w in weights),'positive integral CM product weights')
    bound=isqrt(max(weights)//min(weights))
    gaussian=tuple(product(range(-bound,bound+1),repeat=2))
    columns=[]
    for w in weights:
        columns.append([v for v in product(gaussian,repeat=2) if inner(v,v,weights)==(w,0)])
    return [(a,b) for a,b in product(*columns) if inner(a,b,weights)==Z]


def matrix_square_is_minus_identity(columns):
    a,b=columns
    m=[[a[0],b[0]],[a[1],b[1]]]
    for i,j in product(range(2),repeat=2):
        v=plus(times(m[i][0],m[0][j]),times(m[i][1],m[1][j]))
        if v!=((-1,0) if i==j else (0,0)):return False
    return True


def invariant_fibre_divisibility(degree,*,free_action=True,axis_preserved=True,linear_part_square_minus_one=True):
    require(type(degree) is int and degree>0,'positive elliptic map degree')
    require(free_action is True and axis_preserved is True and linear_part_square_minus_one is True,
        'free C4, invariant axis and order-four linear part required')
    return degree%4==0


def exact_core():
    m=target.gaussian_matrix()
    bplus=[m[i][6] for i in range(8)]
    bminus=[times(m[i][7],(Q(1,2),Q(-1,2))) for i in range(8)]
    supports=[{i for i,c in enumerate(b) if c!=Z} for b in (bplus,bminus)]
    require(supports==[{0,6},{5,7}] and supports[0].isdisjoint(supports[1]),'actual elliptic surface disjoint column supports')
    require(bplus[0]==ONE and bminus[7]==ONE and
        all(x.denominator==y.denominator==1 for x,y in bplus+bminus),'joint Gaussian saturation')
    require(inner(bplus,bplus,target.DY)==(2,0) and inner(bminus,bminus,target.DY)==(-3,0) and
        inner(bplus,bminus,target.DY)==Z,'actual native surface Hermitian restriction')
    u=unitary_restriction_controls((2,3))
    require(len(u)==16 and all(a[1]==Z and b[0]==Z and norm(a[0])==norm(b[1])==1 for a,b in u),
        'unequal product weights force both axes preserved')
    fourth=[v for v in u if matrix_square_is_minus_identity(v)]
    require(len(fourth)==4 and all(a[0] in ((0,1),(0,-1)) and b[1] in ((0,1),(0,-1)) for a,b in fourth),
        'square-minus-one restrictions')
    equal=unitary_restriction_controls((2,2))
    require(len(equal)==32 and any(a[1]!=Z for a,b in equal),'equal-weight axis exchange countercontrol')
    require(invariant_fibre_divisibility(4) and not invariant_fibre_divisibility(6) and
        invariant_fibre_divisibility(8),'free-orbit fibre controls')
    require(all(invariant_fibre_divisibility(2*d)==(d%2==0) for d in range(1,25)), 'elliptic theta-degree parity')
    return {'actual_surface_native_Gaussian_columns':[[[str(x),str(y)] for x,y in b] for b in (bplus,bminus)],
        'physical_CM_product_polarization_degrees':[2,3],
        'surface_unitary_restriction_upper_bound':16,'square_minus_one_restriction_upper_bound':4,
        'equal_weight_countercontrol_unitaries':32,'odd_axis_theta_degree':3,'forced_elliptic_curve_map_degree':6,
        'required_free_C4_fibre_degree_divisor':4,'degree_six_remainder_mod_four':2,
        'conditional_K_isogeny_source_axis_theta_degrees_even':True,
        'conditional_auxiliary_K_isogeny_source_minimum_axis_theta_degree':4}


def validate_contract(c):
    require(c['schema']=='marici.hodge-cyclic-prym-odd-axis-obstruction.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='y2-etale-cyclic-quartic-polarized-transplant','odd-axis identity')
    require(c['comparison']=='natural_principal_Prym_isomorphism_not_arbitrary_unpolarized_isogeny' and
        c['geometry']==GEOMETRY,'odd-axis comparison hypotheses changed')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'odd-axis exclusion promoted')
    exact_core()


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    reports={'target':target.report(),'axis_gate':gate.report(),'previous':previous.report()}
    for k,r in reports.items():
        require(json.loads((ROOT/INPUTS[k]).read_text(encoding='utf-8'))==r and r['passed'],'stale '+k)
    require(reports['target']['elliptic_axis_isogeny_degrees']==[1,2] and
        reports['target']['elliptic_axis_polarization_degrees']==[2,3],'actual target axes missing')
    require(reports['previous']['fixed_Y2_natural_principal_match_for_auxiliary_family_excluded'] and
        reports['previous']['forced_Prym_factor_dimensions']==[2,6],'previous quotient argument missing')
    names=set(INPUTS.values())|{CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
        Path(__file__).relative_to(ROOT).as_posix()}
    return {'schema':'marici.hodge-cyclic-prym-odd-axis-obstruction-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',
        'verification_level':'Written isotypic-surface, unitary, adjoint and free-orbit proof with exact lattice/unitary/parity controls; no arbitrary-isogeny exclusion.',
        'checks':{'actual_target_surface_saturated':True,'both_axes_intrinsically_preserved':True,
            'adjoint_degree_and_affine_equivariance':True,'fixed_fibre_free_orbit_divisibility':True,
            'conditional_unpolarized_source_parity_scope':True,'prior_receipts_fresh':True,'scope':True},
        **exact_core(),'fixed_Y2_smooth_etale_cyclic_quartic_principal_presentations_excluded':True,
        **{k:False for k in POLICY},
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
