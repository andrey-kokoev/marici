"""Direct (3,8) test on all subsets of four labeled optional blue ports; extract minimal forbidden supports and minimal transversals."""
from itertools import combinations
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results'
z=json.loads((D/'ramsey_cube_third_depth.json').read_text())['unrestricted'];A,C=z['first'];B=z['later'][0];ports=dict(a=A,b=B,c=C,e=0)
def subsets(s):return [frozenset(q) for i in range(len(s)+1) for q in combinations(s,i)]
def minimal(rows):return [q for q in rows if not any(p<q for p in rows)]
def inspect(root,q):
    v=list(range(1,13))+['root']+sorted(q);supports={'root':root,**ports}
    def red(i,j):
        if isinstance(j,int):return j==i+1
        return isinstance(i,int) and bool(supports[j]>>(i-1)&1)
    edges={frozenset((i,j)) for i,j in combinations(v,2) if red(i,j)}
    assert not any(all(frozenset(p) in edges for p in combinations(t,2)) for t in combinations(v,3))
    return next((t for t in combinations(v,8) if all(frozenset(p) not in edges for p in combinations(t,2))),None)
def run(root):
    Q=subsets(ports);w={q:inspect(root,q) for q in Q};bad=minimal([q for q in Q if w[q]]);reps=minimal([q for q in Q if all(q&h for h in bad)])
    assert all(bool(w[q])==any(h<=q for h in bad) for q in Q)
    return dict(columns=list(ports),rows=[dict(slots=sorted(h),incidence=[int(i in h) for i in ports],blue_eight=w[h]) for h in bad],legal_subsets=sum(t is None for t in w.values()),minimal_repairs=[sorted(q) for q in reps])
r={s:run(root) for s,root in [('A',A),('C',C)]};print(r);(D/'ramsey_path_conflict_tensor.json').write_text(json.dumps(r,indent=1)+'\n')
