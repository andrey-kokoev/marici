"""Synthesize and verify the least boundary repair for coherent possibilities.

Preservation target: possible executions conditional on the retained local tuple
and truthful observed transitions. This is NOT selection of the actual run.
"""
from pathlib import Path
from collections import defaultdict,deque
from itertools import combinations
import json,hashlib,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')

def main():
    source_path=OUT/'causal-interface-construction.json';data=load(source_path)
    parent=load(OUT/'causal-interface-construction-contract.json')
    contract={'schema':'minimal-relational-boundary-repair-v1','source_sha256':sha(source_path),
      'parent_contract_sha256':sha(OUT/'causal-interface-construction-contract.json'),
      'preservation_target':'All possible coherent executions consistent with an initially given admitted tuple and subsequent truthful action/admission/next-tuple observations.',
      'not_target':'Predicting the actual origin from ambiguous initial evidence.',
      'initial_information':'Any admitted local-view tuple, with its whole same-state fiber; no extra past observations assumed.',
      'construction_rule':'From declared dependency-live fields, retain only coordinates nonconstant within a joint local-view fiber. Propagate subsets of their values without resetting to a full fiber.',
      'current_language':'first sixteen labels, without origin audits','extended_language':'all eighteen labels including origin audits',
      'predictions':{'current_zero_repair':'No false possible trace under the current language.',
        'extended_repair_field':['origin'],'max_boundary_predicates':1,
        'max_nonempty_knowledge_values_per_tuple':3,'max_additional_storage_bits':2,
        'max_extended_knowledge_states':79,'strict_minimality':'Zero repair fails and all three origin-possibility states are distinguishable at ambiguous tuples.'},
      'runtime_bound':'A tuple plus a two-bit origin-set mask; at most two lifted-kernel lookups per candidate observation; no concrete-source history or full-source-state set at runtime.',
      'empty_update':'Reject the observation packet as inconsistent; never issue a decision from an empty fiber.',
      'scope':'Fixed source-bound atomic protocol. Faithful observed evidence and immutable bindings are assumed; no new analytical-task or network semantics.'}
    cp=OUT/'minimal-relational-boundary-repair-contract.json';save(cp,contract)
    subprocess.run([sys.executable,str(ROOT/'nima/checkers/verify_relational_membership_live_witness.py')],check=True,capture_output=True,text=True)
    fields=parent['fields'];names=['source','acquisition','recipient'];states=data['states'];labels=parent['labels'];table=data['transitions']
    views=[tuple(data['naive_local_partitions'][name][i] for name in names) for i in range(70)]
    fibers=defaultdict(set)
    for i,v in enumerate(views):fibers[v].add(i)
    candidates=[f for f in data['derived_live_fields'] if any(len({states[i][fields.index(f)] for i in fiber})>1 for fiber in fibers.values())]
    assert candidates==['origin']
    bit_index=fields.index(candidates[0]);bits=[s[bit_index] for s in states]
    # Compile only boundary values and local tuples. Original state IDs stay in
    # the offline checking side, never in the runtime transition packet.
    kernel={}
    for i,v in enumerate(views):
        row=[(a,views[j],bits[j]) for a,j in table[i]]
        key=v,bits[i]
        if key in kernel:assert kernel[key]==row
        kernel[key]=row
    def possible_values(v):return sum(1<<b for b in (0,1) if (v,b) in kernel)
    def observations(v,mask,width):
        out=set()
        for b in (0,1):
            if mask&(1<<b):
                for label,(accepted,nextv,nextb) in enumerate(kernel[v,b][:width]):out.add((label,accepted,nextv))
        return sorted(out)
    def update(v,mask,event):
        label,accepted,nextv=event;result=0
        for b in (0,1):
            if mask&(1<<b):
                a,nv,nb=kernel[v,b][label]
                if (a,nv)==(accepted,nextv):result|=1<<nb
        return result
    def actual_update(fiber,event):
        label,accepted,nextv=event
        return frozenset(j for i in fiber for a,j in [table[i][label]] if a==accepted and views[j]==nextv)
    # Exact product exploration checks whether reset-to-full-fiber projection
    # admits any observation word without a coherent source execution.
    def attack_reset(width):
        queue=deque((v,frozenset(fiber),[]) for v,fiber in sorted(fibers.items()))
        seen={(v,frozenset(fiber)) for v,fiber in fibers.items()};steps=0
        while queue:
            v,fiber,word=queue.popleft()
            for event in observations(v,possible_values(v),width):
                new=actual_update(fiber,event);steps+=1
                if not new:return {'exact':False,'initial_views':list(word[0][0]) if word else list(v),
                    'trace':[{'from_views':list(start),'label':label,'accepted':a,'next_views':list(nv)} for start,(label,a,nv) in word+[(v,event)]],
                    'product_states_explored':len(seen),'edge_checks':steps}
                key=event[2],new
                if key not in seen:seen.add(key);queue.append((event[2],new,word+[(v,event)]))
        return {'exact':True,'product_states_explored':len(seen),'edge_checks':steps}
    current=attack_reset(16);extended=attack_reset(18)
    # Explore the repaired knowledge machine from full fibers, checking exact
    # equality with the joint constraints of the entire observation history.
    initial=[(v,possible_values(v)) for v in sorted(fibers)];seen=set(initial);queue=deque(initial);graph={};checks=0
    while queue:
        v,mask=queue.popleft();fiber=frozenset(i for i in fibers[v] if mask&(1<<bits[i]));edges=[]
        assert fiber
        for event in observations(v,mask,18):
            nextmask=update(v,mask,event);real=actual_update(fiber,event)
            represented={i for i in fibers[event[2]] if nextmask&(1<<bits[i])}
            assert nextmask and set(real)==represented;checks+=1
            nxt=event[2],nextmask;edges.append((event,nxt))
            if nxt not in seen:seen.add(nxt);queue.append(nxt)
        graph[v,mask]=edges
    ordered=sorted(seen);ids={s:i for i,s in enumerate(ordered)}
    # Missing transitions reject inconsistent evidence and retain the old state.
    # State outputs are the known local tuple, NOT its hidden possibility mask.
    all_events=sorted({event for edges in graph.values() for event,nxt in edges})
    eventids={event:i for i,event in enumerate(all_events)}
    sparse=[]
    for s in ordered:sparse.append({eventids[e]:ids[n] for e,n in graph[s]})
    witnesses=[]
    for i,j in combinations(range(len(ordered)),2):
        queue=deque([(i,j,[])]);visited={(i,j)};found=None
        while queue and found is None:
            a,b,word=queue.popleft()
            if ordered[a][0]!=ordered[b][0]:found=word;break
            for e in sorted(set(sparse[a])|set(sparse[b])):
                if (e in sparse[a])!=(e in sparse[b]):found=word+[e];break
                an,bn=sparse[a][e],sparse[b][e];pair=tuple(sorted((an,bn)))
                if pair not in visited:visited.add(pair);queue.append((an,bn,word+[e]))
        assert found is not None
        witnesses.append({'states':[i,j],'observations':found})
    ambiguous=[v for v in fibers if possible_values(v)==3];assert len(ambiguous)==9
    for v in ambiguous:assert all((v,mask) in seen for mask in (1,2,3))
    v=ambiguous[0]
    assert update(v,3,(16,True,v))==1
    assert update(v,1,(17,True,v))==0
    success=current['exact'] and not extended['exact'] and len(seen)==79 and len(candidates)==1
    admission_knowledge=[];definite_issuances=[]
    for v,mask in ordered:
        classifications=[]
        for label in range(18):
            statuses={kernel[v,b][label][0] for b in (0,1) if mask&(1<<b)}
            classifications.append('ALLOWED' if statuses=={True} else 'REJECTED' if statuses=={False} else 'UNDETERMINED')
        admission_knowledge.append(classifications)
        definite_issuances.append([labels[label][1] for label in (14,15) if classifications[label]=='ALLOWED'])
    packet={'labels':labels,'boundary_field':candidates[0],'context':parent['context'],'contract_sha256':sha(cp),
      'kernel_rows':[{'views':list(v),'origin':b,'transitions':[[a,list(nv),nb] for a,nv,nb in kernel[v,b]]} for v,b in sorted(kernel)],
      'knowledge_states':[{'views':list(v),'mask':mask,'edges':[[e,j] for e,j in sorted(sparse[i].items())],
                           'admission_knowledge':admission_knowledge[i],'definite_issuances':definite_issuances[i]}
                          for i,(v,mask) in enumerate(ordered)],
      'initial_knowledge_states':[ids[s] for s in initial],
      'observation_alphabet':[{'label':l,'accepted':a,'next_views':list(nv)} for l,a,nv in all_events],
      'mask_semantics':{'1':'origin zero only','2':'origin one only','3':'either origin','0':'inconsistent observation; not an admitted knowledge state'},
      'distinguishing_observations':witnesses}
    packet_path=OUT/'minimal-relational-boundary-repair-packet.json';save(packet_path,packet)
    assert sha(source_path)==contract['source_sha256']
    report={'verdict':'CORROBORATED_FOR_FROZEN_POSSIBILITY_TARGET' if success else 'REFUTED',
      'contract_sha256':sha(cp),'packet_sha256':sha(packet_path),'derived_boundary_fields':candidates,
      'current_language_without_repair':current,'extended_language_without_repair':extended,
      'repaired_knowledge_states':len(seen),'initial_view_tuples':len(initial),'exact_update_checks':checks,
      'ambiguous_tuples':len(ambiguous),'knowledge_values_at_each_ambiguous_tuple':3,'minimum_additional_binary_storage_bits':2,
      'pairwise_minimality_witnesses':len(witnesses),'false_audit_sequence_rejected':True,
      'interpretation':'Possible-path preservation needs no repair for the old language, despite its 62-state faithful deterministic observer. With audits it needs coherent uncertainty, not an invented actual selector.',
      'minimality_scope':'All knowledge states have distinct local-view/observation-admission behavior. The ternary bound holds conditional on a fixed ambiguous tuple; it is not a bound for arbitrary future audit languages.',
      'trust_scope':'Exact inference conditional on truthful bound observations; it cannot authenticate a fabricated but internally coherent history.'}
    save(OUT/'minimal-relational-boundary-repair.json',report)
    print(json.dumps({k:report[k] for k in ('verdict','derived_boundary_fields','repaired_knowledge_states','exact_update_checks','minimum_additional_binary_storage_bits','pairwise_minimality_witnesses')},indent=2))
    print('Current reset exact:',current['exact'],'Extended reset exact:',extended['exact'])
if __name__=='__main__':main()
