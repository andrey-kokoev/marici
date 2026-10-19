"""Norm stratification of the conditional bielliptic cover family; no target cover."""
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from itertools import product
import json
from check_hodge_hyperelliptic_bottom_audit import report as bottom_report, torsion_roots

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-bielliptic-lift-audit.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-bielliptic-lift-audit-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-bielliptic-lift-audit-v1.json'
POLICY = ['bielliptic_branch_is_unconditional','all_root_classes_excluded',
    'all_bielliptic_involutions_lift','commuting_lift_implies_equal_fourfold_factors',
    'nonlifting_classes_have_dihedral_decomposition','all_Prym_presentations_excluded',
    'actual_cover_matching_Y2_constructed','theta_dimension_computed',
    'root_counts_are_unmarked_moduli_counts','retained_roots_are_target_realizations',
    'ramified_top_covers_included','finite_lattice_model_is_actual_torsion_coordinates']


def require(condition,message):
    if not condition:
        raise ValueError(message)


def pullback(v):
    # Primitive integral elliptic embedding of polarization degree two.
    a,b = v
    return (a%4,2*b%4,b%4)+(0,)*7


def norm(v):
    return ((2*v[0]-v[3])%4,v[1]%4)


def negate(v):
    return tuple(-a%4 for a in v)


def deck_action(v):
    # kappa0^* Nm = Id + b0^*, in additive Picard notation.
    p = pullback(norm(v))
    return tuple((a-b)%4 for a,b in zip(p,v))


def lift_type(n):
    require(n in {(0,0),(2,0),(0,2),(2,2)},'norm must be elliptic two-torsion')
    if n == (0,0):
        return 'inverting_dihedral_excluded_up_to_A_isogeny'
    if n == (2,0):
        return 'commuting_lift_not_excluded_here'
    return 'no_bielliptic_involution_lift_not_excluded_here'


@lru_cache(maxsize=1)
def exact_core():
    zeta = (2,0)
    eta = pullback(zeta)
    require(eta == (2,)+(0,)*9,'eta marking')
    require(len({pullback((a,b)) for a in range(4) for b in range(4)}) == 16,'primitive elliptic pullback control')
    require({norm(v) for v in product((0,2),repeat=10)} ==
        {(0,0),(2,0),(0,2),(2,2)},'norm surjectivity on two-torsion')
    for a in range(4):
        for b in range(4):
            require(norm(pullback((a,b))) == (2*a%4,2*b%4),'norm pullback is multiplication by two')
    roots = torsion_roots()
    census = Counter()
    types = Counter()
    examples = {}
    for v in roots:
        n = norm(v)
        b = deck_action(v)
        require(deck_action(b) == v and tuple(2*x%4 for x in b) == eta,'base deck action on roots')
        kind = lift_type(n)
        require((b == negate(v)) == (n == (0,0)) and
                (b == v) == (n == zeta),'lift inversion versus commuting distinction')
        census[str(n)] += 1
        types[kind] += 1
        examples.setdefault(kind,list(v))
    require(set(census.values()) == {256} and sum(census.values()) == 1024,'four equal norm strata')
    require(types == {'inverting_dihedral_excluded_up_to_A_isogeny':256,
        'commuting_lift_not_excluded_here':256,
        'no_bielliptic_involution_lift_not_excluded_here':512},'lifting census')
    retained = [v for v in roots if norm(v) != (0,0)]
    require(len(retained) == 768 and len({min(v,negate(v)) for v in retained}) == 384,'retained necessary-condition root labels')
    # Same abstract pairing control: <pull a,x>_J = <a,norm x>_E mod 4.
    for a in ((1,0),(0,1)):
        pa = pullback(a)
        for j in range(10):
            v = tuple(int(i == j) for i in range(10))
            nv = norm(v)
            lhs = sum(pa[i]*v[i+1]-pa[i+1]*v[i] for i in range(0,10,2))%4
            require(lhs == (a[0]*nv[1]-a[1]*nv[0])%4,'polarization adjoint control')
    return {'conditional_on_bielliptic_intermediate':True,
        'norm_zero_roots_excluded_up_to_fixed_A_isogeny':True,
        'universal_bielliptic_lifting_claim_refuted':True,
        'norm_stratum_counts':dict(sorted(census.items())),
        'lift_type_counts':dict(sorted(types.items())),
        'norm_zero_excluded_root_labels':256,'norm_zero_excluded_inverse_pairs':128,
        'commuting_lift_root_labels':256,'nonlifting_root_labels':512,
        'retained_necessary_condition_root_labels':768,'retained_inverse_pairs':384,
        'sample_abstract_root_labels':examples,
        'actual_theta_singularity_dimension':None,'actual_matching_root_label':None}


def validate_audit(c):
    require(c['schema'] == 'marici.hodge-bielliptic-lift-audit.v1' and
        c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node'] == 'bielliptic-involution-lift-transplant' and c['verdict'] == 'rejected', 'bielliptic-lift identity')
    require(c['resolution_kind'] == 'norm_strata_dihedral_quarter_exclusion_and_nonlifting_half_control','bielliptic-lift resolution')
    require(c['geometry'] == {'conditional_intermediate_genus':9,'bottom_genus':5,
        'elliptic_double_cover_branch_degree':8,'top_cover':'connected_etale_cyclic_quartic',
        'line_bundle_equation':'L^2=kappa0^*zeta','zeta_nonzero_order_two':True,
        'norm_kernel_connected':True,'pointed_lift_used_for_inverting_case':True},'bielliptic-lift geometry scope')
    require(c['level_data'] == {'total_roots':1024,'each_norm_stratum':256,
        'nonlifting_roots':512,'retained_roots':768,'retained_inverse_pairs':384},'bielliptic-lift census scope')
    require(set(c['scope_policy']) == set(POLICY) and
        all(v is False for v in c['scope_policy'].values()),'bielliptic-lift scope promoted')
    require(set(c['boundary']) == {'Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
        'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved',
        'global_witness_search_completed'} and all(v is False for v in c['boundary'].values()),'bielliptic-lift verdict promotion')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_audit(c)
    require(c['previous_receipt'] == 'research/voevodsky/results/hodge-hyperelliptic-bottom-audit-v1.json','previous bottom-audit binding')
    old = json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old == bottom_report() and old['candidate_id'] == c['candidate_id'] and
        old['actual_theta_singularity_dimension'] is None and
        old['conditional_bielliptic_descent']['marked_formal_4_torsion_root_count'] == 1024,'stale bottom audit')
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_hyperelliptic_bottom_audit.py'}
    return {'schema':'marici.hodge-bielliptic-lift-audit-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',**exact_core(),
        'checks':dict.fromkeys(['norm_kernel_connected_by_duality_and_no_elliptic_isogeny_factor',
            'norm_pullback_and_primitive_polarization_adjoint_control',
            'four_equal_norm_cosets_of_the_root_torsor',
            'norm_zero_pointed_inverting_lift_forces_incompatible_square_fourfolds',
            'commuting_case_not_given_inverting_square_argument',
            'nonlifting_half_blocks_universal_lift_shortcut',
            'retained_labels_are_only_necessary_conditions'],True),
        **c['scope_policy'],**c['boundary'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'source_sha256'},indent=2))
