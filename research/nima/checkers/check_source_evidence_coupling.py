"""An explicit finite source/acquisition/delivery/issuance coupling.

Uses actual source paths, recorder and assembled rows. The protocol is NEW and
explicit: it is not imported as an unproved coupling to the theta task ledger.
"""
from pathlib import Path
from itertools import permutations,product
from collections import defaultdict,deque
import importlib.util,json,hashlib,copy,sys,subprocess
ROOT=Path(__file__).resolve().parents[2];N=ROOT/'nima/results';V=ROOT/'voevodsky/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def require(x,message):
    if not x:raise ValueError(message)
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
    recorder_path=ROOT/'voevodsky/certificates/verify_filtered_obstruction.py'
    source=module('source',recorder_path)
    action_script=ROOT/'voevodsky/checkers/check_actual_opposite_observer_transport.py'
    subprocess.run([sys.executable,str(action_script)],check=True,capture_output=True,text=True)
    action_path=V/'actual-opposite-observer-transport.json';action=load(action_path);assert action['passed']
    base_path=N/'actual-private-core-with-original-cubic.json';union_path=N/'actual-retained-cubic-observer-union.json'
    witness_path=V/'actual-observer-reversal-descent.json'
    base=load(base_path);union=load(union_path);witness=load(witness_path)
    assert witness['presentation_sha256']==action['presentation_sha256']
    assert witness['witness']['original_observer_column']==[]
    row=base['rows'][0]
    assert row=={'corner_masks':[0,3],'terms':[{'word':[0,1],'marks':[0,0],'coefficient':'1'}]}
    rowhash=digest(row)
    contract={'schema':'actual-source-evidence-coupling-v1','task':'Certify whether the initial two-event canonical vacuum reading is ONE or ZERO, after event 3 has occurred.',
      'initial_histories':[[0,1],[1,0]],'initial_marks':[0,0],
      'source_workflow':'At mask 3, only append forgotten event 3; thereafter any unused event 2,4,5 with either retained mark. The recorder checks every extension.',
      'acquisition':'Optional explicit acquisition at corner (0,3) of actual base row 0; not performed by source extension.',
      'delivery':'Reliable explicit delivery of the SAME source-authorized pending record; not performed by acquisition or extension.',
      'issuance':'After event 3, issue ONE/ZERO once, only after local validation of the delivered matching record.',
      'calibration':'Exact unit vacuum row in the declared ideal protocol; no physical acquisition/error model claimed.',
      'admission_authority':'Finite execution semantics below ties records to the actual generating prefix. Hashes are bindings, not authentication.',
      'path_comparison':'Same corner and recorder value; compare assembled rows on their IDEAL difference, not an unrestricted O3 observer on individual paths.',
      'row_sha256':rowhash,'inputs_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in (recorder_path,base_path,union_path,witness_path,action_path)},
      'scope':'A newly declared finite coupling, not an authoritative coupling of every source path to the separate signed-calibration ledger.'}
    cp=N/'source-evidence-coupling-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
    # A frame's lineage is constructed by an actual acquisition transition.
    def make_frame(prefix):
        return {'task_sha256':digest(contract['task']),'row_sha256':rowhash,'corner':[0,3],
                'prefix':list(prefix),'marks':[0,0],'value':int(prefix==(0,1))}
    frames={v:make_frame(p) for v,p in ((1,(0,1)),(0,(1,0)))}
    def validate(frame):
        require(set(frame)==set(frames[0]),'bad frame shape')
        require(frame['task_sha256']==digest(contract['task']),'wrong task')
        require(frame['row_sha256']==rowhash and frame['corner']==[0,3],'wrong observation anchor')
        prefix=tuple(frame['prefix']);require(prefix in ((0,1),(1,0)) and frame['marks']==[0,0],'invalid acquired prefix')
        source.record(0,prefix,(0,0))
        require(type(frame['value']) is int and frame['value']==int(prefix==(0,1)),'wrong acquired value')
        return frame['value']
    for frame in frames.values():validate(frame)
    # Formal raw-row coefficients are used only to prove zero ideal differences.
    # Equality of these expressions implies equality at the actual calibration;
    # no independent-parameter specialization is used.
    bycorner=defaultdict(lambda:defaultdict(list));index=0
    for r in base['rows']:
        for term in r['terms']:
            bycorner[tuple(r['corner_masks'])][tuple(term['word']),tuple(term['marks'])].append((index,(('base:'+term['coefficient'],1),)))
        index+=1
    for frame in union['frames']:
        for r in frame['rows']:
            for term in r['terms']:
                coeff=tuple((frame['family']+':'+str(j)+':'+str(term['windows']),v) for j,v in enumerate(term['component_coefficients']) if v)
                bycorner[tuple(r['corner_masks'])][tuple(term['word']),tuple(term['marks'])].append((index,coeff))
            index+=1
    assert index==3591
    def mask(word):return sum(1<<e for e in word)
    def signature(word,marks):
        return tuple(bycorner[0,mask(word)].get((word,marks),()))
    def recording(word,marks):return tuple(sorted((k,str(v)) for k,v in source.record(0,word,marks).items()))
    # Exhaust every common suffix, including all retained-mark assignments.
    suffixes=[]
    for length in range(4):
        for w in permutations((2,4,5),length):
            for m in product((0,1),repeat=length):suffixes.append((w,m))
    assert len(suffixes)==79
    for w,m in suffixes:
        a,b=(0,1,3)+w,(1,0,3)+w;marks=(0,0,0)+m
        assert recording(a,marks)==recording(b,marks)
        assert signature(a,marks)==signature(b,marks)
    # State: source word, marks, producer record value, received value, issued value.
    # None means no event yet. Only source-authorized states are reachable.
    initial=[((0,1),(0,0),None,None,None),((1,0),(0,0),None,None,None)]
    def transitions(state):
        word,marks,p,r,d=state;end=mask(word);out={}
        if end==3:
            candidates=[(3,0)]
            if p is None:
                v=int(word==(0,1));out[('acquire',)]=(word,marks,v,r,d)
        else:candidates=[(e,m) for e in (2,4,5) if not end&(1<<e) for m in (0,1)]
        for e,m in candidates:
            source.record(0,word+(e,),marks+(m,))
            out[('source',e,m)]=(word+(e,),marks+(m,),p,r,d)
        if p is not None:
            require(frames[p]['prefix']==list(word[:2]),'record not produced by this history')
            v=validate(frames[p]);out[('deliver',)]=(word,marks,p,v,d)
        if end&8 and r is not None and d is None:
            out[('issue',r)]=(word,marks,p,r,r)
        return out
    states=set(initial);queue=deque(initial);graph={}
    while queue:
        state=queue.popleft();edges=transitions(state);graph[state]=edges
        for nxt in edges.values():
            if nxt not in states:states.add(nxt);queue.append(nxt)
    assert len(states)==638
    def current_key(s):
        w,m=s[:2];return (0,mask(w),recording(w,m),signature(w,m))
    def enriched_key(s):return current_key(s)+s[2:]
    groups=defaultdict(list)
    for s in states:groups[enriched_key(s)].append(s)
    checks=0
    for group in groups.values():
        first=graph[group[0]]
        for state in group[1:]:
            other=graph[state];assert set(first)==set(other)
            for event,nxt in first.items():assert enriched_key(nxt)==enriched_key(other[event]);checks+=1
    h1=((0,1,3),(0,0,0),1,1,None)
    h0=((1,0,3),(0,0,0),0,0,None)
    missing=((0,1,3),(0,0,0),1,None,None)
    unacquired=((0,1,3),(0,0,0),None,None,None)
    issued=((0,1,3),(0,0,0),1,1,1)
    assert all(s in states for s in (h1,h0,missing,unacquired,issued))
    assert current_key(h1)==current_key(h0)==current_key(missing)
    assert ('issue',1) in graph[h1] and ('issue',0) in graph[h0]
    assert not any(e[0]=='issue' for e in graph[missing])
    assert ('deliver',) in graph[missing] and ('deliver',) not in graph[unacquired]
    assert not any(e[0]=='issue' for e in graph[issued])
    # Every issued value is the actual historical readout, not a guessed label.
    for state in states:
        if state[4] is not None:assert state[4]==int(state[0][:2]==(0,1))==state[3]==state[2]
    rejected=[]
    for field,value in [('task_sha256','wrong'),('row_sha256','wrong'),('corner',[0,11]),('value',0)]:
        bad=copy.deepcopy(frames[1]);bad[field]=value
        try:validate(bad)
        except ValueError:rejected.append(field)
        else:raise AssertionError('invalid record accepted')
    for name,h in contract['inputs_sha256'].items():assert sha(ROOT/name)==h
    ordered=sorted(states,key=repr);ids={state:i for i,state in enumerate(ordered)}
    state_table=[{'word':list(state[0]),'marks':list(state[1]),'producer':state[2],'received':state[3],'issued':state[4],
                  'current_class':digest(current_key(state)),'enriched_class':digest(enriched_key(state)),
                  'transitions':[[list(event),ids[nxt]] for event,nxt in sorted(graph[state].items(),key=lambda x:repr(x[0]))]}
                 for state in ordered]
    report={'passed':True,'contract_sha256':sha(cp),'initial_state_ids':[ids[s] for s in initial],'states':state_table,'source_histories':160,'reachable_coupled_states':len(states),
      'common_suffix_collisions_checked':len(suffixes),'enriched_classes':len(groups),'matched_transition_checks':checks,
      'current_observer_sufficiency':'REFUTED for this declared evidence-dependent protocol',
      'counterexample':{'corner':[0,11],'one_history':list(h1[0]),'zero_history':list(h0[0]),'marks':[0,0,0],
          'difference':'the owning hidden ideal relation, up to sign','assembled_difference':'zero',
          'earlier_actual_row_values':[1,0],'allowed_issuances':['ONE','ZERO']},
      'availability_counterexample':'Same source history and pending record: issue enabled after delivery, forbidden before delivery.',
      'enrichment':{'state':'typed source-relative observer class + producer record + locally received record + issued flag',
          'result':'equal enriched states have the same admitted event labels and equal enriched successors throughout the finite graph',
          'necessity_controls':['producer record controls delivery','received record controls issuance','record value controls correct answer','issued flag controls one-shot issuance'],
          'minimality_scope':'These fields are sufficient and individually motivated for this protocol, not a universally minimal encoding.'},
      'frames':frames,'negative_controls_rejected':rejected,
      'analytical_equality_scope':'Finite enumeration uses sufficient exact formal coefficient equalities. Full source-relative descent also follows from verified action equivariance and guards depending only on endpoint and retained records; acquisition reads actual row 0.',
      'boundary':'Ideal exact acquisition and reliable modeled delivery only. No physical sensing, trusted-channel implementation, quantitative deadline, or general coupling to signed theta-task evidence is established.'}
    (N/'actual-source-evidence-coupling.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('passed','reachable_coupled_states','common_suffix_collisions_checked','enriched_classes','matched_transition_checks','current_observer_sufficiency')},indent=2))
if __name__=='__main__':main()
