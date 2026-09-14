#!/usr/bin/env python3
"""Exact cellular audit of the tetrahedral evaluation-groupoid candidate."""
import hashlib,json,platform
from fractions import Fraction
from itertools import combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
FIX=ROOT/'research/voevodsky/fixtures/tetrahedral_evaluation_groupoid_completion.v1.json'
OUT=ROOT/'research/voevodsky/results/tetrahedral_evaluation_groupoid_completion.json'
data=json.loads(FIX.read_text())
V=tuple(data['vertices'])

def cells(maxdim):
 return {d:list(combinations(range(4),d+1)) for d in range(maxdim+1)}
def boundary(domain,codomain):
 rows={c:i for i,c in enumerate(codomain)};m=[[Fraction(0) for _ in domain] for _ in codomain]
 for j,s in enumerate(domain):
  for i in range(len(s)):
   face=s[:i]+s[i+1:];m[rows[face]][j]+=Fraction((-1)**i)
 return m
def rank(m):
 if not m:return 0
 a=[r[:] for r in m];nr=len(a);nc=len(a[0]);r=0
 for c in range(nc):
  pivot=next((i for i in range(r,nr) if a[i][c]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];q=a[r][c];a[r]=[x/q for x in a[r]]
  for i in range(nr):
   if i!=r and a[i][c]:
    q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
  r+=1
 return r
def multiply(a,b):
 if not a or not b:return []
 return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def audit(maxdim):
 c=cells(maxdim);ds={d:boundary(c[d],c[d-1]) for d in range(1,maxdim+1)}
 chain_ok=all(all(x==0 for row in multiply(ds[d-1],ds[d]) for x in row) for d in range(2,maxdim+1))
 betti=[]
 for d in range(maxdim+1):
  rd=rank(ds[d]) if d else 0;rup=rank(ds[d+1]) if d<maxdim else 0
  betti.append(len(c[d])-rd-rup)
 return betti,chain_ok
checks={};observed={}
for case in data['surroundings']:
 md=max(case['include_dimensions']);b,ok=audit(md);observed[case['id']]={'betti':b,'chain_complex':ok};checks[f"{case['id']}_betti"]=b==case['expected_betti'];checks[f"{case['id']}_boundary_squared_zero"]=ok
face_order=[f['id'] for f in data['oriented_faces']];coeff=[f['coefficient'] for f in data['oriented_faces']]
checks['oriented_tetrahedral_boundary']=face_order==['F1','F2','F3','F4'] and coeff==[1,-1,1,-1] and data['bulk']['boundary']=='F1-F2+F3-F4'
checks['missing_bulk_deliberate_failure_exhibits_H2']=observed['boundary_only']['betti'][2]==1
checks['bulk_kills_exact_boundary_obstruction']=observed['full_bulk']['betti'][2]==0
out={'schema':'marici.voevodsky.tetrahedral-evaluation-groupoid-completion-check.v1','passed':all(checks.values()),'checks':checks,'observed':observed,'disposition':'The full tetrahedral component is contractible; its boundary, edge, and vertex truncations are not. Simplification to one evaluation is licensed only for this local completed component.','claim_boundary':data['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_tetrahedral_evaluation_groupoid_completion.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
