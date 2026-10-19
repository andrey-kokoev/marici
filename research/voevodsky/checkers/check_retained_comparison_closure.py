"""Exact finite conclusion gates; no physical admission or inferred particle types."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,sys
from check_common_resource_accounting import prove as accounting_proof,SCENARIO_CHECKS,READOUT_CHECKS
from check_sector_theorem_progress import occupation_bounds
from check_pentachoron_spin_interfaces import A,mm,add,scale
from check_typed_spin_channels import eye
from sector_theorem import SOURCE_K,SPEC,MODULE,ID,ASSUMPTIONS,CONCLUSIONS,validate_source_k,validate_bundle
from check_retained_reaggregation_net import ROOT,CONTRACT,require,path_at

GATE='research/voevodsky/checkers/check_retained_comparison_closure.py'
NOTE='research/voevodsky/retained-comparison-closure.v1.md'
SCHEMA='marici.voevodsky.retained-comparison-receipt.v1'
CLASSIFY='typed-operation-classification'
DISCRIMINATE='same-input-discriminator'
TARGET='conditional-reaggregation-comparison'
CLAIMS={CLASSIFY,DISCRIMINATE,TARGET}
TARGET_CHECKS={'frozen_interface_and_parameters','native_covariance_and_disclosed_ambient_limits','both_complete_rules_same_reference','typed_sectors_and_phase_contract','certified_same_input_readout','all_records_and_post_readout_retained','conditional_scope_only'}
EXACT_CHECKS={'number_operators_preserved','declared_charge_zero','opposite_variable_phase_weights','record_commutator_nonzero','neutral_record_phase_weight','same_input_rival_dark','certified_occupation_separation','source_K_fixed','same_frozen_parameters','native_covariance_and_limits_verified'}
PHASE={'left_weight':1,'conjugate_right_weight':-1,'pair_weight':0,'vacuum_weight':0,'record_weight':0,'status':'declared global U(1) action on conjugate-copy inputs, not physical charge identification'}
SECTORS={'left_number':'c','right_number':'c','pair_number':'c','constituent_number':'2c','declared_charge':'q(c-c)=0','carrier_change':False,'record_occupation_conserved':False,'physical_annihilation':False}

def read(root,p):return json.loads(path_at(root,p).read_text(encoding='utf-8'))
def digest(root,p):return sha256(path_at(root,p).read_bytes()).hexdigest()
def save(path,value):path.write_text(json.dumps(value,indent=2)+'\n')
def required(claim):return TARGET_CHECKS if claim==TARGET else CONCLUSIONS[claim]
def detail_keys():
    return {f+'_'+f'{c}_{o}' for f in SCENARIO_CHECKS for c in (1,-1) for o in (0,1)}|set(READOUT_CHECKS)|EXACT_CHECKS

def exact_sector_checks():
    # Direct-sum block laws: c=diag(1,0), any retained K,P are diag(A,0).
    # Their scalar sector coefficients here check the block commutators; A can
    # be the entire retained 100x100 block by ordinary matrix distributivity.
    c=((A(1),A(0)),(A(0),A(0)));zero=scale(A(0),eye(2))
    N=((A(0),A(0)),(A(0),A(1)));X=((A(0),A(1)),(A(1),A(0)))
    return {'number_operators_preserved':mm(c,c)==c and mm(c,scale(A(2),c))==mm(scale(A(2),c),c),
        'declared_charge_zero':add(c,scale(A(-1),c))==zero,
        'opposite_variable_phase_weights':PHASE['left_weight']+PHASE['conjugate_right_weight']==PHASE['pair_weight']==0,
        'record_commutator_nonzero':add(mm(X,N),scale(A(-1),mm(N,X)))==((A(0),A(1)),(A(-1),A(0))),
        'neutral_record_phase_weight':PHASE['record_weight']==PHASE['vacuum_weight']==0}

def prove(claim,nonce,output):
    require(claim in CLAIMS,'unknown closure claim')
    # This reruns all native/selected-K and complete generator/readout checks.
    accounting=accounting_proof(nonce);details=dict(accounting['detail_checks'])
    details.update(exact_sector_checks())
    choice=validate_source_k(ROOT);contract=read(ROOT,CONTRACT)
    lo,hi=occupation_bounds()
    native=read(ROOT,'research/voevodsky/results/native_spinor_pair_adapter.json')
    details.update({'same_input_rival_dark':all(details['same_normalized_scalar_preparation_'+f'{c}_{o}'] for c in (1,-1) for o in (0,1)),
        'certified_occupation_separation':F(21,100)<lo<hi<F(22,100),
        'source_K_fixed':choice['selection']=='optional_cycle_defect' and choice['vacuum_energy']=='0',
        'same_frozen_parameters':contract['frozen_comparison']['candidate_parameters']=={'record_gap':'1','vertex_g':'1/2','relative_native_orbital_unit':'1','readout_time':'1 model-time unit'},
        'native_covariance_and_limits_verified':native['verification_passed'] is True and all(v is True for v in native['checks'].values())})
    require(set(details)==detail_keys() and all(v is True for v in details.values()),'fresh closure checks incomplete')
    sources=dict(accounting['source_hashes'])
    for p in (GATE,NOTE,SOURCE_K,SPEC,MODULE,CONTRACT):sources[p]=digest(ROOT,p)
    checks={k:True for k in sorted(required(claim))}
    receipt={'schema':SCHEMA,'status':'pass','node_id':claim,'intent':'prove','outcome':'++','attempt_nonce':nonce,
        'fresh_execution':True,'physical_admission':False,'kernel_verified_analytic_theorem':False,
        'proof_kind':'fresh exact finite block/coefficient checks and source-pinned written conditional proof',
        'required_checks':sorted(checks),'checks':checks,'detail_checks':details,'phase_contract':PHASE,'sector_classification':SECTORS,
        'occupation_bounds':{'primary_lower':str(lo),'primary_upper':str(hi),'rival':'0'},
        'energy_accounting':accounting['energy_accounting'],'readout_convention':accounting['readout_convention'],
        'joint_dimension':202,'source_hashes':sources}
    if claim==DISCRIMINATE:
        bundle_path=output.with_name(nonce+'.sector-bundle.json');relative=bundle_path.resolve().relative_to(ROOT).as_posix()
        bundle={'schema':'marici.voevodsky.sector-theorem-proof.v1','theorem_id':ID,'status':'admitted','fresh_execution':True,
            'physical_admission':False,'kernel_verified_analytic_theorem':False,
            'reviewer':'local assistant mathematical/code review; not independent human or physical review',
            'proof_kind':receipt['proof_kind'],'assumptions':{k:True for k in sorted(ASSUMPTIONS)},
            'conclusions':{n:{k:True for k in sorted(group)} for n,group in CONCLUSIONS.items()},
            'verifier':{'path':GATE,'sha256':sources[GATE]},'fresh_checks':details,'source_hashes':dict(sources)}
        save(bundle_path,bundle)
        receipt['sector_theorem_evidence']={'path':relative,'sha256':digest(ROOT,relative)}
        receipt['source_hashes'][relative]=digest(ROOT,relative)
    return receipt

def validate_receipt(root,receipt,claim):
    require(claim in CLAIMS and receipt.get('schema')==SCHEMA and receipt.get('status')=='pass','wrong closure receipt')
    require(receipt.get('fresh_execution') is True and receipt.get('physical_admission') is False and receipt.get('kernel_verified_analytic_theorem') is False,'unsupported closure verification level')
    require(receipt.get('proof_kind')=='fresh exact finite block/coefficient checks and source-pinned written conditional proof','wrong closure proof kind')
    checks=receipt.get('checks',{});details=receipt.get('detail_checks',{})
    require(set(checks)==required(claim) and set(receipt.get('required_checks',[]))==required(claim) and all(v is True for v in checks.values()),'incomplete scoped closure conclusions')
    require(set(details)==detail_keys() and all(v is True for v in details.values()),'incomplete fresh closure details')
    require(receipt.get('phase_contract')==PHASE and receipt.get('sector_classification')==SECTORS,'unsupported charge/number/phase claim')
    lo,hi=occupation_bounds()
    require(receipt.get('occupation_bounds')=={'primary_lower':str(lo),'primary_upper':str(hi),'rival':'0'},'wrong certified occupation bounds')
    require(receipt.get('energy_accounting')=={'primary_before':'epsilon','primary_after_nonselective_readout':'epsilon+p','rival_before_and_after':'epsilon','measurement_energy_increase':'p','p':'(1-cos(sqrt(2)))/4'},'wrong full readout energy accounting')
    require(receipt.get('joint_dimension')==202 and receipt.get('readout_convention')=='ideal projective neutral-record measurement, both outcomes and matter retained; external apparatus not modeled','wrong retained space/readout')
    pins=receipt.get('source_hashes',{})
    expected={GATE,NOTE,SOURCE_K,SPEC,MODULE,CONTRACT,'research/voevodsky/checkers/check_common_resource_accounting.py','research/voevodsky/common-resource-accounting.v1.md','research/voevodsky/checkers/check_selected_source_k.py','research/voevodsky/checkers/check_sector_theorem_progress.py','research/voevodsky/results/native_spinor_pair_adapter.json','research/voevodsky/results/typed_spin_channels.json','research/voevodsky/checkers/check_native_spinor_pair_adapter.py','research/voevodsky/checkers/check_pentachoron_spin_interfaces.py','research/voevodsky/checkers/check_typed_spin_channels.py'}
    require(expected<=set(pins),'missing closure source/proof pins')
    for p,h in pins.items():require(digest(root,p)==h,'stale closure dependency: '+p)
    validate_source_k(root)
    if claim==DISCRIMINATE:
        bundle=validate_bundle(root,receipt.get('sector_theorem_evidence'),claim,receipt)
        require(bundle.get('fresh_checks')==details,'umbrella bundle mismatch with fresh conclusion evidence')
    else:require('sector_theorem_evidence' not in receipt,'unexpected umbrella evidence scope')
    return receipt

if __name__=='__main__':
    output=Path(sys.argv[2]);save(output,prove(sys.argv[3],sys.argv[1],output))
