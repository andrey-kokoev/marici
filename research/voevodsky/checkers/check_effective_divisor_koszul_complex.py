#!/usr/bin/env python3
"""Exact cubical boundary and graded-product checks for divisor cells."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/effective_divisor_cube_chains_form_a_partial_koszul_complex.md'
RESULT=ROOT/'research/voevodsky/results/effective_divisor_koszul_complex.json'
PRIMES=(2,3,5,7,11,13,17,19)
# A cell is (base divisor tuple, ordered direction tuple).
def root(base,i):
 out=list(base);out[i]-=1;out[i+1]+=1
 return tuple(out)
def add_base(a,b):return tuple(x+y for x,y in zip(a,b))
def admissible(cell):
 base,I=cell
 for r in range(len(I)+1):
  for S in combinations(I,r):
   d=base
   for i in S:d=root(d,i)
   if min(d)<0:return False
 return True
def chain_add(out,cell,value):
 out[cell]=out.get(cell,0)+value
 if out[cell]==0:del out[cell]
def boundary_cell(cell):
 base,I=cell;out={}
 for r,i in enumerate(I):
  face=I[:r]+I[r+1:];sign=-1 if r%2 else 1
  chain_add(out,(root(base,i),face),sign);chain_add(out,(base,face),-sign)
 return out
def boundary(chain):
 out={}
 for cell,coefficient in chain.items():
  for face,value in boundary_cell(cell).items():chain_add(out,face,coefficient*value)
 return out
def product_cell(a,b):
 da,I=a;db,J=b
 if set(I)&set(J):return None
 inversions=sum(i>j for i in I for j in J);sign=-1 if inversions%2 else 1
 return (add_base(da,db),tuple(sorted(I+J))),sign
def product(a,b):
 out={}
 for ca,xa in a.items():
  for cb,xb in b.items():
   p=product_cell(ca,cb)
   if p:chain_add(out,p[0],xa*xb*p[1])
 return out
def integer(d):
 out=1
 for p,e in zip(PRIMES,d):out*=p**e
 return out
def minimal(I):
 d=[0]*len(PRIMES)
 for i in I:d[i]+=1
 return tuple(d)

checks={};cells=[];boundary_tests=0;face_tests=0
for size in range(1,7):
 for I in combinations(range(6),size):
  cell=(minimal(I),I);cells.append(cell);checks[f'admissible_{I}']=admissible(cell)
  checks[f'boundary_squared_{I}']=boundary(boundary({cell:1}))=={};boundary_tests+=1
  base,I0=cell
  for face,coefficient in boundary_cell(cell).items():
   fb,FI=face;checks[f'face_admissible_{I}_{integer(fb)}_{FI}_{coefficient}']=admissible(face)
   # Face base is one of the cube's arithmetic subset vertices.
   quotient=integer(fb)
   checks[f'face_integer_{I}_{quotient}_{FI}_{coefficient}']=quotient>=1;face_tests+=1
leibniz_tests=0
for a in cells:
 for b in cells:
  if set(a[1])&set(b[1]):continue
  left=boundary(product({a:1},{b:1}));right=product(boundary({a:1}),{b:1});term=product({a:1},boundary({b:1}));sign=-1 if len(a[1])%2 else 1
  for cell,value in term.items():chain_add(right,cell,sign*value)
  checks[f'leibniz_{a[1]}_{b[1]}']=left==right;leibniz_tests+=1
# Deliberate scope edge: exterior repetition vanishes although two chips can move serially.
i=2;double=[0]*len(PRIMES);double[i]=2;double=tuple(double)
checks['overlap_product_zero']=product_cell((double,(i,)),(double,(i,))) is None
checks['two_same_shell_serial_moves_effective']=min(root(root(double,i),i))>=0
text=PACKET.read_text(encoding='utf-8');checks['repeated_move_scope_retained']='divided-power or labelled-chip extension' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.effective-divisor-koszul-complex.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'cells_tested':len(cells),'boundary_squared_tests':boundary_tests,'face_tests':face_tests,'leibniz_tests':leibniz_tests,'checks':checks,'passed':all(checks.values()),'disposition':{'established':'oriented divisor cubes form a partial Koszul chain algebra for distinct shell directions','residual':'same-shell multiplicities need divided powers or labelled-chip cubical data'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'cells':len(cells),'boundary_squared':boundary_tests,'faces':face_tests,'leibniz':leibniz_tests}));raise SystemExit(0 if result['passed'] else 1)
