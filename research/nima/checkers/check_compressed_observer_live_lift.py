"""Frozen finite DPC: strict operational compression and a provenance-backed lift.

The extension audits a faithfully retained origin bit; it does not claim to
measure an erased past or support arbitrary future continuation languages.
"""
from pathlib import Path
from collections import deque
import json,hashlib,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def digest(x):return hashlib.sha256(canonical(x).encode()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')

def partition(outputs,table):
    def classify(keys):
        ids={};return [ids.setdefault(key,len(ids)) for key in keys]
    classes=classify(outputs);rounds=0
    while True:
        keys=[(outputs[i],tuple((accepted,classes[j]) for accepted,j in edges)) for i,edges in enumerate(table)]
        new=classify(keys);rounds+=1
        if new==classes:break
        classes=new
    groups=[[] for _ in range(max(classes)+1)]
    for i,c in enumerate(classes):groups[c].append(i)
    quotient=[]
    for group in groups:
        i=group[0];transitions=[(a,classes[j]) for a,j in table[i]]
        assert all(outputs[j]==outputs[i] and [(a,classes[k]) for a,k in table[j]]==transitions for j in group)
        quotient.append({'members':group,'output':outputs[i],'transitions':transitions})
    return classes,quotient,rounds

def distinguishing(q):
    result=[]
    for i in range(len(q)):
        for j in range(i+1,len(q)):
            queue=deque([(i,j,[])]);seen={(i,j)};found=None
            while queue and found is None:
                a,b,word=queue.popleft()
                if q[a]['output']!=q[b]['output']:found=word;break
                for label,((aa,an),(ba,bn)) in enumerate(zip(q[a]['transitions'],q[b]['transitions'])):
                    if aa!=ba:found=word+[label];break
                    pair=tuple(sorted((an,bn)))
                    if pair not in seen:seen.add(pair);queue.append((an,bn,word+[label]))
            assert found is not None,'Nonminimal quotient'
            result.append({'classes':[i,j],'word':found})
    return result

def main():
    source=OUT/'actual-source-evidence-coupling.json';data=load(source);states=data['states'];assert len(states)==638
    labels=[('source',e,m) for e in range(6) for m in (0,1)]+[('acquire',),('deliver',),('issue',0),('issue',1)]
    extended=labels+[('audit-origin',0),('audit-origin',1)]
    cp=OUT/'compressed-observer-live-lift-contract.json'
    contract={'schema':'compressed-observer-live-lift-DPC-v1','source_sha256':sha(source),
      'source_contract_sha256':sha(OUT/'source-evidence-coupling-contract.json'),
      'current_labels':labels,'extended_labels':extended,
      'outputs':['typed source corner (0,end_mask)','locally received validated value or absent','issued value or absent'],
      'rejection':'Observable rejected action, with unchanged state.',
      'extension':'audit-origin(b) is accepted iff b equals the faithfully retained origin_is_01 bit; state unchanged.',
      'provenance':{'field':'origin_is_01','values':[0,1],
        'initialization':'Known actual initial state: prefix [0,1] initializes 1; prefix [1,0] initializes 0.',
        'update':'Retain unchanged under every accepted or rejected event.',
        'authority':'Trusted initialization and faithful storage are assumptions. No hash proves that the bit is true or that its retention was complete.'},
      'prediction':'Current quotient has fewer than 638 states; current class plus origin bit has a unique faithful lift to the extended quotient.',
      'nonclaims':['preservation of the entire numerical assembled-observer vector','arbitrary future extensions','physical past acquisition','authenticated storage or crash recovery']}
    save(cp,contract)
    subprocess.run([sys.executable,str(ROOT/'nima/checkers/verify_source_evidence_coupling.py')],check=True,capture_output=True,text=True)
    outputs=[(0,sum(1<<e for e in s['word']),s['received'],s['issued']) for s in states]
    bits=[int(s['word'][:2]==[0,1]) for s in states]
    table=[];newtable=[]
    for i,s in enumerate(states):
        edges={tuple(e):j for e,j in s['transitions']}
        assert set(edges)<=set(labels)
        old=[(label in edges,edges.get(label,i)) for label in labels]
        table.append(old);newtable.append(old+[(b==bits[i],i) for b in (0,1)])
    oldclass,oldq,oldrounds=partition(outputs,table)
    newclass,newq,newrounds=partition(outputs,newtable)
    oldwords=distinguishing(oldq);newwords=distinguishing(newq)
    projection=[]
    for group in newq:
        parents={oldclass[i] for i in group['members']};assert len(parents)==1
        projection.append(parents.pop())
    for i,q in enumerate(newq):
        assert q['output']==oldq[projection[i]]['output']
        for event,(admitted,nxt) in enumerate(q['transitions'][:len(labels)]):
            assert (admitted,projection[nxt])==oldq[projection[i]]['transitions'][event]
    lift={}
    for i in range(len(states)):
        key=(oldclass[i],bits[i])
        if key in lift:assert lift[key]==newclass[i]
        lift[key]=newclass[i]
    # Invariant under ALL labels, including rejected self-loops, proves the
    # lift for arbitrary finite executions rather than bounded journal samples.
    step_checks=0
    for i,edges in enumerate(newtable):
        for label,(admitted,j) in enumerate(edges):
            assert bits[j]==bits[i]
            assert lift[oldclass[j],bits[j]]==newclass[j]
            assert (admitted,lift[oldclass[j],bits[j]])==newq[lift[oldclass[i],bits[i]]]['transitions'][label]
            step_checks+=1
    for i in data['initial_state_ids']:assert lift[oldclass[i],bits[i]]==newclass[i]
    collisions=[]
    for oldid,q in enumerate(oldq):
        descendants={newclass[i] for i in q['members']}
        if len(descendants)>1:
            pair=next((i,j) for i in q['members'] for j in q['members'] if newclass[i]!=newclass[j])
            i,j=pair
            assert bits[i]!=bits[j]
            assert newtable[i][-1][0]!=newtable[j][-1][0]
            collisions.append({'old_class':oldid,'source_states':list(pair),
                               'new_classes':[newclass[i],newclass[j]],'origin_bits':[bits[i],bits[j]],
                               'distinguishing_label':['audit-origin',1]})
    assert collisions,'The extension unexpectedly needs no lift provenance'
    # A forged opposite bit can pass lookup at split classes: binding/storage
    # authenticity cannot be inferred from a successful table lookup.
    i=collisions[0]['source_states'][0]
    assert (oldclass[i],1-bits[i]) in lift
    assert lift[oldclass[i],1-bits[i]]!=newclass[i]
    assert sha(source)==contract['source_sha256']
    passed=len(oldq)<638 and len(newq)<638
    report={'verdict':'CORROBORATED_FOR_FROZEN_EXTENSION' if passed else 'REFUTED',
      'contract_sha256':sha(cp),'source_sha256':sha(source),'old_partition':oldclass,'new_partition':newclass,
      'old_quotient':oldq,'new_quotient':newq,'old_refinement_rounds':oldrounds,'new_refinement_rounds':newrounds,
      'old_distinguishing_words':oldwords,'new_distinguishing_words':newwords,
      'refined_to_old_projection':projection,'lift_table':[[c,b,n] for (c,b),n in sorted(lift.items())],
      'old_class_split_obstructions':collisions,'all_label_lift_checks':step_checks,
      'retention_assumption_negative_control':'Opposite provenance bit at a split class selects the wrong refined state; lookup does not authenticate origin.',
      'proof':'Known initialization plus invariant origin bit and the checked commuting transitions gives correct lifting for every finite admitted execution, including arbitrarily many idempotent deliveries.',
      'scope':'Minimality is for the frozen outputs and action languages only, not full source reconstruction or a universally upgradeable observer.'}
    save(OUT/'compressed-observer-live-lift.json',report)
    print(json.dumps({'verdict':report['verdict'],'source_states':638,'current_minimal_states':len(oldq),
      'extended_minimal_states':len(newq),'compatible_class_bit_pairs':len(lift),
      'split_old_classes':len(collisions),'all_label_lift_checks':step_checks,
      'old_distinguishing_pairs':len(oldwords),'new_distinguishing_pairs':len(newwords)},indent=2))
if __name__=='__main__':main()
