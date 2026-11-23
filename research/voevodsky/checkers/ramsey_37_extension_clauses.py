"""Lossless propositional reduction: degree saturation, inclusion-minimal hit clauses, and independence conflicts. Show connected components after unit propagation on positive and negative clauses."""
import itertools,json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';E=[set(e) for e in json.loads((D/'ramsey_37_dual_stars.json').read_text())['red_edges']];out=[]
for deleted in [{1,20},{0,7}]:
 V=set(range(22))-deleted;e=[v for v in E if v<=V];U={i for i in V if sum(i in a for a in e)<6};req={frozenset(U.intersection(a)) for a in itertools.combinations(V,6) if not any(t.issubset(a) for t in e)};positive=[v for v in req if not any(w<v for w in req)];negative=[v for v in e if v<=U];on=set();off=set()
 while True:
  p=[v-off for v in positive if not v&on];n=[v-on for v in negative if not v&off];assert all(p) and all(n);x={next(iter(v)) for v in p if len(v)==1};y={next(iter(v)) for v in n if len(v)==1};on|=x;off|=y;assert not on&off
  if not x|y:break
 def norm(l):return sorted([sorted(v) for v in set(map(frozenset,l)) if not any(w<v for w in l)])
 row=dict(deleted=sorted(deleted),positive=norm(positive),negative=norm(negative),on=sorted(on),off=sorted(off),residualPositive=norm(p),residualNegative=norm(n),free=sorted(U-on-off));out.append(row);print(row)
(D/'ramsey_37_extension_clauses.json').write_text(json.dumps(out,indent=2)+'\n')
