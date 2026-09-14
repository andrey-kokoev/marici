#!/usr/bin/env python3
"""Persistent homology census in degree three through grade 20000."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/degree_three_persistence_synchronization_test.md'
RESULT=ROOT/'research/voevodsky/results/degree_three_persistence_synchronization.json'
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
 return out+(1 if n>1 else 0)
def min_grade(I):return PS[I[-1]-1]*product(PS[i] for i in I)
def min_base(I):return product(PS[i-1] for i in I)
def vertex_birth(v):
 c=[]
 for p,q in zip(PS,PS[1:]):
  if v%p==0:c.append(v*q)
  if v%q==0:c.append(v*p)
 return min(c) if c else None
K=max(i for i in range(1,len(PS)) if PS[i-1]*PS[i]<=LIMIT);birth={}
for size in (1,2,3):
 for I in combinations(range(1,K+1),size):
  g=min_grade(I)
  if g>LIMIT:continue
  B=min_base(I)
  for k in range(1,LIMIT//g+1):
   base=k*B
   if omega(base)==3:birth[(base,I)]=k*g
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
def census(p):
 reduced,pairs=reduce(p);out={str(d):[] for d in (1,2,3)}
 for c in cells:
  d=len(c[1])
  if d==0 or reduced[c]:continue
  death=pairs.get(c);out[str(d)].append({'cell':{'base':c[0],'directions':list(c[1])},'birth':birth[c],'death':birth[death] if death else None,'killer':{'base':death[0],'directions':list(death[1])} if death else None})
 return out
cens={str(p):census(p) for p in MODS};main=cens[str(MODS[0])];summary={}
for d,items in main.items():
 summary[d]={'births':len(items),'zero_length':sum(x['death']==x['birth'] for x in items),'positive_length':sum(x['death'] is not None and x['death']>x['birth'] for x in items),'right_censored':sum(x['death'] is None for x in items),'first_positive':next((x for x in items if x['death'] is None or x['death']>x['birth']),None)}
square=True
for c in (x for x in cells if len(x[1])>=2):
 total={}
 for f,a in boundary(c).items():
  for x,b in boundary(f).items():total[x]=total.get(x,0)+a*b
 if any(total.values()):square=False;break
checks={'boundary_squared':square,'fields_agree':cens[str(MODS[0])]==cens[str(MODS[1])],'all_positive_degrees_classified':all(v['births']==v['zero_length']+v['positive_length']+v['right_censored'] for v in summary.values()),'scope_retained':'does not test repeated-shell cubes' in PACKET.read_text(encoding='utf-8')};predictions={'h1_synchronized':summary['1']['positive_length']==summary['1']['right_censored']==0,'h2_synchronized':summary['2']['positive_length']==summary['2']['right_censored']==0};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.degree-three-persistence.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'limit':LIMIT,'cell_counts':{str(d):sum(len(c[1])==d for c in cells) for d in range(4)},'interval_summary':summary,'predictions':predictions,'checks':checks,'passed':all(checks.values()),'disposition':{'synchronization':'survives bounded sector' if all(predictions.values()) else 'falsified','residual':'higher degree, repeated-shell cells, and integral torsion untested'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'cell_counts':result['cell_counts'],'summary':summary,'predictions':predictions,'checks':checks}));raise SystemExit(0 if result['passed'] else 1)
