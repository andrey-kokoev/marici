"""Compile bounded admission and live-witness kernels from actual local views.

The runtime packet contains local-view tuples, one meaningful origin bit and
behavioral transitions, not original history/state identifiers. Existential
membership is distinguished from preservation of an actual execution.
"""
from pathlib import Path
from collections import defaultdict
from itertools import product
import json,hashlib,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def compose(first,second):
    by=defaultdict(set)
    for a,b in second:by[a].add(b)
    return {(a,c) for a,b in first for c in by[b]}
def opposite(relation):return {(b,a) for a,b in relation}

class Runtime:
    """Only the admitted packet is consulted by these operations."""
    def __init__(self,packet):
        self.context=packet['context_sha256'];self.labels=list(map(tuple,packet['labels']))
        self.label_index={json.dumps(label,separators=(',',':')):i for i,label in enumerate(packet['labels'])}
        self.admitted=set(map(tuple,packet['admitted_view_tuples']))
        self.lifts={(tuple(row['views']),row['origin']):row for row in packet['lifted_rows']}
    def admit(self,context,views):
        return context==self.context and len(views)==3 and all(type(v) is int for v in views) and tuple(views) in self.admitted
    def admit_lift(self,context,views,bit):
        return self.admit(context,views) and type(bit) is int and (tuple(views),bit) in self.lifts
    def step(self,context,views,bit,label):
        if not self.admit_lift(context,views,bit):raise ValueError('UNADMITTED_LIFT')
        try:index=self.label_index[json.dumps(list(label),separators=(',',':'))]
        except KeyError:raise ValueError('UNDECLARED_LABEL')
        accepted,next_views,next_bit=self.lifts[tuple(views),bit]['transitions'][index]
        return accepted,tuple(next_views),next_bit
    def check_transition(self,context,views,bit,label,accepted,next_views,next_bit):
        return self.step(context,views,bit,label)==(accepted,tuple(next_views),next_bit)

def main():
    path=OUT/'causal-interface-construction.json';data=load(path)
    parent=load(OUT/'causal-interface-construction-contract.json')
    names=['source','acquisition','recipient'];labels=parent['labels']
    contract={'schema':'relational-membership-and-live-witness-v1','input_sha256':sha(path),
      'input_contract_sha256':sha(OUT/'causal-interface-construction-contract.json'),
      'views':'The three isolated current-language quotients, with full extension actions subsequently admitted only through witnessed transitions.',
      'local_view_order':names,'context':parent['context'],'labels':labels,
      'bounds':{'membership_witness_bits':0,'live_witness_bits':1,'admitted_tuple_rows':61,'lifted_rows':70,'transition_cells':1260},
      'witness_meaning':'origin_is_01, truthfully initialized from the known actual prefix and faithfully retained; not an arbitrary complete-source-state identifier.',
      'membership':'Existence of a same-state realization in the closed source-bound carrier, not evidence that it is the actual current execution.',
      'runtime':'Only a preverified tuple relation and compiled transition kernel; no hidden concrete-source records or complete histories consulted.',
      'trust':'Known truthful initialization, faithful retention, fixed context and the existing atomic source-authorized operation semantics.',
      'attack':'Existentially projecting each step may allow incompatible intermediate source witnesses to switch between steps.',
      'scope':'Finite closed family, no arbitrary future proofs, signatures, physical acquisition or delayed-network guarantee.'}
    cp=OUT/'relational-membership-live-witness-contract.json';save(cp,contract)
    subprocess.run([sys.executable,str(ROOT/'nima/checkers/verify_causal_observer_interface.py')],check=True,capture_output=True,text=True)
    states=data['states'];table=data['transitions'];outputs=data['outputs']
    views=[tuple(data['naive_local_partitions'][name][i] for name in names) for i in range(len(states))]
    bits=[s[1] for s in states];relation=set(views);lifts={}
    fibers=defaultdict(list)
    for i,v in enumerate(views):fibers[v].append(i)
    assert len(states)==70 and len(relation)==61
    for i,(v,bit) in enumerate(zip(views,bits)):
        key=v,bit;row={'views':list(v),'origin':bit,'output':outputs[i],
                     'transitions':[[a,list(views[j]),bits[j]] for a,j in table[i]]}
        if key in lifts:assert lifts[key]==row
        lifts[key]=row
    assert len(lifts)==70
    context=digest(parent['context'])
    packet={'schema':'bounded-source-compatible-runtime-kernel-v1','context_sha256':context,'labels':labels,
      'admitted_view_tuples':[list(v) for v in sorted(relation)],
      'lifted_rows':[lifts[k] for k in sorted(lifts)],
      'packet_scope':'Tuples are local quotient values. One bit selects behaviorally necessary origin; no original state IDs or words are stored.'}
    packet_path=OUT/'relational-live-witness-runtime.json';save(packet_path,packet)
    runtime=Runtime(load(packet_path))
    # Exhaust soundness and completeness, including every incompatible tuple.
    carriers=[sorted(set(data['naive_local_partitions'][name])) for name in names]
    membership_checks=0
    for v in product(*carriers):
        assert runtime.admit(context,v)==bool(fibers.get(v));membership_checks+=1
        for bit in (0,1):assert runtime.admit_lift(context,v,bit)==any(bits[i]==bit for i in fibers.get(v,[]))
    assert not runtime.admit('foreign-context',views[0])
    assert not runtime.admit_lift(context,views[0],True)
    checks=0
    for i,v in enumerate(views):
        for label,(a,j) in zip(labels,table[i]):
            assert runtime.step(context,v,bits[i],label)==(a,views[j],bits[j])
            assert bits[j]==bits[i];checks+=1
    for i in data['initial_state_ids']:assert runtime.admit_lift(context,views[i],bits[i])
    # Relations retain accepted/rejected strata as separate labels.
    strata=[(label,accepted) for label in range(18) for accepted in (False,True)]
    concrete=[{(i,j) for i,row in enumerate(table) for a,j in [row[label]] if a==accepted} for label,accepted in strata]
    def project(rel):return {(views[i],views[j]) for i,j in rel}
    def witness_image(rel):return {((views[i],bits[i]),(views[j],bits[j])) for i,j in rel}
    projected=list(map(project,concrete));lifted=list(map(witness_image,concrete))
    failures=0;strict_examples=[]
    for i,j in product(range(36),repeat=2):
        exact=project(compose(concrete[i],concrete[j]));coarse=compose(projected[i],projected[j])
        assert exact<=coarse
        if exact!=coarse:
            failures+=1
            if len(strict_examples)<4:strict_examples.append({'first':list(strata[i]),'second':list(strata[j]),'spurious_pairs':len(coarse-exact)})
        assert witness_image(compose(concrete[i],concrete[j]))==compose(lifted[i],lifted[j])
        assert opposite(compose(concrete[i],concrete[j]))==compose(opposite(concrete[j]),opposite(concrete[i]))
    for i in range(36):
        assert project(opposite(concrete[i]))==opposite(projected[i])
        assert witness_image(opposite(concrete[i]))==opposite(lifted[i])
    first=strata.index((16,True));second=strata.index((17,True))
    assert labels[16]==['audit-origin',0] and labels[17]==['audit-origin',1]
    assert not compose(concrete[first],concrete[second])
    spurious=compose(projected[first],projected[second]);assert len(spurious)==9
    v=sorted(spurious)[0][0];assert (v,v) in spurious
    assert runtime.admit_lift(context,v,0) and runtime.admit_lift(context,v,1)
    # Either selector is a possible state. A transition cannot silently flip it.
    a,nv,nb=runtime.step(context,v,0,labels[16]);assert a and nb==0
    assert runtime.step(context,nv,nb,labels[17])[0] is False
    assert not runtime.check_transition(context,v,0,labels[16],True,nv,1)
    # Reverse compatibility may have multiple predecessors; none is selected.
    max_backward=max(len({a for a,b in rel if b==target}) for rel in lifted for target in {b for a,b in rel})
    assert max_backward>=2
    histogram=defaultdict(int)
    for indices in fibers.values():histogram[len({data['new_partition'][i] for i in indices})]+=1
    assert dict(histogram)=={1:52,2:9}
    # Every double fiber needs two distinguishable selector values for faithful
    # extended execution; the earlier minimality certificate supplies witnesses.
    assert len(set(data['new_partition']))==70
    assert sha(path)==contract['input_sha256']
    report={'verdict':'MEMBERSHIP_AND_FAITHFUL_SELECTION_SEPARATED','contract_sha256':sha(cp),'runtime_sha256':sha(packet_path),
      'local_carrier_sizes':list(map(len,carriers)),'all_local_tuples_checked':membership_checks,
      'jointly_admitted_tuples':61,'inadmissible_tuples_rejected':membership_checks-61,
      'behavioral_fiber_histogram':dict(histogram),'membership_witness_bits':0,'live_selector_bits':1,
      'compiled_lifted_rows':70,'runtime_transition_checks':checks,
      'relation_compositions_checked':1296,'existential_projection_composition_failures':failures,
      'first_composition_failures':strict_examples,
      'explicit_false_path':{'views':list(v),'accepted_labels':[labels[16],labels[17]],
        'coarse_projection_allows_both':True,'same_source_realizations':0,'spurious_diagonal_pairs':9},
      'witnessed_composition_and_transpose':'All 1296 stratum-pair compositions and 36 transposes commute with witnessed encoding.',
      'maximum_backward_predecessors':max_backward,
      'provenance_attack':'Both bit values can pass existential admission at a double fiber. Only truthful initialization and checked unchanged-bit updates select the actual run.',
      'representation_scope':'Views plus selector determine the 70-state minimal behavior, necessarily; they do not recover the 638 concrete histories. The bound includes the fixed verifier tables, not merely a claimed one-bit payload.',
      'interpretation':'Projected relations preserve transpose but can invent composite paths by switching witnesses. Retaining the same behavioral witness across steps repairs this finite case.'}
    save(OUT/'relational-membership-live-witness.json',report)
    print(json.dumps({k:report[k] for k in ('verdict','all_local_tuples_checked','jointly_admitted_tuples','behavioral_fiber_histogram','runtime_transition_checks','existential_projection_composition_failures','maximum_backward_predecessors')},indent=2))
if __name__=='__main__':main()
