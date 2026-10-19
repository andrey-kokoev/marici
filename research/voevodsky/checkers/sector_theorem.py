"""Shared theorem routing and fail-closed proof-bundle admission, not a prover."""
from hashlib import sha256
import json
from check_retained_reaggregation_net import require, path_at, CONTRACT

SPEC='research/voevodsky/contracts/retained-reaggregation-sector-theorem.v1.json'
MODULE='research/voevodsky/checkers/sector_theorem.py'
SOURCE_K='research/voevodsky/contracts/retained-reaggregation-source-k.v1.json'
ID='shared-sector-decomposition-and-exact-dynamics'
ASSUMPTIONS={'frozen_source_K_identified','K_self_adjoint','K_commutes_with_c_and_Pi','same_frozen_parameters_and_preparation','separate_vacuum_and_neutral_record'}
CONCLUSIONS={
    'common-resource-accounting':{'both_full_generators_derived','common_empty_reference_derived','all_complementary_records_retained','finite_self_adjoint_joint_reversibility'},
    'typed-operation-classification':{'carrier_number_and_charge_operators_identified','sector_commutators_computed','variable_phase_contract_stated','neutral_record_not_carrier_annihilation'},
    'same-input-discriminator':{'exact_sector_propagators','same_initial_state_both_rules','frozen_time_readout_difference','exact_or_certified_readout_bounds','joint_energy_and_retained_post_readout_accounted'},
}

def read(root,path):return json.loads(path_at(root,path).read_text(encoding='utf-8'))
def digest(root,path):return sha256(path_at(root,path).read_bytes()).hexdigest()

def validate_source_k(root):
    selection=read(root,SOURCE_K)
    expected={'schema':'marici.voevodsky.reaggregation-source-k.v1','source_contract':CONTRACT,
        'selection':'optional_cycle_defect','single_operator':'H_native=L+2I-T-Tdagger',
        'pair_operator':'K_pair=H_native tensor I10+I10 tensor conjugate(H_native)',
        'matter_operator':'K=K_pair direct_sum 0_vacuum',
        'single_mismatch':'L=(4-sqrt(6))Q_low+(4+2sqrt(6)/3)(I10-Q_low)',
        'low_projector':'Q_low=W0 W0dagger+W1 W1dagger',
        'transport':'T=transport_matrix(source spin_lift); use the displayed lift for both doublet options',
        'native_cases':[[1,0],[1,1],[-1,0],[-1,1]],'native_pair_dimension':100,'matter_dimension':101,
        'vacuum_energy':'0','additional_orbital_terms':[],'additional_sector_mixing_terms':[],
        'scale':'relative_native_orbital_unit=1; no extra pi/4 multiplier',
        'empty_reference':'K vacuum energy 0 plus record-ready energy g=1/2 before the common subtraction; zero after subtraction'}
    require(all(selection.get(k)==v for k,v in expected.items()),'source K selection changed or incomplete')
    require(selection.get('physical_admission') is False and selection.get('selection_basis') and selection.get('scope_policy'),'unscoped source K selection')
    pins=selection.get('source_hashes',{})
    require({CONTRACT,'research/voevodsky/native-spinor-pair-adapter.md','research/voevodsky/results/native_spinor_pair_adapter.json'}<=set(pins),'missing source K provenance')
    for path,h in pins.items():require(digest(root,path)==h,'stale source K dependency: '+path)
    return selection

def validate_spec(root,contract):
    validate_source_k(root)
    spec=read(root,SPEC);nodes={n['id']:n for n in contract['conjectures']}
    require(spec.get('schema')=='marici.voevodsky.sector-theorem.v1' and spec.get('source_contract')==CONTRACT and spec.get('id')==ID,'wrong sector theorem spec')
    require(set(spec.get('depends_on',[]))=={'freeze-common-interface','native-signed-record-rule','rival-defect-record-rule'} and set(spec['depends_on'])<=set(nodes),'wrong sector theorem prerequisites')
    require(set(spec.get('required_assumptions',[]))==ASSUMPTIONS,'missing sector theorem assumptions')
    require({k:set(v) for k,v in spec.get('conclusions',{}).items()}==CONCLUSIONS and set(CONCLUSIONS)<=set(nodes),'wrong sector conclusion mapping')
    require(spec.get('entry_action')=='prove/common-resource-accounting' and spec.get('indirect_consumer')==contract['objective']['target'],'wrong sector theorem routing')
    require(set(spec.get('outcome_ports',{}))=={'++','+-','-+','--'} and all(spec['outcome_ports'].values()),'incomplete sector theorem ports')
    require(spec.get('statement') and spec.get('planning_policy') and spec.get('admission_policy') and spec.get('physical_admission') is False,'unscoped sector theorem')
    return spec

def validate_bundle(root,reference,claim,receipt):
    """A generic reviewed conclusion receipt may cite one shared proof bundle.

    The outer receipt remains nonce-bound and reviewer-bound. The shared bundle
    has no attempt nonce and cannot by itself finish another action.
    """
    require(claim in CONCLUSIONS and receipt.get('outcome')=='++','sector proof bundle cannot refute or promote an unrelated claim')
    require(isinstance(reference,dict) and reference.get('path') and reference.get('sha256'),'missing sector bundle reference')
    path=reference['path'];require(digest(root,path)==reference['sha256'],'stale sector bundle')
    bundle=read(root,path)
    require(bundle.get('schema')=='marici.voevodsky.sector-theorem-proof.v1' and bundle.get('theorem_id')==ID and bundle.get('status')=='admitted','wrong sector proof bundle')
    require(bundle.get('fresh_execution') is True and bundle.get('physical_admission') is False and bundle.get('kernel_verified_analytic_theorem') is False,'unsupported sector verification level')
    require(isinstance(bundle.get('reviewer'),str) and bundle['reviewer'].strip() and bundle.get('proof_kind'),'missing sector theorem review')
    assumptions=bundle.get('assumptions',{})
    require(set(assumptions)==ASSUMPTIONS and all(v is True for v in assumptions.values()),'sector assumptions must be established, not assumed')
    conclusions=bundle.get('conclusions',{})
    require(set(conclusions)==set(CONCLUSIONS),'missing sector theorem conclusion')
    for node,required in CONCLUSIONS.items():
        checks=conclusions[node]
        require(isinstance(checks,dict) and set(checks)==required and all(v is True for v in checks.values()),'incomplete sector theorem conclusion: '+node)
    pins=bundle.get('source_hashes',{});verifier=bundle.get('verifier',{})
    validate_source_k(root)
    require({SPEC,CONTRACT,MODULE,SOURCE_K}<=set(pins) and verifier.get('path') in pins and verifier.get('sha256')==pins[verifier['path']],'missing sector verifier/context pins')
    for source,h in pins.items():require(digest(root,source)==h,'stale sector theorem dependency: '+source)
    outer=receipt.get('source_hashes',{})
    require(outer.get(path)==reference['sha256'] and outer.get(SPEC)==digest(root,SPEC) and outer.get(SOURCE_K)==digest(root,SOURCE_K),'conclusion receipt must pin shared bundle, spec and source K')
    require(set(receipt.get('required_checks',[]))==CONCLUSIONS[claim] and receipt.get('checks')==conclusions[claim],'conclusion receipt mismatches shared proof')
    return bundle

def diagnose(root,contract,state):
    spec=validate_spec(root,contract);outcomes=state['outcomes']
    missing=[n for n in spec['depends_on'] if outcomes.get(n)!='++']
    references={}
    for attempt in state['attempts'].values():
        if attempt.get('outcome')=='++' and attempt['claim'] in CONCLUSIONS:
            receipt=read(root,attempt['receipt']);reference=receipt.get('sector_theorem_evidence')
            if reference:
                validate_bundle(root,reference,attempt['claim'],receipt)
                references[reference['sha256']]=reference
    return {'id':ID,'statement':spec['statement'],'outcome':'++' if references else None,
        'status':'proved_by_reviewed_shared_bundle' if references else 'blocked_on_prerequisites' if missing else 'ready_for_proof',
        'missing_prerequisites':missing,'entry_action':spec['entry_action'],
        'source_k':{'path':SOURCE_K,'sha256':digest(root,SOURCE_K),'selection':'optional_cycle_defect','vacuum_energy':'0','status':'explicit_constructor_choice_not_proof'},
        'required_assumptions':spec['required_assumptions'],'conclusion_checks':spec['conclusions'],
        'conclusion_outcomes':{n:outcomes.get(n) for n in CONCLUSIONS},
        'indirect_consumer':spec['indirect_consumer'],'evidence':list(references.values()),
        'independent_action':False,'automatic_promotion':False,'physical_admission':False,
        'planning_policy':spec['planning_policy']}
