"""Independent finite implementation/reference correspondence replay."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    cp=OUT/'compositional-observer-interface-contract.json';c=load(cp)
    rp=OUT/'compositional-observer-interfaces.json';r=load(rp)
    assert sha(cp)==r['contract_sha256']
    sp=OUT/'actual-source-evidence-coupling.json';qp=OUT/'compressed-observer-live-lift.json'
    assert sha(sp)==c['reference_source_sha256'] and sha(qp)==c['reference_quotient_sha256']
    assert sha(OUT/'source-evidence-coupling-contract.json')==c['reference_contract_sha256']
    src=load(sp);q=load(qp);states=list(map(tuple,r['component_states']));ids={s:i for i,s in enumerate(states)}
    assert len(states)==len(ids)==70
    labels=list(map(tuple,c['labels']));assert len(labels)==18
    transitions=r['transitions'];assert len(transitions)==70
    initial=set(r['initial_states']);assert {states[i] for i in initial}=={(3,0,None,None,None),(3,1,None,None,None)}
    reached=set(initial);todo=list(initial)
    while todo:
        i=todo.pop()
        for accepted,j in transitions[i]:
            assert type(accepted) is bool and 0<=j<70
            if j not in reached:reached.add(j);todo.append(j)
    assert len(reached)==70
    for i,s in enumerate(states):
        end,b,p,v,d=s
        assert b in (0,1) and (p is None or p==b) and (v is None or v==p==b)
        assert d is None or d==v==p==b and end&8
        assert len(transitions[i])==len(labels)
        for label,(accepted,j) in zip(labels,transitions[i]):
            nxt=list(s);kind=label[0]
            if kind=='source':
                e,m=label[1:];ok=(e,m)==(3,0) if end==3 else e in (2,4,5) and not end&(1<<e) and m in (0,1)
                if ok:nxt[0]=end|(1<<e)
            elif kind=='acquire':
                ok=end==3 and p is None
                if ok:nxt[2]=b
            elif kind=='deliver':
                ok=p is not None
                if ok:nxt[3]=p
            elif kind=='issue':
                ok=bool(end&8) and v is not None and d is None and label[1]==v
                if ok:nxt[4]=v
            elif kind=='audit-origin':ok=label[1]==b
            else:raise AssertionError('undeclared operation')
            assert accepted==ok and states[j]==tuple(nxt)
    collapse=r['reference_state_to_implementation'];old=r['to_62_state_observer'];new=r['to_70_state_observer']
    assert len(collapse)==638 and len(old)==len(new)==70
    checks=0
    for i,s in enumerate(src['states']):
        image=collapse[i];assert states[image]==(sum(1<<e for e in s['word']),int(s['word'][:2]==[0,1]),s['producer'],s['received'],s['issued'])
        assert old[image]==q['old_partition'][i] and new[image]==q['new_partition'][i]
        edges={tuple(e):j for e,j in s['transitions']}
        for label,(accepted,j) in zip(labels,transitions[image]):
            if label[0]=='audit-origin':assert accepted==(label[1]==states[image][1]) and j==image
            else:assert accepted==(label in edges) and j==(collapse[edges[label]] if label in edges else image)
            checks+=1
    assert checks==r['reference_step_checks']==11484
    assert set(old)==set(range(62)) and set(new)==set(range(70))
    lift={(a,b):n for a,b,n in q['lift_table']}
    for i,s in enumerate(states):
        assert lift[old[i],s[1]]==new[i]
        assert [0,s[0],s[3],s[4]]==q['old_quotient'][old[i]]['output']==q['new_quotient'][new[i]]['output']
        for label,(accepted,j) in enumerate(transitions[i]):
            assert [accepted,new[j]]==q['new_quotient'][new[i]]['transitions'][label]
            if label<16:assert [accepted,old[j]]==q['old_quotient'][old[i]]['transitions'][label]
    counts={'source':len({s[:2] for s in states}),'acquisition':len({s[2] for s in states}),'recipient':len({s[3:] for s in states})}
    assert counts==r['local_carrier_sizes']=={'source':18,'acquisition':3,'recipient':5}
    mixed=tuple(r['negative_controls']['mixed_local_states']);assert mixed not in ids
    assert mixed[:2] in {s[:2] for s in states} and mixed[2] in {s[2] for s in states} and mixed[3:] in {s[3:] for s in states}
    def follow(trace):
        i=ids[3,1,None,None,None];last=None
        for event in trace:last,i=transitions[i][labels.index(tuple(event))]
        return last
    assert follow(r['negative_controls']['stale_acquisition']['trace']) is False
    assert follow(r['negative_controls']['stale_issue']['trace']) is True
    report={'passed':True,'source_states_covered':638,'reachable_component_states':70,
      'current_observer_states':62,'upgraded_observer_states':70,'local_carrier_sizes':counts,
      'reference_transition_checks':checks,'all_declared_interleavings':'By checked initialization and one-step correspondence, including rejected stutters.',
      'scope':'Declared atomic ports with source-authorized delivery; not an asynchronous network implementation or an authentication theorem.',
      'certificate_sha256':sha(rp)}
    (OUT/'compositional-observer-interface-verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
