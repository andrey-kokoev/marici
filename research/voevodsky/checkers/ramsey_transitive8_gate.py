"""Enumerate all inclusion-minimal transitive subgroups of one Sylow 2-subgroup of S8. Every transitive degree-eight group has a transitive Sylow 2-subgroup (choose one over a Sylow 2-subgroup of a point stabilizer, compare orders). All such groups embed up to conjugacy in this order-128 binary tree automorphism group. All maximal subgroups of a finite 2-group are index 2. Enumerate via its elementary abelian quotient by squares, using cosets and all hyperplanes."""
import itertools,collections,json,sys
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';perms=[tuple(range(8))];gens=[]
for k in [1,2,4]:
 for s in range(0,8,2*k):gens.append(tuple((i^k) if s<=i<s+2*k else i for i in range(8)))
seen=set(perms)
for p in perms:
 for g in gens:
  t=tuple(p[g[i]] for i in range(8))
  if t not in seen:seen.add(t);perms.append(t)
assert len(perms)==128;idx={p:i for i,p in enumerate(perms)};M=[[idx[tuple(p[q[i]] for i in range(8))] for q in perms] for p in perms]
def closure(gens):
 s={0};ls=[0]
 for x in ls:
  for y in gens:
   z=M[x][y]
   if z not in s:s.add(z);ls.append(z)
 return s
def children(H):
 K=closure({M[x][x] for x in H});basis={0:K};n=1
 while n*len(K)<len(H):
  x=next(iter(H-set.union(*basis.values())));basis.update({n+i:{M[x][k] for k in v} for i,v in list(basis.items())});n*=2
 for w in range(1,n):
  J=frozenset().union(*(v for i,v in basis.items() if (i&w).bit_count()%2==0));assert len(J)*2==len(H)
  if len({perms[x][0] for x in J})==8:yield J
ls=[frozenset(range(128))];seen=set(ls);mins=[]
for h in ls:
 cs=list(children(h));
 if not cs:mins.append(h)
 for c in cs:
  if c not in seen:ls.append(c);seen.add(c)
print('transitive subgroups',len(ls),'minimal',collections.Counter(map(len,mins)));(P/'ramsey_transitive8_gate.json').write_text(json.dumps(dict(subgroups=len(ls),minimal_orders=dict(collections.Counter(map(len,mins))),nonregular=[[perms[j] for j in sorted(h)] for h in mins if len(h)>8]))+'\n')
