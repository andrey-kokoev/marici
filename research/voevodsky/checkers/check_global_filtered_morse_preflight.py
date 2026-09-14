#!/usr/bin/env python3
"""Bounded greedy filtered-Morse preflight in multiplicative degrees 2..5."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];PACKET=ROOT/'research/voevodsky/global_filtered_morse_matching_preflight.md';RESULT=ROOT/'research/voevodsky/results/global_filtered_morse_preflight.json';LIMIT=20000
def primes(n):
 a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if a[p]:a[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if a[i]]
PS=primes(1000)
def product(xs):
 z=1
 for x in xs:z*=x
 return z
def omega(n):
 z=0
 for p in PS:
  while n%p==0:n//=p;z+=1
  if n==1:break
 return z+(1 if n>1 else 0)
def ming(I):return PS[I[-1]-1]*product(PS[i] for i in I)
def minb(I):return product(PS[i-1] for i in I)
def vbirth(v):
 c=[]
 for p,q in zip(PS,PS[1:]):
  if v%p==0:c.append(v*q)
  if v%q==0:c.append(v*p)
 return min(c) if c else None
K=max(i for i in range(1,len(PS)) if PS[i-1]*PS[i]<=LIMIT)
def build(D):
 birth={}
 for size in range(1,D+1):
  for I in combinations(range(1,K+1),size):
   g=ming(I)
   if g>LIMIT:continue
   B=minb(I)
   for k in range(1,LIMIT//g+1):
    base=k*B
    if omega(base)==D:birth[(base,I)]=k*g
 edges=[c for c in birth if len(c[1])==1];vertices=set()
 for b,(i,) in edges:vertices|={b,b*PS[i]//PS[i-1]}
 for v in vertices:
  g=vbirth(v)
  if g is not None and g<=LIMIT:birth[(v,())]=g
 cells={d:sorted((c for c in birth if len(c[1])==d),key=lambda c:(birth[c],c[1],c[0])) for d in range(D+1)};cellset=set(birth);faces={}
 for d in range(1,D+1):
  for c in cells[d]:
   base,I=c;out=[]
   for r,i in enumerate(I):
    J=I[:r]+I[r+1:];upper=base*PS[i]//PS[i-1]
    for f in ((upper,J),(base,J)):
     if f in cellset:out.append(f)
   faces[c]=set(out)
 return birth,cells,faces
def cycle(nodes,arrows):
 indeg={x:0 for x in nodes};adj={x:[] for x in nodes}
 for a,b in arrows:adj[a].append(b);indeg[b]+=1
 stack=[x for x in nodes if indeg[x]==0];seen=0
 while stack:
  x=stack.pop();seen+=1
  for y in adj[x]:
   indeg[y]-=1
   if indeg[y]==0:stack.append(y)
 return seen!=len(nodes)
def test(D):
 birth,cells,faces=build(D);matched=set();pairs=[]
 for d in range(D):
  co={f:[] for f in cells[d]}
  for c in cells[d+1]:
   for f in faces[c]:co[f].append(c)
  for f in cells[d]:
   if f in matched:continue
   options=sorted((c for c in co[f] if c not in matched),key=lambda c:(birth[c],c[1],c[0]))
   if options:c=options[0];matched|={f,c};pairs.append((f,c))
 nodes=[c for d in cells for c in cells[d]];pairset=set(pairs);arrows=[]
 for d in range(1,D+1):
  for c in cells[d]:
   for f in faces[c]:arrows.append((f,c) if (f,c) in pairset else (c,f))
 # Absolute component count from the graph.
 parent={v:v for v in cells[0]}
 def find(x):
  while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
  return x
 for e in cells[1]:
  vs=list(faces[e])
  if len(vs)==2:
   a,b=map(find,vs)
   if a!=b:parent[a]=b
 h0=len({find(v) for v in cells[0]});unmatched=[c for c in nodes if c not in matched];positive=[c for c in unmatched if c[1]]
 crossing=[(f,c) for f,c in pairs if f[1] and birth[f]!=birth[c]]
 return {'cell_counts':[len(cells[d]) for d in range(D+1)],'pairs':len(pairs),'unmatched_vertices':len(unmatched)-len(positive),'absolute_h0':h0,'unmatched_positive_count':len(positive),'cross_grade_positive_pairs':len(crossing),'gradient_cycle':cycle(nodes,arrows),'first_unmatched_positive':[positive[0][0],list(positive[0][1])] if positive else None}
predictions={};sectors={}
for D in range(2,6):
 r=test(D);sectors[str(D)]=r;predictions[f'only_vertices_D{D}']=r['unmatched_positive_count']==0;predictions[f'equal_grade_positive_D{D}']=r['cross_grade_positive_pairs']==0;predictions[f'acyclic_D{D}']=not r['gradient_cycle'];predictions[f'critical_vertices_match_h0_D{D}']=r['unmatched_vertices']==r['absolute_h0']
text=PACKET.read_text(encoding='utf-8');checks={'all_sectors_enumerated':set(sectors)=={'2','3','4','5'},'failures_retained':any(not v for v in predictions.values()),'bounded_scope_retained':'not yet an all-dimensional theorem' in text};checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.global-filtered-morse-preflight.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'limit':LIMIT,'sectors':sectors,'predictions':predictions,'checks':checks,'passed':all(checks.values()),'disposition':{'conjecture':'greedy rule fails','residual':'reserve positive-dimensional same-grade pairs before vertex-edge component pairs'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'sectors':sectors,'prediction_failures':[k for k,v in predictions.items() if not v]}));raise SystemExit(0 if result['passed'] else 1)
