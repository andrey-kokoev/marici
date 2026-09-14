#!/usr/bin/env python3
"""Scan exact-grade distinct-shell relative homology through grade 20000."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/noncanonical_attachment_homology_scan.md'
RESULT=ROOT/'research/voevodsky/results/noncanonical_attachment_homology_scan.json'
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
def min_grade(I):return PS[I[-1]-1]*product(PS[i] for i in I)
def min_base(I):return product(PS[i-1] for i in I)
def vertex_birth(v):
 costs=[]
 for p,q in zip(PS,PS[1:]):
  if v%p==0:costs.append(v*q)
  if v%q==0:costs.append(v*p)
 return min(costs) if costs else None
def rank(columns,row_index,p):
 basis={}
 for entries in columns:
  col={row_index[x]:a%p for x,a in entries.items()}
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
# Enumerate positive cells by exact birth grade.
K=max(i for i in range(1,len(PS)) if PS[i-1]*PS[i]<=LIMIT)
by_grade={}
for size in range(1,10):
 any_cell=False
 for I in combinations(range(1,K+1),size):
  g=min_grade(I)
  if g>LIMIT:continue
  any_cell=True;B=min_base(I)
  for k in range(1,LIMIT//g+1):by_grade.setdefault(k*g,{}).setdefault(size,[]).append((k*B,I))
 if not any_cell:break
# Degree-zero generators come from endpoints whose first incident edge has this grade.
for L,degrees in by_grade.items():
 endpoints=set()
 for base,(i,) in degrees.get(1,[]):endpoints|={base,base*PS[i]//PS[i-1]}
 degrees[0]=[(v,()) for v in sorted(endpoints) if vertex_birth(v)==L]
checks={};nonzero=[];first_by_degree={};canonical={525,8085}
for L in sorted(by_grade):
 cells=by_grade[L];top=max(cells);sets={k:set(cells.get(k,[])) for k in range(top+1)}
 def boundary(cell):
  base,I=cell;out={}
  for r,i in enumerate(I):
   J=I[:r]+I[r+1:];sign=-1 if r%2 else 1;upper=base*PS[i]//PS[i-1]
   for f,a in (((upper,J),sign),((base,J),-sign)):
    if f in sets[len(J)]:out[f]=out.get(f,0)+a
  return {f:a for f,a in out.items() if a}
 columns={k:[boundary(c) for c in cells.get(k,[])] for k in range(1,top+1)}
 square=True
 for k in range(2,top+1):
  for col in columns[k]:
   total={}
   for f,a in col.items():
    for x,b in boundary(f).items():total[x]=total.get(x,0)+a*b
   if any(total.values()):square=False
 checks[f'boundary_squared_{L}']=square
 ranksets=[]
 for p in MODS:ranksets.append({k:rank(columns[k],{c:i for i,c in enumerate(cells.get(k-1,[]))},p) for k in range(1,top+1)})
 checks[f'fields_agree_{L}']=ranksets[0]==ranksets[1]
 betti=[len(cells.get(k,[]))-ranksets[0].get(k,0)-ranksets[0].get(k+1,0) for k in range(top+1)]
 if any(betti):
  record={'grade':L,'cell_counts':[len(cells.get(k,[])) for k in range(top+1)],'boundary_ranks':[ranksets[0].get(k,0) for k in range(1,top+1)],'betti':betti}
  nonzero.append(record)
  for k,b in enumerate(betti):
   if b and str(k) not in first_by_degree:first_by_degree[str(k)]=record
 if L in canonical:checks[f'canonical_acyclic_{L}']=not any(betti)
summary={'event_grades':len(by_grade),'nonzero_event_grades':len(nonzero),'first_noncanonical':next((r for r in nonzero if r['grade'] not in canonical),None),'first_by_degree':first_by_degree,'canonical_grades_checked':sorted(canonical & set(by_grade))}
checks['noncanonical_example_found']=summary['first_noncanonical'] is not None
checks['both_canonical_grades_acyclic']=summary['canonical_grades_checked']==[525,8085] and all(not any(next(r['betti'] for r in nonzero if r['grade']==L)) if any(r['grade']==L for r in nonzero) else True for L in canonical)
text=PACKET.read_text(encoding='utf-8');checks['persistence_boundary_retained']='does not by itself establish persistent absolute homology' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.noncanonical-attachment-homology-scan.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'limit':LIMIT,'summary':summary,'first_twenty_nonzero':nonzero[:20],'checks':checks,'passed':all(checks.values()),'disposition':{'prediction':'survives bounded scan' if summary['first_noncanonical'] else 'fails bounded scan','residual':'persistence of relative classes not tested'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'summary':summary,'checks':len(checks)}));raise SystemExit(0 if result['passed'] else 1)
