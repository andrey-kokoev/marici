"""Ablate the interval sorting convention. Start with full body sets and fixed carrier kind words. Test whether previously specified relational constraints jointly select windows. No numeric subscript comparisons. Treat chronological overlap as a tested assumption, not a physical law."""
from pathlib import Path
from itertools import permutations,product,combinations
import json
D=Path(__file__).resolve().parents[1];load=lambda n:json.loads((D/'results'/n).read_text());M=load('pne_body_membership_decoder.json')['template'];b=[{v for v,s in M.items() if s[i]=='1'} for i in range(3)];w=load('pne_kind_index_projection.json')['windows'];opts=[[p[:3] for p in permutations(sorted(s)) if ''.join(x[0] for x in p[:3])==t] for s,t in zip(b,['CMC','MCM','MCC'])];
def shared(a,b):return {frozenset(e) for e in zip(a,a[1:])}&{frozenset(e) for e in zip(b,b[1:])}
def join(a,b):return any(a[-k:]==b[:k] for k in (1,2))
keys=['PN_face','NE_face','two_distinct_shared_legs','PN_ordered_join','NE_ordered_join'];rows=[]
for p,n,e in product(*opts):
 a=shared(p,n);c=shared(n,e);flags=[set(n)==b[0]&b[1],set(e)==b[1]&b[2],len(a)==len(c)==1 and a!=c,join(p,n),join(n,e)];rows.append(([p,n,e],dict(zip(keys,flags))))
counts={};minimal=[]
for k in range(6):
 for comb in combinations(keys,k):
  z=[v for v,f in rows if all(f[x] for x in comb)];counts['+'.join(comb)]=len(z)
  if len(z)==1:
   assert list(map(list,z[0]))==w
   if not any(set(s)<=set(comb) for s in minimal):minimal.append(comb)
o=dict(counts=counts,minimal_sufficient_subsets=minimal);print(minimal);print({x:counts['+'.join(k for k in keys if k!=x)] for x in keys});print('faces+legs',counts['+'.join(keys[:3])]);(D/'results/pne_joint_order_constraints.json').write_text(json.dumps(o,indent=2)+'\n')
