"""Validate subjective bridge estimates and stress-test the local IG frontier."""
from pathlib import Path
import hashlib
import json
import math
import random

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT/'contracts/current-problem-bridge-planning.v1.json'
NET = ROOT/'contracts/current-problem-conjecture-net.v1.json'

def entropy(p):
    p = min(1.0, max(0.0, p))  # Endpoint roundoff in Bayes normalization.
    return 0.0 if p in (0, 1) else -p*math.log2(p)-(1-p)*math.log2(1-p)

def information(p, q, intent):
    # Sound certificate: the conclusive branch has posterior entropy zero.
    success = p*q if intent == 'prove' else (1-p)*q
    fail = 1-success
    posterior = (p*(1-q) if intent == 'prove' else p)/fail if fail else 0
    return max(0.0, entropy(p)-fail*entropy(posterior))

def main():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    net = json.loads(NET.read_text(encoding='utf-8'))
    checks = []
    def require(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    require('planning-not-proof', c['status']=='subjective_uncalibrated_planning_only')
    bridges = c['bridges']
    require('three-unique-bridge-targets',len({b['id'] for b in bridges})==len(bridges)==3)
    require('covers-net-bridges', {b['net_bridge_id'] for b in bridges}=={b['id'] for b in net['bridge_gaps']})
    known = {b['id'] for b in bridges} | {c['diagnostic']['id']} | set(c['external_dependencies'])
    central, ranges = {}, {}
    for b in bridges:
        require('dependency-identities/'+b['id'],set(b['dependencies'])<=known and b['id'] not in b['dependencies'])
        require('readiness/'+b['id'], b['ready']==(not b['dependencies']))
        require('scoped-estimate/'+b['id'], all(b.get(k) for k in ('claim','scope','basis')))
        pkey = b['id']+'/prior'
        ranges[pkey] = b['prior_true']
        for intent, likelihood in [('prove','success_given_truth'),('reject','success_given_falsehood')]:
            action = b[intent]
            prefix = b['id']+'/'+intent
            require('bounded-protocol/'+prefix,all(action.get(k) for k in ('protocol','stop_rule','unblocks')))
            ranges[prefix+'/cost'] = action['cost_effort_units']
            ranges[prefix+'/q'] = action[likelihood]
    graph = {b['id']:b['dependencies'] for b in bridges}
    def visit(node, stack):
        require('acyclic/'+'/'.join(stack+[node]),node not in stack)
        for dep in graph.get(node,[]):
            visit(dep,stack+[node])
    for node in graph:
        visit(node,[])
    for key, values in ranges.items():
        require('ordered-range/'+key,len(values)==3 and all(math.isfinite(x) for x in values) and values[0]<=values[1]<=values[2])
        require('valid-range/'+key,values[0]>0 if key.endswith('/cost') else 0<=values[0]<=values[2]<=1)
        central[key] = values[1]
    for p in (0,0.2,0.5,0.95,1):
        for intent in ('prove','reject'):
            require(f'zero-information/{p}/{intent}',information(p,0,intent)<1e-12)
            require(f'perfect-information/{p}/{intent}',abs(information(p,1,intent)-entropy(p))<1e-12)
    def ranking(params):
        rows=[]
        for b in bridges:
            p=params[b['id']+'/prior']
            for intent in ('prove','reject'):
                key=b['id']+'/'+intent
                q,cost=params[key+'/q'],params[key+'/cost']
                ig=information(p,q,intent)
                require('information-bounds/'+key, -1e-12<=ig<=entropy(p)+1e-12)
                success=p*q if intent=='prove' else (1-p)*q
                rows.append({'action':key,'ready':b['ready'],'cost':cost,'information_bits':ig,
                             'bits_per_effort':ig/cost,'outcome_probabilities':
                             ({'++':success,'+-':1-success} if intent=='prove' else {'-+':success,'--':1-success})})
        return sorted(rows,key=lambda r:(-r['bits_per_effort'],r['action']))
    base=ranking(central)
    winners={row['action']:0 for row in base}
    changes=[]
    for key,values in ranges.items():
        for index in (0,2):
            params=dict(central); params[key]=values[index]
            winner=ranking(params)[0]['action']
            if winner!=base[0]['action']:
                changes.append({'parameter':key,'value':values[index],'winner':winner})
    rng=random.Random(c['sensitivity']['seed'])
    for _ in range(c['sensitivity']['scenarios']):
        params={key:rng.uniform(v[0],v[2]) for key,v in ranges.items()}
        winners[ranking(params)[0]['action']]+=1
    stable=not changes and winners[base[0]['action']]==c['sensitivity']['scenarios']
    sources=[CONTRACT,NET,Path(__file__).resolve()]
    result={'status':'pass','checks_passed':len(checks),'estimate_status':c['status'],
            'conditional_ranking':base,'ready_ranking':[row for row in base if row['ready']],
            'one_parameter_winner_changes':changes,'scenario_winner_counts':winners,
            'sensitivity_seed':c['sensitivity']['seed'],'scenario_count':c['sensitivity']['scenarios'],
            'winner_stable_in_tested_scenarios':stable,
            'global_optimum_established':False,
            'recommendation':None,
            'planning_status':'historical_estimates_require_revision_after_scope_clarification',
            'historical_recommendation':c['diagnostic']['id'] if not stable else 'Review dependency eligibility before executing the ranked action.',
            'recommendation_basis':'No live recommendation: the local-core proof changes the frontier; retained calculations are historical diagnostics.',
            'source_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    (ROOT/'results/bridge-planning.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
