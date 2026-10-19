"""Executable budgeted planner, append-only attempt ledger and scoped admission.
Planning likelihoods are subjective; only validated receipts resolve propositions.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
from datetime import datetime,timezone
from contextlib import contextmanager
import argparse,copy,json,math,os,subprocess,sys,uuid
from check_retained_reaggregation_net import validate,require,NetError,path_at,CONTRACT,ROOT
sys.path.insert(0,str(ROOT/'research/conjecture_net'))
from bayesian_outcome_planner import Planner,likelihood,action_metrics,marginal,condition
from check_retained_comparison_closure import GATE as CLOSURE_GATE, CLAIMS as CLOSURE_CLAIMS, SCHEMA as CLOSURE_SCHEMA, validate_receipt as validate_closure_receipt
from sector_theorem import SOURCE_K, CONCLUSIONS as SECTOR_CONCLUSIONS, SPEC as SECTOR_THEOREM, MODULE as SECTOR_MODULE, validate_spec as validate_sector_spec, validate_bundle as validate_sector_bundle, diagnose as diagnose_sector_theorem

MODEL='research/voevodsky/contracts/retained-reaggregation-planning.v1.json'
ROUTES='research/voevodsky/contracts/retained-reaggregation-four-port-routing.v1.json'
INVARIANTS='research/voevodsky/contracts/retained-reaggregation-coherence-invariants.v1.json'
PHYSICAL='research/voevodsky/contracts/retained-reaggregation-physical-admission-gate.v1.json'
REFINEMENTS='research/voevodsky/contracts/retained-reaggregation-rule-refinements.v1.json'
LEDGER='research/voevodsky/contracts/retained-reaggregation-attempts.v1.json'
OUT='research/voevodsky/results/retained_reaggregation_planning.json'
NATIVE='research/voevodsky/results/native_spinor_pair_adapter.json'
MEDIATOR='research/voevodsky/results/finite_record_mediator_constructor.json'
NATIVE_GATE='research/voevodsky/checkers/check_native_signed_record_rule.py'
RIVAL_GATE='research/voevodsky/checkers/check_rival_defect_record_rule.py'
ACCOUNTING_GATE='research/voevodsky/checkers/check_common_resource_accounting.py'
GATE='research/voevodsky/checkers/check_reaggregation_common_interface.py'
ENGINE='research/conjecture_net/bayesian_outcome_planner.py'

def read(root,p):return json.loads(path_at(root,p).read_text(encoding='utf-8'))
def digest(root,p):return sha256(path_at(root,p).read_bytes()).hexdigest()
def object_hash(value):return sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def write_atomic(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_name(path.name+'.'+uuid.uuid4().hex+'.tmp')
    tmp.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8');os.replace(tmp,path)
@contextmanager
def locked(root):
    lock=root/(LEDGER+'.lock');lock.parent.mkdir(parents=True,exist_ok=True)
    try:fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    except FileExistsError:raise NetError('ledger locked; do not start a concurrent attempt')
    try:yield
    finally:os.close(fd);lock.unlink()

def model_data(root,contract):
    m=read(root,MODEL)
    require(m.get('schema')=='marici.voevodsky.reaggregation-planning.v1' and m.get('estimate_status')=='subjective_uncalibrated_planning_only' and m.get('empirically_calibrated') is False,'wrong/unlabelled model')
    target=contract['objective']['target'];physical=contract['objective']['physical_followup']
    require(m['target']==target,'model target mismatch')
    require(isinstance(m['budget_effort_units'],int) and m['budget_effort_units']>0,'bad budget')
    nodes={n['id']:n for n in contract['conjectures'] if n['id']!=physical}
    require(set(m['estimates'])==set(nodes),'estimates must cover conditional route exactly')
    validate_sector_spec(root,contract)
    routing=read(root,ROUTES)
    refinements=read(root,REFINEMENTS)
    require(refinements.get('schema')=='marici.voevodsky.rule-refinements.v1' and refinements.get('source_contract')==CONTRACT,'wrong rule-refinement contract')
    expected_refinements={'primary-control-transport':'native-signed-record-rule','primary-complete-generator':'native-signed-record-rule','rival-vacuum-safe-defect-control':'rival-defect-record-rule','rival-identical-input-resource-accounting':'rival-defect-record-rule'}
    require({r.get('id'):r.get('parent') for r in refinements.get('refinements',[])}==expected_refinements,'incomplete rule refinement claims')
    require(all(r.get('statement') and (r.get('required_checks') or r.get('required_check_families')) for r in refinements['refinements']),'refinement lacks scoped acceptance checks')
    physical_gate=read(root,PHYSICAL)
    require(physical_gate.get('schema')=='marici.voevodsky.physical-admission-gate.v1' and physical_gate.get('source_contract')==CONTRACT and physical_gate.get('target_node')==physical,'wrong physical admission gate')
    required_physical={'identified-native-system','independent-scale-and-coupling-calibration','physical-preparation-and-record-readout','preregistered-discriminating-predictions','independent-review-and-replication'}
    require({e.get('id') for e in physical_gate.get('required_evidence_classes',[])}==required_physical,'incomplete physical evidence classes')
    require(physical_gate.get('not_in_planning_portfolio') is True and physical_gate.get('admission_policy',{}).get('no_automatic_promotion') is True,'physical gate must remain outside conditional planner')
    require(physical_gate.get('admission_policy',{}).get('required_conditional_outcome')=='++' and set(physical_gate.get('admission_policy',{}).get('outcome_ports',{}))=={'++','+-','-+','--'},'physical admission port policy incomplete')
    invariants=read(root,INVARIANTS)
    require(invariants.get('schema')=='marici.voevodsky.coherence-invariants.v1' and invariants.get('source_contract')==CONTRACT,'wrong coherence-invariant contract')
    invariant_nodes={n['id'] for n in contract['conjectures']}
    records=invariants.get('invariants',[])
    require(len(records)>=1 and len({r.get('id') for r in records})==len(records),'missing/duplicate coherence invariant')
    require(all(r.get('owner') in invariant_nodes and r.get('requirement') and r.get('contract_fields') for r in records),'unscoped coherence invariant')
    def contract_field(path):
        value=contract
        for part in path.split('.'):
            value=next((n for n in value if n.get('id')==part),None) if isinstance(value,list) else value.get(part) if isinstance(value,dict) else None
            require(value is not None,'unresolved invariant contract field: '+path)
        return value
    for record in records:
        for field in record['contract_fields']:contract_field(field)
    obligations=invariants.get('shared_obligations',[])
    obligation_ids={o.get('id') for o in obligations}
    require(obligations and len(obligation_ids)==len(obligations),'shared obligations must have unique canonical IDs')
    for obligation in obligations:
        require(obligation.get('owner') in invariant_nodes and obligation.get('consumers') and obligation.get('one_evidence_identity') is True,'malformed shared obligation')
        require(all(c in invariant_nodes for c in obligation['consumers']),'unknown shared-obligation consumer')
    require(invariants.get('contradiction_policy',{}).get('status')=='no_hard_scientific_contradictions_admitted','unknown contradiction policy')
    frozen=contract['frozen_comparison']
    require('100-state pair' in frozen['carrier'] and 'separately retained empty sector' in frozen['carrier'],'carrier/vacuum coherence mismatch')
    require('zero on vacuum' in frozen['primary_control'] and 'zero on vacuum' in frozen['rival_control'] and 'NOT unrestricted I-Pi' in frozen['rival_control'],'vacuum-control coherence mismatch')
    require(frozen['preparation'] and frozen['records'] and len(frozen['candidate_parameters'])>=3,'common-input specification incomplete')
    require({'neutral occupation projector','complete joint Hamiltonian energy/readout with common empty reference'}<=set(frozen['observables']),'common observable/reference incomplete')
    require({r['owner'] for r in records}>={'freeze-common-interface','common-resource-accounting','same-input-discriminator','physical-admission-and-selection'},'missing critical coherence owner')
    require(routing.get('schema')=='marici.voevodsky.four-port-routing.v1' and routing.get('source_contract_sha256')==digest(root,CONTRACT),'stale/malformed four-port routing contract')
    require(set(routing.get('routes',{}))==set(nodes)-{physical},'every conditional node needs explicit four-port routes')
    for claim,ports in routing['routes'].items():require(set(ports)=={'++','+-','-+','--'},'incomplete four-port routing for '+claim)
    alternatives=routing.get('alternative_routes',[])
    require(routing.get('alternative_route_policy',{}).get('status') in ('no_reviewed_alternative_routes_registered','reviewed_alternatives_available'),'missing alternative-route policy')
    alt_ids=set()
    for alt in alternatives:
        require(alt.get('id') and alt['id'] not in alt_ids and alt.get('target')==target,'malformed alternative route')
        alt_ids.add(alt['id']);deps=alt.get('proof_dependencies',[])
        require(deps and len(deps)==len(set(deps)) and set(deps)<=set(nodes),'invalid alternative proof route')
        require(alt.get('review_status')=='reviewed' and alt.get('evidence_path') and alt.get('evidence_sha256'),'unreviewed alternative route cannot be active')
        require(digest(root,alt['evidence_path'])==alt['evidence_sha256'],'stale alternative-route review evidence')
    require(bool(alternatives)==(routing['alternative_route_policy']['status']=='reviewed_alternatives_available'),'route registry/status mismatch')
    actions=[]
    for claim,e in m['estimates'].items():
        for intent in ('prove','reject'):
            cost=e[intent+'_cost'];low,high=e[intent+'_cost_range']
            sensitivity=e[intent+'_success_given_'+('true' if intent=='prove' else 'false')]
            require(isinstance(cost,int) and 0<low<=cost<=high and math.isfinite(sensitivity) and 0<=sensitivity<=1,'bad action estimate')
            if intent=='reject' and (not e['rejection_available'] or claim not in routing['routes']):continue
            actions.append({'id':intent+'/'+claim,'claim':claim,'intent':intent,'cost':cost,'sensitivity':sensitivity,'requires':nodes[claim]['depends_on'] if intent=='prove' else []})
    priority=m.get('priority_policy',{})
    require(priority.get('status')=='diagnostic_only_not_scientific_evidence' and priority.get('formula')=='target_information_bits_per_effort + coherence_weight * normalized_number_of_transitively_unlocked_conjectures','missing/unknown priority diagnostics policy')
    require(priority.get('coherence_weights') and all(isinstance(w,(int,float)) and w>=0 for w in priority['coherence_weights']),'invalid coherence weights')
    joint=m['joint_model'];base=joint['base_claim_probabilities']
    require(set(base)==set(nodes)-{target},'wrong joint base claims')
    probabilities=list(base.values())+[joint['target_given_all_components_true'],joint['target_given_otherwise']]
    require(all(math.isfinite(p) and 0<p<1 for p in probabilities),'invalid joint probabilities')
    require(joint.get('constraint_status')=='reviewed_constraint_registry_no_hard_constraints_admitted_yet','unreviewed joint constraint semantics')
    constraints=joint.get('hard_constraints',[])
    for constraint in constraints:
        require(constraint.get('kind')=='mutually_exclusive' and len(constraint.get('claims',[]))>=2,'unsupported/malformed hard constraint')
        require(set(constraint['claims'])<=set(base) | {target},'constraint names unknown proposition')
        require(constraint.get('review_status')=='admitted' and constraint.get('evidence_path') and constraint.get('evidence_sha256'),'constraint lacks reviewed pinned evidence')
        require(digest(root,constraint['evidence_path'])==constraint['evidence_sha256'],'stale constraint evidence')
    worlds=[];claims=list(base)
    for truth in product((False,True),repeat=len(claims)):
        t=dict(zip(claims,truth));p=math.prod(base[c] if v else 1-base[c] for c,v in t.items())
        tp=joint['target_given_all_components_true' if all(truth) else 'target_given_otherwise']
        for target_true in (False,True):
            truth=dict(t,**{target:target_true})
            if any(sum(bool(truth[c]) for c in constraint['claims'])>1 for constraint in constraints):continue
            worlds.append({'id':str(len(worlds)),'truth':truth,'probability':p*(tp if target_true else 1-tp)})
    mass=sum(w['probability'] for w in worlds);require(mass>0,'constraints exclude all worlds')
    raw_world_mass=mass
    worlds=[dict(w,probability=w['probability']/mass) for w in worlds]
    require(abs(sum(w['probability'] for w in worlds)-1)<1e-12,'worlds not normalized')
    require(any(w['truth'][target] and not all(w['truth'][c] for c in claims) for w in worlds),'alternative-route truth erased')
    return m,actions,worlds,{'hard_constraint_count':len(constraints),'raw_world_mass':raw_world_mass}

def new_ledger(root,model):
    return {'schema':'marici.voevodsky.reaggregation-attempt-ledger.v1','contract_sha256':digest(root,CONTRACT),'model_sha256':digest(root,MODEL),'engine_sha256':digest(root,ENGINE),'refinements_sha256':digest(root,REFINEMENTS),'sector_theorem_sha256':digest(root,SECTOR_THEOREM),'source_k_sha256':digest(root,SOURCE_K),'initial_budget':model['budget_effort_units'],'events':[]}

def append_event(ledger,event):
    event=dict(event,index=len(ledger['events']),previous=ledger['events'][-1]['hash'] if ledger['events'] else None)
    event['hash']=object_hash(event);ledger['events'].append(event)

def admitted_receipt(root,event,attempt):
    receipt=read(root,event['receipt']);require(digest(root,event['receipt'])==event['receipt_sha256'],'stale attempt receipt')
    require(receipt.get('node_id')==attempt['claim'] and receipt.get('attempt_nonce')==attempt['nonce'] and receipt.get('intent')==attempt['intent'] and receipt.get('outcome')==event['outcome'],'receipt scope/replay mismatch')
    outcome=event['outcome']
    if outcome in ('+-','--'):
        require(receipt.get('status')=='incomplete' and receipt.get('scientific_outcome') is None,'failed attempt must not resolve truth')
        require(isinstance(receipt.get('reason'),str) and receipt['reason'],'missing failure record')
        return receipt
    if attempt['action']=='prove/freeze-common-interface' and outcome=='++':
        require(receipt.get('schema')=='marici.voevodsky.reaggregation-gate-receipt.v1' and receipt.get('status')=='pass' and receipt.get('fresh_execution') is True and receipt.get('physical_admission') is False,'wrong proof receipt')
        expected={'scalar_preparation_normalized','vacuum_and_record_contract'}
    elif attempt['action']=='prove/native-signed-record-rule' and outcome=='++':
        require(receipt.get('schema')=='marici.voevodsky.native-signed-record-receipt.v1' and receipt.get('status')=='pass' and receipt.get('fresh_execution') is True and receipt.get('physical_admission') is False,'wrong native signed-record receipt')
        expected=set();native=json.loads(path_at(root,NATIVE).read_text(encoding='utf-8'))
        for row in native['adapter_reports']:
            label=f"{row['chirality']}_{row['doublet_option']}"
            expected.update(k+'_'+label for k in ('native_pair_isometry','transported_scalar_projection','retained_native_complement','plus_signed_involution','minus_signed_involution','signed_controls_self_adjoint','two_controls_sum_full_diagonal','complete_hamiltonian_diagonal_and_scalar','common_reference_subtraction','native_interaction_annihilates_complement'))
        expected.update('source_signed_control_verified_'+c for c in ('proton','belt'))
        expected.update(('same_candidate_parameters','common_neutral_pool_law','vacuum_extension_is_separate_and_dark'))
        require(receipt.get('native_pair_dimension')==100 and receipt.get('scalar_projector_rank')==1 and receipt.get('retained_complement_dimension')==99,'wrong native rule dimensions')
        require(receipt.get('candidate_parameters')=={'record_gap':'1','vertex_g':'1/2','relative_native_orbital_unit':'1','readout_time':'1 model-time unit'},'candidate model changed')
        require(receipt.get('Hamiltonian')=='Before common empty subtraction: N+g(I-Pi⊗X); for M=1,g=1/2 the record blocks are [[gI,-gPi],[-gPi,(1+g)I]]. Subtract common empty reference gI to obtain N-gPi⊗X.','missing complete Hamiltonian derivation')
        pins=receipt.get('source_hashes',{});require(NATIVE_GATE in pins and CONTRACT in pins and NATIVE in pins and MEDIATOR in pins,'missing native gate provenance pins')
        for p,h in pins.items():require(digest(root,p)==h,'stale native signed-record dependency: '+p)
        require(set(receipt.get('checks',{}))==expected and all(receipt['checks'].values()),'incomplete native signed-record obligations')
        return receipt
    elif attempt['action']=='prove/rival-defect-record-rule' and outcome=='++':
        require(receipt.get('schema')=='marici.voevodsky.rival-defect-record-receipt.v1' and receipt.get('status')=='pass' and receipt.get('fresh_execution') is True and receipt.get('physical_admission') is False,'wrong rival defect receipt')
        refinements=read(root,REFINEMENTS)['refinements'];expected=set().union(*(set(r['required_checks']) for r in refinements if r['parent']==attempt['claim']))
        require(set(receipt.get('required_checks',[]))==expected and set(receipt.get('checks',{}))==expected and all(v is True for v in receipt['checks'].values()),'rival receipt must discharge both exact refinements')
        labels={f'{chirality}_{option}' for chirality in (1,-1) for option in (0,1)}
        detail_expected=expected|{family+'_'+label for family in expected|{'native_carrier_same','rival_defect_projection','rival_orthogonal_to_scalar'} for label in labels}
        details=receipt.get('detail_checks',{})
        require(set(details)==detail_expected and all(v is True for v in details.values()),'missing exact rival scenario checks')
        require(receipt.get('candidate_parameters')==read(root,CONTRACT)['frozen_comparison']['candidate_parameters'],'rival candidate parameters changed')
        require(receipt.get('control')=='Q=c-Pi on carrier; Q=0 on separate vacuum; H_rival=N-g Q⊗X after common empty-reference subtraction.','wrong rival generator')
        require(receipt.get('native_carrier_dimension')==100 and receipt.get('separate_vacuum_dimension')==1 and receipt.get('record_dimension')==2 and receipt.get('rival_projector_rank')==99,'wrong rival carrier dimensions')
        pins=receipt.get('source_hashes',{})
        required_pins={RIVAL_GATE,REFINEMENTS,CONTRACT,NATIVE,'research/voevodsky/results/typed_spin_channels.json','research/voevodsky/checkers/check_native_spinor_pair_adapter.py','research/voevodsky/checkers/check_typed_spin_channels.py','research/voevodsky/checkers/check_pentachoron_spin_interfaces.py'}
        require(required_pins<=set(pins),'missing rival theorem provenance')
        for p,h in pins.items():require(digest(root,p)==h,'stale rival theorem dependency: '+p)
        return receipt
    elif attempt['action']=='prove/common-resource-accounting' and outcome=='++' and receipt.get('schema')=='marici.voevodsky.common-resource-receipt.v1':
        require(receipt.get('status')=='pass' and receipt.get('fresh_execution') is True and receipt.get('physical_admission') is False and receipt.get('kernel_verified_analytic_theorem') is False,'wrong accounting verification level')
        expected=SECTOR_CONCLUSIONS['common-resource-accounting'];checks=receipt.get('checks',{})
        require(set(checks)==expected and all(v is True for v in checks.values()),'incomplete accounting conclusions')
        labels={f'{chirality}_{option}' for chirality in (1,-1) for option in (0,1)}
        families={'same_complete_diagonals','both_signed_involutions','both_controls_self_adjoint','shared_vacuum_reference','all_joint_coordinates_retained','same_normalized_scalar_preparation','selected_K_self_adjoint'}
        expected_details={f+'_'+label for f in families for label in labels}|{'centered_record_involution','unitary_coefficient_identity','density_trace_coefficients','record_occupation_coefficients','interaction_energy_coefficients','unitary_energy_coefficients','dephased_energy_coefficients','conditional_projective_states','measurement_energy_change_operator','rival_ready_state_dark'}
        details=receipt.get('detail_checks',{})
        require(set(details)==expected_details and all(v is True for v in details.values()),'incomplete accounting/readout details')
        require(receipt.get('joint_dimension')==202 and receipt.get('empty_ready_energy_before_subtraction')=='1/2' and receipt.get('empty_ready_energy_after_subtraction')=='0','wrong accounting dimensions/reference')
        require(receipt.get('readout_convention')=='ideal projective neutral-record measurement, both outcomes and matter retained; external apparatus not modeled','unsupported measurement model')
        require(receipt.get('energy_accounting')=={'primary_before':'epsilon','primary_after_nonselective_readout':'epsilon+p','rival_before_and_after':'epsilon','measurement_energy_increase':'p','p':'(1-cos(sqrt(2)))/4'},'incorrect unitary/readout energy ledger')
        require(receipt.get('proof_kind')=='exact finite signed-control blocks, common reference and readout coefficient identities; written finite-dimensional spectral argument for joint reversibility','unsupported accounting proof kind')
        pins=receipt.get('source_hashes',{})
        required={ACCOUNTING_GATE,CONTRACT,SOURCE_K,NATIVE,SECTOR_THEOREM,SECTOR_MODULE,RIVAL_GATE,'research/voevodsky/common-resource-accounting.v1.md','research/voevodsky/checkers/check_selected_source_k.py','research/voevodsky/checkers/check_sector_theorem_progress.py','research/voevodsky/checkers/check_pentachoron_spin_interfaces.py','research/voevodsky/checkers/check_typed_spin_channels.py','research/voevodsky/results/typed_spin_channels.json'}
        require(required<=set(pins),'missing accounting proof/source pins')
        for p,h in pins.items():require(digest(root,p)==h,'stale accounting dependency: '+p)
        return receipt
    elif attempt['claim'] in CLOSURE_CLAIMS and outcome=='++' and receipt.get('schema')==CLOSURE_SCHEMA:
        return validate_closure_receipt(root,receipt,attempt['claim'])
    else:
        require(receipt.get('schema')=='marici.voevodsky.scoped-review-receipt.v1' and receipt.get('status')=='admitted' and receipt.get('fresh_execution') is True,'conclusive outcome requires scoped reviewed evidence')
        require(receipt.get('proof_kind') if outcome=='++' else receipt.get('counterexample_kind'),'missing proof/counterexample characterization')
        require(isinstance(receipt.get('reviewer'),str) and receipt['reviewer'].strip(),'missing accountable reviewer')
        verifier=receipt.get('verifier');require(isinstance(verifier,dict) and verifier.get('path') and verifier.get('sha256'),'missing theorem-specific verifier pin')
        pins=receipt.get('source_hashes');require(isinstance(pins,dict) and pins.get(verifier['path'])==verifier['sha256'] and CONTRACT in pins,'verifier/source pins missing')
        if attempt['claim'] in set(SECTOR_CONCLUSIONS)|{'conditional-reaggregation-comparison'}:
            require(pins.get(SOURCE_K)==digest(root,SOURCE_K),'accounting/dynamics/comparison receipt must pin selected source K')
        for p,h in pins.items():require(digest(root,p)==h,'stale reviewed evidence dependency: '+p)
        expected=set(receipt.get('required_checks',[]));observed=receipt.get('checks',{})
        if attempt['claim']=='rival-defect-record-rule' and outcome=='++':
            refinements=read(root,REFINEMENTS)['refinements'];required=set().union(*(set(r['required_checks']) for r in refinements if r['parent']==attempt['claim']))
            require(expected==required and pins.get(REFINEMENTS)==digest(root,REFINEMENTS),'rival receipt must discharge/pin both refined subclaims')
        require(expected and set(observed)==expected and all(v is True for v in observed.values()),'incomplete reviewed theorem-specific checks')
        require(receipt.get('physical_admission') is False,'conditional claim cannot certify physical admission')
        if 'sector_theorem_evidence' in receipt:
            validate_sector_bundle(root,receipt['sector_theorem_evidence'],attempt['claim'],receipt)
        return receipt
    for chirality in (1,-1):
        for option in (0,1):
            for key in ('native_metric','same_preparation_controls','complement_retained','scalar_cycle_fixed'):expected.add(key+'_'+str(chirality)+'_'+str(option))
    require(set(receipt.get('checks',{}))==expected and all(v is True for v in receipt['checks'].values()),'incomplete gate obligation set')
    require(receipt.get('dimensions')=={'native_pair':100,'matter_with_vacuum':101,'matter_and_one_neutral_record':202},'wrong native interface')
    pins=receipt.get('source_hashes',{});require(GATE in pins and CONTRACT in pins,'missing theorem-specific source pins')
    for p,h in pins.items():require(digest(root,p)==h,'stale theorem dependency: '+p)
    require(receipt.get('kernel_verified_analytic_theorem') is False,'unsupported verification upgrade')
    return receipt

def replay(root,contract,m,actions,ledger):
    require(ledger.get('schema')=='marici.voevodsky.reaggregation-attempt-ledger.v1','wrong ledger schema')
    require(ledger.get('contract_sha256')==digest(root,CONTRACT) and ledger.get('model_sha256')==digest(root,MODEL) and ledger.get('engine_sha256')==digest(root,ENGINE) and ledger.get('refinements_sha256')==digest(root,REFINEMENTS) and ledger.get('sector_theorem_sha256')==digest(root,SECTOR_THEOREM) and ledger.get('source_k_sha256')==digest(root,SOURCE_K),'contract/model/engine/refinement/sector/source K context changed: reviewed migration required, no reset')
    require(ledger.get('initial_budget')==m['budget_effort_units'],'budget reset')
    imports=validate(root,contract)['imports']
    by_id={a['id']:a for a in actions};used=set();attempts={};outcomes={i:r['outcome'] for i,r in imports.items() if r['outcome'] in ('++','-+')};spent=0;active=None;observations=[];last=None
    for index,event in enumerate(ledger['events']):
        bare={k:v for k,v in event.items() if k!='hash'}
        require(event.get('index')==index and event.get('previous')==last and event.get('hash')==object_hash(bare),'broken event chain')
        last=event['hash'];kind=event.get('type');nonce=event.get('nonce')
        if kind=='start':
            require(active is None and nonce not in attempts and not any(a['state']=='paused' for a in attempts.values()),'concurrent/replayed or paused attempt')
            a=by_id.get(event.get('action'));require(a is not None and a['id'] not in used,'unknown/exhausted canonical action')
            require(a['claim'] not in outcomes,'already resolved claim')
            require(all(outcomes.get(d)=='++' for d in a['requires']),'missing proof prerequisites; probability is not certificate')
            require(event.get('cost')==a['cost'] and spent+a['cost']<=ledger['initial_budget'],'cost/budget violation')
            used.add(a['id']);spent+=a['cost'];active=nonce
            attempts[nonce]=dict(a,action=a['id'],nonce=nonce,state='active',checkpoints=[])
        elif kind in ('pause','resume','checkpoint','finish'):
            require(nonce in attempts,'unknown attempt nonce');a=attempts[nonce]
            if kind=='resume':
                require(a['state']=='paused' and active is None,'attempt cannot resume');a['state']='active';active=nonce
            else:
                require(active==nonce and a['state']=='active','attempt not active')
                if kind=='pause':a['state']='paused';active=None
                elif kind=='checkpoint':
                    require(digest(root,event['path'])==event['sha256'],'stale checkpoint');a['checkpoints'].append(event['path'])
                elif kind=='finish':
                    o=event.get('outcome');require(o in (('++','+-') if a['intent']=='prove' else ('-+','--')),'intent/outcome mismatch')
                    admitted_receipt(root,event,a);a['state']='finished';a['outcome']=o;a['receipt']=event['receipt'];a['receipt_sha256']=event['receipt_sha256'];active=None
                    if o in ('++','-+'):outcomes[a['claim']]=o
                    observations.append((by_id[a['action']],o))
        elif kind=='review':
            require(nonce in attempts,'review for unknown attempt');a=attempts[nonce]
            require(a['state']=='finished' and 'review' not in a,'review must follow a finished attempt exactly once')
            require(isinstance(event.get('actual_focus_effort_eu'),(int,float)) and event['actual_focus_effort_eu']>0,'actual focused effort must be positive')
            require(event.get('review_result') in ('confirmed','needs_revision','inconclusive'),'invalid review result')
            require(isinstance(event.get('blocker_category'),str) and event['blocker_category'],'missing blocker classification')
            require(isinstance(event.get('reviewer'),str) and event['reviewer'].strip(),'missing reviewer')
            a['review']={k:event[k] for k in ('actual_focus_effort_eu','review_result','blocker_category','reviewer','time')}
        else:raise NetError('unknown event type')
    return {'outcomes':outcomes,'spent':spent,'remaining':ledger['initial_budget']-spent,'active':active,'attempts':attempts,'used':used,'observations':observations}

def calibration_report(state):
    reviewed=[a for a in state['attempts'].values() if 'review' in a]
    by_intent={intent:[a for a in reviewed if a['intent']==intent] for intent in ('prove','reject')}
    groups={intent:{'reviewed_attempts':len(items),'confirmed':sum(a['review']['review_result']=='confirmed' for a in items),'needs_revision':sum(a['review']['review_result']=='needs_revision' for a in items),'inconclusive':sum(a['review']['review_result']=='inconclusive' for a in items),'mean_actual_focus_effort_eu':sum(a['review']['actual_focus_effort_eu'] for a in items)/len(items) if items else None,'blocker_categories':sorted({a['review']['blocker_category'] for a in items})} for intent,items in by_intent.items()}
    cost_review_ready=all(groups[i]['reviewed_attempts']>=5 for i in groups)
    return {'status':'reviewed_history_observed_not_calibrated' if reviewed else 'no_reviewed_attempts_yet','reviewed_sample_count':len(reviewed),'groups':groups,'empirically_calibrated':False,'eligible_for_cost_model_review':cost_review_ready,'likelihood_calibration_status':'not_calibratable_from_attempt_outcomes_alone; needs independent truth labels for successes and failures plus a larger reviewed sample','cost_review_threshold':'At least five reviewed attempts per intent; any model change still requires explicit review/migration.','model_estimates_changed':False,'interpretation':'Actual focused effort and reviewer/blocker annotations are observations, not automatic revisions to subjective costs, sensitivities, or scientific truth.'}

def diagnose_physical_gate(root,contract,outcomes):
    spec=read(root,PHYSICAL);required={e['id'] for e in spec['required_evidence_classes']}
    registered={e['class_id']:e for e in spec.get('evidence_packages',[])}
    require(set(registered)<=required,'unknown physical evidence class')
    for item in registered.values():require(item.get('path') and item.get('sha256') and digest(root,item['path'])==item['sha256'],'stale/unpinned physical evidence')
    missing=sorted(required-set(registered));conditional=outcomes.get(contract['objective']['target'])
    return {'status':'blocked_until_conditional_target_plusplus' if conditional!='++' else 'awaiting_physical_evidence' if missing else 'ready_for_independent_physical_review',
        'conditional_target_outcome':conditional,'required_evidence_classes':sorted(required),'registered_evidence_classes':sorted(registered),'missing_evidence_classes':missing,
        'evidence_package_count':len(registered),'physical_admission':False,'automatic_promotion':False,
        'rule':'Readiness is not admission; only a dedicated reviewed physical receipt can resolve the physical node.'}

def diagnose_routes(root,contract,outcomes):
    target=contract['objective']['target'];target_node=next(n for n in contract['conjectures'] if n['id']==target)
    blocked=sorted(n for n,o in outcomes.items() if o=='-+' and n!=target)
    direct=sorted(d for d in target_node['depends_on'] if outcomes.get(d)=='-+')
    routes=read(root,ROUTES).get('alternative_routes',[])
    return {'primary_route_status':'refuted' if outcomes.get(target)=='-+' else 'blocked_by_refuted_component' if blocked else 'active',
        'target_outcome':outcomes.get(target),'refuted_components':blocked,'target_direct_blockers':direct,'reviewed_alternatives':routes,
        'alternative_status':'reviewed_alternatives_available' if routes else 'none_registered_route_design_review_needed' if blocked else 'not_needed_yet',
        'interpretation':'Component refutation blocks only routes that require it; target remains unresolved absent target-scoped evidence.'}

def analyze(root,contract,include_sensitivity=True):
    structure=validate(root,contract);m,actions,worlds,joint_report=model_data(root,contract)
    invariant_contract=read(root,INVARIANTS);records=invariant_contract['invariants']
    ledger=read(root,LEDGER) if (root/LEDGER).is_file() else new_ledger(root,m)
    state=replay(root,contract,m,actions,ledger);target=m['target'];weights=[w['probability'] for w in worlds]
    for a,o in state['observations']:
        weights=[p*likelihood(a,w['truth'][a['claim']],o) for p,w in zip(weights,worlds)]
    total=sum(weights);require(total>0,'zero-likelihood observed history')
    posterior=[dict(w,probability=p/total) for w,p in zip(worlds,weights) if p>0]
    proved={c for c,o in state['outcomes'].items() if o=='++'};refuted={c for c,o in state['outcomes'].items() if o=='-+'}
    available=[a for a in actions if a['id'] not in state['used'] and a['claim'] not in proved|refuted]
    def solve(av,budget):
        if target in proved:return {'first_action':None,'success_probability':1.,'expected_total_effort':0.,'budget':budget,'success_branch_trace':[],'states_evaluated':0}
        if target in refuted or not any(a['id']=='prove/'+target for a in av):return {'first_action':None,'success_probability':0.,'expected_total_effort':0.,'budget':budget,'success_branch_trace':[],'states_evaluated':0}
        return Planner(posterior,av,target,proved,budget).solve()
    pending=[a for a in state['attempts'].values() if a['state'] in ('active','paused')]
    central=None if pending else solve(available,state['remaining'])
    route_diagnostics=diagnose_routes(root,contract,state['outcomes'])
    refinement_records=read(root,REFINEMENTS)['refinements']
    refinement_status=[]
    for refinement in refinement_records:
        parent=next((a for a in state['attempts'].values() if a['claim']==refinement['parent'] and a.get('outcome')=='++'),None)
        verified=False
        if parent:
            checks=read(root,parent['receipt']).get('checks',{})
            labels=[f"{row['chirality']}_{row['doublet_option']}" for row in read(root,NATIVE)['adapter_reports']]
            families=refinement.get('required_check_families',[])
            required={family+'_'+label for family in families if family!='common_neutral_pool_law' for label in labels}
            if 'common_neutral_pool_law' in families:required.add('common_neutral_pool_law')
            required.update(refinement.get('required_checks',[]))
            verified=required<=set(checks) and all(checks.get(k) is True for k in required)
        refinement_status.append({'id':refinement['id'],'parent':refinement['parent'],'statement':refinement['statement'],'outcome':'++' if verified else None,'status':'proved_by_parent_scoped_receipt' if verified else 'unresolved','required_checks':refinement.get('required_checks',refinement.get('required_check_families'))})
    sector_diagnostics=diagnose_sector_theorem(root,contract,state)
    physical_diagnostics=diagnose_physical_gate(root,contract,state['outcomes'])
    calibration=calibration_report(state)
    continuation=('continue/' if pending and pending[0]['state']=='active' else 'resume/')+pending[0]['action'] if pending else None
    recommendation=continuation or central['first_action']
    ready=[a for a in available if set(a['requires'])<=proved]
    diagnostics=[dict(action=a['id'],cost=a['cost'],**action_metrics(posterior,a,target)) for a in ready]
    descendants={n['id']:set() for n in contract['conjectures']};children={n['id']:[] for n in contract['conjectures']}
    for node in contract['conjectures']:
        for prerequisite in node['depends_on']:
            if prerequisite in children:children[prerequisite].append(node['id'])
    def downstream(name,seen=None):
        seen=set() if seen is None else seen
        for child in children.get(name,[]):
            if child not in seen:seen.add(child);downstream(child,seen)
        return seen
    descendants={name:downstream(name) for name in children}
    max_unlock=max((len(descendants.get(a['claim'],set())) for a in ready),default=0)
    leverage={a['id']:(len(descendants.get(a['claim'],set()))/max_unlock if max_unlock else 0.) for a in ready}
    priority_scenarios=[]
    for weight in m['priority_policy']['coherence_weights']:
        ranked=sorted(diagnostics,key=lambda d:(-(d['target_information_per_effort']+weight*leverage.get(d['action'],0.)),d['action']))
        priority_scenarios.append({'coherence_weight':weight,'top_action':ranked[0]['action'] if ranked else None,'ranking':[{'action':d['action'],'target_information_bits_per_effort':d['target_information_per_effort'],'normalized_unlocked_descendants':leverage.get(d['action'],0.),'diagnostic_score':d['target_information_per_effort']+weight*leverage.get(d['action'],0.)} for d in ranked]})
    rows=[]
    for a in available:
        predicates={d:True for d in a['requires'] if d not in proved and d in posterior[0]['truth']}
        try:context=condition(posterior,predicates) if predicates else posterior
        except ValueError:context=[]
        rows.append(dict(action=a['id'],claim=a['claim'],intent=a['intent'],cost=a['cost'],cost_range=m['estimates'][a['claim']][a['intent']+'_cost_range'],
            ready_now=set(a['requires'])<=proved,prerequisite_certificates=a['requires'],
            context='current state' if not predicates else 'hypothetical prerequisite proof certificates, not current facts',
            metrics=action_metrics(context,a,target) if context else None))
    scenarios=[]
    if include_sensitivity and not pending:
        for budget,cost_multiplier,sensitivity_multiplier in product(m['sensitivity']['budgets'],m['sensitivity']['proof_cost_multipliers'],m['sensitivity']['proof_sensitivity_multipliers']):
            changed=copy.deepcopy(available)
            for a in changed:
                if a['intent']=='prove':a['cost']*=cost_multiplier;a['sensitivity']*=sensitivity_multiplier
            value=solve(changed,max(0,budget-state['spent']))
            scenarios.append(dict(value,hypothetical_initial_budget=budget,actual_spent_effort_retained=state['spent'],cost_multiplier=cost_multiplier,sensitivity_multiplier=sensitivity_multiplier))
    return {'status':'pass','validation_passed':True,'planning_only':True,'estimate_status':m['estimate_status'],'empirically_calibrated':False,
        'scientific_outcomes_changed':False,'scientific_outcome':state['outcomes'].get(target),'target_outcome':state['outcomes'].get(target),
        'physical_admission':False,'state':'resolved-conditional-only' if target in proved|refuted else 'active',
        'node_count':len(contract['conjectures']),'refinement_node_count':len(refinement_records),'umbrella_node_count':1,'sector_theorem':sector_diagnostics,'combined_obligation_count':len(contract['conjectures'])+len(refinement_records)+1,'refinement_nodes':refinement_status,'imports':structure['imports'],
        'locally_proved_claims':sorted(proved&{n['id'] for n in contract['conjectures']}),'locally_refuted_claims':sorted(refuted&{n['id'] for n in contract['conjectures']}),
        'unresolved_nodes':sorted(n['id'] for n in contract['conjectures'] if n['id'] not in proved|refuted),
        'recommended_action':recommendation,'central':central,'continuation_action':continuation,
        'initial_budget':ledger['initial_budget'],'spent_effort':state['spent'],'remaining_effort':state['remaining'],
        'canonical_action_count':len(actions),'ready_actions':[a['id'] for a in ready],'information_diagnostic':diagnostics,'rows':rows,
        'posterior_claim_probabilities':{n:marginal(posterior,n) for n in m['estimates']},'joint_worlds':posterior,
        'sensitivity':{'scenario_count':len(scenarios),'scenarios':scenarios,'recommendation_stable':bool(scenarios) and all(s['first_action']==recommendation for s in scenarios)},
        'attempts':list(state['attempts'].values()),'evidence_hashes':structure['evidence_hashes'],
        'coherence_invariants':{'path':INVARIANTS,'sha256':digest(root,INVARIANTS),'status':'static_contract_consistency_pass_scientific_satisfaction_unresolved','items':[dict(id=i['id'],owner=i['owner'],requirement=i['requirement'],owner_outcome=state['outcomes'].get(i['owner']),scientifically_satisfied=state['outcomes'].get(i['owner'])=='++') for i in records]},
        'shared_obligations':{'status':'canonical_single_evidence_identity','items':[dict(o,owner_outcome=state['outcomes'].get(o['owner']),consumers_ready=[c for c in o['consumers'] if all(d in proved for d in next(n['depends_on'] for n in contract['conjectures'] if n['id']==c))]) for o in invariant_contract['shared_obligations']]},
        'joint_constraint_report':{'status':m['joint_model']['constraint_status'],'hard_constraint_count':len(m['joint_model']['hard_constraints']),'probability_mass_before_conditioning':joint_report['raw_world_mass'],'coherence_world_count':len(worlds)},
        'priority_diagnostic':{'policy':m['priority_policy'],'central_policy_unchanged':True,'weights_are_truth_neutral':True,'scenarios':priority_scenarios,'recommendation_changes_with_weight':len({s['top_action'] for s in priority_scenarios})>1},
        'route_diagnostics':route_diagnostics,'physical_gate':physical_diagnostics,'calibration':calibration,
        'source_hashes':{p:digest(root,p) for p in (CONTRACT,MODEL,ROUTES,INVARIANTS,PHYSICAL,REFINEMENTS,SECTOR_THEOREM,SECTOR_MODULE,SOURCE_K,ENGINE,'research/voevodsky/checkers/reaggregation_harness.py')},
        'ledger_sha256':digest(root,LEDGER) if (root/LEDGER).is_file() else None,
        'boundary':'Finite one-shot policy under subjective assumptions, not empirical truth or a global optimum. Failed attempts retain unresolved truth and consumed cost.'}

def live_result(root,contract):return analyze(root,contract)

def mutate(root,command,action=None,receipt=None,outcome=None,path=None,reason=None,actual_focus_effort_eu=None,blocker_category=None,review_result=None,reviewer=None):
    with locked(root):
        c=read(root,CONTRACT);validate(root,c);m,actions,_,_=model_data(root,c)
        ledger=read(root,LEDGER) if (root/LEDGER).is_file() else new_ledger(root,m)
        state=replay(root,c,m,actions,ledger);now=datetime.now(timezone.utc).isoformat()
        if command=='init':require(not (root/LEDGER).exists(),'ledger already exists; cannot reset')
        elif command=='review':
            nonce=action;attempt=state['attempts'].get(nonce);require(attempt is not None and attempt['state']=='finished','review requires a finished attempt nonce')
            append_event(ledger,{'type':'review','nonce':nonce,'time':now,'actual_focus_effort_eu':actual_focus_effort_eu,'blocker_category':blocker_category,'review_result':review_result,'reviewer':reviewer})
        elif command=='start':
            paused=[a for a in state['attempts'].values() if a['state']=='paused'];require(not paused,'resume paused attempt before starting another')
            a=next((a for a in actions if a['id']==action),None);require(a is not None,'unknown action')
            append_event(ledger,{'type':'start','action':action,'cost':a['cost'],'nonce':uuid.uuid4().hex,'time':now})
        else:
            pending=[a for a in state['attempts'].values() if a['state']!='finished'];require(len(pending)==1,'no unique pending attempt')
            a=pending[0];event={'type':command,'nonce':a['nonce'],'time':now}
            if command=='finish':
                event.update(receipt=receipt,receipt_sha256=digest(root,receipt),outcome=outcome)
            elif command=='checkpoint':event.update(path=path,sha256=digest(root,path))
            elif command=='fail':
                relative='research/voevodsky/results/reaggregation-attempts/'+a['nonce']+'.incomplete.json'
                incomplete={'status':'incomplete','scientific_outcome':None,'node_id':a['claim'],'attempt_nonce':a['nonce'],'intent':a['intent'],'outcome':'+-' if a['intent']=='prove' else '--','reason':reason or 'Bounded attempt unfinished; not a refutation.'}
                write_atomic(root/relative,incomplete);event.update(type='finish',receipt=relative,receipt_sha256=digest(root,relative),outcome=incomplete['outcome'])
            append_event(ledger,event)
        replay(root,c,m,actions,ledger);write_atomic(root/LEDGER,ledger)
    result=analyze(root,c);result['ledger_updated']=True
    result['scientific_outcomes_changed']=command=='finish' and outcome in ('++','-+')
    result['planning_only']=not result['scientific_outcomes_changed']
    return result

def run_gate(root,action):
    runners={'prove/freeze-common-interface':GATE,'prove/native-signed-record-rule':NATIVE_GATE,'prove/rival-defect-record-rule':RIVAL_GATE,'prove/common-resource-accounting':ACCOUNTING_GATE}
    runners.update({'prove/'+claim:CLOSURE_GATE for claim in CLOSURE_CLAIMS})
    require(action in runners,'no automatic theorem runner registered; start a manual attempt and add scoped evidence')
    if (root/LEDGER).is_file():
        c=read(root,CONTRACT);m,actions,_,_=model_data(root,c);state=replay(root,c,m,actions,read(root,LEDGER))
        pending=[a for a in state['attempts'].values() if a['state']!='finished']
    else:pending=[]
    if pending:
        require(len(pending)==1 and pending[0]['action']==action,'another attempt is pending')
        if pending[0]['state']=='paused':mutate(root,'resume')
    else:mutate(root,'start',action=action)
    c=read(root,CONTRACT);m,actions,_,_=model_data(root,c);state=replay(root,c,m,actions,read(root,LEDGER));a=state['attempts'][state['active']]
    suffix={ 'prove/native-signed-record-rule':'.native-signed-record.json','prove/rival-defect-record-rule':'.rival-defect-record.json','prove/common-resource-accounting':'.common-resource.json'}.get(action,'.proof.json')
    if a['claim'] in CLOSURE_CLAIMS:suffix='.closure.json'
    relative='research/voevodsky/results/reaggregation-attempts/'+a['nonce']+suffix;(root/relative).parent.mkdir(parents=True,exist_ok=True)
    command=[sys.executable,str(root/runners[action]),a['nonce'],str(root/relative)]
    if a['claim'] in CLOSURE_CLAIMS:command.append(a['claim'])
    subprocess.run(command,check=True,timeout=600)
    return mutate(root,'finish',receipt=relative,outcome='++')

def export_outcome(root,claim):
    # Immutable snapshots compatible with the shared outcome-reference resolver.
    from outcome_reference import resolve,PORTS
    c=read(root,CONTRACT);r=analyze(root,c,False);o='++' if claim in r['locally_proved_claims'] else '-+' if claim in r['locally_refuted_claims'] else None
    require(o is not None and any(n['id']==claim for n in c['conjectures']),'cannot re-export unresolved or foreign truth as a local proposition')
    ledger=read(root,LEDGER);proof=next(e for e in reversed(ledger['events']) if e['type']=='finish' and e['outcome']==o and read(root,e['receipt'])['node_id']==claim)
    verification=read(root,proof['receipt']);key=object_hash({'format_version':2,'claim':claim,'ledger':digest(root,LEDGER),'receipt':proof['receipt_sha256']})
    prefix='research/voevodsky/exports/reaggregation/'+key;directory=root/prefix
    if directory.exists():
        pointer_path=prefix+'/pointer.json';pointer=read(root,pointer_path);resolve(root,pointer)
        return {'export_pointer':pointer_path,'outcome':o,'claim':claim,'existing_immutable_export_verified':True}
    directory.mkdir(parents=True)
    snapshot=copy.deepcopy(c);snapshot['outcome_ports']=PORTS
    for n in snapshot['conjectures']:n['outcome']='++' if n['id'] in r['locally_proved_claims'] else '-+' if n['id'] in r['locally_refuted_claims'] else None
    files={'contract.json':snapshot,'result.json':{'status':'pass','claims':{n['id']:{'id':n['id'],'outcome':n['outcome']} for n in snapshot['conjectures']}},'verification.json':verification,'ledger.json':ledger}
    for name,data in files.items():write_atomic(directory/name,data)
    index=next(i for i,n in enumerate(snapshot['conjectures']) if n['id']==claim);node=snapshot['conjectures'][index];head=prefix+'/head.json'
    pins={prefix+'/'+name:digest(root,prefix+'/'+name) for name in files}
    pins.update(verification['source_hashes'])
    level={k:verification[k] for k in ('proof_kind','kernel_verified_analytic_theorem')}
    export={'schema':'marici.conjecture-net.outcome-export.v1','outcome_semantics':'proof-attempt-outcomes-v1','export_id':key,'head_path':head,'artifact_sha256':pins,'source':{'contract':prefix+'/contract.json','result':prefix+'/result.json','node_pointer':'/conjectures/'+str(index),'result_claim_pointer':'/claims/'+claim+'/id','result_outcome_pointer':'/claims/'+claim+'/outcome'},'claim_bindings':{k:'/conjectures/'+str(index)+'/'+k for k in ('id','statement','scope_id')},'claim':{k:node[k] for k in ('id','statement','scope_id')},'outcome':o,'verification_receipt':prefix+'/verification.json','verification':level}
    write_atomic(directory/'export.json',export);ref={'path':prefix+'/export.json','sha256':digest(root,prefix+'/export.json')}
    write_atomic(root/head,{'schema':'marici.conjecture-net.outcome-head.v1','status':'active','export':ref,'export_id':key})
    pointer={'schema':'marici.conjecture-net.outcome-pointer.v1','export':ref,'head':head,'expected_claim':export['claim'],'expected_outcome':o,'accepted_verification':level}
    write_atomic(directory/'pointer.json',pointer)
    try:resolve(root,pointer)
    except ValueError:
        write_atomic(root/head,{'schema':'marici.conjecture-net.outcome-head.v1','status':'revoked','export':ref,'export_id':key,'reason':'Failed initial shared resolver validation; preserved as failed history.'})
        raise
    return {'export_pointer':prefix+'/pointer.json','outcome':o,'claim':claim}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['plan','status','init','start','pause','resume','checkpoint','finish','fail','review','run','export','revoke']);parser.add_argument('argument',nargs='?');parser.add_argument('--receipt');parser.add_argument('--outcome',choices=['++','+-','-+','--']);parser.add_argument('--reason');parser.add_argument('--actual-focus-effort-eu',type=float);parser.add_argument('--blocker-category');parser.add_argument('--review-result',choices=['confirmed','needs_revision','inconclusive']);parser.add_argument('--reviewer')
    args=parser.parse_args()
    try:
        if args.command in ('plan','status'):result=analyze(ROOT,read(ROOT,CONTRACT),args.command=='plan')
        elif args.command=='run':result=run_gate(ROOT,args.argument)
        elif args.command=='export':result=export_outcome(ROOT,args.argument)
        elif args.command=='revoke':
            pointer=read(ROOT,args.argument);head=pointer['head'];require(head.startswith('research/voevodsky/exports/reaggregation/'),'cannot revoke another owning surface')
            require(args.reason,'revocation requires explicit reason');h=read(ROOT,head);h.update(status='revoked',reason=args.reason);write_atomic(ROOT/head,h)
            result={'export_pointer':args.argument,'status':'revoked','scientific_outcomes_changed':False}
        else:result=mutate(ROOT,args.command,action=args.argument,receipt=args.receipt,outcome=args.outcome,path=args.argument,reason=args.reason,actual_focus_effort_eu=args.actual_focus_effort_eu,blocker_category=args.blocker_category,review_result=args.review_result,reviewer=args.reviewer)
        destination='research/voevodsky/results/reaggregation-last-export.json' if args.command in ('export','revoke') else OUT
        write_atomic(ROOT/destination,result)
        print(json.dumps({k:result[k] for k in ('status','recommended_action','central','continuation_action','spent_effort','remaining_effort','locally_proved_claims','target_outcome','export_pointer') if k in result},indent=2))
    except (NetError,ValueError,KeyError,OSError,TypeError,subprocess.SubprocessError) as error:
        print('BLOCKED:',error,file=sys.stderr)
        if args.command=='run':print('A started attempt remains charged and active until explicitly resumed or finished.',file=sys.stderr)
        raise SystemExit(1)

if __name__=='__main__':main()
