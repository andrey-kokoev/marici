"""Exhaust source-selected reversed rank pairing, tie fibers and arithmetic quotient."""
from itertools import permutations,product
from collections import Counter,defaultdict
from pathlib import Path
import json
P=list(permutations(range(4)));key=lambda a,b:tuple(sorted((tuple(sorted(a)),tuple(sorted(b)))));match=lambda p:key((p[0],p[3]),(p[1],p[2]));frame={};out={};fiber=defaultdict(set);num=lambda seq:sum(v*10**(3-i) for i,v in enumerate(seq));hist=Counter()
for x in product(range(10),repeat=4):
 s=sorted(x);f=frozenset(match(p) for p in P if all(x[p[i]]<=x[p[i+1]] for i in range(3)));frame[x]=f;hist[len(f)]+=1;g=(s[3]-s[0],s[2]-s[1]);v=num(s[::-1])-num(s);assert v==999*g[0]+90*g[1];out[x]=v;fiber[f].add(v)
for p in P:
 for x,f in frame.items():
  y=tuple(x[p.index(i)] for i in range(4));assert frame[y]=={key(tuple(p[i] for i in a),tuple(p[i] for i in b)) for a,b in f} and out[x]==out[y]
K=lambda x:out[tuple(map(int,x))];o=dict(domain=len(frame),relabel_checks=len(frame)*24,matching_multiplicities=dict(hist),numeric_outputs=len(set(out.values())),example={s:dict(K=K(s),matchings=sorted(frame[tuple(map(int,s))])) for s in ('1234','1235','1123','1223','6174','0000')});print(o);(Path(__file__).resolve().parents[1]/'results/kaprekar_four_role.json').write_text(json.dumps(o,indent=2)+'\n')
