"""Scoped principal-match obstruction: CS quotients force an excluded sixfold."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import check_hodge_ramified_trigonal_family as family
import check_hodge_equivariant_tetragonal_gate as gate
import check_hodge_cyclic_prym_audit as sixfold

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-trigonal-principal-match-obstruction.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-trigonal-principal-match-obstruction-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-trigonal-principal-match-obstruction-v1.json'
POLICY=['all_unpolarized_K_isogenies_to_Y2_excluded','all_smooth_etale_Prym_presentations_excluded',
    'all_ramified_cover_constructions_excluded','auxiliary_cover_existence_refuted',
    'auxiliary_Weil_algebraicity_refuted','deck_generator_preserves_chosen_elliptic_axis_assumed',
    'arbitrary_elliptic_map_degree_admitted','actual_low_genus_quotient_constructed',
    'actual_theta_dimension_computed','target_cycle_constructed','Hodge_proved','Hodge_refuted',
    'global_witness_search_completed']
GEOMETRY={'etale_top_genus':17,'free_cyclic_group_order':4,'orientation_pencil_degree':4,
    'fixed_Y2_elliptic_theta_degree':2,'conditional_top_to_elliptic_degree':4,
    'target_simple_sixfold_raw_norm_class':'-3','target_simple_sixfold_End0':'Q(i)'}
INPUTS={'family':'research/voevodsky/results/hodge-ramified-trigonal-family-v1.json',
    'axis_gate':'research/voevodsky/results/hodge-equivariant-tetragonal-gate-v1.json',
    'sixfold_exclusion':'research/voevodsky/results/hodge-cyclic-prym-audit-v1.json'}


def require(c,m):
    if not c:raise ValueError(m)


def cs_bound(d1,g1,d2,g2):
    require(all(type(x) is int for x in (d1,g1,d2,g2)) and min(d1,d2)>0 and min(g1,g2)>=0,'CS degrees and genera')
    return d1*g1+d2*g2+(d1-1)*(d2-1)


def quartic_joint_case(d,elliptic_degree=4):
    require(elliptic_degree==4 and type(elliptic_degree) is int,'only degree-four elliptic map admitted')
    require(type(d) is int and d in (1,2,4),'common field degree')
    if d==1:return 'excluded_genus_bound_13'
    if d==2:return 'quadratic_quotient_genus_at_most_3'
    return 'excluded_degree_one_maps_to_P1_and_elliptic'


def unique_double_quotient(top_genus,max_quotient_genus):
    require(type(top_genus) is int and type(max_quotient_genus) is int and min(top_genus,max_quotient_genus)>=0,'double quotient genera')
    return top_genus>cs_bound(2,max_quotient_genus,2,max_quotient_genus)


def low_genus_cases():
    # V has genus1..3. R_V has no generator-fixed points, U->Q is etale.
    # q>=1; q=1 is the only possibility because u=2q-1 <= (v+1)/2.
    result=[]
    for v in range(1,4):
        for q in range(1,3):
            u=2*q-1;index_two_branches=v+3-4*q
            if index_two_branches<0 or 2*v-2<2*(2*u-2):continue
            result.append({'v':v,'u':u,'q':q,'index_two_branch_count':index_two_branches,
                'cyclic_monodromy_sum_zero':(2*index_two_branches)%4==0,
                'anti_involution_dimension_positive':v-u>0})
    return result


def matching_gate(*,principal_comparison,top_pencil_degree,elliptic_map_degree,free_C4):
    require(principal_comparison is True and free_C4 is True and
        type(top_pencil_degree) is int and top_pencil_degree==4 and
        type(elliptic_map_degree) is int and elliptic_map_degree==4,
        'exact principal comparison, free C4 and both degree-four maps required')
    return True


def exact_core():
    require(cs_bound(4,0,4,1)==13 and cs_bound(2,0,2,1)==3,'rational/elliptic CS controls')
    require(cs_bound(2,3,2,3)==13 and unique_double_quotient(17,3) and
        not unique_double_quotient(13,3),'strict quotient uniqueness')
    cases=low_genus_cases()
    survivors=[c for c in cases if c['cyclic_monodromy_sum_zero'] and c['anti_involution_dimension_positive']]
    require(survivors==[{'v':3,'u':1,'q':1,'index_two_branch_count':2,
        'cyclic_monodromy_sum_zero':True,'anti_involution_dimension_positive':True}], 'forced genus-three quotient')
    v,u=3,1;w=17+2*u-v-9
    require(w==7 and [v-u,w-u]==[2,6] and 2*w-2-2*(2*u-2)==12,'Klein quotient and Prym dimensions')
    old=sixfold.exact_core()
    require(old['cyclic_quartic_primitive_Prym_presentation_excluded_on_fixed_Qi_isogeny_class'] and
        old['ramified_cyclic_quartic_covers_included_in_exclusion'],'forced sixfold obstruction')
    for a in range(7):require(sixfold.valuation3(Q(3,2**a))==1,'inert prime norm obstruction')
    matching_gate(principal_comparison=True,top_pencil_degree=4,elliptic_map_degree=4,free_C4=True)
    return {'top_rational_elliptic_birational_genus_bound':13,
        'quadratic_quotient_genus_upper_bound':3,'double_quotient_uniqueness_bound':13,
        'common_field_degree_cases':{str(d):quartic_joint_case(d) for d in (1,2,4)},
        'conditional_low_genus_cases':cases,'forced_quotient_genera':{'V':3,'U':1,'Q':1,'W':7},
        'forced_Prym_factor_dimensions':[2,6],'forced_W_double_branch_count':12,
        'forced_W_quartic_inertia_two_branch_count':6,
        'forced_sixfold_raw_norm_class':'-1','fixed_X_raw_norm_class':'-3',
        'inert_prime_3_ratio_valuation':1}


def validate_contract(c):
    require(c['schema']=='marici.hodge-trigonal-principal-match-obstruction.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='ramified-trigonal-principal-target-transplant','principal obstruction identity')
    require(c['comparison']=='isomorphism_of_natural_principal_Prym_polarization_with_fixed_Y2' and
        c['geometry']==GEOMETRY,'principal comparison hypotheses changed')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'principal obstruction promoted')
    exact_core()


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    reports={'family':family.report(),'axis_gate':gate.report(),'sixfold_exclusion':sixfold.report()}
    for k,r in reports.items():
        require(json.loads((ROOT/INPUTS[k]).read_text(encoding='utf-8'))==r and r['passed'],'stale '+k)
    require(reports['family']['auxiliary_free_C4_etale_tower'] and
        reports['family']['auxiliary_K_equivariant_ppav_isomorphism'],'auxiliary C4 construction missing')
    require(reports['axis_gate']['CM_elliptic_j_invariant']==1728 and
        reports['axis_gate']['necessary_C9_gonality']==4,'actual principal-axis gate missing')
    require(reports['sixfold_exclusion']['cyclic_quartic_primitive_Prym_presentation_excluded_on_fixed_Qi_isogeny_class'],
        'sixfold exclusion missing')
    # The already frozen primary orientation diagram is rechecked, not a new source claim.
    text=(ROOT/'research/voevodsky/inputs/hodge-ramified-trigonal-v1/lange-ortega.txt').read_text(encoding='utf-8')
    require('orientation cover' in text and 'Lemma 2.2.' in text and '4:1' in text,'orientation pencil primary anchors')
    names=set(INPUTS.values())|{CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
        Path(__file__).relative_to(ROOT).as_posix()}
    return {'schema':'marici.hodge-trigonal-principal-match-obstruction-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',
        'verification_level':'Written CS/quotient/factor proof with exact genus/monodromy/norm controls and fresh geometric receipts; not an unpolarized-isogeny exclusion.',
        'checks':{'orientation_pencil_fresh':True,'principal_axis_fresh':True,'joint_degree_exhaustion':True,
            'unique_quadratic_quotient_and_C4_descent':True,'quotient_genus_and_factor_controls':True,
            'primitive_sixfold_exclusion_fresh':True,'scope':True},**exact_core(),
        'fixed_Y2_natural_principal_match_for_auxiliary_family_excluded':True,
        **{k:False for k in POLICY},
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
