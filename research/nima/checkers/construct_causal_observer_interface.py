"""Dependency-derived causal interfaces, followed by independent reference tests.

Finite, exact, atomic-port construction. No interface is defined by inspecting
reference quotient classes. The reference is used only after synthesis.
"""
from pathlib import Path
from collections import deque,defaultdict
import json,hashlib,importlib.util,sys,subprocess,copy
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def module(name,p):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def V(name):return {'var':name}
def A(index):return {'arg':index}
def E(op,*args):return {'op':op,'args':list(args)}
def reads(expr):
    if not isinstance(expr,dict):return set()
    if 'var' in expr:return {expr['var']}
    return set().union(*(reads(x) for x in expr.get('args',[])))
def evaluate(expr,env,args):
    if not isinstance(expr,dict):return expr
    if 'var' in expr:return env[expr['var']]
    if 'arg' in expr:return args[expr['arg']]
    op=expr['op'];a=expr['args']
    if op=='if':return evaluate(a[1] if evaluate(a[0],env,args) else a[2],env,args)
    if op=='and':return all(evaluate(x,env,args) for x in a)
    if op=='or':return any(evaluate(x,env,args) for x in a)
    values=[evaluate(x,env,args) for x in a]
    if op=='eq':return values[0]==values[1]
    if op=='not':return not values[0]
    if op=='bitand':return values[0]&values[1]
    if op=='bitor':return values[0]|values[1]
    if op=='shift':return values[0]<<values[1]
    if op=='in':return values[0] in values[1]
    raise ValueError('undeclared operation')


def main():
    fields=['end','origin','pending','received','issued']
    owners={'end':'source','origin':'source','pending':'acquisition','received':'recipient','issued':'recipient'}
    end,origin,pending,received,issued=map(V,fields)
    source_guard=E('if',E('eq',end,3),E('and',E('eq',A(0),3),E('eq',A(1),0)),
        E('and',E('in',A(0),[2,4,5]),E('in',A(1),[0,1]),E('not',E('bitand',end,E('shift',1,A(0))))))
    rules={
      'source':{'owner':'source','guard':source_guard,'updates':{'end':E('bitor',end,E('shift',1,A(0))) }},
      'acquire':{'owner':'acquisition','guard':E('and',E('eq',end,3),E('eq',pending,None)),'updates':{'pending':origin}},
      'deliver':{'owner':'recipient','guard':E('and',E('not',E('eq',pending,None)),E('or',E('eq',received,None),E('eq',received,pending))), 'updates':{'received':pending}},
      'issue':{'owner':'recipient','guard':E('and',E('bitand',end,8),E('not',E('eq',received,None)),E('eq',issued,None),E('eq',A(0),received)),'updates':{'issued':received}},
      'audit-origin':{'owner':'source','guard':E('eq',origin,A(0)),'updates':{}}}
    labels=[['source',e,m] for e in range(6) for m in (0,1)]+[['acquire'],['deliver'],['issue',0],['issue',1],['audit-origin',0],['audit-origin',1]]
    output_expr=[0,end,received,issued]
    source_path=OUT/'actual-source-evidence-coupling.json';quotient_path=OUT/'compressed-observer-live-lift.json'
    context={'source_contract_sha256':sha(OUT/'source-evidence-coupling-contract.json'),
             'task_sha256':digest(load(OUT/'source-evidence-coupling-contract.json')['task']),
             'row_sha256':load(OUT/'source-evidence-coupling-contract.json')['row_sha256'],'run':'known-initial-run'}
    contract={'schema':'dependency-derived-causal-interface-v1','fields':fields,'owners':owners,'rules':rules,
      'outputs':output_expr,'labels':labels,'initial_states':[[3,0,None,None,None],[3,1,None,None,None]],
      'origin_initialization':'Truthful known initial prefix: [0,1] -> 1, [1,0] -> 0; unchanged thereafter.',
      'context':context,'source_sha256':sha(source_path),'reference_quotient_sha256':sha(quotient_path),
      'construction':'Read guards/updates/outputs; close under update dependencies; export remote field requirements by owner and guard/payload phase. Only then explore and minimize.',
      'prediction':'Dependency-closed local interfaces determine all declared mixed continuations and both observer views without a history journal.',
      'atomicity':'Guard reads and accepted update commit refer to one authoritative source-bound snapshot; rejected operations reveal no update payload.',
      'retention':'Trusted initialization and faithful storage; not authentication or recovery from erased provenance.',
      'scope':'Actual frozen coupling and origin-audit extension. No mixing with the separately bound analytical task ledger.'}
    cp=OUT/'causal-interface-construction-contract.json';save(cp,contract)
    # Interface synthesis runs before loading reference graph or partitions.
    live=set().union(*(reads(x) for x in output_expr))
    for rule in rules.values():live|=reads(rule['guard'])
    changed=True
    while changed:
        before=set(live)
        for rule in rules.values():
            for target,expr in rule['updates'].items():
                if target in live:live|=reads(expr)
        changed=before!=live
    if not live<=set(fields):raise ValueError('undeclared state dependency')
    interface={actor:sorted(f for f in live if owners[f]==actor) for actor in sorted(set(owners.values()))}
    ports={}
    for name,rule in rules.items():
        guard=reads(rule['guard']);payload=set().union(*(reads(x) for x in rule['updates'].values()))
        assert guard|payload<=set(fields)
        assert all(owners[target]==rule['owner'] for target in rule['updates'])
        ports[name]={'actor':rule['owner'],'guard_fields':sorted(guard),'accepted_payload_fields':sorted(payload),
                     'remote_guard':sorted(f for f in guard if owners[f]!=rule['owner']),
                     'remote_payload':sorted(f for f in payload if owners[f]!=rule['owner'])}
    binding=digest(context)
    def port(state,names,provided_binding):
        if provided_binding!=binding:raise ValueError('incompatible source/task/run binding')
        return {f:state[fields.index(f)] for f in names}
    def step(state,label):
        if list(label) not in labels:return False,state
        name,*args=label;rule=rules[name];spec=ports[name]
        env=port(state,spec['guard_fields'],binding)
        if not evaluate(rule['guard'],env,args):return False,state
        # Only an accepted, same-snapshot operation obtains its payload fields.
        env.update(port(state,spec['accepted_payload_fields'],binding))
        out=list(state)
        for target,expr in rule['updates'].items():out[fields.index(target)]=evaluate(expr,env,args)
        return True,tuple(out)
    def output(state):
        env=port(state,set().union(*(reads(x) for x in output_expr)),binding)
        return tuple(evaluate(x,env,[]) for x in output_expr)
    initial=list(map(tuple,contract['initial_states']));seen=set(initial);queue=deque(initial);graph={}
    while queue:
        s=queue.popleft();edges=[]
        for label in labels:
            accepted,nxt=step(s,label);edges.append((accepted,nxt))
            if nxt not in seen:seen.add(nxt);queue.append(nxt)
        graph[s]=edges
    states=sorted(seen,key=repr);ids={s:i for i,s in enumerate(states)}
    table=[[(a,ids[n]) for a,n in graph[s]] for s in states];outputs=[output(s) for s in states]
    # Partition routine is generic. Reference classes have still not been read.
    minimizer=module('minimize',ROOT/'nima/checkers/check_compressed_observer_live_lift.py')
    oldclass,oldq,_=minimizer.partition(outputs,[row[:16] for row in table])
    newclass,newq,_=minimizer.partition(outputs,table)
    # Attack ordinary per-language compression using ONLY user-visible outputs.
    sublanguages={'source':list(range(12)),'acquisition':[12],'recipient':[13,14,15]}
    localclasses={name:minimizer.partition(outputs,[[row[i] for i in indices] for row in table])[0]
                  for name,indices in sublanguages.items()}
    i,j=map(ids.get,initial)
    assert outputs[i]==outputs[j] and all(classes[i]==classes[j] for classes in localclasses.values())
    naive_joint_count=len({tuple(classes[k] for classes in localclasses.values()) for k in range(len(states))})
    mixed_initial=[i,j]
    a,b=i,j
    mixed_word=[12,13]
    for label in mixed_word:
        aa,a=table[a][label];ba,b=table[b][label];assert aa==ba
    assert outputs[a]!=outputs[b]
    # Dependency-derived local projections distinguish exactly what this mixed
    # interaction needs; their admitted joint carrier is not a Cartesian product.
    localvalues={actor:[tuple(s[fields.index(f)] for f in names) for s in states] for actor,names in interface.items()}
    jointkeys=[tuple(localvalues[actor][i] for actor in sorted(interface)) for i in range(len(states))]
    groups=defaultdict(list)
    for i,k in enumerate(jointkeys):groups[k].append(i)
    for group in groups.values():
        for j in group:
            assert outputs[j]==outputs[group[0]]
            assert [(a,jointkeys[n]) for a,n in table[j]]==[(a,jointkeys[n]) for a,n in table[group[0]]]
    assert len(groups)==len(newq)==70 and len(oldq)==62
    # Each selected coordinate is necessary for this extended output language.
    ablations=[]
    for f in fields:
        k=fields.index(f);buckets=defaultdict(list)
        for i,s in enumerate(states):buckets[s[:k]+s[k+1:]].append(i)
        pair=next(( (a,b) for group in buckets.values() for a in group for b in group if newclass[a]!=newclass[b]),None)
        assert pair is not None
        ablations.append({'omitted_field':f,'states':list(pair),'refined_classes':[newclass[x] for x in pair]})
    rejected=[]
    try:port(initial[0],['origin'],digest({**context,'run':'other-run'}))
    except ValueError:rejected.append('foreign run binding')
    try:
        unknown=reads(E('eq',V('delivery_before_cut'),True))
        if not unknown<=set(fields):raise ValueError('undeclared state dependency')
    except ValueError:rejected.append('undeclared future audit dependency')
    mixed=(11,1,1,0,None)
    assert mixed not in seen
    assert all(tuple(mixed[fields.index(f)] for f in names) in set(localvalues[actor]) for actor,names in interface.items())
    # Validation only: compare construction with owning reference after synthesis.
    subprocess.run([sys.executable,str(ROOT/'nima/checkers/verify_compressed_observer_live_lift.py')],check=True,capture_output=True,text=True)
    src=load(source_path);ref=load(quotient_path);oldmap={};newmap={};checks=0
    for r,s in enumerate(src['states']):
        state=(sum(1<<e for e in s['word']),int(s['word'][:2]==[0,1]),s['producer'],s['received'],s['issued']);index=ids[state]
        for mapping,constructed,reference in ((oldmap,oldclass[index],ref['old_partition'][r]),(newmap,newclass[index],ref['new_partition'][r])):
            if constructed in mapping:assert mapping[constructed]==reference
            mapping[constructed]=reference
        edges={tuple(e):n for e,n in s['transitions']}
        for label,(accepted,nxt) in zip(labels,table[index]):
            if label[0]=='audit-origin':assert accepted==(label[1]==state[1]) and nxt==index
            else:
                assert accepted==(tuple(label) in edges)
                target=src['states'][edges[tuple(label)]] if accepted else s
                expected=(sum(1<<e for e in target['word']),int(target['word'][:2]==[0,1]),target['producer'],target['received'],target['issued'])
                assert states[nxt]==expected
            checks+=1
    assert len(set(oldmap.values()))==62 and len(set(newmap.values()))==70
    assert sha(source_path)==contract['source_sha256'] and sha(quotient_path)==contract['reference_quotient_sha256']
    report={'verdict':'CORROBORATED_FOR_FROZEN_DEPENDENCY_CONSTRUCTION','contract_sha256':sha(cp),
      'derived_live_fields':sorted(live),'derived_interfaces':interface,'derived_ports':ports,
      'states':[list(s) for s in states],'initial_state_ids':[ids[s] for s in initial],
      'transitions':table,'outputs':outputs,'old_partition':oldclass,'new_partition':newclass,
      'old_quotient':oldq,'new_quotient':newq,
      'old_distinguishing_words':minimizer.distinguishing(oldq),'new_distinguishing_words':minimizer.distinguishing(newq),
      'reference_old_class_map':oldmap,'reference_new_class_map':newmap,'reference_step_checks':checks,
      'naive_local_partitions':localclasses,'naive_joint_class_count':naive_joint_count,'naive_composition_counterexample':{'initial_states':mixed_initial,
          'word':[labels[x] for x in mixed_word],'initial_outputs_equal':True,'all_local_classes_equal':True,
          'resulting_outputs':[outputs[a],outputs[b]],'conclusion':'Plain local user-output minimization does NOT commute with mixed continuation.'},
      'boundary_carrier_sizes':{actor:len(set(values)) for actor,values in localvalues.items()},
      'dependency_closed_joint_carrier':len(groups),'current_view_states':len(oldq),'extended_view_states':len(newq),
      'field_omission_witnesses':ablations,'rejections':rejected,'incompatible_cartesian_tuple':list(mixed),
      'construction_scope':'Rule read-dependencies are extracted mechanically; semantic correctness of the frozen declarations is checked against the reference. This is not automatic discovery of missing physical or undeclared causal dependencies.',
      'trust_atomicity_scope':'Bindings do not authenticate a producer; initialization/retention and source-authorized atomic ports remain assumptions.',
      'cross_protocol_scope':'No joint admission of unrelated analytical tasks or evidence ledgers is inferred.'}
    save(OUT/'causal-interface-construction.json',report)
    print(json.dumps({'verdict':report['verdict'],'derived_interfaces':interface,
        'naive_local_classes':{k:len(set(v)) for k,v in localclasses.items()},
        'naive_joint_classes':naive_joint_count,'mixed_counterexample':[labels[x] for x in mixed_word],
        'dependency_closed_states':len(groups),'current_view_states':len(oldq),'extended_view_states':len(newq),
        'reference_step_checks':checks},indent=2))
if __name__=='__main__':main()
