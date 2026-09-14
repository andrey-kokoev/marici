#!/usr/bin/env python3
"""Enumerate typed routes, cubical fillers, and residual homology at 522/525."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations,permutations
from math import factorial
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/pyramid_surface_paths_and_fillers_at_cutoff_525.md'
RESULT=ROOT/'research/voevodsky/results/pyramid_surface_paths_and_fillers_525.json'

def primes(n):
 s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
 for p in range(2,int(n**.5)+1):
  if s[p]:s[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if s[i]]
def rank(a):
 if not a:return 0
 a=[r[:] for r in a];out=0
 for c in range(len(a[0]) if a else 0):
  p=next((i for i in range(out,len(a)) if a[i][c]),None)
  if p is None:continue
  a[out],a[p]=a[p],a[out];q=a[out][c];a[out]=[x/q for x in a[out]]
  for i in range(out+1,len(a)):
   if a[i][c]:
    q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[out])]
  out+=1
 return out
def graph(L):
 ps=primes(L//2+2);edges=[]
 for shell,(p,q) in enumerate(zip(ps,ps[1:]),1):
  for k in range(1,L//(p*q)+1):edges.append((k*p,shell,k*q,k*p*q,p,q))
 edges.sort(key=lambda x:(x[3],x[1],x[0]));vertices=sorted({e[0] for e in edges}|{e[2] for e in edges})
 return ps,vertices,edges
def enumerate_cells(L):
 ps,vertices,edges=graph(L);lookup={(s,i):t for s,i,t,_,_,_ in edges};outgoing={v:[] for v in vertices}
 for s,i,t,*_ in edges:outgoing[s].append(i)
 cells={0:[(v,()) for v in vertices],1:[(s,(i,)) for s,i,_,_,_,_ in edges]}
 max_out=max((len(set(x)) for x in outgoing.values()),default=0)
 for degree in range(2,max_out+1):
  found=[]
  for base in vertices:
   for I in combinations(sorted(set(outgoing[base])),degree):
    cube_vertices={0:base};ok=True
    for mask in range(1<<degree):
     if mask not in cube_vertices:continue
     value=cube_vertices[mask]
     for bit,i in enumerate(I):
      if mask>>bit&1:continue
      target=lookup.get((value,i))
      if target is None:ok=False;break
      new=mask|1<<bit
      if new in cube_vertices and cube_vertices[new]!=target:ok=False;break
      cube_vertices[new]=target
     if not ok:break
    if ok and len(cube_vertices)==1<<degree:found.append((base,I))
  if not found:break
  cells[degree]=found
 return ps,vertices,edges,cells
def boundary(cell,ps):
 base,I=cell;out={}
 for r,i in enumerate(I):
  face=I[:r]+I[r+1:];sign=-1 if r%2 else 1;upper=base*ps[i]//ps[i-1]
  out[(upper,face)]=out.get((upper,face),0)+sign;out[(base,face)]=out.get((base,face),0)-sign
 return {k:v for k,v in out.items() if v}
def matrix(domain,codomain,ps):
 ri={c:i for i,c in enumerate(codomain)};a=[[F(0)]*len(domain) for _ in codomain]
 for j,cell in enumerate(domain):
  for face,value in boundary(cell,ps).items():a[ri[face]][j]=F(value)
 return a

checks={};censuses={}
for L in (522,525):
 ps,vertices,edges,cells=enumerate_cells(L);max_degree=max(cells);ranks={};matrices={}
 for degree in range(1,max_degree+1):
  matrices[degree]=matrix(cells[degree],cells[degree-1],ps);ranks[degree]=rank(matrices[degree])
  if degree>=2:
   # Matrix product d_{degree-1} d_degree.
   left=matrices[degree-1];right=matrices[degree]
   checks[f'boundary_squared_{L}_{degree}']=all(sum(left[i][k]*right[k][j] for k in range(len(right)))==0 for i in range(len(left)) for j in range(len(right[0])))
 betti={}
 for degree in range(max_degree+1):
  dim=len(cells[degree]);rank_down=ranks.get(degree,0);rank_up=ranks.get(degree+1,0);betti[degree]=dim-rank_down-rank_up
 censuses[str(L)]={'cell_counts':{str(k):len(v) for k,v in cells.items()},'boundary_ranks':{str(k):v for k,v in ranks.items()},'betti':{str(k):v for k,v in betti.items()},'typed_maximal_paths':sum(factorial(k)*len(v) for k,v in cells.items() if k>=1)}
 checks[f'h1_zero_{L}']=betti.get(1)==0;checks[f'h2_zero_{L}']=betti.get(2,0)==0
checks['cutoff_522_square_count']=censuses['522']['cell_counts'].get('2')==21
checks['cutoff_522_no_cube']=censuses['522']['cell_counts'].get('3',0)==0
checks['cutoff_525_square_count']=censuses['525']['cell_counts'].get('2')==23
checks['cutoff_525_unique_cube']=censuses['525']['cell_counts'].get('3')==1
checks['cutoff_525_cycle_dimension_22']=censuses['525']['cell_counts']['1']-censuses['525']['boundary_ranks']['1']==22
checks['cutoff_525_square_relation_one']=censuses['525']['cell_counts']['2']-censuses['525']['boundary_ranks']['2']==1
ps,vertices,edges,cells=enumerate_cells(525);cube=(30,(1,2,3));checks['canonical_cube_enumerated']=cube in cells[3]
routes=[]
for order in permutations(cube[1]):
 value=cube[0];path=[value]
 for i in order:value=value*ps[i]//ps[i-1];path.append(value)
 routes.append({'order':order,'vertices':path})
checks['six_surface_routes']=len(routes)==6 and len({tuple(r['vertices']) for r in routes})==6
checks['all_routes_30_to_105']=all(r['vertices'][0]==30 and r['vertices'][-1]==105 for r in routes)
text=PACKET.read_text(encoding='utf-8');checks['view_scope_retained']='does not assert that every future pyramid view' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.pyramid-surface-paths-fillers-525.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'censuses':censuses,'canonical_cube_routes':routes,'checks':checks,'passed':all(checks.values()),'disposition':{'surface':'typed maximal paths enumerated per admitted cell','fillers':'all source-derived divisor cubes attached','residuals':'H1 and H2 vanish at 522 and 525; the unique new square relation is filled by the canonical cube'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'censuses':censuses,'cube_routes':len(routes)}));raise SystemExit(0 if result['passed'] else 1)
