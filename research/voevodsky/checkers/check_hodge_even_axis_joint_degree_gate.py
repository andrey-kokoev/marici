"""Joint-map constraints for a fixed principal Y3 Prym presentation, not all covers."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import check_hodge_even_axis_principal_model as model
import check_hodge_even_axis_coupled_kummer_gate as kummer
import check_hodge_y2_curve_audit as toreli

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-even-axis-joint-degree-gate.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-even-axis-joint-degree-gate-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-even-axis-joint-degree-gate-v1.json'
POLICY=['actual_joint_map_degree_computed','all_degree_two_joint_maps_excluded',
    'all_scalar_sources_excluded_for_Y3','Y2_polarized_exclusions_transferred_to_Y3',
    'all_coupled_Kummer_covers_with_joint_degree4_excluded','all_Y3_Prym_presentations_excluded',
    'all_isogenous_Jacobians_excluded','normalization_defects_counted_as_distinct_nodes',
    'actual_theta_singularity_dimension_computed','actual_curve_or_functions_constructed',
    'fixed_Y3_Prym_membership_constructed','nonzero_target_exceptional_cycle_constructed',
    'Hodge_proved','Hodge_refuted','global_witness_search_completed']
GEOMETRY={'fixed_principal_target':'Y3','elliptic_curve_map_degrees':[8,12],
    'joint_map_degree_divisors':[1,2,4],'actual_elliptic_surface_theta_Euler_characteristic':24,
    'induced_Prym_polarization_kernel_killed_by':2,'remaining_conditional_joint_degrees':[1,2],
    'Y3_hypothetical_Jacobian_elliptic_degree':4,'hyperelliptic_genus_bound':7,
    'degree2_normalization_genus':9,'degree2_ramified_Prym_genus_pair':[9,1],
    'degree2_ramified_Prym_branch_points':16,'degree2_ramified_Prym_induced_theta_type':[1]*7+[2],
    'degree2_ramified_Prym_isogeny_to_Y3_degree':2,'degree2_bielliptic_top_branch_points':32,
    'image_arithmetic_genera_for_joint_degrees_1_2':[97,25],
    'normalization_defect_sums_for_joint_degrees_1_2':[80,16],
    'quotient_surface_image_normalization_genera_for_joint_degrees_1_2':[5,1]}
INPUTS={'model':'research/voevodsky/results/hodge-even-axis-principal-model-v1.json',
    'kummer':'research/voevodsky/results/hodge-even-axis-coupled-kummer-gate-v1.json'}


def require(c,m):
    if not c:raise ValueError(m)


def common_degrees():return [d for d in range(1,9) if 8%d==12%d==0]


def small_prym_isogeny_degree(joint_degree,induced_euler,elliptic_surface_euler=24):
    require(joint_degree in (2,4) and all(type(n) is int and n>0 for n in (induced_euler,elliptic_surface_euler)),
        'small Prym positive Euler data and joint degree2 or4')
    return Q(joint_degree,2)**2*induced_euler/elliptic_surface_euler


def rh_anti_cases(joint_degree):
    require(joint_degree in (2,4),'nonbirational joint degree')
    cases=[]
    for gv in range(2,18):
        ram_cv=32-joint_degree*(2*gv-2)
        if ram_cv<0:continue
        for gw in range(gv):
            anti=gv-gw;ram_vw=2*gv+2-4*gw
            if anti in (2,8) and ram_vw>=0:
                cases.append({'gV':gv,'gW':gw,'anti_dimension':anti,
                    'ramification_C_to_V':ram_cv,'branch_points_V_to_W':ram_vw})
    return cases


def image_arithmetic_genus(joint_degree):
    require(type(joint_degree) is int and joint_degree in common_degrees(),'joint degree divides both maps')
    # Cross correspondence zero is proved from opposite characters in the note.
    return 1+(8//joint_degree)*(12//joint_degree)


def v4_character_dimensions():
    gc,gd,gv,gw=17,9,9,1
    return {'h+sigma+':gw,'h+sigma-':gd-gw,'h-sigma+':gv-gw,'h-sigma-':gc-gd-gv+gw}


def exact_core():
    require(common_degrees()==[1,2,4],'complete common-degree census')
    require(toreli.hyperelliptic_elliptic_genus_bound(4)==7 and 8>7,'new degree-four Y3 Jacobian bound')
    ratios={str(d):[str(small_prym_isogeny_degree(d,e)) for e in (1,2,4)] for d in (2,4)}
    require(ratios=={'2':['1/24','1/12','1/6'],'4':['1/6','1/3','2/3']} and
        all(small_prym_isogeny_degree(d,e).denominator>1 for d in (2,4) for e in (1,2,4)),
        'Euler factor-three obstruction')
    require(small_prym_isogeny_degree(4,1,4)==1 and small_prym_isogeny_degree(4,6)==1,
        'obstruction depends on actual target and two-primary source')
    four=rh_anti_cases(4);two=rh_anti_cases(2)
    require([(r['gV'],r['gW'],r['anti_dimension']) for r in four]==[(2,0,2),(3,1,2),(4,2,2),(5,3,2)],'degree4 RH alternatives')
    big=[r for r in two if r['anti_dimension']==8]
    require(big==[{'gV':8,'gW':0,'anti_dimension':8,'ramification_C_to_V':4,'branch_points_V_to_W':18},
        {'gV':9,'gW':1,'anti_dimension':8,'ramification_C_to_V':0,'branch_points_V_to_W':16}], 'degree2 large Prym alternatives')
    dims=v4_character_dimensions()
    require(list(dims.values())==[1,8,8,0] and sum(dims.values())==17 and
        dims['h+sigma+']+dims['h-sigma-']==1,'bielliptic third quotient character table')
    add=lambda a,b:((a[0]+b[0])%4,(a[1]+b[1])%2)
    rho,h,sigma,beta=(1,0),(2,0),(0,1),(2,1)
    require(add(rho,rho)==h and add(h,sigma)==beta and add(beta,beta)==(0,0) and
        add(rho,beta)==add(beta,rho) and h!=sigma!=beta!=h,'C4 times C2 quotient controls')
    require([image_arithmetic_genus(d) for d in (1,2,4)]==[97,25,7] and
        [image_arithmetic_genus(1)-17,image_arithmetic_genus(2)-9]==[80,16],'adjunction and normalization defects')
    require(2*17-2==32 and 2*5-2==8 and 2*9-2==16,'bielliptic branch counts')
    return {'joint_degrees_before_constraints':[1,2,4],'remaining_conditional_joint_degrees':[1,2],
        'fixed_principal_Y3_Jacobian_presentation_excluded':True,'Y3_Jacobian_genus_bound':7,
        'joint_degree4_excluded_for_fixed_Y3':True,'small_Prym_candidate_isogeny_degrees':ratios,
        'degree4_RH_anti_cases':four,'degree2_eight_dimensional_anti_cases':big,
        'degree2_requires_bielliptic_C17':True,'degree2_requires_scalar_elliptic_isogeny_pullback':True,
        'degree2_V4_holomorphic_character_dimensions':dims,
        'degree2_ramified_Prym_genus_pair':[9,1],'degree2_ramified_Prym_branch_points':16,
        'degree2_ramified_Prym_induced_theta_type':[1]*7+[2],
        'degree2_ramified_Prym_isogeny_to_Y3_degree':2,
        'image_arithmetic_genera_for_joint_degrees_1_2':[97,25],
        'normalization_defect_sums_for_joint_degrees_1_2':[80,16],
        'quotient_surface_image_normalization_genera_for_joint_degrees_1_2':[5,1]}


def validate_contract(c):
    require(c['schema']=='marici.hodge-even-axis-joint-degree-gate.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='even-axis-joint-degree-gate','joint-degree identity')
    require(c['geometry']==GEOMETRY,'joint-degree geometry changed')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),
        'joint-degree gate promoted beyond fixed target')
    exact_core()


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    toreli.validate_sources() # Reuse the primary theorem, NOT the old Y2 exclusion.
    rs={'model':model.report(),'kummer':kummer.report()}
    for k,r in rs.items():require(json.loads((ROOT/INPUTS[k]).read_text(encoding='utf-8'))==r and r['passed'],'stale '+k)
    require(rs['model']['physical_elliptic_surface_polarization_degrees']==[4,6] and
        rs['model']['principal_polarization_indecomposable'] and
        rs['kummer']['base_function_degrees']==[8,12] and rs['kummer']['opposite_Kummer_characters']==[1,3],
        'joint-degree actual target boundary')
    names=set(INPUTS.values())|toreli.source_paths()|{CONTRACT.relative_to(ROOT).as_posix(),
        NOTE.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix(),
        'research/voevodsky/checkers/check_hodge_y2_curve_audit.py'}
    return {'schema':'marici.hodge-even-axis-joint-degree-gate-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',
        'verification_level':'Written fixed-polarization Prym/Euler, Torelli, quotient-group and adjunction proofs; exact controls do not construct a curve, identify a degree or match a Prym.',
        'checks':{'fresh_actual_Y3_and_Kummer_gate':True,'fresh_Torelli_not_Y2_exclusion_transplant':True,
            'two_primary_restricted_Prym_and_Euler_degree_formula':True,'common_degree4_excluded':True,
            'degree2_scalar_branch_classified_not_excluded':True,'image_defects_not_node_counts':True,
            'scope':True},**exact_core(),**{k:False for k in POLICY},
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
