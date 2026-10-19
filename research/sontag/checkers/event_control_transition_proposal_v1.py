"""Build and structurally test an UNAPPLIED net transition proposal."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/conjecture_net/contracts/event-sourced-control-work-net.v1.json'
spec=importlib.util.spec_from_file_location('owner_validator',ROOT/'research/nima/checkers/check_event_sourced_control_net.py')
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
live=v.load(CONTRACT)
livepins=v.load(live['source_pins'])
v.validate(live,livepins)
c=copy.deepcopy(live)
by={n['id']:n for n in c['conjectures']}
updates={
 'typed-event-control-interface':('Three fixed source dictionaries; retained WG, exact energy, external context commands.','typed-event-control-interface-v1.md'),
 'history-to-state-congruence':('Numeric energy gain/read congruence, full-context congruence, fixed WG nested/flattened retained-history isomorphism; no arbitrary equivalence or attachment bridge.','wg-retained-history-congruence-v1.md'),
 'observation-feedback-realization':('Exact model energy target feedback using public transcripts and updated probe state; no physical binding or noise margin.','observation-feedback-realization-v1.md'),
 'presentation-naturality':('Fixed Composite.correct/rebase WG presentation and invertible energy chart; source choices and actual payloads retained.','presentation-naturality-v1.md'),
 'mathematical-control-realization':('Bounded candidate on the same fixed vocabularies; attachment comparison excluded, mathematical readers only.','mathematical-control-realization-candidate-v1.md')}
proposal=[]
for node,(scope,packet) in updates.items():
    aid='sontag-proposal-'+node
    paths=['research/sontag/'+packet]
    if node=='history-to-state-congruence': paths.append('research/sontag/history-to-state-congruence-v1.md')
    c['artifacts'].append({'id':aid,'paths':paths})
    by[node].update(status='resolved',verdict='constructed',scope=scope,evidence=[aid])
    proposal.append({'node':node,'proposed_status':'resolved','proposed_verdict':'constructed','scope':scope,'packet':paths[0],
                     'requires_owner_scope_review':True})
physical=by['physical-control-binding']
physical.update(status='deferred',verdict='open',
 blocker={'type':'MissingPhysicalOperationPackage','fields':['carrier/preparation/actuation','reader/back-action','time','resources','outcome records']},
 reopening_condition='Source-admitted physical operation package on the same event vocabulary and prospective composed comparison.')
c['artifacts'].append({'id':'sontag-physical-deferral','paths':['research/sontag/physical-control-binding-audit-v1.md']})
physical['evidence']=['sontag-physical-deferral']
# Coverage evidence is preparatory only: preserve the unresolved prerequisite.
c['artifacts'].append({'id':'sontag-coverage-boundary','paths':['research/sontag/extension-and-coverage-boundary-v1.md']})
by['extension-and-coverage']['evidence']=['sontag-coverage-boundary']
c['frontier']=[n['id'] for n in c['conjectures'] if n['status']=='open' and all(by[d]['status']=='resolved' for d in n['depends_on'])]
c['recommended_start']=c['frontier'][0] if c['frontier'] else None
pins={'source_sha256':{p:v.sha(p) for p in v.sources(c)}}
v.validate(c,pins)  # structural simulation, NOT truth admission
hostiles=[]
for name in ('premature-root','remove-physical-prerequisite','untyped-deferral','stale-frontier'):
    bad=copy.deepcopy(c); b={n['id']:n for n in bad['conjectures']}
    if name=='premature-root': b['common-event-sourced-control-realization'].update(status='resolved',verdict='constructed',evidence=['wg'])
    elif name=='remove-physical-prerequisite': b['same-source-control-comparison']['depends_on']=['mathematical-control-realization']
    elif name=='untyped-deferral': del b['physical-control-binding']['blocker']
    else: bad['frontier']=['same-source-control-comparison']
    try: v.validate(bad,pins)
    except ValueError: hostiles.append(name)
    else: raise AssertionError('accepted hostile '+name)
out={'schema':'marici.sontag.event-control-transition-proposal.v1','applied':False,
 'owner':'marici.Nima','requires_owner_review':True,'base_contract':CONTRACT,'base_sha256':v.sha(CONTRACT),
 'proposed_transitions':proposal,
 'physical_deferral':{'node':'physical-control-binding','blocker':physical['blocker'],'reopening_condition':physical['reopening_condition']},
 'coverage_disposition':'preparatory evidence only; remains open',
 'projected_frontier':c['frontier'],'projected_recommended_start':c['recommended_start'],
 'no_actionable_frontier_reason':'if owner accepts scoped transitions, further positive net progress awaits physical operation package',
 'validation':'owner structural validator passed on in-memory simulation only',
 'rejected_corruption_controls':hostiles,
 'source_pins_for_review':pins['source_sha256'],'passed':True}
path=ROOT/'research/sontag/results/event-control-transition-proposal-v1.json'
path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'applied':False,'proposed_transitions':len(proposal),'projected_frontier':c['frontier'],'rejected_controls':len(hostiles)},indent=2))
