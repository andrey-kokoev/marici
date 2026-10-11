"""Compile the current route into the EXISTING sequential and objective engines.

No scientific certificates are created: all transitions are planning scenarios.
"""
from pathlib import Path
import hashlib
import json
import math
import sys
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(REPO/'research/conjecture_net'))
from interpretation_planner import Action, Branch, Decoder, Effect, Implication, Planner, State, OUTCOMES
from objective_projection import ActionAssessment, Objective, ObjectiveKind, recommend

CONTRACT = ROOT/'contracts/current-problem-closure-planning.v1.json'
ESTIMATES = ROOT/'contracts/current-problem-bridge-planning.v1.json'

def load():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'))
    old=json.loads(ESTIMATES.read_text(encoding='utf-8'))
    by_id={b['id']:b for b in old['bridges']}
    ranges={}
    for stage in c['stages']:
        if 'estimate_ref' in stage:
            b=by_id[stage['estimate_ref']]
            e={'prior_true':b['prior_true'], 'prove_cost':b['prove']['cost_effort_units'],
               'prove_q':b['prove']['success_given_truth'], 'reject_cost':b['reject']['cost_effort_units'],
               'reject_q':b['reject']['success_given_falsehood']}
        else:
            e=stage['estimate']
        for key,value in e.items():
            ranges[stage['id']+'/'+key]=value
    return c,ranges

def compile_model(c,params):
    actions=[]
    for s in c['stages']:
        sid=s['id']; ticket='unattempted/'+sid
        for intent in ('prove','reject'):
            prefix=sid+'/'+intent
            if prefix+'_cost' not in params:
                continue
            p=params[sid+'/prior_true']; q=params[prefix+'_q']
            success=p*q if intent=='prove' else (1-p)*q
            conclusive,inconclusive=('++','+-') if intent=='prove' else ('-+','--')
            branches={}
            for outcome in OUTCOMES:
                probability=success if outcome==conclusive else (1-success if outcome==inconclusive else 0)
                positive=outcome=='++' and intent=='prove'
                added=frozenset(s['adds_on_proof']) if positive else frozenset()
                removed=frozenset({ticket}) if positive else frozenset({ticket,'route-live'})
                raw='certified/'+sid if positive else None
                effect=Effect(add=added,remove=removed,raw=raw)
                # These are hypothetical branch implications, not imported evidence.
                rules=tuple(Implication(f'{prefix}={outcome}','entails',name) for name in added)
                if not rules:
                    rules=(Implication(f'{prefix}={outcome}','blocks','current-one-attempt-portfolio'),)
                branches[outcome]=Branch(probability,effect,rules)
            actions.append(Action(prefix,params[prefix+'_cost'],frozenset(s['requires'])|{ticket,'route-live'},branches))
    d=c['decoder']; target=c['objective']['target']
    decoder=Decoder(d['stage']+'/prove','certified/'+d['stage'],frozenset(d['requires']),target)
    initial=State(frozenset({'current-route'}),frozenset(c['initial_interfaces'])|frozenset('unattempted/'+s['id'] for s in c['stages']))
    for observation in c.get('observed_attempts',[]):
        action=next(a for a in actions if a.name==observation['action'])
        if not action.available(initial):
            raise ValueError('Observed action was not available: '+action.name)
        branch=action.branches[observation['outcome']]
        if branch.probability==0:
            raise ValueError('Observed outcome contradicts this planning model')
        initial=branch.effect.apply(initial.resolve(action.name,observation['outcome'])).derive(branch.implications,assume_branch_premises=True)
        actions=[a for a in actions if a.name!=action.name]
    return actions,[decoder],initial

def solve(c,params,frontier=False):
    actions,decoders,initial=compile_model(c,params)
    target=c['objective']['target']
    value=Planner(actions,decoders,target,require_implications=True).solve_expected(initial)
    result={'first_action':value.first_action,'success_probability':value.success,'expected_total_effort':value.expected_cost}
    if frontier:
        rows=[]
        for action in actions:
            if not action.available(initial):
                continue
            success=0.; cost=action.cost
            remaining=[a for a in actions if a.name!=action.name]
            for outcome,b in action.branches.items():
                if not b.probability:
                    continue
                ns=b.effect.apply(initial.resolve(action.name,outcome)).derive(b.implications,assume_branch_premises=True)
                done=any(d.decode(action.name,b.effect.raw,ns)==target for d in decoders)
                if done:
                    success+=b.probability
                else:
                    child=Planner(remaining,decoders,target,require_implications=True).solve_expected(ns)
                    success+=b.probability*child.success
                    cost+=b.probability*child.expected_cost
            rows.append({'action':action.name,'success_probability':success,'expected_total_effort':cost})
        # Same objective projection over sequentially computed values, not local IG.
        assessments=[ActionAssessment(r['action'],frozenset({target}),r['expected_total_effort'],
                     sum(a.cost for a in actions),r['success_probability']) for r in rows]
        obj=Objective(c['objective']['name'],ObjectiveKind.SCIENTIFIC_TARGET,target,c['objective']['functional'])
        projection=recommend(obj,assessments)
        result['executable_first_action_values']=rows
        result['objective_projection']={'action':projection.action,'reason':projection.reason}
        # Report the computed policy's all-success spine, not a hand-written order.
        pending=list(actions); state=initial; spine=[]
        while pending:
            step=Planner(pending,decoders,target,require_implications=True).solve_expected(state)
            if step.first_action is None:
                break
            action=next(a for a in pending if a.name==step.first_action)
            branch=action.branches['++']
            if branch.probability==0:
                break
            spine.append({'action':action.name,'effort':action.cost})
            state=branch.effect.apply(state.resolve(action.name,'++')).derive(branch.implications,assume_branch_premises=True)
            if any(d.decode(action.name,branch.effect.raw,state)==target for d in decoders):
                break
            pending=[a for a in pending if a.name!=action.name]
        result['all_success_policy_spine']=spine
        result['all_success_path_effort']=sum(step['effort'] for step in spine)
    return result

def main():
    c,ranges=load(); central={k:v[1] for k,v in ranges.items()}
    checks=[]
    def require(name,condition):
        if not condition: raise AssertionError(name)
        checks.append(name)
    for key,v in ranges.items():
        require('ordered/'+key,len(v)==3 and all(math.isfinite(x) for x in v) and v[0]<=v[1]<=v[2])
        require('domain/'+key,v[0]>0 if key.endswith('_cost') else 0<=v[0]<=v[2]<=1)
    actions,decoders,initial=compile_model(c,central)
    observed=c.get('observed_attempts',[])
    require('directional-actions-account-for-observations',len(actions)==9-len(observed))
    if observed:
        for observation in observed:
            receipt=json.loads((REPO/observation['receipt']).read_text(encoding='utf-8'))
            require('observed-audit-evidence',receipt['status']=='pass' and receipt['fresh_dependency_check']
                    and receipt['audit_stage_outcome']==observation['outcome'] and not receipt['source_contract_unlocked'])
        require('inconclusive-portfolio-stopped',not any(a.available(initial) for a in actions))
    else:
        require('only-audit-and-norm-ready',{a.name for a in actions if a.available(initial)}=={'source-contract-audit/prove','completion-phase/prove','completion-phase/reject'})
    for action in actions:
        require('normalized/'+action.name,abs(sum(b.probability for b in action.branches.values())-1)<1e-12)
        for outcome,b in action.branches.items():
            if outcome!='++':
                require('no-false-unlock/'+action.name+'/'+outcome,not b.effect.add and 'route-live' in b.effect.remove)
    base=solve(c,central,frontier=True)
    require('projection-agrees-with-sequential-planner',base['first_action']==base['objective_projection']['action'])
    analytic_success=0 if observed else math.prod(central[s['id']+'/prior_true']*central[s['id']+'/prove_q'] for s in c['stages'])
    require('closure-requires-all-five-certificates',math.isclose(base['success_probability'],analytic_success,abs_tol=1e-12))
    scenarios=[]
    for key,v in ranges.items():
        for index in (0,2):
            params=dict(central); params[key]=v[index]
            scenarios.append({'change':key,'value':v[index],**solve(c,params)})
    for index,label in ((0,'all-low'),(2,'all-high')):
        scenarios.append({'change':label,**solve(c,{k:v[index] for k,v in ranges.items()})})
    counts={}
    for s in scenarios: counts[s['first_action']]=counts.get(s['first_action'],0)+1
    regression = subprocess.run([sys.executable,str(ROOT/'checkers/test_closure_planning.py')],capture_output=True,text=True,timeout=60)
    require('closure-regressions-pass',regression.returncode==0)
    sources=[CONTRACT,ESTIMATES,Path(__file__).resolve(),ROOT/'checkers/test_closure_planning.py',REPO/'research/conjecture_net/interpretation_planner.py',REPO/'research/conjecture_net/objective_projection.py']
    sources += [REPO/o['receipt'] for o in observed]
    result={'status':'pass','checks_passed':len(checks),'objective':c['objective'],
            'planning_only':True,'global_optimum_established':False,'central':base,
            'regression_test_output':regression.stdout+regression.stderr,
            'sensitivity_first_action_counts':counts,'sensitivity':scenarios,
            'stable_in_tested_scenarios':base['first_action'] is not None and len(counts)==1 and base['first_action'] in counts,
            'decision_status':'replan_required_after_observed_attempt' if observed and base['first_action'] is None else 'prospective_ranking',
            'observed_attempts':observed,
            'source_sha256':{str(p.relative_to(REPO)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    (ROOT/'results/closure-planning.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('sensitivity','source_sha256')},indent=2))

if __name__=='__main__': main()
