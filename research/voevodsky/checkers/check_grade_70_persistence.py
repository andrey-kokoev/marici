#!/usr/bin/env python3
"""Persistent-chain test of the degree-two shell-3 edge born at grade 70."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/grade_70_relative_class_persistence_test.md'
RESULT=ROOT/'research/voevodsky/results/grade_70_relative_class_persistence.json'
LIMIT=2000;MODS=(1000000007,1000000009)
def primes(n):
 s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if s[p]:s[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if s[i]]
PS=primes(500)
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
def cell_birth(base,I):return base//min_base(I)*min_grade(I)
def vertex_birth(v):
 costs=[]
 for p,q in zip(PS,PS[1:]):
  if v%p==0:costs.append(v*q)
  if v%q==0:costs.append(v*p)
 return min(costs) if costs else None
# Enumerate degree-two positive cells.
K=max(i for i in range(1,len(PS)) if PS[i-1]*PS[i]<=LIMIT)
cells=[];birth={}
for size in (1,2):
 for I in combinations(range(1,K+1),size):
  g=min_grade(I)
  if g>LIMIT:continue
  B=min_base(I)
  for k in range(1,LIMIT//g+1):
   base=k*B
   if omega(base)==2:
    c=(base,I);cells.append(c);birth[c]=k*g
vertices=set()
for base,(i,) in (c for c in cells if len(c[1])==1):vertices|={base,base*PS[i]//PS[i-1]}
for v in vertices:
 b=vertex_birth(v)
 if b is not None and b<=LIMIT:birth[(v,())]=b
cells=list(birth);cells.sort(key=lambda c:(birth[c],len(c[1]),c[1],c[0]));cellset=set(cells)
def boundary(cell):
 base,I=cell;out={}
 for r,i in enumerate(I):
  J=I[:r]+I[r+1:];sign=-1 if r%2 else 1;upper=base*PS[i]//PS[i-1]
  for f,a in (((upper,J),sign),((base,J),-sign)):
   if f in cellset:out[f]=out.get(f,0)+a
 return {f:a for f,a in out.items() if a}
def rank(cols,rows,p):
 ri={x:i for i,x in enumerate(rows)};basis={}
 for entries in cols:
  col={ri[x]:a%p for x,a in entries.items()}
  while col:
   lead=min(col)
   if lead not in basis:
    inv=pow(col[lead],p-2,p);basis[lead]={k:v*inv%p for k,v in col.items() if v*inv%p};break
   q=col[lead]
   for k,v in basis[lead].items():
    z=(col.get(k,0)-q*v)%p
    if z:col[k]=z
    else:col.pop(k,None)
 return len(basis)
def betti_at(L,p):
 by={k:[c for c in cells if len(c[1])==k and birth[c]<=L] for k in range(3)}
 r1=rank([boundary(c) for c in by[1]],by[0],p);r2=rank([boundary(c) for c in by[2]],by[1],p)
 return [len(by[0])-r1,len(by[1])-r1-r2,len(by[2])-r2]
def persistence(p):
 index={c:i for i,c in enumerate(cells)};basis={};reduced={};pairs={}
 for j,c in enumerate(cells):
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
  if col:
   low=max(col);basis[low]=col;pairs[cells[low]]=c
 return reduced,pairs
edge=(10,(3,));square=(10,(1,3));checks={};snapshots={}
for p in MODS:
 snapshots[str(p)]={str(L):betti_at(L,p) for L in (69,70,104,105)}
red0,pairs0=persistence(MODS[0]);red1,pairs1=persistence(MODS[1])
checks['target_birth_70']=birth.get(edge)==70
checks['edge_reduced_nonzero_both_fields']=bool(red0[edge]) and bool(red1[edge])
checks['edge_not_persistence_birth']=edge not in pairs0 and edge not in pairs1
checks['h0_drops_h1_constant_at_70']=snapshots[str(MODS[0])]['69'][0]-1==snapshots[str(MODS[0])]['70'][0] and snapshots[str(MODS[0])]['69'][1]==snapshots[str(MODS[0])]['70'][1]
checks['fields_agree']=snapshots[str(MODS[0])]==snapshots[str(MODS[1])]
checks['square_birth_105']=birth.get(square)==105
checks['square_contains_edge']=edge in boundary(square)
checks['edge_not_paired_with_square']=pairs0.get(edge)!=square and pairs1.get(edge)!=square
text=PACKET.read_text(encoding='utf-8');checks['scope_retained']='restricted to the multiplicative-degree-two distinct-shell sector' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.grade-70-persistence.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'target_edge':{'base':10,'directions':[3],'birth':birth[edge],'boundary':[{'base':b,'directions':list(I),'birth':birth[(b,I)]} for b,I in boundary(edge)]},'grade_105_square_boundary':[{'base':b,'directions':list(I),'birth':birth[(b,I)]} for b,I in boundary(square)],'absolute_betti':snapshots,'edge_reduced_pivots':{str(MODS[0]):cells[max(red0[edge])][0],str(MODS[1]):cells[max(red1[edge])][0]},'checks':checks,'passed':all(checks.values()),'disposition':{'survivor':'prediction 2','rejected':['absolute H1 birth at 70','persistence pair 70--105'],'meaning':'relative H1 maps to a pre-existing H0 component difference'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'absolute_betti':snapshots,'edge_boundary':result['target_edge']['boundary'],'checks':checks}));raise SystemExit(0 if result['passed'] else 1)
