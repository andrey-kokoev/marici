#!/usr/bin/env python3
"""Verify the explicit direction-one Morse matching through dimension fourteen."""
from hashlib import sha256
from itertools import combinations
from math import comb
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/direction_one_matching_contracts_every_canonical_attachment.md'
RESULT=ROOT/'research/voevodsky/results/direction_one_attachment_matching.json'

def primes(n):
 s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if s[p]:s[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if s[i]]
PS=primes(200)
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
def poset(n):
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
 return cells,sets,faces
def cyclic(nodes,arrows):
 indegree={x:0 for x in nodes};adj={x:[] for x in nodes}
 for a,b in arrows:adj[a].append(b);indegree[b]+=1
 stack=[x for x in nodes if indegree[x]==0];seen=0
 while stack:
  x=stack.pop();seen+=1
  for y in adj[x]:
   indegree[y]-=1
   if indegree[y]==0:stack.append(y)
 return seen!=len(nodes)
def lex_pairs(n,cells,faces):
 matched=set();pairs=[]
 for k in range(n):
  co={f:[] for f in cells[k]}
  for c in cells[k+1]:
   for f in faces[c]:co[f].append(c)
  for f in sorted(cells[k],key=lambda x:(x[1],x[0])):
   if f in matched:continue
   candidates=sorted((c for c in co[f] if c not in matched),key=lambda x:(x[1],x[0]))
   if candidates:c=candidates[0];matched|={f,c};pairs.append((f,c))
 return set(pairs)
def explicit(n):
 cells,sets,faces=poset(n);pairs=[];vertex=cells[0][0];edge=next(c for c in cells[1] if c[1]==(2,));pairs.append((vertex,edge))
 integral=True;face_ok=True
 for k in range(1,n):
  for lower in cells[k]:
   base,I=lower
   if 1 in I or I==(2,):continue
   if 2*base%3:integral=False;continue
   upper=(2*base//3,(1,)+I);pairs.append((lower,upper));face_ok&=upper in sets[k+1] and lower in faces.get(upper,[])
 pairset=set(pairs);nodes=[c for k in cells for c in cells[k]];matched={x for pair in pairs for x in pair};arrows=[]
 for k in range(1,n+1):
  for c in cells[k]:
   for f in faces[c]:arrows.append((f,c) if (f,c) in pairset else (c,f))
 counts=[sum(len(f[1])==k for f,c in pairs) for k in range(n)]
 return {'cells':len(nodes),'pairs':len(pairs),'complete':len(matched)==len(nodes),'integral':integral,'face_incidence':face_ok,'pair_counts':counts,'expected':attachment(n-1),'gradient_cycle':cyclic(nodes,arrows),'equals_lexicographic':pairset==lex_pairs(n,cells,faces)}
checks={};dimensions={}
for n in range(3,15):
 rec=explicit(n);dimensions[str(n)]=rec
 for field in ('complete','integral','face_incidence','equals_lexicographic'):checks[f'{field}_n{n}']=rec[field]
 checks[f'pair_counts_n{n}']=rec['pair_counts']==rec['expected'];checks[f'acyclic_n{n}']=not rec['gradient_cycle']
text=PACKET.read_text(encoding='utf-8');checks['scope_retained']='does not address arbitrary noncanonical attachment grades' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.direction-one-attachment-matching.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'dimensions':dimensions,'checks':checks,'passed':all(checks.values()),'disposition':{'theorem':'direction-one matching completely and acyclically pairs every canonical relative attachment for n>=3','verification':'implementation agrees with lexicographic search through n=14'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'n14':dimensions['14']}));raise SystemExit(0 if result['passed'] else 1)
