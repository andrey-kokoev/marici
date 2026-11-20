"""Separate two notions of independence: literal row-copy transport (no closed walk swaps the copies) versus disconnection of folded prism rims. Hold exit D out, isolate entry A, and enumerate the minimal extra deletions for copy transport."""
from itertools import combinations
from ramsey_strip_prism_proof import labels,E,V,r,rep,P,T
inv={v:i for i,v in labels.items()};N=[set() for _ in r]
for i,d in enumerate(P):
    for j,m in enumerate(T,15):
        if d in m:N[i].add(j);N[j].add(i)
def step(x,w):
    y,=[y for y in N[x] if rep(y)==inv[w]];return y
def twist(word):
    x=inv[word[0]];y=x
    for w in word[1:]+word[:1]:y=step(y,w)
    assert y in (x,r[x]);return y!=x
def consistent(keep):
    lifts={}
    for root in sorted(keep):
        if root in lifts:continue
        lifts[root]=inv[root];q=[root]
        for v in q:
            for w in keep:
                if tuple(sorted((v,w))) not in E:continue
                y=step(lifts[v],w)
                if w in lifts and lifts[w]!=y:return False
                if w not in lifts:lifts[w]=y;q.append(w)
    return True
faces={k:[v+k for v in 'abcd'] for k in '01'};faces.update({a+b:[a+'0',b+'0',b.upper(),b+'1',a+'1',a.upper()] for a,b in zip('abcd','bcda')});print('sheet swap around each face',{k:twist(v) for k,v in faces.items()});base=V-{'D','a0','a1'};print('without extra cuts',consistent(base));
for k in range(len(base)+1):
    hits=[s for s in combinations(sorted(base-{'A'}),k) if consistent(base-set(s))];
    if hits:print('minimum extra deletions',hits);break
assert not consistent(base) and consistent(base-{'B'}) and consistent(base-{'C'});assert all(twist(v) for v in faces.values());
