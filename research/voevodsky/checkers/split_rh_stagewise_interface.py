"""One-time reviewed structural migration; keeps prior pin/sidecar versions.
Run once, then use normal validators. No outcome is promoted.
"""
import copy
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
HOME='research/conjecture_net/contracts/'


def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def save(p,c):(ROOT/p).write_text(json.dumps(c,indent=2)+'\n',encoding='utf-8')


def main():
    path=HOME+'rh-realization-work-net.v1.json';c=load(path)
    by={n['id']:n for n in c['conjectures']}
    assert 'rh-stage-dictionary' not in by,'migration already applied'
    old=copy.deepcopy(by['rh-stagewise-interface'])
    specs=[
      ('rh-stage-dictionary',old['depends_on'],
       'Freeze the stage and comparison-cell inventory for the existing bounded RH realization.',
       'Actual finite coefficient, retained-history, distribution, test-dual and Mellin stages; inventory only, not proof of transport.',
       'Assign stable stage/map/cell IDs; record types, domains, operations, supplied choices, kernels/retained data and evidence pointers. Every required cell has an owner child and explicit open or evidenced state; independent sources are not silently identified.',
       'A stage or cell lacks its actual source/domain, or an inventory entry is counted as a compatibility proof.',
       'Extract the dictionary from existing RH maps and typed WG sources; list operation, continuation and completion cells without constructing another generic framework.',
       'Versioned stage/map/cell dictionary with evidence and unresolved-choice inventory.'),
      ('rh-operation-composition-squares',['rh-stage-dictionary'],
       'Verify the frozen operation and composition comparison cells.',
       'Only generators and compositions enumerated in the dictionary; native extension and Fourier operations remain distinct.',
       'Every required operation/composition cell has a typed commuting witness or an explicitly scoped replacement excluding the falsified candidate. Reuse old-frame leakage and native-tick mismatch controls; no omitted failed cell is marked proved.',
       'A required generator or composition disagrees between routes, or a native tick is silently replaced by Fourier.',
       'Replay finite intertwiners against the frozen cells, then test the first uncovered composition.',
       'Cell-indexed operation/composition witnesses and executable mismatch regressions.'),
      ('rh-identity-continuation-transport',['rh-stage-dictionary'],
       'Verify task-relative identity and licensed continuation transport for the frozen stages.',
       'Fixed observation contexts, retained source data and permitted future operations; no universal equivalence from scalar equality.',
       'Each required identity/continuation cell specifies equivalence, kernel, reconstruction or retained distinctions and transported future witnesses. Test rank-one specialization and an equal-readout/different-future pair. Apply ideal-attachment or half-phase controls only after a documented source binding.',
       'Equal current readouts are identified despite a permitted future distinction, or source-action attachments become unrelated archived coordinates.',
       'Declare task-relative equivalences and compare two retained states with the same Riemann readout; audit applicability of Strominger controls without imposing an unbound carrier.',
       'Cell-indexed identity/continuation witnesses, reconstruction data and counterexample controls.'),
      ('rh-analytic-domain-completion-transport',['rh-stage-dictionary'],
       'Verify domain and completion transport for the frozen analytic comparison cells.',
       'Distribution, test-dual and Mellin transitions under declared conventions; not source-form equality or positivity.',
       'Each required analytic cell declares domain, topology, normalization and map with appropriate continuity, density/extension and limit-transport witnesses. Distinguish supplied analytic choices from carrier-derived laws.',
       'A comparison is used outside its domain, extension changes normalization, or finite agreement substitutes for completion proof.',
       'Inventory existing extension arguments against dictionary cells and audit the first missing domain/topology witness.',
       'Cell-indexed analytic-domain/completion ledger and extension/limit witnesses.')]
    children=[]
    for i,deps,statement,scope,acceptance,falsifier,action,deliverable in specs:
        n=dict(id=i,depends_on=deps,status='open',verdict='open',outcome=None,evidence=[],statement=statement,scope=scope,acceptance=acceptance,falsifier=falsifier,next_action=action,deliverable=deliverable)
        if i!='rh-stage-dictionary':n['required_verdicts']={'rh-stage-dictionary':'constructed'}
        children.append(n)
    ids=[n['id'] for n in children]
    parent=by['rh-stagewise-interface']
    parent.update(depends_on=ids,required_verdicts=dict.fromkeys(ids,'constructed'),
      statement='Assemble and review the four scoped stagewise-interface witnesses for the mathematical branch.',
      scope='One frozen dictionary and compatible maps/domains across all children; reuse existing generic WG composition.',
      acceptance='All four children are constructed; every required dictionary cell is accounted for, and operation, continuation and analytic witnesses agree on overlaps. Review against the mathematical branch interface without inferring universal realization.',
      falsifier='Children use incompatible source/map/domain conventions, a required cell remains unproved, or inventory/rejection substitutes for a constructed witness.',
      next_action='After all four child gates close, compose cell-indexed witnesses and review overlaps; a filled table alone cannot close this parent.',
      deliverable='Reviewed bounded stagewise-interface assembly with four incoming witness references.')
    pos=c['conjectures'].index(parent);c['conjectures'][pos:pos]=children
    p=c['branch_projections'][0];pos=p['focus'].index(parent['id']);p['focus'][pos:pos]=ids
    c['frontier']=[n['id'] for n in c['conjectures'] if n['status']=='open' and all(by.get(d,{'status':'open'})['status']=='resolved' for d in n['depends_on'])]
    oldport=HOME+'math-rh-port-connections.v1.json';newport=HOME+'math-rh-port-connections.v2.json'
    c['context_sources']=[newport if s==oldport else s for s in c['context_sources']]
    c['port_model']=newport;c['source_pins']='research/voevodsky/inputs/rh-realization-work-source-pins.v3.json'
    save(path,c)
    for name in ('common-foundations','mathematical-realization','same-source-compatibility'):
        p=HOME+name+'-conjecture-net.v1.json';b=load(p);b['port_model']=newport
        if name=='common-foundations':b['source_pins']='research/voevodsky/inputs/common-foundations-source-pins.v4.json'
        if name=='mathematical-realization':
            for w in b['work_nets']:w['entry_nodes']=['rh-stage-dictionary' if x=='rh-stagewise-interface' else x for x in w['entry_nodes']]
        save(p,b)
    # Preserve previous planning and card sidecars; create revised inputs.
    planning=load(HOME+'conjecture-test-planning.v1.json')
    r=next(r for r in planning['conjectures'] if r['id']=='rh:rh-stagewise-interface')
    estimates={
      'rh-stage-dictionary':(.80,.05,2,'Existing stages/maps are explicit; principal risk is incomplete indexing or concealed source choices.'),
      'rh-operation-composition-squares':(.65,.20,3,'Finite intertwiners exist, but uncovered compositions may fail.'),
      'rh-identity-continuation-transport':(.50,.30,4,'Retained reconstructions exist; task-relative continuation and attachment binding need review.'),
      'rh-analytic-domain-completion-transport':(.45,.25,5,'Existing analytic constructions help, but domain/topology extension obligations are substantive.'),
      'rh-stagewise-interface':(.75,.15,2,'Conditional on all four constructed children, review overlaps and assemble; no child proof is included in this budget.')}
    for n in children+[parent]:
        x=copy.deepcopy(r);x['id']='rh:'+n['id']
        a,b,e,why=estimates[n['id']]
        x['test'].update(acceptance=n['acceptance'],falsifier=n['falsifier'],scope=n['scope'],next_action=n['next_action'])
        basis=dict(estimator='assistant',date='2026-10-13',method='subjective post-split task-scope elicitation, not calibrated frequency',rationale=why)
        x['probability'].update(values=dict(accepted=a,rejected=b,inconclusive=round(1-a-b,2)),basis=basis)
        x['test_cost'].update(assistant_effort_units=e,basis=basis)
        if n['id']==parent['id']:planning['conjectures'][planning['conjectures'].index(r)]=x
        else:planning['conjectures'].append(x)
    cards=load(HOME+'conjecture-action-cards.v1.json');r=next(r for r in cards['cards'] if r['id']=='rh:rh-stagewise-interface')
    for n in children+[parent]:
        x=copy.deepcopy(r);x.update(id='rh:'+n['id'],first_action=n['next_action'],deliverable=n['deliverable'],acceptance=n['acceptance'],falsifier=n['falsifier'])
        if n['id']==parent['id']:cards['cards'][cards['cards'].index(r)]=x
        else:cards['cards'].append(x)
    from hashlib import sha256
    for m in (planning,cards):
        m['source_sha256']={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in m['source_sha256']}
    save(HOME+'conjecture-test-planning.v2.json',planning)
    save(HOME+'conjecture-action-cards.v2.json',cards)
    print('Split recorded: 4 new children; parent remains open. Previous sidecars and pins retained.')


if __name__=='__main__':main()
