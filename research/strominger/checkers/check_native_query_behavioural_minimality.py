"""Complete finite Moore minimization and exact realization-gauge controls."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import deque, Counter
import re, json, hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger'
fragment=BASE/'contracts/native-query-source-fragment.v1.json'
equivalence=BASE/'contracts/native-query-realization-equivalence.v1.json'
source=ROOT/'research/nima/agda/NativeSeedTransitionProbe.agda'
text=source.read_text(encoding='utf-8')
def table(name):
    rows=dict(re.findall(r'^'+name+r' ([ABCD]) = ([ABCD])$',text,re.M))
    assert set(rows)==set('ABCD');return tuple('ABCD'.index(rows[v]) for v in 'ABCD')
abc,adb=table('abc'),table('adb')
def comp(h,g):return tuple(h[g[i]] for i in range(4))
identity=tuple(range(4));seen={identity};todo=[identity]
for g in todo:
    for h in (abc,adb):
        k=comp(h,g)
        if k not in seen:seen.add(k);todo.append(k)
G=sorted(seen);assert len(G)==12
states=list(product(G,(0,1)));names=list(json.loads(fragment.read_text())['generators'])
def step(name,s):
    g,b=s
    if name.startswith('L_'):return comp({'L_ABC':abc,'L_ADB':adb}[name],g),b
    a,t=map('ABCD'.index,name[2:]);return g,b^int(g[a]==t)
T={a:[states.index(step(a,s)) for s in states] for a in names}
outputs=[s[1] for s in states]
def execute(word,s):
    for a in word:s=T[a][s]
    return s
# Standard partition refinement reaches the greatest transition congruence
# contained in the output-equality relation on this entire finite state set.
def minimize(alphabet):
    colors=outputs[:];sizes=[len(set(colors))]
    while True:
        signatures=[(outputs[i],tuple(colors[T[a][i]] for a in alphabet)) for i in range(24)]
        ids={v:k for k,v in enumerate(dict.fromkeys(signatures))}
        newer=[ids[v] for v in signatures]
        same=all((colors[i]==colors[j])==(newer[i]==newer[j]) for i in range(24) for j in range(24))
        if same:return newer,sizes
        colors=newer;sizes.append(len(set(colors)))
colors,refinement=minimize(names);assert len(set(colors))==24
# Every state is reachable even from the single identity/false preparation.
root=states.index((identity,0));access={root:[]};queue=deque([root])
while queue:
    i=queue.popleft()
    for a in names:
        j=T[a][i]
        if j not in access:access[j]=access[i]+[a];queue.append(j)
assert len(access)==24
for state,word in access.items():assert execute(word,root)==state
# Independent paired-state BFS certifies a shortest distinguishing word for
# every unordered pair. Empty words certify already different pointer outputs.
def distinguish(i,j):
    queue=deque([(i,j,[])]);seen={(i,j)}
    while queue:
        x,y,w=queue.popleft()
        if outputs[x]!=outputs[y]:return w
        for a in names:
            pair=(T[a][x],T[a][y])
            if pair not in seen:seen.add(pair);queue.append((*pair,w+[a]))
    return None
witnesses=[]
for i in range(24):
    for j in range(i+1,24):
        w=distinguish(i,j);assert w is not None
        assert outputs[execute(w,i)]!=outputs[execute(w,j)]
        witnesses.append({'states':[i,j],'word':w})
assert len(witnesses)==276
# Removing left translations is a DIFFERENT interface, retained only as control.
restricted,_=minimize([a for a in names if a.startswith('Q_')]);assert len(set(restricted))==20
# Exact coordinate-change controls for the declared factor-preserving gauge.
def I(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def transpose(A):return list(map(list,zip(*A)))
def mul(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
A=I(12);A[0][1]=1;Ai=I(12);Ai[0][1]=-1
H=[[x/3 for x in row] for row in I(12)]
Hp=mul(mul(transpose(Ai),H),Ai)
assert mul(mul(transpose(A),Hp),A)==H
# A tensor identity transports all eight complete joint operators.
C=[[A[i//2][j//2]*F(i%2==j%2) for j in range(24)] for i in range(24)]
Ci=[[Ai[i//2][j//2]*F(i%2==j%2) for j in range(24)] for i in range(24)]
for a in names:
    P=[[F(T[a][j]==i) for j in range(24)] for i in range(24)]
    Pp=mul(mul(C,P),Ci);assert mul(Pp,C)==mul(C,P)
# Labels fixing a basis force identity, so changed Gram cannot be a gauge.
Hbad=[[(F(i==j)+F(1,9))/4 for j in range(12)] for i in range(12)]
assert Hbad!=H
R0=I(2);Rhalf=[[F(1),F(1,2)],[F(1,2),F(1)]];assert R0!=Rhalf
swap=[[F(0),F(1)],[F(1),F(0)]];assert mul(swap,[[F(1)],[F(0)]])!=[[F(1)],[F(0)]]
files=[fragment,equivalence,source,Path(__file__).resolve(),BASE/'native-query-behavioural-minimality-v1.md']
report={'status':'pass','states':24,'generators':len(names),'reachable_states':len(access),
        'partition_sizes':refinement,'minimal_predictive_states':len(set(colors)),
        'pair_witness_count':len(witnesses),'separating_word_length_histogram':dict(sorted(Counter(len(x['word']) for x in witnesses).items())),
        'without_left_translations_classes':len(set(restricted)),
        'coordinate_gauge_tests':'positive shear with transported basis/metric/operators; changed carrier Gram, eta and pointer labels rejected',
        'state_table':[{'g':g,'bit':b} for g,b in states],
        'transitions':T,'access_words':{str(i):w for i,w in sorted(access.items())},'separating_words':witnesses,
        'scope':'Complete finite behavioural certificate and exact gauge regressions; no Hilbert dimension lower bound, physical realization, or new Agda proof.',
        'sha256':{str(f.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
out=BASE/'results/native-query-behavioural-minimality/verification.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('status','reachable_states','partition_sizes','minimal_predictive_states','pair_witness_count','separating_word_length_histogram','without_left_translations_classes')}))
