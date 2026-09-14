#!/usr/bin/env python3
"""Construct exact split-basis contractions of canonical relative attachments."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/canonical_relative_attachments_admit_explicit_chain_contractions.md'
RESULT=ROOT/'research/voevodsky/results/canonical_relative_chain_contractions.json'

def primes(n):
 a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if a[p]:a[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if a[i]]
PS=primes(100)
def product(xs):
 out=1
 for x in xs:out*=x
 return out
def grade(n):return PS[n-1]*product(PS[1:n+1])
def min_grade(I):return PS[I[-1]-1]*product(PS[i] for i in I)
def min_base(I):return product(PS[i-1] for i in I)
def vertex_birth(v):
 costs=[]
 for p,q in zip(PS,PS[1:]):
  if v%p==0:costs.append(v*q)
  if v%q==0:costs.append(v*p)
 return min(costs) if costs else None
def complex_at(n):
 L=grade(n);cells={k:[] for k in range(1,n+1)}
 for size in range(1,n+1):
  for I in combinations(range(1,n+1),size):
   g=min_grade(I)
   if L%g==0:cells[size].append((L//g*min_base(I),I))
 endpoints=set()
 for base,(i,) in cells[1]:endpoints|={base,base*PS[i]//PS[i-1]}
 cells[0]=[(v,()) for v in sorted(endpoints) if vertex_birth(v)==L];sets={k:set(x) for k,x in cells.items()}
 def boundary(cell):
  base,I=cell;out={}
  for r,i in enumerate(I):
   J=I[:r]+I[r+1:];sign=-1 if r%2 else 1;upper=base*PS[i]//PS[i-1]
   for f,v in (((upper,J),sign),((base,J),-sign)):
    if f in sets[len(J)]:out[f]=out.get(f,0)+v
  return {f:v for f,v in out.items() if v}
 D={}
 for k in range(1,n+1):
  ri={c:i for i,c in enumerate(cells[k-1])};matrix=s.zeros(len(cells[k-1]),len(cells[k]))
  for j,cell in enumerate(cells[k]):
   for face,value in boundary(cell).items():matrix[ri[face],j]=value
  D[k]=matrix
 return cells,D

def contraction(n):
 cells,D=complex_at(n);dims=[len(cells[k]) for k in range(n+1)];B={};S={};P={};unit_bases=True
 for k in range(n+1):
  B[k]=D[k+1].columnspace() if k<n else []
  pivots=D[k].rref()[1] if k>0 else ()
  S[k]=[s.eye(dims[k]).col(j) for j in pivots]
  columns=B[k]+S[k];P[k]=s.Matrix.hstack(*columns) if columns else s.zeros(dims[k],0)
  if P[k].shape!=(dims[k],dims[k]) or abs(P[k].det())!=1:unit_bases=False
 Dp={k:P[k-1].inv()*D[k]*P[k] for k in range(1,n+1)}
 H={};unit_blocks=True
 for k in range(n):
  bk=len(B[k]);bnext=len(B[k+1]);A=Dp[k+1][:bk,bnext:]
  if A.shape!=(bk,bk) or (bk and abs(A.det())!=1):unit_blocks=False
  h=s.zeros(dims[k+1],dims[k])
  if bk:h[bnext:bnext+bk,0:bk]=A.inv()
  H[k]=h
 identity=True
 for k in range(n+1):
  term=s.zeros(dims[k])
  if k<n:term+=Dp[k+1]*H[k]
  if k>0:term+=H[k-1]*Dp[k]
  if term!=s.eye(dims[k]):identity=False
 return {'dimensions':dims,'boundary_ranks':[D[k].rank() for k in range(1,n+1)],'unit_basis_changes':unit_bases,'unit_differential_blocks':unit_blocks,'contraction_identity':identity}

checks={};dimensions={}
for n in range(3,9):
 rec=contraction(n);dimensions[str(n)]=rec
 checks[f'unit_bases_n{n}']=rec['unit_basis_changes'];checks[f'unit_blocks_n{n}']=rec['unit_differential_blocks'];checks[f'contraction_n{n}']=rec['contraction_identity']
text=PACKET.read_text(encoding='utf-8');checks['choice_boundary_retained']='selected filler representative is not yet canonical' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.canonical-relative-chain-contractions.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'dimensions':dimensions,'checks':checks,'passed':all(checks.values()),'disposition':{'established':'explicit integral split-basis contractions through n=8','residual':'uniform combinatorial contraction independent of pivot choices'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'dimensions':{n:{k:v for k,v in r.items() if k!='dimensions' and k!='boundary_ranks'} for n,r in dimensions.items()}}));raise SystemExit(0 if result['passed'] else 1)
