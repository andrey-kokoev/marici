"""Freeze tests on source link positions, evaluate on one mask; completed wiring orbits only for validation. Greedy deletion is a pilot compression, not a minimum certificate."""
from ramsey_six_boundary_moves import G,ws,D,json,E,P,combinations,Counter,A,B,R
from collections import defaultdict
from math import comb
n=len(E);I=tuple(range(n));G0={I};stack=[I]
while stack:
    g=stack.pop()
    for s in G:
        h=tuple(s[j] for j in g)
        if h not in G0:G0.add(h);stack.append(h)
assert len(G0)==8

def fam(k):
    todo=set(combinations(range(n),k));out=[]
    while todo:
        t=min(todo);o={tuple(sorted(g[j] for j in t)) for g in G0};todo-=o;out.append((t,sorted(sum(1<<j for j in u) for u in o)))
    return out

def addr(i):return '-'.join(''.join(map(str,P[j])) for j in E[i])
words=sorted(ws);spec=[];columns=[];stages=[];labels=[];idx={w:i for i,w in enumerate(words)};true=[min(sum((w>>i&1)<<k for i,k in enumerate(g)) for g in G0) for w in words];reps=[idx[w] for w in sorted(set(true))];assert len(reps)==36
for k in (1,2,3):
    for t,masks in fam(k):
        x=tuple(sum((w&m)==m for m in masks) for w in words);assert all(x[i]==x[idx[true[i]]] for i in range(len(words)));columns.append(x);spec.append((t,masks))
    keys=list(zip(*columns));levels=Counter(Counter(keys[i] for i in reps).values());stages.append(dict(degree=k,features=len(columns),number_keys=len(set(keys)),cubes_per_key=levels))
    if len(set(keys))==36:break
assert len(set(keys))==36;pending=set(combinations(reps,2));chosen=[]
while pending:
    score=lambda j:(sum(columns[j][a]!=columns[j][b] for a,b in pending),-len(spec[j][0]),-j);j=max(range(len(spec)),key=score);chosen.append(j);pending={(a,b) for a,b in pending if columns[j][a]==columns[j][b]}
for j in chosen[::-1]:
    sub=[k for k in chosen if k!=j];
    if len({tuple(columns[k][i] for k in sub) for i in reps})==36:chosen=sub
mini=lambda i:[columns[j][i] for j in chosen];assert len({tuple(mini(i)) for i in reps})==36
from ramsey_six_boundary_moves import seed
r=dict(stages=stages,seed_label=mini(idx[seed]),row_mate_label=mini(idx[R[seed]]),greedy_counts=[dict(template=[addr(i) for i in spec[j][0]],orbit_size=len(spec[j][1]),masks=spec[j][1]) for j in chosen],distinct_links_read=len({i for j in chosen for m in spec[j][1] for i in range(n) if m>>i&1}),labels=[mini(i) for i in reps]);print(stages);print([(o['template'],o['orbit_size']) for o in r['greedy_counts']],r['distinct_links_read']);(D/'ramsey_six_component_label.json').write_text(json.dumps(r,indent=2)+'\n')
