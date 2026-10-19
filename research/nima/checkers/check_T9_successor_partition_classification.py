# /// script
# dependencies = ["sympy"]
# ///
"""Classify successor-key ambiguity under the existing retained-family contract.

Original137 rows/values/masses and first incoming fibres are fixed. Only the
first promoted targets vary by a declared quotient of the32 grouping keys.
These are controls, not new physically selected T9s.
"""
from contextlib import redirect_stdout
from dataclasses import replace
from itertools import combinations
from pathlib import Path
import hashlib
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/T9-successor-partition-classification.json'
OUT.unlink(missing_ok=True)
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
with redirect_stdout(io.StringIO()):
    family=runpy.run_path(str(HERE/'check_native_family_feedback_binding.py'))
m=family['m']; rows=m['source']
check('native-family-and-record-binding-fresh',family['result']['verification_status']=='pass')
first=m['incoming_promotion'](rows,1,'inherited')
N=len(first)
check('actual32-first-fibres-fixed',N==32)
base_read=m['read_at_four'](m['indexed'](rows,'target'))

def normalize(values):
    names={}; out=[]
    for value in values:
        if value not in names: names[value]=len(names)
        out.append(names[value])
    return tuple(out)

partitions=set()
# Every possible final family COUNT, without assuming count selects physics.
for count in range(1,N+1):
    merged=N-count+1
    partitions.add(normalize([0]*merged+list(range(1,count))))
# Exhaust all minimal nontrivial coarsenings of the actual32-fibre relation.
for i,j in combinations(range(N),2):
    values=list(range(N)); values[j]=values[i]
    partitions.add(normalize(values))
profiles=[]
for number,partition in enumerate(sorted(partitions)):
    # The old target determines first-family membership. Successor keys are
    # declared quotient labels. Member values, masses and packets never change.
    supplied=tuple(replace(row,target=('partition-port',1,partition[i])) for i,row in enumerate(first))
    final=m['incoming_promotion'](supplied,2,'inherited')
    expected_count=len(set(partition))
    check('successor-partition-count/'+str(number),len(final)==expected_count)
    check('original-leaves-and-endpoints/'+str(number),m['leaves'](final)==rows)
    check('original-member-mass/'+str(number),sum(row.mass for row in final)==137)
    check('endpoint-uniqueness/'+str(number),len({(row.source,row.target) for row in final})==expected_count)
    right6=final; right5=m['indexed'](final,'source'); right4=m['indexed'](m['unindex'](right5),'target')
    def T9(input_rows):
        mid=m['incoming_promotion'](input_rows,1,'inherited')
        return m['incoming_promotion'](tuple(replace(row,target=('partition-port',1,partition[i])) for i,row in enumerate(mid)),2,'inherited')
    left11=m['indexed'](rows,'source'); left10=m['indexed'](m['unindex'](left11),'target')
    check('upper-presentation-square/'+str(number),m['indexed'](T9(m['unindex'](left11)),'source')==right5)
    check('lower-presentation-square/'+str(number),m['indexed'](T9(m['unindex'](left10)),'target')==right4)
    check('unchanged-J4/'+str(number),m['read_at_four'](right4)==base_read)
    weights=[row.mass for row in final]
    support=sum(weight**2 for weight in weights)
    profiles.append({'partition':partition,'final_rows':expected_count,'supported_leaf_pairs':support})
check('all-final-counts-realized',{p['final_rows'] for p in profiles}==set(range(1,33)))
check('all496-one-merge-controls-present',sum(p['final_rows']==31 for p in profiles)==496)
check('strict-support-increases-for-coarsenings',all(p['supported_leaf_pairs']>977 for p in profiles if p['final_rows']<32))
check('known-extreme-supports-recovered',{p['supported_leaf_pairs'] for p in profiles if p['final_rows'] in (1,32)}=={977,18769})

# Bell recurrence counts ALL equivalence relations on32 distinguished fibres.
# It is not an exhaustive numerical run over that enormous set.
bell=[1]
for n in range(1,N+1):
    from math import comb
    bell.append(sum(comb(n-1,k)*bell[k] for k in range(n)))
check('bell-recurrence-base-controls',bell[:6]==[1,1,2,5,15,52])
source_paths=[ROOT.parents[1]/'docs/system-characteristics.md',ROOT/'rung-transport-diagram-and-fixed-reference.md',
              ROOT/'native-promotion-constructor-trace.md',ROOT/'native-family-feedback-binding.md']
result={
 'schema':'marici.nima.T9-successor-partition-classification.v1','verification_status':'pass','checks':checks,
 'fixed_first_fibres':32,'tested_distinct_partitions':len(profiles),'partition_controls':profiles,
 'all_successor_relations_up_to_port_renaming':str(bell[32]),
 'classification_argument':'A successor map on32 first-family keys induces a kernel partition. Conversely every partition is realized by its block-label map. Second incoming promotion groups exactly those blocks.',
 'general_readout_argument':'sum_blocks(M_B/137)*sum_members(m_i/M_B)*C_i=sum_i(m_i/137)*C_i. Original leaves and fixed d4 are unchanged; presentation maps are invertible retained indexing.',
 'not_claimed':'Only the listed527 controls are executed; the all-partition statement follows from the explicit construction and algebra, not finite extrapolation.',
 'intended_T9_status':'Not identifiable from retained reconstruction, endpoint uniqueness, presentation squares, or unchanged J4. Any selection requires an additional context/successor contract.',
 'objective_complete':False,
 'source_specification_sha256':{str(p.relative_to(ROOT.parents[1])).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths},
 'missing_selection_fields':['successor equivalence relation on original target fibres','whether mean aggregation or another family operation is intended','member measure and protected response task'],
 'scope':'Fixed input fixture and fixed two-round incoming-family former, with arbitrary declared first successor-key maps. Other native constructors are not classified.'}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} successor-partition classification checks; {len(profiles)} exact candidates')
print(f'Every target size1..32 passes; all496 one-merge controls retain the same J4.')
print(f'Total successor context partitions on32 fixed fibres: {bell[32]}.')
