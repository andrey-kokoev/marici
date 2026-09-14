#!/usr/bin/env python3
"""Exact checks of the Boolean Walsh--Vandermonde nullity formula."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from math import comb
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/cubical_probe_nullity_is_a_boolean_walsh_vandermonde_sum.md'
RESULT=ROOT/'research/voevodsky/results/cubical_probe_nullity_formula.json'
SETTINGS=(F(1),F(5,6),F(3,4),F(7,10),F(2,3),F(3,5),F(4,7),F(5,9))

def rank(a):
 a=[r[:] for r in a];out=0
 for c in range(len(a[0]) if a else 0):
  p=next((i for i in range(out,len(a)) if a[i][c]),None)
  if p is None:continue
  a[out],a[p]=a[p],a[out];q=a[out][c];a[out]=[x/q for x in a[out]]
  for i in range(out+1,len(a)):
   if a[i][c]:
    q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[out])]
  out+=1
  if out==len(a):break
 return out

def predicted(n,m):return sum((k-m)*comb(n,k) for k in range(m+1,n+1))
def cube_matrix(n,m,settings=SETTINGS):
 edges=[(mask,mask|1<<i,i+1) for mask in range(1<<n) for i in range(n) if not(mask>>i&1)]
 rows=[]
 for t in settings[:m]:
  for v in range(1<<n):
   row=[F(0)]*len(edges)
   for c,(s,target,direction) in enumerate(edges):
    if s==v:row[c]-=t**direction
    if target==v:row[c]+=t**direction
   rows.append(row)
 return rows,len(edges)

checks={};direct={}
for n in range(2,6):
 seq=[]
 for m in range(1,n+1):
  matrix,edge_count=cube_matrix(n,m);actual=edge_count-rank(matrix);expected=predicted(n,m)
  seq.append(actual);checks[f'direct_n{n}_m{m}']=actual==expected
 direct[str(n)]={'nullities':seq,'predicted':[predicted(n,m) for m in range(1,n+1)]}
block_count=0
for n in range(2,9):
 for size in range(1,n+1):
  for subset in combinations(range(1,n+1),size):
   for m in range(1,min(n,size)+1):
    matrix=[[t**j for j in subset] for t in SETTINGS[:m]]
    checks[f'block_n{n}_K{"-".join(map(str,subset))}_m{m}']=rank(matrix)==min(m,size);block_count+=1
bad=SETTINGS[:4]+(SETTINGS[3],)
bad_matrix,edge_count=cube_matrix(5,5,bad);bad_nullity=edge_count-rank(bad_matrix)
checks['duplicate_setting_retains_blind_direction']=bad_nullity==1
text=PACKET.read_text(encoding='utf-8');checks['global_transfer_boundary_retained']='transfer to the full arithmetic graph requires' in text
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.cubical-probe-nullity-formula.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'settings':[f'{x.numerator}/{x.denominator}' for x in SETTINGS],'direct_cube_tests':direct,'vandermonde_blocks_tested':block_count,'duplicate_setting_nullity':bad_nullity,'check_count':len(checks),'checks':checks,'passed':all(checks.values()),'disposition':{'established':'direct cube ranks through n=5 and all subset blocks through n=8 match the formula','residual':'global arithmetic filtration theorem locating first availability of each full-support Walsh block'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'blocks':block_count,'n5':direct['5']['nullities'],'duplicate_nullity':bad_nullity}));raise SystemExit(0 if result['passed'] else 1)
