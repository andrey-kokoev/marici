#!/usr/bin/env python3
"""Persistent H1 census in the degree-two distinct-shell sector."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/degree_two_persistent_one_homology_scan.md'
RESULT=ROOT/'research/voevodsky/results/degree_two_persistent_one_homology_scan.json'
LIMIT=20000;MODS=(1000000007,1000000009)
def primes(n):
 s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if s[p]:s[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if s[i]]
PS=primes(1000)
def product(xs):
 out=1
 for x in xs:out*=x
 return out
def omega(n):
 out=0
 for p in PS:
  while n%p==0:n//=p;out+=1
  if n==1:break
 return out+(n>1)
def min_grade(I):return PS[I[-1]-1]*product(PS[i] for i in I)
def min_base(I):return product(PS[i-1] for i in I)
def vertex_birth(v):
 c=[]
 for p,q in zip(PS,PS[1:]):
  if v%p==0:c.append(v*q)
  if v%q==0:c.append(v*p)
 return min(c) if c else None
K=max(i for i in range(1,len(PS)) if PS[i-1]*PS[i]<=LIMIT);birth={}
for size in (1,2):
 for I in combinations(range(1,K+1),size):
  g=min_grade(I)
  if g>LIMIT:continue
  B=min_base(I)
  for k in range(1,LIMIT//g+1):
   base=k*B
   if omega(base)==2:birth[(base,I)]=k*g
edges=[c for c in birth if len(c[1])==1];vertices=set()
for base,(i,) in edges:vertices|={base,base*PS[i]//PS[i-1]}
for v in vertices:
 b=vertex_birth(v)
 if b is not None and b<=LIMIT:birth[(v,())]=b
cells=sorted(birth,key=lambda c:(birth[c],len(c[1]),c[1],c[0]));cellset=set(cells);index={c:i for i,c in enumerate(cells)}
def boundary(cell):
 base,I=cell;out={}
 for r,i in enumerate(I):
  J=I[:r]+I[r+1:];sign=-1 if r%2 else 1;upper=base*PS[i]//PS[i-1]
  for f,a in (((upper,J),sign),((base,J),-sign)):
   if f in cellset:out[f]=out.get(f,0)+a
 return {f:a for f,a in out.items() if a}
def reduce(p):
 basis={};reduced={};pairs={}
 for c in cells:
  col={index[f]:a%p for f,a in boundary(c).items()}
  while col:
   low=max(col)
   if low not in basis:break
   q=col[low]*pow(basis[low][low],p-2,p)%p
   for i,a in basis[low].items():
    z=(col.get(i,0)-q*a)%p
    if z:col[i]=z
    else:col.pop(i,None)
  reduced[c]=col
  if col:low=max(col);basis[low]=col;pairs[cells[low]]=c
 return reduced,pairs
def intervals(p):
 reduced,pairs=reduce(p);out=[]
 for e in edges:
  if reduced[e]:continue
  death=pairs.get(e);out.append({'edge':{'base':e[0],'direction':e[1][0]},'birth':birth[e],'death':birth[death] if death else None,'killer':{'base':death[0],'directions':list(death[1])} if death else None})
 return sorted(out,key=lambda x:(x['birth'],x['edge']['direction'],x['edge']['base']))
ints={str(p):intervals(p) for p in MODS};main=ints[str(MODS[0])]
positive=[x for x in main if x['death'] is None or x['death']>x['birth']];zero=[x for x in main if x['death']==x['birth']]
# Verify square boundaries compose to zero integrally.
square_ok=True
for c in (x for x in cells if len(x[1])==2):
 total={}
 for e,a in boundary(c).items():
  for v,b in boundary(e).items():total[v]=total.get(v,0)+a*b
 if any(total.values()):square_ok=False;break
ratio=len(positive)/len(edges)
checks={'boundary_squared':square_ok,'fields_agree':ints[str(MODS[0])]==ints[str(MODS[1])],'all_h1_births_classified':len(main)==len(positive)+len(zero),'scope_retained':'does not infer integral torsion' in PACKET.read_text(encoding='utf-8')};checks={k:bool(v) for k,v in checks.items()}
predictions={'positive_bar_exists':bool(positive),'bounded_sparse_ratio':ratio<0.05}
result={'schema':'marici.voevodsky.degree-two-persistent-h1.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'limit':LIMIT,'cell_counts':{'vertices':sum(len(c[1])==0 for c in cells),'edges':len(edges),'squares':sum(len(c[1])==2 for c in cells)},'interval_counts':{'all_h1_births':len(main),'positive_or_censored':len(positive),'zero_length':len(zero),'right_censored':sum(x['death'] is None for x in positive)},'positive_birth_edge_ratio':ratio,'first_twenty_positive':positive[:20],'longest_twenty_finite':sorted((x for x in positive if x['death'] is not None),key=lambda x:x['death']-x['birth'],reverse=True)[:20],'checks':checks,'predictions':predictions,'passed':all(checks.values()),'disposition':{'existence':'survives' if positive else 'falsified on bounded sector','bounded_sparsity':'vacuous because no positive bars' if not positive else ('survives' if ratio<0.05 else 'fails'),'residual':'higher degree and integral torsion untested'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'cell_counts':result['cell_counts'],'interval_counts':result['interval_counts'],'ratio':ratio,'first':positive[:5],'checks':checks}));raise SystemExit(0 if result['passed'] else 1)
