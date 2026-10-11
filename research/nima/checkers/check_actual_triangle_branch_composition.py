"""Compose the actual two seed components with unit occurrence counts.

Unit counts are structural indicators, not physically prepared amplitudes.
The existing registered endpoint product is reused without a new update law.
Component roles remain attached; merging them can cancel branch detail.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_natural_tower_return import PACKETS
from retained_path_successor import RetainedSuccessorLedger

ROOT=Path(__file__).resolve().parents[1]
ledger=RetainedSuccessorLedger(PACKETS)
root=ledger.root
child=ledger.successor(root)
words=tuple(tuple(e[2] for e in path) for path in child.paths)
word_index={word:i for i,word in enumerate(words)}
components={'L':('AB','BC','CA'),'R':('BA','AD','DB')}
registry={label:(source,target) for label,source,target in PACKETS}
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)


def component(owner,source_ledger):
    wanted=set(components[owner])
    paths=tuple(p for p in source_ledger.root.paths if p[0][2] in wanted)
    return source_ledger.retain_path_payload(paths,(F(1),)*len(paths))


def extend_to_full(payload):
    result=[F(0)]*len(words)
    for path,value in zip(payload.paths,payload.values):
        result[word_index[tuple(e[2] for e in path)]]=value
    return tuple(result)


L,R=component('L',ledger),component('R',ledger)
check('actual-disjoint-occurrence-components',set(components['L']).isdisjoint(components['R'])
      and set(components['L'])|set(components['R'])==set(registry))
for name,cycle in components.items():
    check('actual-cycle-attachment/'+name,all(registry[a][1]==registry[b][0]
          for a,b in zip(cycle,cycle[1:]+cycle[:1])))

products={}
report={}
for name,left,right in [('LL',L,L),('LR',L,R),('RL',R,L),('RR',R,R)]:
    p=ledger.compose_payloads(left,right)
    parents,slots=ledger.deconstruct_payload(p)
    check('retained-operands/'+name,parents[0] is left and parents[1] is right)
    check('occurrence-counts/'+name,all(v==1 for v in p.values))
    full=extend_to_full(p)
    means,residual=ledger.split_payload(child,full)
    check('exact-successor-reconstruction/'+name,ledger.reassemble_payload(child,means,residual)==full)
    summary=ledger.summarize(child,full)
    products[name]=full
    report[name]={
        'words':[list(tuple(e[2] for e in path)) for path in p.paths],
        'parent_means':[str(v) for v in means],
        'branch_detail':{','.join(word):str(v) for word,v in zip(words,residual) if v},
        'final_occurrence_summary':[str(v) for v in summary],
        'detail_final_summary':[str(v) for v in ledger.summarize(child,residual)],
    }
    if name in ('LR','RL'):
        check('nonzero-cross-branch-detail/'+name,any(residual))
        check('detail-not-only-coarse-hidden/'+name,any(ledger.summarize(child,residual)))
check('forward-cross-words',set(map(tuple,report['LR']['words']))=={('AB','BA'),('CA','AD')})
check('reverse-cross-words',set(map(tuple,report['RL']['words']))=={('BA','AB'),('DB','BC')})
check('source-ten-word-domain',len(words)==10)

def target_read(values):
    return tuple(sum(value for word,value in zip(words,values) if registry[word[-1]][1]==vertex)
                 for vertex in 'ABCD')

left_targets=target_read(products['LR'])
right_targets=target_read(products['RL'])
check('actual-target-readout-LR',left_targets==(1,0,0,1))
check('actual-target-readout-RL',right_targets==(0,1,1,0))
check('opposite-role-contrast',tuple(a-b for a,b in zip(left_targets,right_targets))==(1,-1,-1,1))
for name in ('LR','RL'):
    _,residual=ledger.split_payload(child,products[name])
    report[name]['target_counts']=list(map(str,target_read(products[name])))
    report[name]['detail_target_counts']=list(map(str,target_read(residual)))
    check('detail-visible-at-actual-endpoints/'+name,any(target_read(residual)))
combined=tuple(sum(products[k][i] for k in products) for i in range(10))
check('all-products-partition-full-domain',combined==(F(1),)*10)
_,unlabelled_detail=ledger.split_payload(child,combined)
check('forgetting-component-roles-cancels-detail',not any(unlabelled_detail))
cross=tuple(products['LR'][i]+products['RL'][i] for i in range(10))
check('mixed-composition-residual',cross==tuple(combined[i]-products['LL'][i]-products['RR'][i] for i in range(10)))
check('cross-domain-has-four-words',sum(cross)==4)

# Separate all shared vertex identities between the two original components,
# retaining each primitive occurrence and its local endpoints/order.
owner={label:name for name,labels in components.items() for label in labels}
unglued=tuple((label,(owner[label],s),(owner[label],t)) for label,s,t in PACKETS)
other=RetainedSuccessorLedger(unglued)
UL,UR=component('L',other),component('R',other)
for name,left,right in [('LR',UL,UR),('RL',UR,UL)]:
    p=other.compose_payloads(left,right)
    check('ungluing-removes-cross-domain/'+name,len(p.paths)==0 and p.operation=='compose')
for name,left in [('LL',UL),('RR',UR)]:
    p=other.compose_payloads(left,left)
    check('ungluing-preserves-local-cycle-products/'+name,
          set(tuple(e[2] for e in path) for path in p.paths)==set(map(tuple,report[name]['words'])))

# Counted multiplicities versus amplitudes: changing an operand coefficient
# changes the result, but the source incidence does not select physical units.
check('zero-extended-role-counts-not-creation-from-zero',
      ledger.compose_primitive_payloads(child,(F(0),)*6,(F(1),)*6)==(F(0),)*10)
result={
    'schema':'marici.nima.actual-triangle-branch-composition.v1','status':'pass','checks':checks,
    'source_components':components,'primitive_order':ledger.labels,'successor_words':[list(w) for w in words],
    'products':report,
    'positive_result':'actual component occurrence indicators produce nonzero cross successor detail via existing endpoint composition; no signed amplitude fixture or new coupling inserted',
    'role_boundary':'summing all four role-labelled products gives the uniform ten-word count and zero branch detail',
    'target_contrast':'LR-RL gives (1,-1,-1,1) on actual A,B,C,D endpoints; a structural count contrast, not yet the physical rung-4 observer',
    'source_dependence':'ungluing the components removes the four cross words while preserving six local words',
    'physical_boundary':'these are structural counts and exact coefficient readouts, not energy, physical preparation, executed interactions, or identification with the intended 137-row rung-4 reference',
    'next_gate':'bind this component-labelled retained successor to the intended rung-4 observer and native operation admission without replacing counts by physical amplitudes',
    'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
        [Path(__file__),ROOT/'checkers/retained_path_successor.py',ROOT/'checkers/check_natural_tower_return.py']},
}
(ROOT/'results/actual-triangle-branch-composition.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact actual-component composition checks')
for name in ('LR','RL'):
    print(name,report[name])
print('Role-labelled detail is nonzero; merging all roles cancels it. Ungluing removes the cross domain.')
