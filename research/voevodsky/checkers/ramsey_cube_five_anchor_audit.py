"""Reconcile all three-erasure verdicts by exact mask keys; check symmetry partitions on nested unresolved blocks, recompute number of labeled cube repairs, and list next (four-erasure) orbits."""
import itertools,json,collections,math
from ramsey_cube_three_gate import options,subdata,REPS,M,P
from ramsey_three_gate_refine import second
from ramsey_three_gate_third import opts as third
read=lambda x:json.loads((P/(x+'.json')).read_text());sym=[[x^sum((i>>j&1)<<k for k,j in enumerate(p)) for i in range(8)] for p in itertools.permutations(range(3)) for x in range(8)]
def orbs(k):
 O={}
 for q in itertools.combinations(range(8),k):
  rep=min(tuple(sorted(g[i] for i in q)) for g in sym);O[rep]=O.get(rep,0)+1
 return O
assert {min(tuple(sorted(g[i] for i in f)) for g in sym) for f in REPS}==set(orbs(3));out=[]
for f in REPS:
 proven={tuple(c['masks']) for file in ('4_1500','5_10000','5_100000','5_150000','5_120000') for r in read('ramsey_three_gate_'+file) if tuple(r['f'])==f for c in r['cases'] if c['ok'] is False}
 if f==(0,3,5):
  _,_,xs=second(f,(1,2,4));pr={tuple(c['x']) for file in ('5000','80000') for r in read(f'ramsey_three_refine_035_124_{file}_5') for c in r['rows'] if c['ok'] is False};assert set(xs)-pr=={(0,1,2,4)} and set(third)=={tuple(c['x']) for c in read('ramsey_three_gate_third_30000') if c['ok'] is False};proven.add((1,2,4))
 if f==(0,1,7):proven.update(tuple(z['o']) for z in read('ramsey_three_gate_order_200000')+[read('ramsey_three_gate_order_last')] if z['ok'] is False)
 assert proven==set(options(f));_,h,gs=subdata(f);types=set();ordered=0
 for ls in itertools.permutations(f):
  a=[sum((s>>l&1)<<j for j,l in enumerate(ls)) for s in M];key=tuple(tuple(sorted(a[i] for i in g)) for g in gs)
  if key not in types:types.add(key);ordered+=math.prod(math.factorial(len(q))//math.prod(math.factorial(v) for v in collections.Counter(q).values()) for q in key)
 out.append(dict(erased=f,noncube_branches=len(proven),labeled_cubic_rows=ordered,relative_types=len(types)))
nexts=[dict(erased=r,orbit=n) for r,n in orbs(4).items()];print(out,nexts);(P/'ramsey_cube_five_anchor_audit.json').write_text(json.dumps(dict(cases=out,four_erasure_orbits=nexts))+'\n')
