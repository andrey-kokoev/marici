#!/usr/bin/env python3
"""Test a uniform lexicographic discrete-Morse matching on canonical attachments."""
from hashlib import sha256
from itertools import combinations
from math import comb
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/lexicographic_morse_matching_for_canonical_attachments.md'
RESULT=ROOT/'research/voevodsky/results/lexicographic_attachment_morse_matching.json'

def primes(n):
 s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if s[p]:s[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if s[i]]
PS=primes(100)
def product(xs):
 out=1
 for x in xs:out*=x
 return out
def grade(n):return PS[n-1]*product(PS[1:n+1])
def min_grade(I):return PS[I[-1]-1]*product(PS[i] for i in I)
def min_base(I):return product(PS[i-1] for i in I)
def vertex_birth(v):
 c=[]
 for p,q in zip(PS,PS[1:]):
  if v%p==0:c.append(v*q)
  if v%q==0:c.append(v*p)
 return min(c) if c else None
def choose(n,k):return comb(n,k) if 0<=k<=n else 0
def attachment(n):return [choose(n-2,k)+choose(n-2,k-1)+choose(n-2,k-2) for k in range(n+1)]
def face_poset(n):
 L=grade(n);cells={k:[] for k in range(1,n+1)}
 for size in range(1,n+1):
  for I in combinations(range(1,n+1),size):
   g=min_grade(I)
   if L%g==0:cells[size].append((L//g*min_base(I),I))
 ends=set()
 for b,(i,) in cells[1]:ends|={b,b*PS[i]//PS[i-1]}
 cells[0]=[(v,()) for v in sorted(ends) if vertex_birth(v)==L];sets={k:set(x) for k,x in cells.items()};faces={}
 for k in range(1,n+1):
  for cell in cells[k]:
   base,I=cell;out=[]
   for r,i in enumerate(I):
    J=I[:r]+I[r+1:];upper=base*PS[i]//PS[i-1]
    for face in ((upper,J),(base,J)):
     if face in sets[k-1]:out.append(face)
   faces[cell]=sorted(set(out),key=lambda x:(x[1],x[0]))
 return cells,faces
def has_cycle(nodes,arrows):
 indegree={x:0 for x in nodes};adj={x:[] for x in nodes}
 for a,b in arrows:adj[a].append(b);indegree[b]+=1
 queue=[x for x in nodes if indegree[x]==0];seen=0
 while queue:
  x=queue.pop();seen+=1
  for y in adj[x]:
   indegree[y]-=1
   if indegree[y]==0:queue.append(y)
 return seen!=len(nodes)

def test(n):
 cells,faces=face_poset(n);matched=set();pairs=[]
 for k in range(n):
  cofaces={f:[] for f in cells[k]}
  for c in cells[k+1]:
   for f in faces[c]:cofaces[f].append(c)
  for f in sorted(cells[k],key=lambda x:(x[1],x[0])):
   if f in matched:continue
   candidates=sorted((c for c in cofaces[f] if c not in matched),key=lambda x:(x[1],x[0]))
   if candidates:
    c=candidates[0];matched|={f,c};pairs.append((f,c))
 nodes=[c for k in cells for c in cells[k]];pairset=set(pairs);arrows=[]
 for k in range(1,n+1):
  for c in cells[k]:
   for f in faces[c]:arrows.append((f,c) if (f,c) in pairset else (c,f))
 pair_counts=[sum(len(f[1])==k for f,c in pairs) for k in range(n)]
 return {'cell_count':len(nodes),'pair_count':len(pairs),'unmatched':[(b,list(I)) for b,I in nodes if (b,I) not in matched],'pair_counts':pair_counts,'expected_pair_counts':attachment(n-1),'gradient_cycle':has_cycle(nodes,arrows)}
checks={};dimensions={}
for n in range(3,11):
 rec=test(n);dimensions[str(n)]=rec;checks[f'complete_n{n}']=not rec['unmatched'];checks[f'pair_counts_n{n}']=rec['pair_counts']==rec['expected_pair_counts'];checks[f'acyclic_n{n}']=not rec['gradient_cycle']
text=PACKET.read_text(encoding='utf-8');checks['all_dimension_boundary_retained']='all-dimensional proof remains separate' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.lexicographic-attachment-morse-matching.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'dimensions':dimensions,'checks':checks,'passed':all(checks.values()),'disposition':{'status':'uniform rule survives through n=10' if all(checks.values()) else 'rule fails in tested range','residual':'prove matching completeness and gradient acyclicity for all n'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'failures':{n:r for n,r in dimensions.items() if r['unmatched'] or r['gradient_cycle'] or r['pair_counts']!=r['expected_pair_counts']}}));raise SystemExit(0 if result['passed'] else 1)
