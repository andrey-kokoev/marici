"""Compile the known state-000 solution into one predicate per geometric type of unordered disjoint cube-feature pair. Evaluation/verification uses NO completed graph, chart fits, or SAT solver (compile is separate). Words read least-significant coordinate first."""
from itertools import permutations,product,combinations
from pathlib import Path
import json,sys
D=Path(__file__).parent
F=sorted(''.join(x) for x in product('01*',repeat=3) if x.count('*')<3);edges=[(a,b) for a,b in combinations(F,2) if any({x,y}=={'0','1'} for x,y in zip(a,b))];G=[]
for p in permutations(range(3)):
    parity=sum(a>b for a,b in combinations(p,2))%2
    for fl in product(range(2),repeat=3):
        rev=(parity+sum(fl))%2
        def act(f,p=p,fl=fl,rev=rev,state=False):return ''.join('*' if f[p[j]]=='*' else str(int(f[p[j]])^fl[j]^(rev if state else 0)) for j in range(3))
        G.append(act)
V=sorted(x for x in F if '*' not in x)

def compile_rules():
    from ramsey_address_to_cube import S
    co=json.loads((D/'ramsey_nine_opposite_faces.json').read_text())['label_coordinates'];T=[]
    for m in S:
        v=[co[i] for i in range(8) if m>>i&1];T.append(''.join('*' if len({u>>i&1 for u in v})==2 else str(v[0]>>i&1) for i in range(3)))
    w=json.loads((D/'ramsey_nine_frame_readout.json').read_text())['coordinate_ordered_wirings'][0];red={tuple(sorted((T[i],T[j]))) for h,(i,j) in enumerate((e for e in combinations(range(26),2) if not S[e[0]]&S[e[1]])) if w>>h&1};rules={}
    for e in edges:
        orbit=[tuple(sorted(map(g,e))) for g in G];rep=min(orbit)
        if e!=rep:continue
        allowed={g('000',state=True) for g in G if next(k for k in edges if tuple(sorted(map(g,k)))==rep) in red};rules[' '.join(rep)]=sorted(allowed)
    return rules

def verify_rules(rules):
    lookup={}
    for pair,R in rules.items():
        for g in G:
            e=tuple(sorted(map(g,pair.split())));U={g(x,state=True) for x in R};assert lookup.setdefault(e,U)==U
    assert set(lookup)==set(edges);from verify_ramsey_catalogue_free_chain import verify
    masks=[]
    for c in V:
        A=[0]*35
        def link(i,j):A[i]|=1<<j;A[j]|=1<<i
        for j,v in enumerate(V):
            link(0,j+1)
            for i,f in enumerate(F):
                if all(a=='*' or a==b for a,b in zip(f,v)):link(j+1,9+i)
        for (a,b),cs in lookup.items():
            if c in cs:link(9+F.index(a),9+F.index(b))
        masks.append(tuple(A));assert verify(A,9)==(35,140,8)
    assert len(set(masks))==8;print('verified all eight from cube rules')
if __name__=='__main__':
    path=D/'ramsey_cube_pair_rules.json'
    if '--compile' in sys.argv:path.write_text(json.dumps(compile_rules(),indent=2)+'\n')
    rules=json.loads(path.read_text());print(rules);verify_rules(rules)
