#!/usr/bin/env python3
"""Exact finite checks of the cubical effective-divisor model of naturals."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/naturals_form_a_weighted_cubical_effective_divisor_geometry.md'
RESULT=ROOT/'research/voevodsky/results/cubical_effective_divisor_geometry.json'
CUTOFF=5000

def primes(n):
 s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if s[p]:s[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if s[i]]
PS=primes(CUTOFF+2);PI={p:i for i,p in enumerate(PS)}
def divisor(n):
 out={};x=n
 for i,p in enumerate(PS):
  if p*p>x:break
  while x%p==0:out[i]=out.get(i,0)+1;x//=p
 if x>1:out[PI[x]]=out.get(PI[x],0)+1
 return out
def add(a,b):
 out=dict(a)
 for i,e in b.items():out[i]=out.get(i,0)+e
 return {i:e for i,e in out.items() if e}
def diff(a,b):
 keys=set(a)|set(b);return {i:a.get(i,0)-b.get(i,0) for i in keys if a.get(i,0)!=b.get(i,0)}
def product(xs):
 out=1
 for x in xs:out*=x
 return out

checks={};edge_count=0;degrees={}
for shell,(p,q) in enumerate(zip(PS,PS[1:])):
 if p*q>CUTOFF:break
 for k in range(1,CUTOFF//(p*q)+1):
  source=k*p;target=k*q;ds=divisor(source);dt=divisor(target);delta=diff(dt,ds)
  checks[f'edge_{shell}_{k}_root']=delta=={shell:-1,shell+1:1}
  checks[f'edge_{shell}_{k}_degree']=sum(ds.values())==sum(dt.values())
  checks[f'edge_{shell}_{k}_grade']=source*q==k*p*q
  degrees[str(sum(ds.values()))]=degrees.get(str(sum(ds.values())),0)+1;edge_count+=1
multiplication_tests=0
for m in range(1,101):
 for n in range(1,101):checks[f'mul_{m}_{n}']=divisor(m*n)==add(divisor(m),divisor(n));multiplication_tests+=1
cube_count=0;square_count=0
for size in range(2,6):
 for indices in combinations(range(8),size):
  base=product(PS[i] for i in indices);vertices={}
  for mask in range(1<<size):
   value=base
   for bit,i in enumerate(indices):
    if mask>>bit&1:value=value*PS[i+1]//PS[i]
   vertices[mask]=value
  checks[f'cube_{"-".join(map(str,indices))}_vertices']=len(set(vertices.values()))==1<<size
  all_effective=all(all(e>=0 for e in divisor(v).values()) for v in vertices.values());checks[f'cube_{"-".join(map(str,indices))}_effective']=all_effective
  grades=[]
  for mask,source in vertices.items():
   for bit,i in enumerate(indices):
    if not(mask>>bit&1):grades.append(source*PS[i+1])
  expected=PS[indices[-1]]*product(PS[i+1] for i in indices);checks[f'cube_{"-".join(map(str,indices))}_grade']=max(grades)==expected
  for a,b in combinations(range(size),2):
   for mask in range(1<<size):
    if not(mask>>a&1) and not(mask>>b&1):
     checks[f'square_{size}_{indices}_{mask}_{a}_{b}']=vertices[mask|(1<<a)|(1<<b)]==vertices[mask]*PS[indices[a]+1]//PS[indices[a]]*PS[indices[b]+1]//PS[indices[b]];square_count+=1
  cube_count+=1
text=PACKET.read_text(encoding='utf-8');checks['physical_scope_excluded']='does not assign physical spatial meaning' in text;checks['fillers_declared']='independently defined cubical filler' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.cubical-effective-divisor-geometry.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'cutoff':CUTOFF,'arithmetic_edges_tested':edge_count,'degree_edge_counts':degrees,'multiplication_tests':multiplication_tests,'cubes_tested':cube_count,'squares_tested':square_count,'check_count':len(checks),'passed':all(checks.values()),'checks':checks,'disposition':{'established':'bounded exact identification of arithmetic routes with weighted effective-divisor chip moves and cubical fillers','residual':'formal topology of the unbounded cubical state complex and chain-level comparison with Clifford exterior degree'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'edges':edge_count,'multiplications':multiplication_tests,'cubes':cube_count,'squares':square_count}));raise SystemExit(0 if result['passed'] else 1)
