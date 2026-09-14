#!/usr/bin/env python3
"""Exact relative attachment counts and ranks for canonical grades n=3..10."""
from hashlib import sha256
from itertools import combinations
from math import comb,factorial
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/canonical_attachment_polynomial_from_prime_divisibility.md'
RESULT=ROOT/'research/voevodsky/results/canonical_attachment_recurrence.json'
MODS=(1000000007,1000000009)

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
def canonical_grade(n):return PS[n-1]*product(PS[1:n+1])
def min_grade(I):return PS[I[-1]-1]*product(PS[i] for i in I)
def min_base(I):return product(PS[i-1] for i in I)
def vertex_birth(v):
 costs=[]
 for p,q in zip(PS,PS[1:]):
  if v%p==0:costs.append(v*q)
  if v%q==0:costs.append(v*p)
 return min(costs) if costs else None
def choose(n,r):return comb(n,r) if 0<=r<=n else 0
def poly(n):return [choose(n-2,r)+choose(n-2,r-1)+choose(n-2,r-2) for r in range(n+1)]
def rank_columns(domain,codomain,boundary,p):
 ri={c:i for i,c in enumerate(codomain)};basis={}
 for cell in domain:
  column={ri[f]:v%p for f,v in boundary(cell).items()}
  while column:
   lead=min(column)
   if lead not in basis:
    inv=pow(column[lead],p-2,p);basis[lead]={k:v*inv%p for k,v in column.items() if v*inv%p};break
   q=column[lead]
   for k,v in basis[lead].items():
    x=(column.get(k,0)-q*v)%p
    if x:column[k]=x
    else:column.pop(k,None)
 return len(basis)

def relative_complex(n):
 L=canonical_grade(n);cells={k:[] for k in range(1,n+1)}
 for size in range(1,n+1):
  for I in combinations(range(1,n+1),size):
   g=min_grade(I)
   if L%g==0:cells[size].append((L//g*min_base(I),I))
 endpoints=set()
 for base,(i,) in cells[1]:endpoints|={base,base*PS[i]//PS[i-1]}
 cells[0]=[(v,()) for v in sorted(endpoints) if vertex_birth(v)==L];sets={k:set(v) for k,v in cells.items()}
 def boundary(cell):
  base,I=cell;out={}
  for r,i in enumerate(I):
   J=I[:r]+I[r+1:];sign=-1 if r%2 else 1;upper=base*PS[i]//PS[i-1]
   for f,v in (((upper,J),sign),((base,J),-sign)):
    if f in sets[len(J)]:out[f]=out.get(f,0)+v
  return {f:v for f,v in out.items() if v}
 return L,cells,boundary

checks={};dimensions={}
for n in range(3,11):
 L,cells,boundary=relative_complex(n);counts=[len(cells[k]) for k in range(n+1)];expected=poly(n)
 checks[f'counts_n{n}']=counts==expected
 rank_sets=[]
 for p in MODS:rank_sets.append([rank_columns(cells[k],cells[k-1],boundary,p) for k in range(1,n+1)])
 expected_ranks=poly(n-1)
 checks[f'moduli_agree_n{n}']=rank_sets[0]==rank_sets[1]
 checks[f'rank_recurrence_n{n}']=rank_sets[0]==expected_ranks
 betti=[counts[k]-(rank_sets[0][k-1] if k else 0)-(rank_sets[0][k] if k<n else 0) for k in range(n+1)]
 checks[f'acyclic_n{n}']=betti==[0]*(n+1)
 boundary_squared=True
 for k in range(2,n+1):
  for cell in cells[k]:
   total={}
   for face,a in boundary(cell).items():
    for sub,b in boundary(face).items():total[sub]=total.get(sub,0)+a*b
   if any(total.values()):boundary_squared=False;break
 checks[f'boundary_squared_n{n}']=boundary_squared
 dimensions[str(n)]={'grade':L,'cell_counts':counts,'boundary_ranks':rank_sets[0],'relative_betti':betti,'path_increment':sum(factorial(k)*counts[k] for k in range(1,n+1))}
text=PACKET.read_text(encoding='utf-8');checks['rank_theorem_boundary_retained']='chain contraction remains to be written' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.canonical-attachment-recurrence.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'dimensions':dimensions,'checks':checks,'passed':all(checks.values()),'disposition':{'proved':'attachment count polynomial by prime divisibility','verified':'relative rank recurrence and acyclicity through n=10','residual':'write an all-dimensional chain contraction'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'n7':dimensions['7'],'n10_paths':dimensions['10']['path_increment']}));raise SystemExit(0 if result['passed'] else 1)
