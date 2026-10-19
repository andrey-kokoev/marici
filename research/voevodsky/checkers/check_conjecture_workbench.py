"""Dependency-aware conjecture workbench: action cards, blockers and live ranking.
--record initializes cards once; normal runs preserve estimates and card edits.
"""
import argparse
import copy
import json
from pathlib import Path
from check_conjecture_test_planning import ROOT, PATHS, MODEL, load, sha, validate, require

CARDS = 'research/conjecture_net/contracts/conjecture-action-cards.v10.json'
REPORT = 'research/voevodsky/results/conjecture-workbench-v1.json'
DASHBOARD = 'research/conjecture_net/WORKBENCH.md'
REUSE = {
 'rh:rh-stage-dictionary': [
  'research/strominger/wg-software-operations-composition-prior-search.md',
  'research/strominger/wg-transport-packet-geometry-prior-search.md',
  'research/strominger/wg-I-squared-rehydration-correction.md',
  'research/strominger/wg-half-phase-prior-research-search.md'],
 'rh:channel-carrier-source-map': ['research/strominger/wg-transport-packet-geometry-prior-search.md'],
 'rh:one-dimensional-source-selection': ['research/strominger/wg-transport-packet-geometry-prior-search.md'],
 'rh:successor-form-candidate': ['research/voevodsky/source-weil-pullback-falsifier-v1.md', 'research/voevodsky/rotor-prime-signature-v1.md'],
 'math:stagewise-mathematical-interface': ['research/strominger/wg-software-operations-composition-prior-search.md', 'research/strominger/wg-I-squared-rehydration-correction.md'],
 'parent:formulation-and-quantifiers': ['research/conjecture_net/COMMON-FOUNDATIONS.md'],
 'compatibility:common-witness-comparison-interface': ['research/strominger/energy-task-reduction.md']}


def index(nets):
    return {a+':'+n['id']:n for a,c in nets.items() for n in c['conjectures']}


def blockers(key, by, nets):
    n=by[key];alias=key.split(':',1)[0];result=[]
    for dep in n['depends_on']:
        d=by[alias+':'+dep];needed=n.get('required_verdicts',{}).get(dep)
        if d['status']!='resolved' or (needed and d.get('verdict')!=needed):
            result.append({'id':alias+':'+dep,'gate':'constructed_witness' if needed else 'resolved_research_prerequisite',
                           'status':d['status'],'verdict':d.get('verdict','open')})
    for req in n.get('requires',[]):
        if req not in nets[alias].get('interfaces',[]):
            result.append({'id':'external:'+req,'gate':'reviewed_external_witness','status':'open','verdict':'open'})
    return result


def initial_cards(nets):
    by=index(nets);cards=[]
    artifacts={a['id']:a for a in nets['rh']['artifacts']}
    for key,n in by.items():
        if n['status']!='open':continue
        alias=key.split(':',1)[0];references=list(REUSE.get(key,[]))
        if alias=='rh':
            for dep in n['depends_on']:
                for aid in by[alias+':'+dep]['evidence']:
                    references.append(artifacts[aid]['note'])
        references=list(dict.fromkeys(references))
        cards.append({'id':key,'first_action':n.get('next_action','Specify one bounded review against the recorded acceptance and falsifier.'),
            'deliverable':n.get('deliverable','Scoped witness or counterexample report, including unresolved obligations.'),
            'acceptance':n['acceptance'],'falsifier':n['falsifier'],
            'reuse_sources':references,
            'reuse_policy':'Read and bind existing constructions before creating new generic machinery. A source-search note is a pointer, not a proof import.',
            'stop_rule':'Stop at an acceptance witness, a scoped counterexample, or the effort budget. Retain source provenance; do not resolve a node from readout agreement alone.',
            'review_promotion':'Record evidence and request scoped verdict review; this card grants no task claim or outcome admission.'})
    cards_by={r['id']:r for r in cards}
    if 'rh:rh-stage-dictionary' in cards_by:
        cards_by['rh:rh-stage-dictionary']['first_action']='Build the stable stage/map/cell inventory from existing typed composition/recovery modules and RH maps. Record source choices and owner audits; inventory is not a transport proof.'
    return {'schema':'marici.conjecture-action-cards.v1','cards':cards,
        'source_sha256':{p:sha(p) for p in PATHS.values()},
        'scope':'Executable research guidance for the open nodes, not new proof outcomes or authority.'}


def validate_cards(cards,nets,paths=None):
    paths=PATHS if paths is None else paths
    by=index(nets);rows={r['id']:r for r in cards['cards']}
    require(cards['schema']=='marici.conjecture-action-cards.v1','card schema')
    require(cards['source_sha256']=={p:sha(p) for p in paths.values()},'card source drift')
    require(len(rows)==len(cards['cards']) and set(rows)=={k for k,n in by.items() if n['status']=='open'},'card coverage')
    for key,r in rows.items():
        require(r['acceptance']==by[key]['acceptance'] and r['falsifier']==by[key]['falsifier'],'gate drift')
        require(all(r[k] for k in ('first_action','deliverable','stop_rule','reuse_policy','review_promotion')),'empty action card')
        require(len(r['reuse_sources'])==len(set(r['reuse_sources'])),'duplicate reuse source')
        for p in r['reuse_sources']:
            require((ROOT/p).resolve().is_relative_to(ROOT) and (ROOT/p).is_file(),'missing/external reuse source')
    return rows


def build(nets,planning,cards,*,paths=None,source_paths=None):
    paths=PATHS if paths is None else paths
    validate(planning,nets,paths);card_rows=validate_cards(cards,nets,paths)
    by=index(nets);est={r['id']:r for r in planning['conjectures']}
    successors={k:[] for k in by}
    for key,n in by.items():
        a=key.split(':',1)[0]
        for d in n['depends_on']:successors[a+':'+d].append(key)
    rows=[]
    for key,n in by.items():
        if n['status']!='open':continue
        blocked=blockers(key,by,nets);r=est[key];p=r['probability'];c=r['test_cost']
        score=None
        if p['status']==c['status']=='estimated' and c['assistant_effort_units']>0:
            score=(p['values']['accepted']+p['values']['rejected'])/c['assistant_effort_units']
        # A construction versus a rejection can unlock different gates.
        construction=copy.deepcopy(by);construction[key].update(status='resolved',verdict='constructed')
        rejection=copy.deepcopy(by);rejection[key].update(status='resolved',verdict='rejected')
        opens=[k for k,v in by.items() if v['status']=='open' and k!=key and blockers(k,by,nets)]
        unlock_c=[k for k in opens if not blockers(k,construction,nets)]
        unlock_r=[k for k in opens if not blockers(k,rejection,nets)]
        visited=set();queue=list(successors[key])
        while queue:
            k=queue.pop()
            if k not in visited:visited.add(k);queue.extend(successors[k])
        rows.append({'id':key,'ready':not blocked,'blockers':blocked,'probability':p['values'],
            'assistant_effort_units':c['assistant_effort_units'],
            'decisive_result_per_effort':None if score is None else round(score,6),
            'direct_dependents':successors[key],'downstream_open_nodes':sorted(k for k in visited if by[k]['status']=='open'),
            'would_unlock_if_constructed':unlock_c,'would_unlock_if_rejected':unlock_r,
            'action_card':card_rows[key]})
    frontier=sorted((r for r in rows if r['ready']),key=lambda r:(r['decisive_result_per_effort'] is None,-(r['decisive_result_per_effort'] or 0),r['id']))
    recommend=next((r['id'] for r in frontier if r['decisive_result_per_effort'] is not None),None)
    goals={a+':'+n['objective']['target'] for a,n in nets.items()}
    goals.update('rh:'+p['target'] for p in nets.get('rh',{}).get('branch_projections',[]))
    goal_frontiers={}
    for goal in sorted(goals):
        ancestors=set();queue=[goal]
        while queue:
            k=queue.pop()
            if k in ancestors:continue
            ancestors.add(k);alias=k.split(':',1)[0]
            queue.extend(alias+':'+d for d in by[k]['depends_on'])
        ready=[r for r in frontier if r['id'] in ancestors]
        goal_frontiers[goal]={'ready_tasks':[r['id'] for r in ready],
            'recommendation':next((r['id'] for r in ready if r['decisive_result_per_effort'] is not None),None),
            'remaining_open_nodes':sorted(k for k in ancestors if by[k]['status']=='open')}
    return {'schema':'marici.conjecture-workbench.v1','passed':True,
        'recommendation':recommend,'strategic_rh_form_priority':nets.get('rh',{}).get('recommended_start','not applicable'),
        'score':'Probability of a decisive bounded-test result / assistant effort; subjective triage, not information gain or theorem probability.',
        'dependency_policy':'Local declared prerequisites only. Cross-net contribution/review links do not automatically discharge or block these gates; see the port model.',
        'unlock_policy':'Hypothetical single reviewed disposition with other statuses held fixed. Unlocked means runnable, not proved. Research prerequisites accept a resolved rejection; constructed-witness gates do not.',
        'coverage':{'open_action_cards':len(rows),'ready_tasks':len(frontier),'blocked_tasks':sum(not r['ready'] for r in rows)},
        'reuse_index_gaps':[r['id'] for r in rows if not r['action_card']['reuse_sources']],
        'frontier':frontier,'blocked':[r for r in rows if not r['ready']],
        'goal_frontiers':goal_frontiers,
        'source_sha256':{p:sha(p) for p in (source_paths if source_paths is not None else [*paths.values(),MODEL,CARDS,'research/conjecture_net/contracts/math-rh-port-connections.v10.json',Path(__file__).relative_to(ROOT).as_posix()])}}


def render(r):
    out=['# Conjecture workbench','', 'Generated from current contracts, estimates and reviewed action cards. Do not edit this view; edit the corresponding machine input and rerun the checker.', '',
         '**Next efficiency recommendation:** `'+str(r['recommendation'])+'`.',
         '**Strategic RH form priority:** `'+r['strategic_rh_form_priority']+'` (a different criterion).','',
         r['score'],'', '| Ready task | Effort | Decisive probability | Score | Opens after construction |', '|---|---:|---:|---:|---|']
    for x in r['frontier']:
        p=x['probability'];prob='unknown' if p is None else f"{100*(p['accepted']+p['rejected']):.0f}%"
        out.append(f"| `{x['id']}` | {x['assistant_effort_units']} | {prob} | {x['decisive_result_per_effort']} | {', '.join(x['would_unlock_if_constructed']) or 'none immediately'} |")
    out+=['','## Goal-directed recommendations','',
        'Within declared local prerequisite ancestry only; cross-net contributions are not automatic proof gates.','']
    for goal,g in r['goal_frontiers'].items():
        out.append('- `'+goal+'`: next `'+str(g['recommendation'])+'`; '+str(len(g['remaining_open_nodes']))+' open nodes in local prerequisite closure.')
    out+=['','## Ready action cards','']
    for x in r['frontier']:
        c=x['action_card'];out+=['### '+x['id'],'',c['first_action'],'','**Deliverable:** '+c['deliverable'],'','**Acceptance:** '+c['acceptance'],'','**Falsifier:** '+c['falsifier'],'','**Reuse:**']
        out += ['- ['+p+'](../../'+p+')' for p in c['reuse_sources']] or ['- No specific source indexed yet; inspect the node evidence and dependency cards.']
        out+=['','**After rejection, runnable:** '+(', '.join(x['would_unlock_if_rejected']) or 'none immediately')+'.','']
    out+=['## Blocked tasks','']
    for x in r['blocked']:
        out.append('- `'+x['id']+'`: '+ '; '.join('`'+b['id']+'` ['+b['gate']+']' for b in x['blockers']))
    out+=['','## Source-reuse index gaps','',
        'These cards lack indexed prior sources; search before building new machinery. Empty indexing is not an absence theorem.','']
    out+=['- `'+k+'`' for k in r['reuse_index_gaps']]
    out+=['','## Boundaries','',r['dependency_policy'],r['unlock_policy'],'',
        'Scores do not include downstream scientific value. Small subjective score differences are not robust. No source claim or formal outcome admission is granted.', '',
        'Machine inputs: [action cards](contracts/conjecture-action-cards.v10.json), [estimates](contracts/conjecture-test-planning.v10.json), [port connections](contracts/math-rh-port-connections.v10.json), [RH stages](contracts/rh-stage-dictionary.v1.json).',
        'Run: `python research/voevodsky/checkers/check_conjecture_workbench.py`.', '']
    return '\n'.join(out)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--record',action='store_true')
    parser.add_argument('--programme',choices=('foundations','low-energy','high-energy','hodge'),default='foundations')
    parser.add_argument('--check',action='store_true',help='verify a scattering or Hodge generated view without writing')
    args=parser.parse_args()
    if args.programme == 'hodge':
        from plan_hodge import main as hodge_main
        hodge_main((['--record'] if args.record else []) + (['--check'] if args.check else []))
        return
    if args.programme in ('low-energy','high-energy'):
        import subprocess
        import sys
        command=[sys.executable,str(ROOT/'research/conjecture_net/plan_low_energy.py'),'--programme',args.programme]
        if args.record:command.append('--record')
        if args.check:command.append('--check')
        subprocess.run(command,check=True)
        return
    if args.check:parser.error('--check currently applies to scattering programmes')
    nets={k:load(p) for k,p in PATHS.items()};planning=load(MODEL)
    if args.record:
        require(not (ROOT/CARDS).exists(),'refusing implicit card overwrite')
        (ROOT/CARDS).write_text(json.dumps(initial_cards(nets),indent=2)+'\n',encoding='utf-8')
    cards=load(CARDS);report=build(nets,planning,cards)
    controls=[]
    for mode in ('missing-card','stale-gate','missing-reuse-source','stale-card-source'):
        bad=copy.deepcopy(cards)
        if mode=='missing-card':bad['cards'].pop()
        elif mode=='stale-gate':bad['cards'][0]['acceptance']='invented'
        elif mode=='missing-reuse-source':bad['cards'][0]['reuse_sources']=['research/not-a-source.md']
        else:bad['source_sha256'][next(iter(PATHS.values()))]='0'*64
        try:validate_cards(bad,nets)
        except ValueError:controls.append(mode)
        else:raise AssertionError('corruption accepted: '+mode)
    by=index(nets)
    # Rejecting a required construction must never unlock assembly.
    fake=copy.deepcopy(by);fake['rh:rh-stagewise-interface'].update(status='resolved',verdict='rejected')
    require(blockers('rh:rh-math-assembly',fake,nets),'rejection promoted to construction')
    fake['rh:rh-stagewise-interface']['verdict']='constructed'
    require(not blockers('rh:rh-math-assembly',fake,nets),'construction gate not recognized')
    child_ids={'rh-stage-dictionary','rh-operation-composition-squares','rh-identity-continuation-transport','rh-analytic-domain-completion-transport'}
    parent=by['rh:rh-stagewise-interface']
    require(set(parent['depends_on'])==child_ids and parent['required_verdicts']==dict.fromkeys(child_ids,'constructed'),'split assembly bypass')
    fake=copy.deepcopy(by)
    for child in child_ids:fake['rh:'+child].update(status='open',verdict='open')
    fake['rh:rh-stage-dictionary'].update(status='resolved',verdict='constructed')
    require(blockers('rh:rh-stagewise-interface',fake,nets),'inventory alone closes parent')
    for child in child_ids:fake['rh:'+child].update(status='resolved',verdict='constructed')
    require(not blockers('rh:rh-stagewise-interface',fake,nets),'split witnesses fail assembly gate')
    for child in child_ids:
        rival=copy.deepcopy(fake);rival['rh:'+child]['verdict']='rejected'
        require(blockers('rh:rh-stagewise-interface',rival,nets),'rejected child satisfies assembly')
    fake=copy.deepcopy(by)
    require(any(b['id']=='external:reviewed-root-assembly' for b in blockers('parent:common-foundations',fake,nets)),'external root gate missing')
    controls+=['rejection-does-not-unlock-construction','construction-unlocks-declared-gate','external-root-review-remains-blocked','split-four-constructed-inputs-required','dictionary-alone-does-not-close-parent','each-rejected-child-blocks-assembly']
    changed=copy.deepcopy(planning)
    ready_ids={r['id'] for r in report['frontier']}
    for r in changed['conjectures']:
        if r['id'] in ready_ids:
            r['test']['protocol_status']='specified'
            r['probability'].update(status='estimated',values={'accepted':.5,'rejected':.3,'inconclusive':.2},basis='synthetic ranking fixture',conditioning='synthetic',uncertainty='synthetic')
            r['test_cost'].update(status='estimated',assistant_effort_units=10,basis='synthetic ranking fixture')
    winner=build(nets,changed,cards)['recommendation']
    next(r for r in changed['conjectures'] if r['id']==winner)['test_cost']['assistant_effort_units']=100
    require(build(nets,changed,cards)['recommendation']!=winner,'ranking ignores live estimates')
    unknown=copy.deepcopy(planning)
    for r in unknown['conjectures']:
        if r['probability']['status']!='not_applicable':
            r['probability'].update(status='unknown',values=None,basis=None)
            r['test_cost'].update(status='unknown',assistant_effort_units=None,basis=None)
    require(build(nets,unknown,cards)['recommendation'] is None,'unknown estimates ranked numerically')
    controls+=['ranking-reacts-to-live-estimates','unknown-estimates-have-no-numeric-recommendation']
    ready_ids={r['id'] for r in report['frontier']}
    for goal,g in report['goal_frontiers'].items():
        require(set(g['ready_tasks']) <= ready_ids,'goal recommends blocked task')
        if g['recommendation'] is not None:require(g['recommendation'] in g['ready_tasks'],'recommendation outside goal ancestry')
    controls+=['goal-frontiers-only-use-ready-local-ancestors']
    report['validation_controls']=controls
    # Keep the older ranking path as a derived projection, not a second algorithm.
    def ranking_row(r):
        return {k:r[k] for k in ('id','assistant_effort_units','probability','decisive_result_per_effort')} | {'unmet_prerequisites':[b['id'] for b in r['blockers']]}
    rh=next((r['id'] for r in report['frontier'] if r['id'].startswith('rh:') and r['decisive_result_per_effort'] is not None),None)
    ranking={'schema':'marici.conjecture-next-test-ranking.v1','estimates_are_subjective':True,
        'recommended_next':report['recommendation'],'rh_recommended_next':rh,
        'existing_rh_recorded_recommended_start':report['strategic_rh_form_priority'],
        'score_definition':report['score'],'limitations':report['dependency_policy']+' '+report['unlock_policy'],
        'goal_frontiers':report['goal_frontiers'],
        'executable_frontier':[ranking_row(r) for r in report['frontier']],
        'blocked_tasks':[ranking_row(r) for r in report['blocked']],
        'source_sha256':report['source_sha256']}
    (ROOT/'research/voevodsky/results/conjecture-next-test-ranking-v1.json').write_text(json.dumps(ranking,indent=2)+'\n',encoding='utf-8')
    (ROOT/REPORT).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (ROOT/DASHBOARD).write_text(render(report),encoding='utf-8')
    print(json.dumps({'passed':True,'recommendation':report['recommendation'],'coverage':report['coverage'],'validation_controls':controls},indent=2))


if __name__=='__main__':main()
