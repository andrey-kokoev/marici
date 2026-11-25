"""Frozen interface: three separated path blocks, all independent labeled supports for a second port, blue port-port edge. No quotient by automorphisms."""
from itertools import combinations,product
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results'
def trial(edges,k):
    def mask(t):return sum(1<<(v-1) for v in t)
    em=[mask(p) for p in edges];ind=[x for x in range(256) if not any(e&x==e for e in em)];assert max(x.bit_count() for x in ind)<=k-2
    danger=[x for x in ind if x.bit_count()==k-2];sets=[];corners=list(product((1,2),(4,5),(7,8)))
    for s in corners:
        S=mask(s);assert S in ind;E=[t for t in ind if all((S|t)&x for x in danger)];sets.append(E)
        # Independent check on complete ten-vertex graphs, enumerating forbidden monochromatic sets directly.
        for t in ind:
            red=set(tuple(sorted(p)) for p in edges)|{(v,9) for v in s}|{(v,10) for v in range(1,9) if t>>(v-1)&1}
            ok=not any(all(p in red for p in combinations(h,2)) for h in combinations(range(1,11),3)) and not any(all(p not in red for p in combinations(h,2)) for h in combinations(range(1,11),k));assert ok==(t in E)
    classes={tuple(E):[] for E in sets}
    for s,E in zip(corners,sets):classes[tuple(E)].append(s)
    witnesses=[]
    for i,j in combinations(range(8),2):
        d=set(sets[i])^set(sets[j]);
        if d:
            t=min(d,key=lambda x:(x.bit_count(),x));witnesses.append(dict(i=i,j=j,T=[v for v in range(1,9) if t>>(v-1)&1],accepted=i if t in sets[i] else j))
    return dict(edges=edges,k=k,domain=len(ind),corner_sets=list(zip(corners,sets)),classes=[dict(corners=v,completions=len(E)) for E,v in classes.items()],distinctions=witnesses)
if __name__=='__main__':
    path=[(i,i+1) for i in range(1,8)];cases={'path':trial(path,6),'path_plus_36':trial(path+[(3,6)],6)}
    for k,r in cases.items():print(k,r['domain'],r['classes'],r['distinctions'][:1]);
    (D/'ramsey_cube_exterior_test.json').write_text(json.dumps(cases,indent=1))
