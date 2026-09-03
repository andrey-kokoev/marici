"""Exact finite checker for the synthetic proof-bearing radial witness."""
import copy,json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path('research/nima')
BASE=json.loads((ROOT/'contracts/g4-proof-bearing-witness-synthetic.v1.json').read_text())
def M(a): return [[F(x) for x in r] for r in a]
def mm(a,b):
 a,b=M(a),M(b);return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def rank(a):
 a=M(a);m=len(a);n=len(a[0]);r=0
 for c in range(n):
  p=next((i for i in range(r,m) if a[i][c]),None)
  if p is None: continue
  a[r],a[p]=a[p],a[r];q=a[r][c];a[r]=[x/q for x in a[r]]
  for i in range(m):
   if i!=r and a[i][c]: q=a[i][c];a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
  r+=1
 return r
def cols(a): return list(map(list,zip(*M(a))))
def span_equal(a,b):
 A=cols(a);B=cols(b);ra=rank(list(map(list,zip(*A)))) if A else 0;rb=rank(list(map(list,zip(*B)))) if B else 0
 joined=A+B; rj=rank(list(map(list,zip(*joined)))) if joined else 0
 return ra==rb==rj
def validate(c):
 e=[];U,D,Q,P,R,G,SC,SX=map(c.get,['U','D','quotient','recovery','return','green_metric','reciprocal_C','reciprocal_X'])
 if mm(SX,U)!=mm(U,SC): e.append('noncommuting_reciprocal_square')
 if mm(P,U)!=M(U): e.append('recovery_not_identity_on_range')
 DU=mm(D,U)
 if rank(U)+len(cols(c['cycle_basis']))!=3 or rank(DU)+len(cols(c['middle_kernel_basis']))!=3: e.append('inexact_kernel_witness')
 if not span_equal(c['cycle_basis'],c['middle_kernel_basis']): e.append('inexact_kernel_sequence')
 if not span_equal(c['cycle_basis'],[[0],[0],[1]]) or not span_equal(c['cycle_basis'],[[0],[0],[1]]): e.append('wrong_cycle_basis')
 if not span_equal(c['cycle_basis'],[[0],[0],[1]]) or rank(G)!=2 or any(mm(G,c['cycle_basis'])[i][0] for i in range(3)): e.append('extra_or_missing_green_radical')
 for p in c['projections'].values():
  if any(mm(p,c['cycle_basis'])[i][0] for i in range(len(p))): e.append('projection_does_not_descend');break
 grades=c['projective_grades']
 for j,g in enumerate(grades):
  for i,h in enumerate(grades):
   if h>g and R[i][j]!=0: e.append('projective_continuity_failure');break
  if e and e[-1]=='projective_continuity_failure': break
 return e
base=validate(BASE);assert base==[]
h={}
for name,mut in {
 'noncommuting':lambda c:c.__setitem__('reciprocal_X',[[1,0,0],[0,1,0],[0,0,1]]),
 'inexact':lambda c:c.__setitem__('middle_kernel_basis',[[1],[0],[0]]),
 'recovery_break':lambda c:c.__setitem__('recovery',[[1,0,0],[0,0,0],[0,0,1]]),
 'projection_break':lambda c:c['projections'].__setitem__('prime',[[1,0,1]]),
 'extra_radical':lambda c:c.__setitem__('green_metric',[[1,0,0],[0,0,0],[0,0,0]]),
 'continuity_break':lambda c:c.__setitem__('return',[[1,0,0],[0,1,0],[1,0,0]])}.items():
 x=copy.deepcopy(BASE);mut(x);h[name]=validate(x);assert h[name]
out={'schema':'marici.g4-proof-bearing-witness-check.v1','status':'passed','baseline_errors':base,'hostile_results':h,'laws_checked':['reciprocal_covariance','kernel_sequence_exactness','recovery_on_range','quotient_projection_descent','green_rank_and_radical','finite_projective_continuity'],'claim_boundary':BASE['claim_boundary']}
(ROOT/'results/g4-proof-bearing-witness-synthetic.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
