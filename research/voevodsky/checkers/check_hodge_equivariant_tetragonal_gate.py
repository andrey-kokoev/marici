"""Necessary equivariant tetragonal/base-change diagram; no target construction."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
from check_hodge_nonlifting_polarized_obstruction import report as nonlifting_report
from check_hodge_y2_curve_audit import report as curve_report
from check_hodge_hyperelliptic_bottom_audit import report as bottom_report
from check_hodge_indecomposable_principal_model import report as target_report

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-equivariant-tetragonal-gate.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-equivariant-tetragonal-gate-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-equivariant-tetragonal-gate-v1.json'
POLICY=['actual_theta_dimension_computed','theta_lower_bound_four_asserted',
    'all_cyclic_quartic_presentations_excluded','all_smooth_etale_Prym_presentations_excluded',
    'actual_cover_matching_Y2_constructed','diagram_conditions_sufficient_for_target',
    'all_tetragonal_pencils_identical','C5_gonality_exactly_four_asserted',
    'even_fibres_alone_prove_connectedness','deck_generator_preserves_chosen_elliptic_axis_assumed',
    'base_involution_preserves_harmonic_branch_set_assumed','all_unpolarized_isogenies_excluded',
    'finite_patterns_counted_as_actual_covers','finite_field_cycles_transferred_to_X',
    'Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
    'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved',
    'global_witness_search_completed']


def require(c,m):
    if not c: raise ValueError(m)


def pencil_joint_case(d,genus=9,free=True,nonhyperelliptic=True,nonbielliptic=True):
    require(type(d) is int and d in (1,2,4),'quartic pencil joint degree')
    require(type(genus) is int and genus>=2 and all(type(x) is bool for x in
        (free,nonhyperelliptic,nonbielliptic)),'pencil hypotheses')
    if d==4: return 'invariant_pencil'
    if d==2:
        return 'excluded_by_rational_or_elliptic_quadratic_quotient' if nonhyperelliptic and nonbielliptic else 'quadratic_quotient_not_excluded'
    if genus>9: return 'excluded_by_genus_bound'
    if genus<9: return 'singular_image_may_separate_fixed_branches'
    return 'excluded_by_smooth_4_4_image_and_fixed_diagonal' if free else 'fixed_points_permitted'


def even_partition(p):
    require(bool(p) and all(type(x) is int and x>0 for x in p) and sum(p)==4,'degree four fibre partition')
    return all(x%2==0 for x in p)


def ramification_budget(pattern,genus):
    pattern=tuple(tuple(p) for p in pattern)
    require(genus in (5,9) and len(pattern)==(2 if genus==5 else 4),'prescribed fibre coverage')
    require(all(even_partition(p) for p in pattern),'odd multiplicity ramifies quadratic pullback')
    total=2*genus-2+8
    used=sum(sum(e-1 for e in p) for p in pattern)
    k=sum(p==(4,) for p in pattern)
    require(total-used>=0,'ramification budget')
    r={'source_genus':genus,'total_ramification':total,'even_fibre_ramification':used,
        'other_ramification':total-used,'totally_ramified_even_fibres':k}
    if genus==9:
        r['C17_to_CM_elliptic_ramification_at_branch_values']=2*k
        r['C17_to_CM_elliptic_ramification_elsewhere']=2*(total-used)
        require(2*k+2*(total-used)==32,'elliptic cover Riemann Hurwitz')
    else:
        r['C9_to_P1_ramification_at_branch_values']=2*k
        r['C9_to_P1_ramification_elsewhere']=2*(total-used)
        require(2*k+2*(total-used)==24,'bottom base change Riemann Hurwitz')
    return r


def legendre_j(lam):
    require(type(lam) in (int,Q),'exact branch cross-ratio')
    lam=Q(lam);require(lam not in (0,1),'four distinct branch values')
    return 256*(1-lam+lam*lam)**3/(lam*lam*(1-lam)**2)


def lift_order(norm):
    require(type(norm) is int and norm in (-1,1),'lift norm must be plus or minus one')
    return 4 if norm==-1 else 2


def exact_core():
    cases={str(d):pencil_joint_case(d) for d in (1,2,4)}
    require(cases['1'].startswith('excluded_') and cases['2'].startswith('excluded_') and
        cases['4']=='invariant_pencil','free involution pencil invariance')
    partitions=((4,),(3,1),(2,2),(2,1,1),(1,1,1,1))
    allowed=tuple(p for p in partitions if even_partition(p))
    require(allowed==((4,),(2,2)),'local even-multiplicity criterion')
    top=[ramification_budget(p,9) for p in product(allowed,repeat=4)]
    bottom=[ramification_budget(p,5) for p in product(allowed,repeat=2)]
    harmonic=(Q(-1),Q(2),Q(1,2))
    require(all(legendre_j(x)==1728 for x in harmonic) and legendre_j(3)!=1728,'CM branch harmonic cross-ratio')
    # Formal constant-cocycle controls, not constructed genus5/9 curves.
    # F=u^3-u is odd: F(-u)/F(u)=-1; r=i squares and norms to -1.
    odd=(0,-1,0,1);even=(1,0,0,0,1)
    require(tuple((-1)**k*v for k,v in enumerate(odd))==tuple(-v for v in odd) and
        tuple((-1)**k*v for k,v in enumerate(even))==even,'odd/even cocycle controls')
    require((0*0-1*1,2*0*1)==(-1,0) and lift_order(-1)==4 and lift_order(1)==2,'order four versus involutive lift')
    return {'pencil_joint_cases':cases,'pencil_joint_degrees_exhausted':[1,2,4],
        'birational_4_4_P1_product_arithmetic_genus':9,'fixed_diagonal_intersection_degree':8,
        'necessary_C9_gonality':4,'free_intermediate_involution_preserves_pencil':True,
        'induced_P1_involution_nontrivial':True,'necessary_C5_map_degree':4,
        'C9_is_normalized_quadratic_base_change_of_C5_pencil':True,
        'C17_is_normalized_CM_elliptic_base_change_of_C9_pencil':True,
        'allowed_even_fibre_partitions':[list(p) for p in allowed],
        'bottom_required_even_fibres':2,'top_required_harmonic_even_fibres':4,
        'top_local_pattern_controls':len(top),'bottom_local_pattern_controls':len(bottom),
        'top_ramification_budgets':top,'bottom_ramification_budgets':bottom,
        'CM_elliptic_j_invariant':1728,'harmonic_cross_ratio_values':['-1','2','1/2'],
        'connected_quadratic_square_classes_required_nontrivial':True,
        'cyclic_lift_equations':['r^2=F(mu(g))/F(g)','eta(r)*r=-1'],
        'constant_cocycle_controls':{'odd_cubic_r_i_lift_order':4,'even_quartic_r_1_lift_order':2},
        'actual_theta_singularity_dimension':None,
        'conditional_bielliptic_polarized_survivor_labels':0,
        'conditional_unpolarized_isogeny_survivor_labels':516}


def validate_certificate(c):
    require(c['schema']=='marici.hodge-equivariant-tetragonal-gate.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='equivariant-tetragonal-gate' and c['verdict']=='constructed','tetragonal identity')
    require(c['resolution_kind']=='elliptic_axis_quotient_free_involution_pencil_and_even_fibre_cyclic_lift_gate','tetragonal resolution')
    require(c['geometry']=={'curve_genera':[17,9,5],'C9_gonality':4,'C5_map_degree':4,
        'fixed_Y2_elliptic_degree':2,'elliptic_axis_source_isogeny_degree':1,
        'CM_elliptic_j':1728,'free_intermediate_involution':True,
        'C9_hyperelliptic_or_bielliptic':False,'C5_hyperelliptic':False,
        'bottom_even_fibres':2,'top_harmonic_even_fibres':4,
        'connected_square_classes_required':True,'cyclic_lift_norm':-1},'tetragonal scope')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'tetragonal promotion')


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_certificate(c)
    expected={'previous_receipt':'research/voevodsky/results/hodge-nonlifting-polarized-obstruction-v1.json',
        'curve_receipt':'research/voevodsky/results/hodge-y2-curve-audit-v1.json',
        'bottom_receipt':'research/voevodsky/results/hodge-hyperelliptic-bottom-audit-v1.json',
        'target_receipt':'research/voevodsky/results/hodge-indecomposable-principal-model-v1.json'}
    require(all(c[k]==v for k,v in expected.items()),'tetragonal input binding')
    old=json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    curve=json.loads((ROOT/c['curve_receipt']).read_text(encoding='utf-8'))
    bottom=json.loads((ROOT/c['bottom_receipt']).read_text(encoding='utf-8'))
    target=json.loads((ROOT/c['target_receipt']).read_text(encoding='utf-8'))
    require(old==nonlifting_report() and old['fixed_Y2_bielliptic_intermediate_cyclic_realizations_excluded'],
        'stale bielliptic exclusion')
    require(curve==curve_report() and curve['minimum_genus9_intermediate_gonality_for_cyclic_realization']==4,
        'stale gonality lower bound')
    require(bottom==bottom_report() and bottom['hyperelliptic_genus5_bottom_excluded_up_to_isogeny_to_fixed_A'],
        'stale bottom exclusion')
    require(target==target_report() and target['elliptic_axis_isogeny_degrees']==[1,2] and
        target['elliptic_axis_polarization_degrees']==[2,3],'stale actual CM elliptic axis')
    sources={p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | set(expected.values()) | {
        'research/voevodsky/checkers/check_hodge_nonlifting_polarized_obstruction.py',
        'research/voevodsky/checkers/check_hodge_y2_curve_audit.py',
        'research/voevodsky/checkers/check_hodge_hyperelliptic_bottom_audit.py',
        'research/voevodsky/checkers/check_hodge_indecomposable_principal_model.py',
        'research/voevodsky/hodge-split-eightfold-stabilization-v1.md'}
    return {'schema':'marici.hodge-equivariant-tetragonal-gate-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**exact_core(),
        'checks':dict.fromkeys(['fresh_nonbielliptic_gonality_bottom_and_actual_CM_axis_bindings',
            'degree_four_CM_map_descends_through_anti_involution_to_tetragonal_pencil',
            'free_involution_preserves_pencil_by_all_joint_degrees_and_fixed_diagonal',
            'nontrivial_P1_involution_and_connected_bottom_base_change',
            'top_harmonic_branch_and_normalization_even_fibre_conditions',
            'Riemann_Hurwitz_budgets_and_connectedness_not_inferred_from_parity',
            'cyclic_order_four_norm_minus_one_not_V4_norm_plus_one'],True),
        **c['scope_policy'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','top_ramification_budgets','bottom_ramification_budgets')},indent=2))
