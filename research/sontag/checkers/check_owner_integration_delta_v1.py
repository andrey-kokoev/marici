"""Fresh read-only integration/provenance audit; no science or compiler reruns."""
import copy
import importlib.util
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
BASE='research/conjecture_net/contracts/event-sourced-control-work-net.v1.json'
MANIFEST='research/sontag/results/event-control-review-manifest-v2.json'
PROPOSAL='research/sontag/results/event-control-transition-proposal-v1.json'
LOCAL='research/sontag/contracts/optical-statistical-control-work-net.v1.json'
OUT='research/sontag/results/owner-integration-delta-v1.json'
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def module(name,p):
    spec=importlib.util.spec_from_file_location(name,ROOT/p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
owner=module('net_owner','research/nima/checkers/check_event_sourced_control_net.py')
central=module('formal_review','research/nima/checkers/check_physics_control_contribution_review.py')
formal=central.FORMAL
count=central.formal_receipt(load(formal))
base,proposal,manifest,local=map(load,(BASE,PROPOSAL,MANIFEST,LOCAL))
owner.validate(base,load(base['source_pins']))
if proposal['base_sha256']!=sha(BASE):raise ValueError('proposal base changed; rebase needed')
if local['frontier'] or local['objective']['outcome'] is not None:raise ValueError('local state changed')
manifest_drift=[p for p,h in manifest['source_sha256'].items() if sha(p)!=h]
proposal_drift=[p for p,h in proposal['source_pins_for_review'].items() if sha(p)!=h]
optical_receipt=load('research/sontag/results/optical-binding-assembly-v1.json')
optical_drift=[p for p,h in optical_receipt['source_sha256'].items() if sha(p)!=h]
if optical_receipt.get('passed') is not True or optical_drift:raise ValueError('optical assembly receipt drift: '+str(optical_drift))
# Report historical snapshots honestly. No automatic regeneration/re-pin.
proofs={
 'typed-event-control-interface':['research/sontag/results/typed-event-control-interface-v1.json'],
 'history-to-state-congruence':['research/sontag/history-to-state-congruence-v1.md','research/sontag/agda/RetainedHistoryTransport.agda',formal,'research/sontag/results/history-to-state-congruence-v1.json'],
 'observation-feedback-realization':['research/sontag/results/observation-feedback-realization-v1.json'],
 'presentation-naturality':['research/sontag/agda/RetainedHistoryTransport.agda',formal,'research/sontag/results/presentation-naturality-v1.json'],
 'mathematical-control-realization':['research/sontag/results/event-control-review-manifest-v2.json','research/sontag/wg-retained-history-formal-verification-v1.md']}
exclusions=['arbitrary WG equivalence','marked relation-algebra attachment transport via Composite F,G',
 'physical exact nondisturbing energy reader','empirical apparatus license','common-system coverage or completed-history theorem']
by={n['id']:n for n in base['conjectures']}
transitions=[];sim=copy.deepcopy(base);sb={n['id']:n for n in sim['conjectures']}
for t in proposal['proposed_transitions']:
    node=t['node'];paths=[t['packet']]+proofs[node]
    aid='integration-'+node
    sim['artifacts'].append({'id':aid,'paths':paths})
    sb[node].update(status=t['proposed_status'],verdict=t['proposed_verdict'],scope=t['scope'],evidence=[aid])
    transitions.append({'node':node,'from':{'status':by[node]['status'],'verdict':by[node]['verdict']},
      'to':{'status':t['proposed_status'],'verdict':t['proposed_verdict']},'scope':t['scope'],
      'prerequisites':by[node]['depends_on'],'required_verdicts':by[node].get('required_verdicts',{}),
      'evidence':{p:sha(p) for p in paths},'unchanged_exclusions':exclusions})
# Exact-reader predecessor is not silently rebound to statistical tap events.
physical=sb['physical-control-binding']
physical.update(status='deferred',verdict='open',blocker='NoLicensedExactReaderPhysicalPackage',
 reopening_condition='Explicit versioned scope admission or evidence of the original physical reader/intervention package; measurement work requires operator reopening.')
physical['evidence']=['integration-physical-gap']
sim['artifacts'].append({'id':'integration-physical-gap','paths':['research/sontag/conditional-statistical-optical-binding-v1.md']})
sim['frontier']=[n['id'] for n in sim['conjectures'] if n['status']=='open' and all(sb[d]['status']=='resolved' for d in n['depends_on'])]
sim['recommended_start']=sim['frontier'][0] if sim['frontier'] else None
owner.validate(sim,{'source_sha256':{p:sha(p) for p in owner.sources(sim)}})
conditional_interface={
 'source':'two coherent equal-frequency signal modes plus fresh vacuum loss/detector ports; supplied Gamma preparation context',
 'history':'ordered retained tap-count/gain events with actual outcomes and prior/calibration identity',
 'tap_count':{'domain':'0<tau<1, 0<eta<=1; nonnegative integer outcomes',
             'state':'(A,B)->((1-tau)A,(1-tau)B)',
             'observation':'independent Poisson means eta*tau*A and eta*tau*B conditional on fixed coherent preparation',
             'resources':'detected mean eta*tau*(A+B), unobserved mean (1-eta)*tau*(A+B); counts not exact removed energy'},
 'gain':{'domain':'0<=q<=1; vacuum-ready environment','state':'(A,B)->(q^2 A,q^4 B)',
         'physical':'R(q) on first signal, R(q^2) on second; retained environment outputs'},
 'information':'Gamma initial shapes plus counts; initial rates plus eta*tau*current-factor exposures; current factors include preceding gains/taps',
 'policy':'public posterior transcript only; target conditional mean, or confidence-certified/abstain with no reset',
 'time':'ordered nonoverlapping pulse intervals with supplied integral kappa; q is not time',
 'comparison':'all prefix states, resource means, count likelihoods and posterior information commute at ideal conditional scope',
 'calibration':'uniform interval bias-plus-variance theorem on supplied boxes, not measured coverage'}
paths={BASE,MANIFEST,PROPOSAL,LOCAL,formal,central.FRESHNESS_POLICY,
 'research/sontag/checkers/check_owner_integration_delta_v1.py',
 'research/nima/physics-interface-geometry-admission-v1.md',
 'research/sontag/conditional-statistical-optical-binding-v1.md',
 'research/sontag/results/optical-binding-assembly-v1.json'}
paths.update(p for a in local['artifacts'] for p in a['paths'])
for t in transitions:paths.update(t['evidence'])
physical_delta={'node':'physical-control-binding','proposed_status':'deferred','verdict':'open',
 'scope':'exact-reader predecessor; conditional statistical optical successor referenced separately, not a same-vocabulary replacement',
 'blocker':physical['blocker'],'reopening_condition':physical['reopening_condition']}
out={'schema':'marici.sontag.owner-integration-delta.v1','passed':True,'applied':False,
 'request_message':'naradaepistemiccommunication:99da0ab4df729f36b81b','base_contract':BASE,'base_sha256':sha(BASE),
 'proposed_transitions':transitions,'physical_predecessor_delta':physical_delta,
 'unchanged_open_nodes':['same-source-control-comparison','extension-and-coverage','common-event-sourced-control-realization'],
 'conditional_optical_interface':conditional_interface,
 'local_state':{'contract':LOCAL,'frontier':local['frontier'],'empirical_node':next(n for n in local['nodes'] if n['id']=='empirical-optical-realization')},
 'measurement_gate':'planning/acquisition/execution parked; only explicit operator reopening authorizes restart',
 'historical_snapshot_audit':{'manifest_drift':manifest_drift,'proposal_source_drift':proposal_drift,
   'original_strict_formal_inventory':'historical receipt; unrelated additions invalidate original equality-based validator; preserved, not re-pinned'},
 'fresh_provenance':{'method':'live source hashes, predecessor structural validation, proposed in-memory validation, central formal v2 dependency-resolution validation',
   'formal_receipt':formal,'recorded_inventory_count':count,'policy':central.FRESHNESS_POLICY,
   'optical_assembly_source_drift':optical_drift,'optical_recorded_checks':optical_receipt['check_count'],
   'compiler_rerun':False,'scientific_suites_rerun':False,'measurement_executed':False},
 'projected_frontier':sim['frontier'],'source_sha256':{p:sha(p) for p in sorted(paths)},
 'root_closure_asserted':False}
(ROOT/OUT).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'transitions':len(transitions),'formal_entries_validated':count,
 'historical_manifest_drift':manifest_drift,'historical_proposal_drift':proposal_drift,'applied':False},indent=2))
