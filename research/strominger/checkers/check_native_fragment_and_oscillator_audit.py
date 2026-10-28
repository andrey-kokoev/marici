"""Exact finite fragment checks and passive-pulse rank obstruction.
No legacy receipts are overwritten; no new physical primitives are admitted.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib, json, re
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger'
fragment=BASE/'contracts/native-query-source-fragment.v1.json'
audit=BASE/'contracts/directed-transition-oscillator-candidate-audit.v1.json'
spec=json.loads(fragment.read_text());candidate=json.loads(audit.read_text())
native=ROOT/'research/nima/agda/NativeSeedTransitionProbe.agda'
text=native.read_text(encoding='utf-8')
def table(name):
    rows=dict(re.findall(r'^'+name+r' ([ABCD]) = ([ABCD])$',text,re.M))
    assert set(rows)==set('ABCD')
    return tuple('ABCD'.index(rows[v]) for v in 'ABCD')
abc,adb=table('abc'),table('adb')
def comp(h,g):return tuple(h[g[i]] for i in range(4))
identity=tuple(range(4));seen={identity};todo=[identity]
for g in todo:
    for h in (abc,adb):
        hg=comp(h,g)
        if hg not in seen:seen.add(hg);todo.append(hg)
G=sorted(seen);assert len(G)==12
states=list(product(G,(0,1)))
source=BASE/'contracts/task-relative-memory-selection.v1.json'
edges=json.loads(source.read_text())['source']['edges']
edge={e:('ABCD'.index(a),'ABCD'.index(b)) for e,a,b in edges}
names=list(spec['generators'])
assert set(names)=={'L_ABC','L_ADB'}|{'Q_'+e for e in edge}
def step(name,state):
    g,b=state
    if name=='L_ABC':return comp(abc,g),b
    if name=='L_ADB':return comp(adb,g),b
    if name.startswith('Q_') and name[2:] in edge:
        a,t=edge[name[2:]];return g,b^int(g[a]==t)
    raise ValueError('Unknown generator')
def run(word,state):
    for name in word:state=step(name,state)
    return state
for name in names:
    assert set(step(name,s) for s in states)==set(states)
    power=3 if name.startswith('L_') else 2
    assert all(run([name]*power,s)==s for s in states)
words=[w for length in range(4) for w in product(names,repeat=length)]
for word in words:
    for state in states:
        for split in range(len(word)+1):
            assert run(word,state)==run(word[split:],run(word[:split],state))
for invalid in ('Q_AA','RESET','AB'):
    try:step(invalid,states[0])
    except ValueError:pass
    else:raise AssertionError('Undeclared syntax accepted')
assert ('Q_AB','Q_AB')!=() and all(run(('Q_AB','Q_AB'),s)==s for s in states)
def rank(matrix):
    a=[list(map(F,row)) for row in matrix];r=0
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];d=a[r][c];a[r]=[x/d for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                d=a[i][c];a[i]=[x-d*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r
# The source oscillator's 24 S4 coordinates, not the twelve A4 coordinates.
S4=list(permutations(range(4)));labels=list(edge)
features={e:[F(g[edge[e][0]]==edge[e][1]) for g in S4] for e in labels}
for f in features.values():assert sum(f)==6
# Raw coordinates have metric counting/6 on carrier, identity on records.
metric=[F(1,6)]*24+[F(1)]*6
vectors=[features[e]+[F(-int(e==name)) for name in labels] for e in labels]
assert rank(vectors)==6
for v in vectors:assert sum(m*x*x for m,x in zip(metric,v))==2
# Each projector is v (v^T M)/2. All angle-dependent departures from identity
# therefore have range in the SAME six-dimensional span and kill its orthogonal complement.
L=[states.index(step('L_ABC',s)) for s in states]
LminusI=[[F(L[j]==i)-F(i==j) for j in range(24)] for i in range(24)]
assert rank(LminusI)==16
remaining=set(range(24));cycles=[]
while remaining:
    start=min(remaining);cycle=[];i=start
    while i not in cycle:cycle.append(i);remaining.remove(i);i=L[i]
    assert i==start;cycles.append(cycle)
assert [len(c) for c in cycles]==[3]*8
assert candidate['added_primitives']==[] and candidate['accepted_physical_model'] is False
assert len(candidate['checklist'])==8
paths=[fragment,audit,native,source,Path(__file__).resolve(),BASE/'native-fragment-and-oscillator-audit-v1.md']
paths += [ROOT/s for s in candidate['sources']]
report={'status':'pass','source_states':24,'generators':8,'words_through_length_three':len(words),
        'source_specification':'declared, with exact finite semantics; native all-word embedding remains a proof obligation',
        'audit':'complete with missing interfaces and scoped linear obstruction',
        'oscillator_modes':30,'pulse_direction_rank':6,'common_fixed_dimension':24,
        'target_triangle_minus_identity_rank':16,'target_three_cycles':8,
        'obstruction':'No faithful linear amplitude/single-excitation intertwiner from the target 24-state representation into the six-pulse 30-mode model.',
        'physical_model_accepted':False,'new_Agda_check':False,
        'sha256':{str(f.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in paths}}
out=BASE/'results/native-fragment-and-oscillator-audit/verification.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='sha256'}))
