#!/usr/bin/env python3
"""Sparse exact-modular cubical census at cutoffs 8084 and 8085."""
from hashlib import sha256
from itertools import combinations,permutations
from math import factorial
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/pyramid_surface_paths_and_fillers_at_cutoff_8085.md'
PROBE=ROOT/'research/voevodsky/results/grade_8085_four_cube_probe_depth.json'
RESULT=ROOT/'research/voevodsky/results/pyramid_surface_paths_and_fillers_8085.json'
MODS=(1000000007,1000000009)

def primes(n):
 s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if s[p]:s[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if s[i]]
def graph(L):
 ps=primes(L//2+2);edges=[]
 for shell,(p,q) in enumerate(zip(ps,ps[1:]),1):
  for k in range(1,L//(p*q)+1):edges.append((k*p,shell,k*q,k*p*q,p,q))
 edges.sort(key=lambda x:(x[3],x[1],x[0]));vertices=sorted({e[0] for e in edges}|{e[2] for e in edges});return ps,vertices,edges
def cells_at(L):
 ps,vertices,edges=graph(L);lookup={(s,i):t for s,i,t,_,_,_ in edges};out={v:set() for v in vertices}
 for s,i,*_ in edges:out[s].add(i)
 cells={0:[(v,()) for v in vertices],1:[(s,(i,)) for s,i,_,_,_,_ in edges]};degree=2
 while True:
  found=[]
  for base in vertices:
   for I in combinations(sorted(out[base]),degree):
    values={0:base};ok=True
    for mask in range(1<<degree):
     if mask not in values:continue
     value=values[mask]
     for bit,i in enumerate(I):
      if mask>>bit&1:continue
      target=lookup.get((value,i));new=mask|1<<bit
      if target is None or (new in values and values[new]!=target):ok=False;break
      values[new]=target
     if not ok:break
    if ok and len(values)==1<<degree:found.append((base,I))
  if not found:break
  cells[degree]=found;degree+=1
 return ps,vertices,edges,cells
def boundary(cell,ps):
 base,I=cell;out={}
 for r,i in enumerate(I):
  face=I[:r]+I[r+1:];sign=-1 if r%2 else 1;upper=base*ps[i]//ps[i-1]
  out[(upper,face)]=out.get((upper,face),0)+sign;out[(base,face)]=out.get((base,face),0)-sign
 return {k:v for k,v in out.items() if v}
def rank_columns(domain,codomain,ps,p):
 row_index={cell:i for i,cell in enumerate(codomain)};basis={}
 for cell in domain:
  column={row_index[face]:value%p for face,value in boundary(cell,ps).items()}
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
def boundary_squared(cell,ps):
 out={}
 for face,a in boundary(cell,ps).items():
  for subface,b in boundary(face,ps).items():out[subface]=out.get(subface,0)+a*b
 return all(v==0 for v in out.values())

checks={};censuses={};raw={}
for L in (8084,8085):
 ps,vertices,edges,cells=cells_at(L);raw[L]=(ps,vertices,edges,cells);ranks_by_mod=[]
 for p in MODS:
  ranks={str(k):rank_columns(cells[k],cells[k-1],ps,p) for k in range(1,max(cells)+1)};ranks_by_mod.append(ranks)
 checks[f'moduli_agree_{L}']=ranks_by_mod[0]==ranks_by_mod[1]
 checks[f'boundary_squared_{L}']=all(boundary_squared(cell,ps) for k in range(2,max(cells)+1) for cell in cells[k])
 ranks={int(k):v for k,v in ranks_by_mod[0].items()};betti={k:len(cells[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in cells}
 checks[f'positive_homology_zero_{L}']=all(betti[k]==0 for k in betti if k>0)
 censuses[str(L)]={'cell_counts':{str(k):len(v) for k,v in cells.items()},'boundary_ranks':ranks_by_mod[0],'betti':{str(k):v for k,v in betti.items()},'typed_maximal_paths':sum(factorial(k)*len(v) for k,v in cells.items() if k>0)}
checks['no_four_cell_below']=censuses['8084']['cell_counts'].get('4',0)==0
checks['unique_four_cell_at']=censuses['8085']['cell_counts'].get('4',0)==1
ps,vertices,edges,cells=raw[8085];canonical=(210,(1,2,3,4));checks['canonical_four_cell']=canonical in cells[4]
routes=[]
for order in permutations(canonical[1]):
 value=canonical[0];path=[value]
 for i in order:value=value*ps[i]//ps[i-1];path.append(value)
 routes.append({'order':order,'vertices':path})
checks['twenty_four_routes']=len(routes)==24 and len({tuple(r['vertices']) for r in routes})==24
checks['routes_share_endpoints']=all(r['vertices'][0]==210 and r['vertices'][-1]==1155 for r in routes)
# Count canonical faces by choosing fixed coordinates outside each direction subset.
canonical_vertices={}
for mask in range(16):
 value=210
 for bit,i in enumerate(canonical[1]):
  if mask>>bit&1:value=value*ps[i]//ps[i-1]
 canonical_vertices[mask]=value
face3=sum((canonical_vertices[mask],tuple(canonical[1][b] for b in dirs)) in cells[3] for dirs in combinations(range(4),3) for mask in range(16) if all(not(mask>>b&1) for b in dirs))
face2=sum((canonical_vertices[mask],tuple(canonical[1][b] for b in dirs)) in cells[2] for dirs in combinations(range(4),2) for mask in range(16) if all(not(mask>>b&1) for b in dirs))
checks['all_eight_three_faces']=face3==8;checks['all_twenty_four_square_faces']=face2==24
probe=json.loads(PROBE.read_text(encoding='utf-8'));checks['probe_zero_one_zero']=all(a['joint'][1]['deficiency']==0 and b['joint'][1]['deficiency']==1 and b['joint'][2]['deficiency']==0 for a,b in zip(probe['census']['8084']['ranks'],probe['census']['8085']['ranks']))
text=PACKET.read_text(encoding='utf-8');checks['residual_commitment_retained']='retained as a genuine pyramid residual' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.pyramid-surface-paths-fillers-8085.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'censuses':censuses,'canonical_four_cube':{'routes':routes,'square_faces':face2,'three_faces':face3},'checks':checks,'passed':all(checks.values()),'disposition':{'surface':'24 canonical paths and all lower faces admitted','fillers':'unique four-cell admitted at 8085','residuals':'positive-degree cubical homology vanishes while probe deficiency follows zero-one-zero'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'censuses':censuses,'faces':[face2,face3],'routes':len(routes)}));raise SystemExit(0 if result['passed'] else 1)
