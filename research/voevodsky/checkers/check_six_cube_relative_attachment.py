#!/usr/bin/env python3
"""Exact relative-chain test at the canonical six-cube grade."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations,permutations
from math import factorial
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/six_cube_relative_attachment_at_grade_3318315.md'
RESULT=ROOT/'research/voevodsky/results/six_cube_relative_attachment.json'
L=3318315

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
def minimal_grade(I):return PS[I[-1]-1]*product(PS[i] for i in I)
def minimal_base(I):return product(PS[i-1] for i in I)
def cell_grade(base,I):return base//minimal_base(I)*minimal_grade(I)
def vertex_birth(n):
 values=[]
 for i,(p,q) in enumerate(zip(PS,PS[1:]),1):
  if n%p==0:values.append(n*q)
  if n%q==0:values.append(n*p)
 return min(values) if values else None
def rank(a):
 if not a:return 0
 a=[r[:] for r in a];out=0
 for c in range(len(a[0])):
  p=next((i for i in range(out,len(a)) if a[i][c]),None)
  if p is None:continue
  a[out],a[p]=a[p],a[out];q=a[out][c];a[out]=[x/q for x in a[out]]
  for i in range(out+1,len(a)):
   if a[i][c]:
    q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[out])]
  out+=1
 return out
# Enumerate all positive-dimensional cells born exactly at L.
cells={k:[] for k in range(1,7)}
for size in range(1,7):
 for I in combinations(range(1,11),size):
  grade=minimal_grade(I)
  if L%grade==0:cells[size].append((L//grade*minimal_base(I),I))
# Degree-zero relative generators are newly born endpoints of new edges.
endpoints=set()
for base,(i,) in cells[1]:endpoints|={base,base*PS[i]//PS[i-1]}
cells[0]=[(v,()) for v in sorted(endpoints) if vertex_birth(v)==L]
sets={k:set(v) for k,v in cells.items()}
def relative_boundary(cell):
 base,I=cell;out={}
 for r,i in enumerate(I):
  J=I[:r]+I[r+1:];sign=-1 if r%2 else 1;upper=base*PS[i]//PS[i-1]
  for face,value in (((upper,J),sign),((base,J),-sign)):
   if face in sets[len(J)]:out[face]=out.get(face,0)+value
 return {k:v for k,v in out.items() if v}
def matrix(k):
 rows={cell:i for i,cell in enumerate(cells[k-1])};a=[[F(0)]*len(cells[k]) for _ in cells[k-1]]
 for j,cell in enumerate(cells[k]):
  for face,value in relative_boundary(cell).items():a[rows[face]][j]=F(value)
 return a
matrices={k:matrix(k) for k in range(1,7)};ranks={k:rank(a) for k,a in matrices.items()}
checks={}
for k in range(2,7):checks[f'boundary_squared_{k}']=all(sum(matrices[k-1][i][r]*matrices[k][r][j] for r in range(len(cells[k-1])))==0 for i in range(len(cells[k-2])) for j in range(len(cells[k])))
counts=[len(cells[k]) for k in range(7)];expected_counts=[1,5,11,14,11,5,1];expected_ranks=[1,4,7,7,4,1]
checks['attachment_vector']=counts==expected_counts
checks['relative_boundary_ranks']=[ranks[k] for k in range(1,7)]==expected_ranks
betti=[len(cells[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(7)];checks['relative_homology_zero']=betti==[0]*7
path_increment=sum(factorial(k)*len(cells[k]) for k in range(1,7));checks['path_increment_1695']=path_increment==1695
canonical=(30030,(1,2,3,4,5,6));checks['unique_top_cell']=cells[6]==[canonical]
tops=set();route_count=0
for order in permutations(canonical[1]):
 value=canonical[0]
 for i in order:value=value*PS[i]//PS[i-1]
 tops.add(value);route_count+=1
checks['canonical_720_paths_common_top']=route_count==720 and tops=={255255}
checks['all_cell_grades_exact']=all(cell_grade(base,I)==L for k in range(1,7) for base,I in cells[k])
text=PACKET.read_text(encoding='utf-8');checks['absolute_rank_boundary_retained']='No absolute-rank or probe-rank conclusion' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.six-cube-relative-attachment.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'grade':L,'cell_counts':counts,'boundary_ranks':[ranks[k] for k in range(1,7)],'relative_betti':betti,'typed_maximal_path_increment':path_increment,'canonical_top_cell':{'base':30030,'directions':[1,2,3,4,5,6],'route_count':route_count,'top':list(tops)[0]},'cells':{str(k):[{'base':b,'directions':list(I)} for b,I in cells[k]] for k in range(7)},'checks':checks,'passed':all(checks.values()),'disposition':{'prediction':'survives' if all(checks.values()) else 'fails','scope':'relative distinct-shell attachment only'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'counts':counts,'ranks':result['boundary_ranks'],'betti':betti,'paths':path_increment}));raise SystemExit(0 if result['passed'] else 1)
