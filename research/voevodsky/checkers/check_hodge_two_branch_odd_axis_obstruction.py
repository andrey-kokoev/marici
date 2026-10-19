"""Two-branch local-character analysis, not a free-orbit shortcut."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import check_hodge_cyclic_prym_odd_axis_obstruction as odd
import check_hodge_indecomposable_principal_model as target
import check_hodge_ramified_trigonal_family as family
import check_hodge_principal_prym_membership as mumford

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-two-branch-odd-axis-obstruction.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-two-branch-odd-axis-obstruction-v1.md'
SOURCES=ROOT/'research/voevodsky/inputs/hodge-two-branch-odd-axis-v1/sources.json'
OUT=ROOT/'research/voevodsky/results/hodge-two-branch-odd-axis-obstruction-v1.json'
POLICY=['free_action_argument_reused_without_fixed_point_analysis','local_characters_omitted',
    'local_residue_profiles_counted_as_actual_maps','all_unpolarized_K_isogenies_excluded',
    'all_nonunit_polarized_isogenies_excluded','all_ramified_Prym_presentations_excluded',
    'all_smooth_etale_double_Prym_presentations_excluded','arbitrary_higher_branch_counts_admitted',
    'auxiliary_cover_existence_refuted','auxiliary_Weil_algebraicity_refuted',
    'degree_four_equivariant_curve_map_constructed','actual_isogeny_source_axes_constructed',
    'target_cycle_constructed','Hodge_proved','Hodge_refuted','global_witness_search_completed']
GEOMETRY={'primitive_Prym_dimension':8,'top_double_cover_branch_count':2,
    'ramified_tower_genera':[16,8,4],'generator_fixed_points':2,'other_short_orbits':0,
    'local_generator_tangent_exponents_mod_four':[1,3],'local_character_compatibility_required':True,
    'principal_Prym_half_of_Jacobian_restriction':True,'target_elliptic_theta_degree':3,'elliptic_curve_map_degree':6}
INPUTS={'odd_axis':'research/voevodsky/results/hodge-cyclic-prym-odd-axis-obstruction-v1.json',
    'target':'research/voevodsky/results/hodge-indecomposable-principal-model-v1.json',
    'family':'research/voevodsky/results/hodge-ramified-trigonal-family-v1.json'}


def require(c,m):
    if not c:raise ValueError(m)


def branch_orbit_cases():
    # F full generator-fixed points; T orbits of two with stabilizer <rho^2>.
    return [{'F':f,'T':t,'quotient_genus':str((Q(30-3*f-2*t,4)+2)/2),
        'integral_quotient_genus':((Q(30-3*f-2*t,4)+2)/2).denominator==1}
        for f,t in ((2,0),(0,1))]


def residue_profiles(degree,target_character=1,source_characters=(1,3),*,enforce_characters=True):
    require(type(degree) is int and degree>0,'positive map degree')
    require(type(target_character) is int and target_character in (1,3) and
        tuple(source_characters) in ((1,3),(3,1)),'primitive opposite tangent characters')
    require(type(enforce_characters) is bool,'character control switch')
    profiles=[]
    for ep,eq in product(range(1,degree+1),repeat=2):
        if enforce_characters and any((a*e-target_character)%4 for a,e in zip(source_characters,(ep,eq))):continue
        for fp,fq in product((0,1),repeat=2):
            used=[ep*int(fp==k)+eq*int(fq==k) for k in (0,1)]
            if all(s<=degree and (degree-s)%4==0 for s in used):
                profiles.append({'ramification_indices':[ep,eq],'fixed_target_assignments':[fp,fq]})
    return profiles


def exact_core():
    require(branch_orbit_cases()==[{'F':2,'T':0,'quotient_genus':'4','integral_quotient_genus':True},
        {'F':0,'T':1,'quotient_genus':'9/2','integral_quotient_genus':False}], 'two-branch orbit exhaustion')
    for chars in ((1,3),(3,1)):
        for b in (1,3):
            require(not residue_profiles(6,b,chars),'degree-six tangent-compatible profile')
            good=residue_profiles(4,b,chars)
            require(good and all(p['fixed_target_assignments'][0]==p['fixed_target_assignments'][1] for p in good),
                'degree-four residue positive control')
    # Failure to impose tangent compatibility really would leave spurious degree-six profiles.
    require(residue_profiles(6,enforce_characters=False),'missing-character countercontrol')
    controls=[]
    for degree in range(1,25):
        p=residue_profiles(degree)
        require(bool(p)==(degree%4==0),'local profile degree divisibility control')
        require(all(s['fixed_target_assignments'][0]==s['fixed_target_assignments'][1] for s in p),'fixed points must share a target')
        controls.append({'degree':degree,'tangent_compatible_residue_profile_exists':bool(p),
            'actual_curve_map_constructed':False})
    return {'ramified_tower_genera':[16,8,4],'branch_orbit_cases':branch_orbit_cases(),
        'generator_fixed_point_count':2,'nonfixed_orbit_length':4,
        'degree_six_tangent_compatible_profile_count':0,'degree_four_residue_control_nonempty':True,
        'omitting_tangent_characters_leaves_spurious_degree_six_profiles':True,
        'local_degree_controls':controls,'conditional_equivariant_elliptic_map_degree_divisor':4,
        'conditional_two_branch_K_isogeny_source_axis_theta_degrees_even':True}


def source_paths():
    data=json.loads(SOURCES.read_text(encoding='utf-8'))
    return {SOURCES.relative_to(ROOT).as_posix()}|{f['path'] for f in data['files']}


def validate_sources():
    mumford.validate_sources()
    d=json.loads(SOURCES.read_text(encoding='utf-8'))
    require(d['schema']=='marici.hodge-two-branch-normalization-source.v1' and
        d['pdf_page']==9 and d['printed_page']==333 and
        d['verified_formula']=='restricted_Jacobian_polarization_equals_twice_principal_Prym_for_zero_or_two_branch_points',
        'two-branch primary normalization identity')
    require({f['path'] for f in d['files']}=={
        'research/voevodsky/inputs/hodge-principal-prym-membership-v1/mumford-prym-I.pdf',
        'research/voevodsky/inputs/hodge-two-branch-odd-axis-v1/mumford-p9.png',
        'research/voevodsky/inputs/hodge-two-branch-odd-axis-v1/mumford-p9.txt'},'two-branch primary coverage')
    for f in d['files']:require(sha256((ROOT/f['path']).read_bytes()).hexdigest()==f['sha256'],'two-branch primary drift')
    text=(ROOT/'research/voevodsky/inputs/hodge-two-branch-odd-axis-v1/mumford-p9.txt').read_text(encoding='utf-8')
    require('Corollary 2.' in text and 'has only two branch points' in text,'two-branch primary text anchor')


def validate_contract(c):
    require(c['schema']=='marici.hodge-two-branch-odd-axis-obstruction.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='y2-two-branch-cyclic-quartic-transplant','two-branch identity')
    require(c['comparison']=='natural_principal_two_branch_Prym_isomorphism_with_fixed_Y2' and
        c['geometry']==GEOMETRY,'two-branch comparison changed')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'two-branch exclusion promoted')
    validate_sources();exact_core()


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    rs={'odd_axis':odd.report(),'target':target.report(),'family':family.report()}
    for k,r in rs.items():
        require(json.loads((ROOT/INPUTS[k]).read_text(encoding='utf-8'))==r and r['passed'],'stale '+k)
    require(rs['odd_axis']['physical_CM_product_polarization_degrees']==[2,3] and
        rs['odd_axis']['fixed_Y2_smooth_etale_cyclic_quartic_principal_presentations_excluded'], 'actual axis proof missing')
    require(rs['family']['auxiliary_smooth_connected_cover_existence'] and
        rs['family']['ramified_tower_genera']==[16,8,4],'actual auxiliary family lost')
    names=source_paths()|set(INPUTS.values())|{CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
        Path(__file__).relative_to(ROOT).as_posix()}
    return {'schema':'marici.hodge-two-branch-odd-axis-obstruction-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',
        'verification_level':'Written fixed-point/tangent/fibre proof, fresh rendered Mumford normalization and exact local residue controls; no arbitrary-isogeny exclusion.',
        'checks':{'two_branch_normalization_primary':True,'target_axis_preservation_fresh':True,
            'generator_orbit_exhaustion':True,'local_tangent_congruences':True,'fixed_fibre_residue_exhaustion':True,
            'auxiliary_existence_retained':True,'scope':True},**exact_core(),
        'fixed_Y2_natural_principal_two_branch_cyclic_quartic_presentations_excluded':True,
        'fixed_Y2_standard_zero_or_two_branch_principal_cyclic_quartic_presentations_excluded':True,
        **{k:False for k in POLICY},
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','local_degree_controls')},indent=2))
