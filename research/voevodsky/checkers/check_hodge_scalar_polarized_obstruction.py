"""Low elliptic degree excludes scalar towers for the fixed principal Y2 only."""
from hashlib import sha256
from math import gcd
from pathlib import Path
import json
from check_hodge_scalar_family_localization import report as family_report
from check_hodge_commuting_prym_audit import report as commuting_report
from check_hodge_indecomposable_principal_model import report as target_report

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-scalar-polarized-obstruction.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-scalar-polarized-obstruction-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-scalar-polarized-obstruction-v1.json'
PRIMARY='research/voevodsky/inputs/hodge-commuting-prym-audit-v1/'
POLICY=['all_scalar_unpolarized_isogenies_excluded','other_principal_polarizations_excluded',
    'general_smooth_etale_Prym_membership_excluded','nonlifting_labels_excluded',
    'nonlifting_joint_map_independence_established','unpolarized_label_census_changed',
    'conditional_biellipticity_asserted_unconditionally','theta_dimension_computed',
    'actual_cover_matching_Y2_constructed','finite_field_cycles_transferred_to_X',
    'Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
    'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved',
    'global_witness_search_completed']


def require(c,m):
    if not c: raise ValueError(m)


def source_paths():
    return {PRIMARY+'mumford.p9.txt',PRIMARY+'mumford.p9.png'}


def joint_degrees(m,n):
    require(all(type(x) is int and x>0 for x in (m,n)),'positive map degrees')
    return [d for d in range(1,gcd(m,n)+1) if m%d==0 and n%d==0]


def independent_elliptic_genus_bound(m,n,joint_degree=1):
    require(joint_degree==1,'birational joint image required')
    joint_degrees(m,n)
    return 1+m*n


def curve_map_degree(elliptic_polarization_degree,jacobian_multiplier=2):
    require(type(elliptic_polarization_degree) is int and elliptic_polarization_degree>0,
        'positive elliptic polarization degree')
    require(jacobian_multiplier==2,'etale Prym restriction must be twice principal')
    return jacobian_multiplier*elliptic_polarization_degree


def minimum_elliptic_degree(genus,source_degree=2,h_on_source='translation'):
    require(type(genus) is int and genus>=2,'top curve genus')
    require(source_degree==2 and h_on_source=='translation','quadratic source and invariant differentials required')
    # Anti-h Prym forms cannot factor through the h-invariant elliptic forms.
    # The quadratic extension then makes the joint map birational.
    return (genus-1+3)//4


def census():
    total,norm_zero,mixed,scalar,nonlifting=1024,256,252,4,512
    require(total-norm_zero-mixed==scalar+nonlifting==516,'inherited isogeny census')
    polarized=total-norm_zero-mixed-scalar
    require(polarized==nonlifting and all(x%2==0 for x in (scalar,polarized,scalar+nonlifting)),
        'inverse label pairing')
    return {'conditional_polarized_Y2_survivor_labels':polarized,
        'conditional_polarized_Y2_survivor_inverse_pairs':polarized//2,
        'conditional_unpolarized_isogeny_survivor_labels':scalar+nonlifting,
        'conditional_unpolarized_isogeny_survivor_inverse_pairs':(scalar+nonlifting)//2,
        'scalar_labels_removed_for_fixed_polarization_only':scalar,
        'nonlifting_labels_not_tested':nonlifting}


def exact_core():
    lower=minimum_elliptic_degree(17)
    require(lower==4,'bielliptic Prym elliptic degree threshold')
    rows=[]
    for e in (1,2,3,4):
        d=curve_map_degree(e);bound=independent_elliptic_genus_bound(2,d)
        require((17>bound)==(e<lower),'genus threshold control')
        rows.append({'elliptic_Prym_polarization_degree':e,'curve_map_degree':d,
            'joint_degrees_before_anti_invariant_argument':joint_degrees(2,d),
            'genus_upper_bound_after_independence':bound,'excluded_at_genus17':17>bound})
    require(joint_degrees(4,4)==[1,2,4] and independent_elliptic_genus_bound(4,4)==17,
        'nonlifting case cannot inherit quadratic independence')
    # Product-elliptic numerical divisor controls with correspondence terms.
    # Hermitian off-diagonal z lowers D^2 by 2|z|^2, never raises the bound.
    intersections=[]
    for a,b in ((0,0),(1,0),(0,1),(1,1)):
        det=2*4-a*a-b*b
        require(det>0 and 1+det<=independent_elliptic_genus_bound(2,4),'cross-term genus bound')
        intersections.append({'off_diagonal':[a,b],'self_intersection':2*det,'arithmetic_genus':1+det})
    return {'top_genus':17,'scalar_bielliptic_map_degree':2,
        'Jacobian_restriction_multiplier':2,'minimum_elliptic_Prym_polarization_degree':lower,
        'target_elliptic_polarization_degrees':[2,3],
        'target_degree_two_curve_map_degree':4,'target_degree_two_genus_upper_bound':9,
        'elliptic_degree_controls':rows,'correspondence_intersection_controls':intersections,
        'quadratic_joint_map_independence_from_anti_invariance':True,
        'all_four_scalar_labels_excluded_for_polarized_Y2':True,
        'canonical_polarized_Y2_scalar_realizations_excluded':True,
        'nonlifting_joint_degrees_still_to_analyze':[1,2,4],
        'nonlifting_4_by_4_genus_bound_if_independent':17,
        'actual_theta_singularity_dimension':None,**census()}


def validate_certificate(c):
    require(c['schema']=='marici.hodge-scalar-polarized-obstruction.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='scalar-polarized-prym-transplant' and c['verdict']=='rejected','scalar polarized identity')
    require(c['resolution_kind']=='anti_invariant_elliptic_map_quadratic_independence_and_genus_bound','scalar polarized resolution')
    require(c['geometry']=={'top_genus':17,'source_elliptic_map_degree':2,
        'h_on_source_elliptic':'translation','Prym_Jacobian_restriction_multiplier':2,
        'fixed_Y2_elliptic_polarization_degree':2,'comparison':'canonical_principal_polarized_isomorphism',
        'scalar_level_labels':4,'nonlifting_labels':512,
        'conditional_polarized_survivor_labels':512,'conditional_unpolarized_survivor_labels':516},
        'scalar polarized scope')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'scalar polarized promotion')


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_certificate(c)
    expected={'previous_receipt':'research/voevodsky/results/hodge-scalar-family-localization-v1.json',
        'commuting_receipt':'research/voevodsky/results/hodge-commuting-prym-audit-v1.json',
        'target_receipt':'research/voevodsky/results/hodge-indecomposable-principal-model-v1.json'}
    require(all(c[k]==v for k,v in expected.items()),'scalar polarized input binding')
    family=json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    old=json.loads((ROOT/c['commuting_receipt']).read_text(encoding='utf-8'))
    target=json.loads((ROOT/c['target_receipt']).read_text(encoding='utf-8'))
    require(family==family_report(),'stale scalar family')
    require(old==commuting_report() and old['remaining_commuting_pulled_root_labels']==4 and
        old['nonlifting_root_labels_not_tested_here']==512,'stale commuting census')
    require(target==target_report() and target['elliptic_axis_polarization_degrees']==[2,3],
        'stale target elliptic degrees')
    text=(ROOT/(PRIMARY+'mumford.p9.txt')).read_text(encoding='utf-8')
    require('Corollary 2.' in text and 'unramified' in text and 'principal polarization' in text,
        'Mumford etale polarization source anchors')
    sources=source_paths() | {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | set(expected.values()) | {
        'research/voevodsky/checkers/check_hodge_scalar_family_localization.py',
        'research/voevodsky/checkers/check_hodge_commuting_prym_audit.py',
        'research/voevodsky/checkers/check_hodge_indecomposable_principal_model.py'}
    return {'schema':'marici.hodge-scalar-polarized-obstruction-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',**exact_core(),
        'checks':dict.fromkeys(['fresh_scalar_classification_target_degrees_and_primary_Mumford_halving',
            'elliptic_embedding_adjoint_gives_curve_degree_two_e',
            'anti_invariance_rules_out_factoring_through_elliptic_source',
            'quadratic_extension_proves_joint_birationality_without_coprimality',
            'Hodge_index_and_adjunction_bound_genus_by_one_plus_degree_product',
            'scalar_polarized_census_separated_from_unpolarized_isogeny_census',
            'nonlifting_degree_four_source_independence_not_assumed'],True),
        **c['scope_policy'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
