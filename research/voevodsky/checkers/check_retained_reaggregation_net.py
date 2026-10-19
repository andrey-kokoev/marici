"""Scoped graph/evidence validator and live ledger/planner entrypoint.
Conclusive outcomes come only from theorem-specific ledger admission.
"""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/voevodsky/contracts/retained-reaggregation-conjecture-net.v1.json'
RESULT='research/voevodsky/results/retained_reaggregation_conjecture_net.json'

class NetError(ValueError):pass

def require(condition,message):
    if not condition:raise NetError(message)

def path_at(root,name):
    require(isinstance(name,str) and name and '\\' not in name,'bad relative evidence path')
    p=Path(name)
    require(not p.is_absolute() and '..' not in p.parts,'unsafe evidence path')
    full=(root/p).resolve()
    require(full.is_relative_to(root.resolve()),'evidence escapes repository')
    require(full.is_file(),'missing evidence: '+name)
    return full

def validate(root,contract):
    require(contract.get('schema')=='marici.voevodsky.retained-reaggregation-conjecture-net.v1','wrong schema')
    require(contract.get('outcome_semantics')=='proof-attempt-outcomes-v1','proof/polarity semantics mismatch')
    require(contract.get('outcome_ports')==['++','+-','-+','--'],'wrong outcome ports')
    import sys
    sys.path.insert(0,str(root/'research/conjecture_net'))
    from outcome_reference import resolve
    imported={}
    for item in contract.get('imports',[]):
        require(isinstance(item,dict) and item.get('id') and item.get('outcome_pointer') and item.get('role'),'unscoped outcome import')
        require(item['id'] not in imported,'duplicate imported claim')
        pointer=json.loads(path_at(root,item['outcome_pointer']).read_text(encoding='utf-8'))
        try: imported[item['id']]=resolve(root,pointer)
        except ValueError as error:raise NetError('invalid outcome import: '+str(error))
    require(contract.get('admission_policy',{}).get('version')=='scoped-ledger-admission-v2','unknown admission policy')
    planner=contract.get('planner',{})
    require(planner.get('status')=='external_executable_planner' and all(planner.get(k) is None for k in ('priors','costs','budget')),'estimates belong in the scoped external planning model')
    bindings=contract.get('evidence_bindings',[]);require(bindings,'no pinned evidence')
    paths=[b.get('path') for b in bindings];require(len(paths)==len(set(paths)),'duplicate evidence binding')
    observed={};context_observations={}
    policy_path=root/'research/voevodsky/contracts/retained-reaggregation-context-policy.v1.json'
    exceptions={}
    if policy_path.is_file():
        policy=json.loads(policy_path.read_text(encoding='utf-8'))
        require(policy.get('schema')=='marici.voevodsky.reaggregation-context-policy.v1' and policy.get('source_contract')==CONTRACT,'invalid context policy')
        require(policy.get('theorem_receipt_pins_exempted') is False and policy.get('outcome_imports_exempted') is False,'context policy cannot exempt proof pins')
        entries=policy.get('unpinned_context',[])
        exceptions={e['path']:e for e in entries}
        require(len(exceptions)==len(entries) and set(exceptions)<=set(paths),'unknown/duplicate context exception')
    for binding in bindings:
        name=binding['path'];digest=sha256(path_at(root,name).read_bytes()).hexdigest()
        if name in exceptions:
            entry=exceptions[name]
            role='scoped supporting evidence/context only; not a resolved net import'
            require(entry.get('required_role')==role and binding.get('role')==role and entry.get('historical_sha256')==binding.get('sha256'),'unpin limited to exact historical context attachment')
            require(name!=contract.get('issue_registry',{}).get('path') and name not in {i.get('outcome_pointer') for i in contract.get('imports',[])},'cannot unpin registry or outcome import')
            context_observations[name]={'historical_sha256':binding['sha256'],'current_sha256':digest,'status':'context_only_not_proof_evidence'}
            continue
        require(digest==binding.get('sha256'),'stale pinned evidence: '+name)
        observed[name]=digest
    registry=contract.get('issue_registry',{})
    require(registry.get('ids')==['U'+str(i) for i in range(1,12)],'issue registry must retain U1-U11')
    require(registry.get('path') in observed,'unpinned issue registry')
    nodes=contract.get('conjectures',[]);require(nodes,'empty net')
    ids=[n.get('id') for n in nodes]
    require(all(isinstance(x,str) and x for x in ids) and len(ids)==len(set(ids)),'bad/duplicate node ID')
    ids=set(ids);require(not ids&set(imported),'import/local claim collision');edges={};all_issues=set()
    for node in nodes:
        name=node['id'];deps=node.get('depends_on')
        require(isinstance(deps,list) and len(deps)==len(set(deps)),'bad dependencies: '+name)
        require(all(d in ids|set(imported) and d!=name for d in deps),'unknown/self dependency: '+name)
        require(node.get('outcome') is None,'scientific promotion requires theorem-specific admission: '+name)
        require(node.get('attempts')==[],'bootstrap requires empty initial attempts; use a reviewed ledger revision')
        require(all(isinstance(node.get(k),str) and node[k] for k in ('statement','scope_id','acceptance')),'missing claim/scope/acceptance')
        issues=node.get('issue_ids',[])
        require(issues and all(i in registry['ids'] for i in issues),'unknown/empty issue scope')
        all_issues.update(issues);edges[name]=deps
    require(all_issues==set(registry['ids']),'untracked understanding issue')
    remaining=set(ids);order=[]
    while remaining:
        layer=sorted(n for n in remaining if not (set(edges[n])&remaining))
        require(layer,'dependency cycle')
        order.extend(layer);remaining.difference_update(layer)
    objective=contract.get('objective',{});target=objective.get('target');physical=objective.get('physical_followup')
    require(target in ids and physical in ids and target!=physical,'bad target/followup')
    require(target in edges[physical],'physical followup must remain separately gated')
    require(physical not in edges[target],'conditional target improperly depends on physical followup')
    # Every conditional node must actually feed the target route. An isolated
    # hypothesis must not disappear from its declared assembly obligations.
    def ancestors(n):
        out=set()
        for d in edges[n]:
            out.add(d)
            if d not in imported:out.update(ancestors(d))
        return out
    require(ancestors(target)-set(imported)==ids-{target,physical},'conditional route contains orphan obligations')
    frozen=contract.get('frozen_comparison',{})
    require(frozen.get('rival_control')=='c-Pi, with carrier-present projector c; zero on vacuum, NOT unrestricted I-Pi','vacuum rival changed')
    require(frozen.get('records')=='one neutral two-level record first; any pool enlargement is a separately versioned input','record apparatus changed')
    require(frozen.get('candidate_parameters')=={'record_gap':'1','vertex_g':'1/2','relative_native_orbital_unit':'1','readout_time':'1 model-time unit'},'comparison parameters changed without revision')
    ready=sorted(n for n in ids if not edges[n])
    return {'validation_passed':True,'scientific_outcome':None,'target_outcome':None,
        'state':'active-unresolved-bootstrap','node_count':len(nodes),'unresolved_nodes':sorted(ids),
        'ready_actions':['prove/'+n for n in ready],'topological_order':order,
        'physical_followup':physical,'physical_admission':False,
        'verification_level':'contract integrity and DAG/readiness only; no theorem admission',
        'evidence_hashes':observed,'unpinned_context_observations':context_observations,'imports':imported,'planning_estimates_available':True}

def main():
    contract_path=ROOT/CONTRACT
    try:
        contract=json.loads(contract_path.read_text(encoding='utf-8'));bootstrap=validate(ROOT,contract)
        from reaggregation_harness import live_result
        result=live_result(ROOT,contract)
        result['unpinned_context_observations']=bootstrap['unpinned_context_observations']
        policy_path=ROOT/'research/voevodsky/contracts/retained-reaggregation-context-policy.v1.json'
        if policy_path.is_file():
            result.setdefault('source_hashes',{})[policy_path.relative_to(ROOT).as_posix()]=sha256(policy_path.read_bytes()).hexdigest()
    except (NetError,KeyError,ValueError,OSError,TypeError) as error:
        result={'validation_passed':False,'state':'blocked','scientific_outcome':None,'target_outcome':None,'physical_admission':False,'error':str(error)}
    result.setdefault('source_hashes',{}).update({CONTRACT:sha256(contract_path.read_bytes()).hexdigest() if contract_path.is_file() else None,
        str(Path(__file__).resolve().relative_to(ROOT)).replace('\\','/'):sha256(Path(__file__).read_bytes()).hexdigest()})
    (ROOT/RESULT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('evidence_hashes','source_hashes')},indent=2))
    if not result['validation_passed']:raise SystemExit(1)

if __name__=='__main__':main()
