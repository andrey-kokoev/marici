"""Bounded source/acquisition/recipient interfaces for the frozen 62/70 observers.

Atomic source authorization is part of this contract. No claim of arbitrary
asynchronous network linearizability, authentication or physical sensing.
"""
from pathlib import Path
from collections import deque
import json,hashlib,subprocess,sys,copy
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def require(x,why):
    if not x:raise ValueError(why)


def main():
    source_path=OUT/'actual-source-evidence-coupling.json';qpath=OUT/'compressed-observer-live-lift.json'
    source=load(source_path);ref=load(qpath);source_contract=load(OUT/'source-evidence-coupling-contract.json')
    labels=load(OUT/'compressed-observer-live-lift-contract.json')['extended_labels'];labels=list(map(tuple,labels))
    assert len(labels)==18
    rowhash=source_contract['row_sha256'];taskhash=digest(source_contract['task']);run='declared-run'
    contract={'schema':'compositional-observer-interfaces-v1','reference_source_sha256':sha(source_path),
      'reference_quotient_sha256':sha(qpath),'reference_contract_sha256':sha(OUT/'source-evidence-coupling-contract.json'),
      'labels':labels,'outputs':['typed corner','received certified value','issued value'],
      'components':{'source':['current endpoint mask','origin bit from trusted known initialization'],
                    'acquisition':['absent or one immutable bound observation frame'],
                    'recipient':['absent or one delivered frame','absent or issued value']},
      'frame_fields':['run binding','task binding','actual observation row binding','observation corner (0,3)','value'],
      'ports':{'source_advance':'Source-local unused-event/workflow check.',
               'acquire':'Atomic source-authorized row evaluation at CURRENT mask 3; acquisition buffer commits that exact bound frame.',
               'deliver':'Recipient receives the exact source-authorized acquisition-buffer frame, with immutable bindings.',
               'issue':'Recipient requires a valid locally delivered frame, no prior issuance and CURRENT source authorization that event 3 has occurred.',
               'audit_origin':'Source authority checks faithfully retained origin bit; no historical measurement is invented.'},
      'scheduling':'Every interleaving of these atomic operations, including rejected stuttering operations and duplicate deliveries. Source validation and associated acquisition/issuance commit have the declared linearization point.',
      'channel':'Reliable source-authorized delivery from the named buffer. Hashes bind data but do not establish physical origin or authentication.',
      'initialization':'Both known initial source orders are tested; no records or issued result initially.',
      'prediction':'Bounded components match every reference permission and output, and retain the unique 70-state origin-audit lift.',
      'negative_interfaces':['stale cached source position','Cartesian mixing of individually valid components','unbound or changed received frame'],
      'nonclaims':['arbitrary delayed network implementation','arbitrary future actions','full numerical observer reconstruction','cryptographic authenticity','physical acquisition']}
    cp=OUT/'compositional-observer-interface-contract.json';save(cp,contract)
    subprocess.run([sys.executable,str(ROOT/'nima/checkers/verify_compressed_observer_live_lift.py')],check=True,capture_output=True,text=True)

    def frame(value):return {'run':run,'task':taskhash,'row':rowhash,'corner':[0,3],'value':value}
    def validate(f):
        require(set(f)==set(frame(0)),'bad fields')
        require(f['run']==run and f['task']==taskhash and f['row']==rowhash and f['corner']==[0,3],'bad binding')
        require(type(f['value']) is int and f['value'] in (0,1),'bad value')
        return f['value']
    def source_port(end,origin,request):
        # Only this component reads source-local position and origin.
        if request==('authorize-acquire',):return frame(origin) if end==3 else None
        if request==('authorize-issue',):return bool(end&8)
        if request[0]=='source':
            _,event,mark=request
            if end==3:ok=(event,mark)==(3,0)
            else:ok=event in (2,4,5) and not end&(1<<event) and mark in (0,1)
            return (ok,end|(1<<event) if ok else end)
        if request[0]=='audit-origin':return request[1]==origin
        raise ValueError('unknown source request')
    def acquisition_port(buffer,grant):
        if buffer is not None or grant is None:return False,buffer
        return True,validate(grant)
    def recipient_deliver(received,payload):
        if payload is None:return False,received
        value=validate(payload)
        require(received is None or received==value,'conflicting delivered record')
        return True,value
    def recipient_issue(received,issued,want,source_grant):
        ok=(received is not None and issued is None and want==received and source_grant)
        return ok,want if ok else issued
    # Compact implementation state encodes immutable frames by their values;
    # decoding restores every fixed binding. It carries no execution word.
    def step(state,event):
        end,origin,pending,received,issued=state;kind=event[0]
        if kind=='source':
            ok,nxt=source_port(end,origin,event);return ok,(nxt,origin,pending,received,issued)
        if kind=='acquire':
            ok,p=acquisition_port(pending,source_port(end,origin,('authorize-acquire',)))
            return ok,(end,origin,p,received,issued)
        if kind=='deliver':
            ok,r=recipient_deliver(received,None if pending is None else frame(pending))
            return ok,(end,origin,pending,r,issued)
        if kind=='issue':
            ok,d=recipient_issue(received,issued,event[1],source_port(end,origin,('authorize-issue',)))
            return ok,(end,origin,pending,received,d)
        if kind=='audit-origin':return source_port(end,origin,event),state
        raise ValueError('unknown operation')
    initials=[(3,b,None,None,None) for b in (0,1)];seen=set(initials);queue=deque(initials);graph={}
    while queue:
        state=queue.popleft();edges=[]
        for event in labels:
            ok,nxt=step(state,event)
            if not ok:assert nxt==state
            edges.append((ok,nxt))
            if nxt not in seen:seen.add(nxt);queue.append(nxt)
        graph[state]=edges
    ordered=sorted(seen,key=repr);ids={s:i for i,s in enumerate(ordered)}
    def collapse(s):return (sum(1<<e for e in s['word']),int(s['word'][:2]==[0,1]),s['producer'],s['received'],s['issued'])
    oldmap={};newmap={};checks=0
    for i,s in enumerate(source['states']):
        c=collapse(s);assert c in seen
        for mapping,cid in ((oldmap,ref['old_partition'][i]),(newmap,ref['new_partition'][i])):
            if c in mapping:assert mapping[c]==cid
            mapping[c]=cid
        assert [0,c[0],c[3],c[4]]==ref['old_quotient'][oldmap[c]]['output']
        edges={tuple(e):j for e,j in s['transitions']}
        for event,(ok,nxt) in zip(labels,graph[c]):
            if event[0]=='audit-origin':expected=(event[1]==c[1],c)
            else:expected=(event in edges,collapse(source['states'][edges[event]]) if event in edges else c)
            assert (ok,nxt)==expected;checks+=1
    assert set(oldmap)==seen and len(seen)==70
    assert len(set(oldmap.values()))==62 and set(newmap.values())==set(range(70))
    for c in seen:
        for label,(ok,nxt) in enumerate(graph[c]):
            assert [ok,newmap[nxt]]==ref['new_quotient'][newmap[c]]['transitions'][label]
            if label<16:assert [ok,oldmap[nxt]]==ref['old_quotient'][oldmap[c]]['transitions'][label]
    for state in seen:
        end,b,p,r,d=state
        assert p is None or p==b
        assert r is None or r==p==b
        assert d is None or d==r==p==b and end&8
    # Concrete attacks on weaker interfaces, not changes to the successful contract.
    s=(3,1,None,None,None);ok,advanced=step(s,('source',3,0));assert ok
    ok,_=step(advanced,('acquire',));assert not ok
    stale_grant=source_port(3,1,('authorize-acquire',))
    stale_ok,_=acquisition_port(None,stale_grant);assert stale_ok
    s=(3,1,None,None,None)
    for event in (('acquire',),('deliver',),('source',3,0)):
        ok,s=step(s,event);assert ok
    actual,_=step(s,('issue',1));assert actual
    cached,_=recipient_issue(s[3],s[4],1,source_port(3,1,('authorize-issue',)));assert not cached
    mixed=(11,1,1,0,None)
    assert mixed not in seen and validate(frame(0))==0
    local_source={(s[0],s[1]) for s in seen};local_a={s[2] for s in seen};local_r={(s[3],s[4]) for s in seen}
    assert mixed[:2] in local_source and mixed[2] in local_a and mixed[3:] in local_r
    rejects=[]
    for field,value in [('run','foreign-run'),('task','foreign-task'),('row','wrong-row'),('corner',[0,11]),('value',2)]:
        f=frame(1);f[field]=value
        try:validate(f)
        except ValueError:rejects.append(field)
        else:raise AssertionError('unbound frame accepted')
    # A same-run forged 0/1 value can be syntactically valid: trust comes from
    # the acquisition/delivery constructors, not from this structural validator.
    assert validate(frame(0))==0
    assert sha(source_path)==contract['reference_source_sha256'] and sha(qpath)==contract['reference_quotient_sha256']
    report={'verdict':'CORROBORATED_FOR_DECLARED_ATOMIC_INTERFACES','contract_sha256':sha(cp),
      'component_states':[list(s) for s in ordered],'initial_states':[ids[s] for s in initials],
      'transitions':[[[ok,ids[nxt]] for ok,nxt in graph[s]] for s in ordered],
      'to_62_state_observer':[oldmap[s] for s in ordered],'to_70_state_observer':[newmap[s] for s in ordered],
      'reference_state_to_implementation':[ids[collapse(s)] for s in source['states']],
      'reference_step_checks':checks,'local_carrier_sizes':{'source':len(local_source),'acquisition':len(local_a),'recipient':len(local_r)},
      'reachable_joint_states':len(seen),'unconstrained_local_product_size':len(local_source)*len(local_a)*len(local_r),
      'negative_controls':{'stale_acquisition':{'trace':[['source',3,0],['acquire']], 'cached_interface':'accepts','reference':'rejects'},
        'stale_issue':{'trace':[['acquire'],['deliver'],['source',3,0],['issue',1]],'cached_interface':'rejects','reference':'accepts'},
        'mixed_local_states':list(mixed),'mixed_state_individually_valid_but_jointly_unreachable':True,
        'rejected_frame_fields':rejects},
      'upgrade':'Source-local origin bit plus current reference class uniquely selects the verified 70-state lift; no whole source word or execution journal is exchanged.',
      'preservation_proof':'Initialization and exhaustive one-step correspondence yield matching outputs and admission for all finite declared interleavings, including rejection and duplicate-delivery loops.',
      'trust_boundary':'Source-authorized reliable delivery and faithful origin-bit retention are assumptions. Same-run fabricated values are not detected by hashes or field checks alone.',
      'atomicity_boundary':'Current source authorization and acquisition/issuance have the stipulated atomic linearization point. Delayed network refinement of these ports requires a separate proof.'}
    save(OUT/'compositional-observer-interfaces.json',report)
    print(json.dumps({k:report[k] for k in ('verdict','local_carrier_sizes','reachable_joint_states','unconstrained_local_product_size','reference_step_checks')},indent=2))
if __name__=='__main__':main()
