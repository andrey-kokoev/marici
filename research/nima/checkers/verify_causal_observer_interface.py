"""Independent dependency, graph, minimality and mixed-counterexample replay."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def variables(expr):
    result=set();todo=[expr]
    while todo:
        x=todo.pop()
        if isinstance(x,dict):
            if 'var' in x:result.add(x['var'])
            todo.extend(x.get('args',[]))
    return result

def main():
    cp=OUT/'causal-interface-construction-contract.json';c=load(cp)
    rp=OUT/'causal-interface-construction.json';r=load(rp)
    assert sha(cp)==r['contract_sha256']
    assert sha(OUT/'actual-source-evidence-coupling.json')==c['source_sha256']
    assert sha(OUT/'compressed-observer-live-lift.json')==c['reference_quotient_sha256']
    live=set().union(*(variables(e) for e in c['outputs']))
    for rule in c['rules'].values():live.update(variables(rule['guard']))
    while True:
        nxt=set(live)
        for rule in c['rules'].values():
            for target,expr in rule['updates'].items():
                if target in live:nxt.update(variables(expr))
        if nxt==live:break
        live=nxt
    assert sorted(live)==r['derived_live_fields']
    interfaces={actor:sorted(f for f in live if c['owners'][f]==actor) for actor in sorted(set(c['owners'].values()))}
    assert interfaces==r['derived_interfaces']
    for name,rule in c['rules'].items():
        guards=variables(rule['guard']);payload=set().union(*(variables(x) for x in rule['updates'].values()))
        assert guards|payload<=set(c['fields']) and all(c['owners'][f]==rule['owner'] for f in rule['updates'])
        assert r['derived_ports'][name]=={'actor':rule['owner'],'guard_fields':sorted(guards),'accepted_payload_fields':sorted(payload),
           'remote_guard':sorted(f for f in guards if c['owners'][f]!=rule['owner']),
           'remote_payload':sorted(f for f in payload if c['owners'][f]!=rule['owner'])}
    # Independently enumerate the declared concrete transition semantics.
    states=list(map(tuple,r['states']));ids={s:i for i,s in enumerate(states)};assert len(ids)==len(states)==70
    labels=list(map(tuple,c['labels']));table=r['transitions'];outputs=r['outputs']
    for i,s in enumerate(states):
        end,b,p,v,d=s;assert outputs[i]==[0,end,v,d]
        for label,(admitted,j) in zip(labels,table[i]):
            nxt=list(s);kind=label[0]
            if kind=='source':
                e,m=label[1:];ok=(e,m)==(3,0) if end==3 else e in (2,4,5) and m in (0,1) and not end&(1<<e)
                if ok:nxt[0]=end|(1<<e)
            elif kind=='acquire':
                ok=end==3 and p is None
                if ok:nxt[2]=b
            elif kind=='deliver':
                ok=p is not None and (v is None or v==p)
                if ok:nxt[3]=p
            elif kind=='issue':
                ok=bool(end&8) and v is not None and d is None and v==label[1]
                if ok:nxt[4]=v
            elif kind=='audit-origin':ok=b==label[1]
            else:raise AssertionError('unknown label')
            assert admitted==ok and states[j]==tuple(nxt)
    reached=set(r['initial_state_ids']);assert {states[i] for i in reached}==set(map(tuple,c['initial_states']))
    todo=list(reached)
    while todo:
        for a,j in table[todo.pop()]:
            if j not in reached:reached.add(j);todo.append(j)
    assert len(reached)==70
    for name,width in (('old',16),('new',18)):
        cls=r[name+'_partition'];q=r[name+'_quotient']
        for i in range(70):
            assert q[cls[i]]['output']==outputs[i]
            assert q[cls[i]]['transitions']==[[a,cls[j]] for a,j in table[i][:width]]
        assert set(cls)==set(range(len(q)))
        pairs=set()
        for witness in r[name+'_distinguishing_words']:
            a,b=witness['classes'];assert a<b and (a,b) not in pairs;pairs.add((a,b))
            differs=q[a]['output']!=q[b]['output']
            for event in witness['word']:
                aa,an=q[a]['transitions'][event];ba,bn=q[b]['transitions'][event]
                differs|=aa!=ba;a,b=an,bn;differs|=q[a]['output']!=q[b]['output']
            assert differs
        assert len(pairs)==len(q)*(len(q)-1)//2
    local=r['naive_local_partitions'];subsets={'source':range(12),'acquisition':[12],'recipient':[13,14,15]}
    # Sound local congruences suffice for the counterexample; minimality of
    # these local partitions is not needed to prove local indistinguishability.
    for name,cls in local.items():
        for i in range(70):
            for j in range(i):
                if cls[i]==cls[j]:
                    assert outputs[i]==outputs[j]
                    for event in subsets[name]:
                        aa,an=table[i][event];ba,bn=table[j][event]
                        assert aa==ba and cls[an]==cls[bn]
    witness=r['naive_composition_counterexample'];a,b=witness['initial_states']
    assert a!=b and {a,b}==set(r['initial_state_ids'])
    assert all(cls[a]==cls[b] for cls in local.values())
    assert outputs[a]==outputs[b]
    for event in witness['word']:
        index=labels.index(tuple(event));aa,a=table[a][index];ba,b=table[b][index];assert aa==ba
    assert outputs[a]!=outputs[b] and [outputs[a],outputs[b]]==witness['resulting_outputs']
    joint_count=len({tuple(cls[i] for cls in local.values()) for i in range(70)})
    assert joint_count==r['naive_joint_class_count']==61
    for witness in r['field_omission_witnesses']:
        k=c['fields'].index(witness['omitted_field']);a,b=witness['states']
        assert states[a][:k]+states[a][k+1:]==states[b][:k]+states[b][k+1:]
        assert r['new_partition'][a]!=r['new_partition'][b]
    assert len(r['old_quotient'])==62 and len(r['new_quotient'])==70
    # Recheck the correspondence with every owning concrete source state.
    src=load(OUT/'actual-source-evidence-coupling.json');ref=load(OUT/'compressed-observer-live-lift.json');checks=0
    for i,s in enumerate(src['states']):
        state=(sum(1<<e for e in s['word']),int(s['word'][:2]==[0,1]),s['producer'],s['received'],s['issued']);j=ids[state]
        assert r['reference_old_class_map'][str(r['old_partition'][j])]==ref['old_partition'][i]
        assert r['reference_new_class_map'][str(r['new_partition'][j])]==ref['new_partition'][i]
        for event,(a,n) in enumerate(table[j]):
            assert [a,r['reference_new_class_map'][str(r['new_partition'][n])]]==ref['new_quotient'][ref['new_partition'][i]]['transitions'][event]
            checks+=1
    assert checks==r['reference_step_checks']==11484
    result={'passed':True,'construction_sha256':sha(rp),'naive_joint_classes':61,'required_current_classes':62,
      'mixed_distinguishing_word':[['acquire'],['deliver']],
      'dependency_closed_carrier':70,'reference_step_checks':checks,
      'scope':'Exact frozen declaration and reference replay. No automatic discovery of undeclared causal dependencies or asynchronous-port correctness.'}
    save=OUT/'causal-interface-construction-verification.json';save.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
