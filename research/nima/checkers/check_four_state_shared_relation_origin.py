"""Two overlapping presentations generated directly from Bool x Bool."""
from pathlib import Path
from itertools import product
from collections import Counter
from contextlib import redirect_stdout
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    source=runpy.run_path(str(HERE/'check_proton_electron_comparison_slots.py'))
X=tuple(range(4)); E=set(source['E'])
def bits(x): return (x>>1,x&1)
def parity(x):
    a,b=bits(x); return a^b
A={e for e in E if bits(e[0])[0]!=bits(e[1])[0]}
B={e for e in E if bits(e[0])[1]!=bits(e[1])[1]}
first_only=A-B; second_only=B-A; shared=A&B
assert len(E)==12
assert (len(first_only),len(second_only),len(shared))==(4,4,4)
assert (len(A),len(B),len(A|B))==(8,8,12)
assert shared=={e for e in E if parity(e[0])==parity(e[1])}
assert first_only|second_only=={e for e in E if parity(e[0])!=parity(e[1])}
# A relation can be generated and retained without any prior composite particle.
# Its triples are constrained: four states, not eight independent bit choices.
triples={(a,b,a^b) for a,b in product((0,1),repeat=2)}
assert len(triples)==4
assert {(a,r) for a,b,r in triples}==set(product((0,1),repeat=2))
for a,b,r in triples:
    assert b==a^r and a==b^r
# Reversible register realization on all inputs, not only a blank record.
def record_gate(a,b,r): return a,b,r^a^b
assert len({record_gate(*v) for v in product((0,1),repeat=3)})==8
for v in product((0,1),repeat=3): assert record_gate(*record_gate(*v))==v
# Fixing the shared record is an ADDITIONAL compatibility condition. Each value
# permits two states and only a simultaneous two-coordinate transition.
sectors={r:[x for x in X if parity(x)==r] for r in (0,1)}
assert sectors=={0:[0,3],1:[1,2]}
for r,states in sectors.items():
    allowed={(x,y) for x in states for y in states if x!=y}
    assert len(allowed)==2 and allowed<=shared
# Keeping a HISTORY of the relation, instead of fixing it, permits private moves.
history=(parity(0),)
x=2  # 00 -> 10: change only first coordinate
history=history+(parity(x),)
assert history==(0,1) and (0,x) in first_only
# Enumerate all two-state relations with both binary projections present.
relations=[]
for selection in product((0,1),repeat=4):
    R={bits(x) for x,included in zip(X,selection) if included}
    if len(R)==2 and {a for a,b in R}=={0,1} and {b for a,b in R}=={0,1}:
        relations.append(R)
assert len(relations)==2
assert {frozenset(r) for r in relations}=={frozenset({(0,0),(1,1)}),frozenset({(0,1),(1,0)})}
# All six invertible binary coordinate charts give the same8+8-4 decomposition.
charts=0
for entries in product((0,1),repeat=4):
    a,b,c,d=entries
    if (a*d-b*c)%2!=1: continue
    def chart(x):
        u,v=bits(x); return ((a*u+b*v)%2,(c*u+d*v)%2)
    left={e for e in E if chart(e[0])[0]!=chart(e[1])[0]}
    right={e for e in E if chart(e[0])[1]!=chart(e[1])[1]}
    assert (len(left),len(right),len(left&right))==(8,8,4)
    charts+=1
assert charts==6
# Seed-cycle compatibility extension: A,B,C,D identified with 00,01,10,11.
# These are the existing vertex actions, not a newly selected physical law.
seed_cycles=((1,2,0,3),(3,0,2,1))  # ABC, ADB
fixed_functions=[]
for values in product((0,1),repeat=4):
    if all(values[p[x]]==values[x] for p in seed_cycles for x in X):
        fixed_functions.append(values)
assert fixed_functions==[(0,0,0,0),(1,1,1,1)]
# The original parity is changed on two states by either whole seed cycle.
assert [sum(parity(p[x])!=parity(x) for x in X) for p in seed_cycles]==[2,2]
# Transporting the relation, rather than freezing it, preserves its evaluation.
original_record=tuple(parity(x) for x in X)
for p in seed_cycles:
    inverse=tuple(p.index(x) for x in X)
    moved_record=tuple(original_record[inverse[x]] for x in X)
    assert all(moved_record[p[x]]==original_record[x] for x in X)
    assert moved_record!=original_record
# Traceable lift into the existing comparison programme, once that programme
# is admitted: class is the first compared arrow's XOR mask or state offset.
families=Counter()
for outer,(kind,a,b) in source['expanded']:
    mask=(a[0]^a[1]) if kind=='arrow' else a
    assert mask in (1,2,3)
    families[mask]+=1
assert families=={1:612,2:612,3:612}
left=families[2]+families[3]; right=families[1]+families[3]
assert left==right==1224 and left+right-families[3]==1836
result={
 'status':'passed','classification':'four_state_origin_of_overlap_with_conditional_joint_dependence',
 'starting_states':['00','01','10','11'],
 'directed_arrow_classes':{'first_only':sorted(first_only),'second_only':sorted(second_only),'both':sorted(shared)},
 'presentation_arrow_counts':{'first':len(A),'second':len(B),'shared':len(shared),'union':len(E)},
 'retained_relation':'r=a XOR b',
 'fixed_record_sectors':{'0':['00','11'],'1':['01','10']},
 'comparison_programme_lift':{'each_presentation':left,'shared':families[3],'union':1836},
 'seed_cycle_control':{'common_invariant_binary_functions':fixed_functions,
                       'parity_changes_per_generator':[2,2],
                       'transported_relation_preserves_evaluation':True,
                       'scope':'Whole ABC/ADB vertex actions; not a prohibition on fixed-record subphases.'},
 'checks':{'source_count_fresh':True,'all_twelve_arrows_enumerated':True,
           'reversible_relation_recording':True,'two_fixed_record_sectors':True,
           'history_retention_alone_allows_private_changes':True,
           'six_binary_coordinate_charts':True,'comparison_count_lift':True},
 'conclusion':'One four-state carrier supplies two8-arrow presentations sharing4 simultaneous-change arrows. The generated parity record gives joint dependence when compatibility requires that record to remain fixed. Merely retaining its changing history does not impose dependence. The1224/612 lift follows upon adding the existing comparison programme; no larger precursor or particle identification is assumed.',
 'next_falsifier':'Determine whether the cycle boundary actually enforces current compatibility with a fixed retained relation, or allows relation updates. This is the precise additional rule needed for joint dependence.'}
out=HERE.parent/'results/four-state-shared-relation-origin.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
