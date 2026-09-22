"""Independent graph/guard replay of the declared finite source-evidence coupling."""
from pathlib import Path
from collections import defaultdict
import json,hashlib,importlib.util
ROOT=Path(__file__).resolve().parents[2];N=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
    path=N/'actual-source-evidence-coupling.json';r=load(path);c=load(N/'source-evidence-coupling-contract.json')
    assert r['contract_sha256']==sha(N/'source-evidence-coupling-contract.json')
    for name,h in c['inputs_sha256'].items():assert sha(ROOT/name)==h
    spec=importlib.util.spec_from_file_location('source',ROOT/'voevodsky/certificates/verify_filtered_obstruction.py')
    source=importlib.util.module_from_spec(spec);spec.loader.exec_module(source)
    base=load(N/'actual-private-core-with-original-cubic.json');union=load(N/'actual-retained-cubic-observer-union.json')
    assert digest(base['rows'][0])==c['row_sha256']
    lookup=defaultdict(lambda:defaultdict(list));index=0
    for row in base['rows']:
        for t in row['terms']:lookup[tuple(row['corner_masks'])][tuple(t['word']),tuple(t['marks'])].append((index,(('base:'+t['coefficient'],1),)))
        index+=1
    for frame in union['frames']:
        for row in frame['rows']:
            for t in row['terms']:
                coeff=tuple((frame['family']+':'+str(j)+':'+str(t['windows']),v) for j,v in enumerate(t['component_coefficients']) if v)
                lookup[tuple(row['corner_masks'])][tuple(t['word']),tuple(t['marks'])].append((index,coeff))
            index+=1
    states=r['states'];assert len(states)==638
    def key(s):return tuple(s['word']),tuple(s['marks']),s['producer'],s['received'],s['issued']
    ids={key(s):i for i,s in enumerate(states)};assert len(ids)==len(states)
    groups=defaultdict(list);edges=0
    for i,s in enumerate(states):
        w,m,p,v,d=key(s);end=sum(1<<e for e in w);assert w[:2] in ((0,1),(1,0)) and m[:2]==(0,0)
        rec=tuple(sorted((k,str(vv)) for k,vv in source.record(0,w,m).items()))
        obs=tuple(lookup[0,end].get((w,m),()))
        current=(0,end,rec,obs);enhanced=current+(p,v,d)
        assert digest(current)==s['current_class'] and digest(enhanced)==s['enriched_class']
        expected={}
        truth=int(w[:2]==(0,1))
        assert p is None or p==truth
        assert v is None or p==v==truth
        assert d is None or end&8 and p==v==d==truth
        if end==3:
            candidates=[(3,0)]
            if p is None:expected[('acquire',)]=(w,m,truth,v,d)
        else:
            assert w[2]==3 and m[2]==0
            candidates=[(e,mark) for e in (2,4,5) if not end&(1<<e) for mark in (0,1)]
        for e,mark in candidates:
            source.record(0,w+(e,),m+(mark,));expected['source',e,mark]=(w+(e,),m+(mark,),p,v,d)
        if p is not None:expected['deliver',]=(w,m,p,p,d)
        if end&8 and v is not None and d is None:expected['issue',v]=(w,m,p,v,v)
        actual={tuple(event):target for event,target in s['transitions']}
        assert len(actual)==len(s['transitions'])
        assert actual=={event:ids[target] for event,target in expected.items()}
        edges+=len(actual);groups[s['enriched_class']].append(i)
    reached=set(r['initial_state_ids']);assert {key(states[i]) for i in reached}=={((0,1),(0,0),None,None,None),((1,0),(0,0),None,None,None)}
    queue=list(reached)
    while queue:
        for event,j in states[queue.pop()]['transitions']:
            if j not in reached:reached.add(j);queue.append(j)
    assert len(reached)==len(states)
    for group in groups.values():
        patterns=[{tuple(event):states[j]['enriched_class'] for event,j in states[i]['transitions']} for i in group]
        assert all(pattern==patterns[0] for pattern in patterns)
    assert len(groups)==r['enriched_classes']
    a=states[ids[((0,1,3),(0,0,0),1,1,None)]];b=states[ids[((1,0,3),(0,0,0),0,0,None)]]
    assert a['current_class']==b['current_class']
    assert any(event==['issue',1] for event,j in a['transitions'])
    assert any(event==['issue',0] for event,j in b['transitions'])
    report={'passed':True,'states_replayed':len(states),'edges_replayed':edges,'enriched_classes':len(groups),
            'source_relative_collision_with_opposite_issuance':True,'enriched_transition_congruence':True,
            'owning_coupling_sha256':sha(path),'scope':'Declared finite ideal protocol; not a physical acquisition or general signed-task ledger coupling.'}
    (N/'source-evidence-coupling-verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
