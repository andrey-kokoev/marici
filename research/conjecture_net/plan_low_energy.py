"""Adapt low-energy propositions to the existing shared test planner/workbench.

--record explicitly elicits initial forecasts/cards once; normal runs preserve them.
No registry outcomes or physical target admissions are made.
"""
import argparse
import copy
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
import check_conjecture_test_planning as planning
import check_conjecture_workbench as workbench

CONTRACT='research/scattering/low-energy/contracts/low-energy-scattering-conjectures.v6.json'
PATHS={'low-energy':CONTRACT}
ESTIMATES='research/conjecture_net/contracts/low-energy-test-planning.v4.json'
CARDS='research/conjecture_net/contracts/low-energy-action-cards.v4.json'
REPORT='research/conjecture_net/results/low-energy-workbench.v1.json'
DASHBOARD='research/conjecture_net/LOW-ENERGY-WORKBENCH.md'
ALIAS='low-energy'


def configure_high_energy():
    global CONTRACT,PATHS,ESTIMATES,CARDS,REPORT,DASHBOARD,ALIAS
    ALIAS='high-energy'
    CONTRACT='research/scattering/high-energy/contracts/high-energy-scattering-conjectures.v2.json'
    PATHS={ALIAS:CONTRACT}
    ESTIMATES='research/conjecture_net/contracts/high-energy-test-planning.v2.json'
    CARDS='research/conjecture_net/contracts/high-energy-action-cards.v2.json'
    REPORT='research/conjecture_net/results/high-energy-workbench.v2.json'
    DASHBOARD='research/conjecture_net/HIGH-ENERGY-WORKBENCH.md'


def adapt(source):
    nodes=[]
    for n in source['conjectures']:
        deps=[e['from'] for e in source['edges'] if e['to']==n['id'] and e['kind']=='premise']
        settled=n['status'] in ('established','refuted')
        nodes.append({**n,'status':'resolved' if settled else 'open',
                      'verdict':('constructed' if n['status']=='established' else 'rejected') if settled else 'open',
                      'depends_on':deps,'required_verdicts':dict.fromkeys(deps,'constructed'),
                      'acceptance':n['statement']+' Quantified scope: '+n['quantifiers']})
    return {ALIAS:{'conjectures':nodes,'interfaces':[],
                   'objective':source.get('objective',{'target':'no-four-mode-single-excitation-port-embedding'})}}


def record(nets):
    model=planning.initial(nets,PATHS);cards=[]
    # Explicit assistant forecasts of bounded-test outcomes, not calibrated
    # truth probabilities. These are editable inputs, not hard-coded ranks.
    attempts={
        'C2':(4,(.50,.05,.45),'Derive the finite-rank resolvent spectral decomposition, treating both band edges. Stop at a complete outgoing-completeness argument, counterexample, or four effort units.'),
        'C5':(1,(.90,.02,.08),'Given a reviewed C2 proof, verify the ordered time/region retention limit and source overlap witnesses. Stop at proof, counterexample, or one unit.'),
        'C6':(1,(.90,.02,.08),'Given the C1/C2 prerequisites, verify the metric-whitened Householder threshold comparison and common-phase obstruction. Stop at proof, counterexample, or one unit.'),
        'C7':(.5,(.98,.01,.01),'Given C2 outgoing multiplicity three, verify the rank-four target obstruction without changing particle sector or energy fiber. Stop at proof, counterexample, or half a unit.'),
        'C8':(1,(.10,.80,.10),'Construct the fixed macro-return D from the pinned paths. Test the target spectral multiplicities first; if they pass, test metric/reducing identities within one unit. Missing target multiplicity rejects; spectra alone never accept. Stop at witness, exact obstruction, or budget.')}
    if ALIAS=='high-energy':
        estimates={'H1':(1,(.90,.02,.08),'Small exact source matrix replay.'),
                   'H2':(1,(.85,.05,.10),'Finite ordered block/path comparison, conditional on local identities.'),
                   'H3':(1,(.90,.02,.08),'Finite encoder replay and transported continuation; actual H_F identification excluded.'),
                   'H4':(2,(.80,.02,.18),'H1 trace estimates and finite positive forms; domain review can be inconclusive.'),
                   'H5':(2,(.80,.05,.15),'Discrete continuity derivation and retained cross-term review.'),
                   'H6':(6,(.35,.45,.20),'Fresh stationary solves are expensive; the prior 9/17 discrepancy makes stability uncertain.'),
                   'H7':(4,(.40,.15,.45),'Uniform inverse bounds can fail at exceptional energies; finite scans cannot certify.'),
                   'H8':(8,(.25,.15,.60),'Common domain, interpolation and ratio/peak convergence are substantial analytic obligations.'),
                   'H10':(2,(.60,.20,.20),'Fixed finite participant permutation is inexpensive, but chirality and endpoint-frame conventions may obstruct independent reconstruction. Subjective estimate; not evidence of symmetry.')}
        attempts={n['label']:(estimates[n['label']][0],estimates[n['label']][1],n['next_action']+' Stop at a complete scoped witness, counterexample, or '+str(estimates[n['label']][0])+' effort units; missing error/domain certification is inconclusive.') for n in nets[ALIAS]['conjectures'] if n['status']!='resolved'}
    if ALIAS=='low-energy':
        for n in nets[ALIAS]['conjectures']:
            if n['label']=='C12':attempts['C12']=(2,(.4,.2,.4),n['next_action'])
    by=workbench.index(nets)
    for r in model['conjectures']:
        n=by[r['id']]
        if n['status']=='resolved':continue
        cost,probs,action=attempts[n['label']]
        basis='Assistant elicitation at scattering workbench integration; versioned initial assessment, not calibrated data. '+(estimates[n['label']][2] if ALIAS=='high-energy' else ('Small exact finite matrix test with a necessary eigenvalue-1 multiplicity check.' if n['label']=='C8' else 'Analytic complexity and prerequisite-conditioned proof/review scope.'))
        r['test'].update(protocol_status='specified',next_action=action)
        r['probability'].update(status='estimated',values=dict(zip(planning.OUTCOMES,probs)),
            conditioning='Declared sources available; required positive prerequisites reviewed for blocked tasks.',
            uncertainty='Subjective forecast; spectral surprises and analytic gaps can change it. Not independent across tests.',basis=basis)
        r['test_cost'].update(status='estimated',assistant_effort_units=cost,basis=basis)
        cards.append({'id':r['id'],'first_action':action,'deliverable':'Scoped proof or exact counterexample, with a certificate and proposition-status update; otherwise explicit inconclusive report.',
            'acceptance':n['acceptance'],'falsifier':n['falsifier'],'reuse_sources':n['sources'],
            'reuse_policy':'Use pinned source operators, metrics and clocks; do not introduce fitted dynamics.',
            'stop_rule':action,'review_promotion':'This planning record grants no physical admission or independent outcome authority.'})
    from datetime import datetime, timezone
    model['elicited_at']=datetime.now(timezone.utc).isoformat()
    model['elicitor']='assistant; subjective bounded-test forecasts, operator-reviewable'
    return model,{'schema':'marici.conjecture-action-cards.v1','source_sha256':{p:planning.sha(p) for p in PATHS.values()},'cards':cards}


def run(model,cards,source):
    nets=adapt(source)
    paths=[CONTRACT,ESTIMATES,CARDS,'research/conjecture_net/plan_low_energy.py',
           'research/voevodsky/checkers/check_conjecture_workbench.py',
           'research/voevodsky/checkers/check_conjecture_test_planning.py']
    report=workbench.build(nets,model,cards,paths=PATHS,source_paths=paths)
    report['adapter_scope']={'established':'resolved/constructed for planning only',
        'refuted':'resolved/rejected for planning only','conditional':'open, with positive-premise blockers',
        'nonblocking_edges':[e for e in source['edges'] if e['kind']!='premise'],
        'physical_target_or_central_registry_outcome_changed':False}
    if ALIAS=='high-energy':
        by=workbench.index(nets);h1=ALIAS+':local-full-spinor-switch';h2=ALIAS+':ordered-switch-composition'
        assert not workbench.blockers(h1,by,nets)
        rival=copy.deepcopy(by);rival[h1].update(status='open',verdict=None)
        assert workbench.blockers(h2,rival,nets)
        rival[h1].update(status='resolved',verdict='rejected')
        assert workbench.blockers(h2,rival,nets)
        rival[h1]['verdict']='constructed';assert not workbench.blockers(h2,rival,nets)
        changed=copy.deepcopy(model);chosen=ALIAS+':uniform-corrected-residual-stability'
        for row in changed['conjectures']:
            if row['id']==chosen:
                # Synthetic control must supply its own protocol/estimates;
                # live H7 may have exhausted its budget and be unknown.
                row['test']['protocol_status']='specified'
                row['probability'].update(status='estimated',values={'accepted':.9,'rejected':.05,'inconclusive':.05},basis='synthetic ranking control only',conditioning='synthetic',uncertainty='synthetic')
                row['test_cost'].update(status='estimated',assistant_effort_units=1,basis='synthetic ranking control only')
            elif row['test_cost']['status']=='estimated':row['test_cost']['assistant_effort_units']=1000
        alternate=workbench.build(nets,changed,cards,paths=PATHS,source_paths=paths)
        assert alternate['recommendation']==chosen
        report['integration_controls']=['positive premise blocks','rejection does not supply construction','construction unlocks ordered comparison','ranking responds to estimates']
        return report
    # Test the adapter semantics and the shared engine, not a bespoke ranker.
    by=workbench.index(nets);c8='low-energy:two-tick-macro-factor-carrier'
    assert not workbench.blockers(c8,by,nets)
    c2='low-energy:three-port-asymptotic-completeness'
    c5='low-energy:three-port-bound-retention'
    unreviewed=copy.deepcopy(by);unreviewed[c2].update(status='open',verdict=None)
    assert workbench.blockers(c5,unreviewed,nets)
    rejected=copy.deepcopy(by);rejected[c2].update(status='resolved',verdict='rejected')
    assert workbench.blockers(c5,rejected,nets)
    positive=copy.deepcopy(by);positive[c2].update(status='resolved',verdict='constructed')
    assert not workbench.blockers(c5,positive,nets)
    if all(n['status']=='resolved' for n in by.values()):
        assert report['recommendation'] is None and not report['frontier'] and not report['blocked']
        report['integration_controls']=['resolved target definitions remain nonblocking','rejection does not discharge a positive premise','constructed premise discharges its gate','all resolved yields no fabricated next test']
        return report
    c12='low-energy:pentachoron-bright-threshold-regularity'
    if {key for key,n in by.items() if n['status']=='open'}=={c12}:
        account=next(card for card in cards['cards'] if card['id']==c12)['protocol_accounting']
        ledger=planning.load(account['attempt_record'])
        assert account['initial_effort_units']==ledger['initial_total_effort_units']==2
        assert account['used_effort_units']==ledger['effort_units_used']==1
        assert account['remaining_effort_units']==ledger['remaining_effort_units']==1
        assert ledger['effort_units_used']+ledger['remaining_effort_units']==2
        assert ledger['automatic_renewal_allowed'] is False and ledger['high_energy_protocol_units_used']==0
        for path,h in ledger['source_sha256'].items():assert planning.sha(path)==h,'stale C12 attempt evidence: '+path
        live=next(row for row in model['conjectures'] if row['id']==c12)
        assert live['test_cost']['assistant_effort_units']==1,'remaining C12 effort not reflected in forecast'
        assert report['recommendation']==c12 and not report['blocked']
        unknown=copy.deepcopy(model)
        next(row for row in unknown['conjectures'] if row['id']==c12)['probability'].update(status='unknown',values=None,basis=None,reason='Synthetic control: no elicited forecast available.')
        assert workbench.build(nets,unknown,cards,paths=PATHS,source_paths=paths)['recommendation'] is None
        report['integration_controls']=['resolved target definitions remain nonblocking','rejection does not discharge a positive premise','constructed premise discharges its gate','independent C12 is ready','unknown forecast suppresses numerical ranking','remaining C12 budget and evidence ledger checked without renewal']
        return report
    # Ranking must react to inputs; this synthetic perturbation is never saved.
    changed=copy.deepcopy(model)
    ranking_target=c2 if by[c2]['status']=='open' else c5
    for r in changed['conjectures']:
        if by[r['id']]['status']=='open' and r['test_cost']['status']=='estimated':r['test_cost']['assistant_effort_units']=1000
        if r['id']==ranking_target:
            r['test_cost']['assistant_effort_units']=1
            r['probability']['values']={'accepted':.9,'rejected':.05,'inconclusive':.05}
    expected=ranking_target
    if workbench.blockers(ranking_target,by,nets):
        expected='low-energy:three-port-no-singular-continuous-spectrum'
        for r in changed['conjectures']:
            if r['id']==expected:
                r['test']['protocol_status']='specified'
                r['test_cost'].update(status='estimated',assistant_effort_units=1,basis='synthetic control only')
                r['probability'].update(status='estimated',values={'accepted':.9,'rejected':.05,'inconclusive':.05},basis='synthetic control only',conditioning='synthetic',uncertainty='synthetic')
    alternate=workbench.build(nets,changed,cards,paths=PATHS,source_paths=paths)
    assert alternate['recommendation']==expected
    report['integration_controls']=['C3 rejection does not block successor C8','C2 rejection cannot discharge C5 positive premise','C2 construction unlocks C5','ranking responds to estimates rather than a fixed next-test string']
    return report


def render(r):
    out=['# '+ALIAS.capitalize()+' conjecture workbench','',
         'Generated by the shared conjecture workbench engine. Do not hand-edit ranks.',
         '',f"**Next test: `{r['recommendation']}`**",'',r['score'],'',
         '| Ready proposition | Effort | Decisive forecast | Score |', '|---|---:|---:|---:|']
    for row in r['frontier']:
        p=row['probability'];prob='unknown' if p is None else f"{p['accepted']+p['rejected']:.0%}"
        out.append(f"| {row['id']} | {row['assistant_effort_units']} | {prob} | {row['decisive_result_per_effort']} |")
    out+=['','## Blocked by positive mathematical premises','']
    for row in r['blocked']:out.append('- '+row['id']+': '+', '.join(b['id'] for b in row['blockers']))
    out+=['','## Selected action','']
    selected=next((row for row in r['frontier'] if row['id']==r['recommendation']),None)
    if selected:out+=[selected['action_card']['first_action']]
    out+=['','## Scope','',
          'Forecasts are explicit subjective assistant estimates of this bounded attempt, not theorem probabilities. Scores omit downstream scientific importance. C9–C11 now have dated subjective forecasts and explicit stopping budgets; every open node has an estimate. These estimates can be revised without changing proof status. C2 now requires C9; C6 requires C11 rather than full C2.',
          'Only premise edges impose positive-witness prerequisites. Successor-test and target-definition edges stay in the proposition graph but do not become truth assumptions.',
          'Resolved mathematical claims are excluded from next-test forecasting. The planning adapter does not admit physical outcomes or alter central registry verdicts.',
          '', 'Inputs: [forecasts](contracts/low-energy-test-planning.v1.json), [action cards](contracts/low-energy-action-cards.v1.json), [propositions](../scattering/low-energy/contracts/low-energy-scattering-conjectures.v4.json).',
          '', 'Refresh: `python research/conjecture_net/plan_low_energy.py`; verify: append `--check`.','']
    text='\n'.join(out)
    if ALIAS=='high-energy':
        text=text.replace('low-energy','high-energy').replace('high-energy-test-planning.v1','high-energy-test-planning.v2').replace('high-energy-action-cards.v1','high-energy-action-cards.v2').replace('high-energy-scattering-conjectures.v4','high-energy-scattering-conjectures.v2')
        text=text.replace('C9–C11 now have dated subjective forecasts and explicit stopping budgets; every open node has an estimate. These estimates can be revised without changing proof status. C2 now requires C9; C6 requires C11 rather than full C2.','Every open proposition has a dated subjective forecast and bounded attempt budget. Local coherence is not path independence; no historical result is promoted. Deferred physical bindings are not scored as executable conjectures.')
        text=text.replace('plan_low_energy.py`','plan_low_energy.py --programme high-energy`')
    if ALIAS=='low-energy' and r['recommendation'] is None and not r['frontier'] and not r['blocked']:
        text=text.replace('**Next test: `None`**','**No unresolved proposition in this scoped net.**')
        text=text.replace('C9–C11 now have dated subjective forecasts and explicit stopping budgets; every open node has an estimate. These estimates can be revised without changing proof status. C2 now requires C9; C6 requires C11 rather than full C2.','All eleven scoped propositions have dispositions. This does not close the wider physical or witnessed-construction programme; a successor requires a separately specified proposition.')
    if ALIAS=='low-energy':
        text=text.replace('All eleven scoped propositions','All scoped propositions')
        text=text.replace('low-energy-test-planning.v1','low-energy-test-planning.v4').replace('low-energy-action-cards.v1','low-energy-action-cards.v4').replace('low-energy-scattering-conjectures.v4','low-energy-scattering-conjectures.v6')
        text=text.replace('C9–C11 now have dated subjective forecasts and explicit stopping budgets; every open node has an estimate. These estimates can be revised without changing proof status. C2 now requires C9; C6 requires C11 rather than full C2.','C12 has used one of its original two effort units; one remains for uniform-proof review. Its current subjective forecast and cost condition on that remaining review, not a renewed attempt. The exact threshold-kernel test passed; neither it nor a numerical scan automatically establishes bright regularity. Forecasts can change without altering proof status.')
        text+='\n## Programme coverage is separate\n\nThis planner ranges over C1–C12. C12 was explicitly admitted in v5 and resolved in v6 after two effort units, with zero remaining and no renewal. Coverage rows are not automatically promoted to propositions. A null recommendation does not establish complete low-energy coverage. See the [source-to-proposition matrix](../scattering/low-energy/COVERAGE.md) for all twelve historical obligations and unformulated/deferred gates. Coverage-review questions are not silently added as conjectures or forecasts.\n'
    return text


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--record',action='store_true');parser.add_argument('--check',action='store_true')
    parser.add_argument('--sync-propositions',action='store_true',help='explicitly reconcile gates/coverage; preserve forecasts, new nodes unknown')
    parser.add_argument('--programme',choices=('low-energy','high-energy'),default='low-energy')
    args=parser.parse_args()
    if sum((args.record,args.check,args.sync_propositions))>1:parser.error('record, sync and check are distinct operations')
    if args.programme=='high-energy':configure_high_energy()
    source=planning.load(CONTRACT)
    if args.record:
        if any((ROOT/p).exists() for p in (ESTIMATES,CARDS)):raise SystemExit('Refusing to overwrite estimates/cards')
        model,cards=record(adapt(source))
        for p,obj in ((ESTIMATES,model),(CARDS,cards)):(ROOT/p).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    if args.sync_propositions:
        nets=adapt(source);by=workbench.index(nets)
        model=planning.load(ESTIMATES);cards=planning.load(CARDS)
        old={r['id']:r for r in model['conjectures']};old_cards={r['id']:r for r in cards['cards']}
        initial=planning.initial(nets,PATHS);rows=[];new_cards=[]
        seeded={r['id']:r for r in record(nets)[0]['conjectures']} if ALIAS=='high-energy' else {}
        for fresh in initial['conjectures']:
            key=fresh['id'];n=by[key];r=copy.deepcopy(old.get(key,seeded.get(key,fresh)))
            r['test'].update(acceptance=n['acceptance'],falsifier=n['falsifier'],scope=n.get('scope',n['statement']))
            if n['status']=='resolved':r=fresh
            rows.append(r)
            if n['status']=='resolved':continue
            card=copy.deepcopy(old_cards.get(key,{}))
            action=r['test']['next_action'] if r['test']['protocol_status']=='specified' else n.get('next_action',r['test']['next_action'])
            if n['label']=='C2':action='Given the required C9 input, construct W_+ on the full free three-lead space, prove isometry and range equal to H_ac(H), and verify the five-mode pure-point projection. Derive the central-input asymptote as a corollary. Stop at a complete proof, counterexample, or four effort units.'
            if n['label']=='C6':action='Given C1 and C11, verify the threshold intertwiner contradiction from scalar versus Householder limits. Full C2 completeness is not a prerequisite. Stop at proof, counterexample, or one effort unit.'
            r['test']['next_action']=action
            card.update(id=key,first_action=action,acceptance=n['acceptance'],falsifier=n['falsifier'],reuse_sources=list(dict.fromkeys(n['sources']+card.get('reuse_sources',[]))))
            card.setdefault('deliverable','Exact scoped witness or counterexample; otherwise explicit inconclusive report.')
            card.setdefault('reuse_policy','Preserve the declared source model, metric and operation class.')
            if r['test']['protocol_status']=='specified':card['stop_rule']=action
            else:card.setdefault('stop_rule','Specify a bounded protocol and budget before estimating or executing this new test.')
            card.setdefault('review_promotion','Planning does not grant physical admission or outcome authority.')
            new_cards.append(card)
        model['conjectures']=rows;model['source_sha256']=initial['source_sha256']
        if any(r['id'] not in old and r['probability']['status']=='estimated' for r in rows):
            from datetime import datetime, timezone
            model['estimates_extended_at']=datetime.now(timezone.utc).isoformat()
        cards['cards']=new_cards;cards['source_sha256']=initial['source_sha256']
        for p,obj in ((ESTIMATES,model),(CARDS,cards)):(ROOT/p).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    report=run(planning.load(ESTIMATES),planning.load(CARDS),source)
    for p,text in ((REPORT,json.dumps(report,indent=2)+'\n'),(DASHBOARD,render(report))):
        path=ROOT/p
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8')!=text:raise SystemExit('Stale workbench: '+p)
        else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8')
    print(json.dumps({'recommendation':report['recommendation'],'coverage':report['coverage'],'shared_engine':'check_conjecture_workbench.build','controls':len(report['integration_controls'])}))


if __name__=='__main__':main()
