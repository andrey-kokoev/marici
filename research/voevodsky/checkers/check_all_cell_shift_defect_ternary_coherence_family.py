#!/usr/bin/env python3
"""Verify the translated native associator family and its cumulative Ward sum."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/all_cell_shift_defect_ternary_coherence_family.v1.json';OUT=ROOT/'research/voevodsky/results/all_cell_shift_defect_ternary_coherence_family.json';D=json.loads(FIX.read_text())
def z(n):return [[Q(0) for _ in range(n)] for _ in range(n)]
def I(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def T(a):return [list(x) for x in zip(*a)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(a))) for j in range(len(b[0]))] for i in range(len(a))]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(len(a))] for i in range(len(a))]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(len(a))] for i in range(len(a))]
def neg(a):return [[-x for x in r] for r in a]
def Dlt(a):return [[a[i][j] if i==j else Q(0) for j in range(len(a))] for i in range(len(a))]
def star(a,b):return Dlt(mm(a,b))
def B(a,b):return sub(mm(a,b),star(a,b))
def A(a,b,c):return sub(star(star(a,b),c),star(a,star(b,c)))
def powm(a,k):
 r=I(len(a))
 for _ in range(k):r=mm(r,a)
 return r
rows=[];all_formula=all_residue=all_terminal=all_sum=True;previous=None
for n in D['dimensions']:
 S=z(n)
 for j in range(n-1):S[j+1][j]=1
 St=T(S);P0=sub(I(n),mm(S,St));Ps=[mm(mm(powm(S,j),P0),powm(St,j)) for j in range(n)];As=[]
 for j,P in enumerate(Ps):
  Y=mm(P,St);Z=mm(S,P);a=A(P,Y,Z)
  if j<n-1:
   all_formula &= a==neg(P);all_residue &= B(P,Y)==Y;As.append(a)
  else:all_terminal &= Y==z(n) and a==z(n)
 total=z(n)
 for a in As:total=add(total,a)
 all_sum &= total==neg(sub(I(n),Ps[-1]))
 if previous is not None:
  # Every previously nonterminal cell remains identical in the prefix block.
  for j in range(n-2):all_formula &= all(Ps[j][r][c]==previous[j][r][c] for r in range(n-1) for c in range(n-1))
 previous=Ps;rows.append({'dimension':n,'nonterminal_associator_count':len(As),'terminal_associator_zero':A(Ps[-1],mm(Ps[-1],St),mm(S,Ps[-1]))==z(n),'cumulative_diagonal':[str(total[j][j]) for j in range(n)]})
checks={'uniform_nonterminal_formula':all_formula,'uniform_binary_edge_residue':all_residue,'terminal_loop_absent':all_terminal,'cumulative_family_is_negative_nonterminal_Ward_projector':all_sum,'coefficient_independent_of_grade_and_cutoff':all_formula,'prefix_family_naturality':all_formula}
out={'schema':'marici.voevodsky.all-cell-shift-defect-ternary-coherence-family-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'cutoff_rows':rows,'local_formula':'A3(Pj,Pj S*,S Pj)=-Pj for j<N','cumulative_formula':'sum_(j<N) A3_j=-(I-P_N)'},'falsification_disposition':'The primitive-exception conjecture is falsified. Every nonterminal cell carries the same translated ternary coherence with coefficient minus one. The finite terminal cell lacks the required outward edge, and the family sums to the negative nonterminal Ward projector.','surviving_scope':'A cutoff-natural local coherence density on all cells once they are nonterminal; no unbounded summation or temporal interpretation.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_all_cell_shift_defect_ternary_coherence_family.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
