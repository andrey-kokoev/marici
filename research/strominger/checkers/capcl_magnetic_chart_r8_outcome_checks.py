import json, math
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/strominger/results/capcl_magnetic_chart_r8_outcome.json"
def rising(x,n): return math.prod(x+i for i in range(n))
def coeffs(g,a,m):
 c=[math.comb(g,j)*(-1)**(g-j)*rising(a,g-j)*rising(4-a,j) for j in range(g+1)]
 return [m*c[0]]+[(m+j)*c[j]+(m+j-1-g)*c[j-1] for j in range(1,g+1)]+[m*c[g]]
def col(g,a,m):
 d=1-g-a-m;s=-a-g if d>0 else -a-g+abs(d);sgn=1 if d>0 else -1
 return {s+j:sgn*v for j,v in enumerate(coeffs(g,a,m)) if v}
def component(g,k,q):
 c=1-g;return [col(g,a,m) for a in range(0,2*k+1,2) for m in (c-q-a,c+q-a)]
def hall_rows(cols):
 owner={}
 def aug(i,seen):
  for r in sorted(cols[i]):
   if r in seen: continue
   seen.add(r)
   if r not in owner or aug(owner[r],seen): owner[r]=i;return True
  return False
 assert sum(aug(i,set()) for i in range(len(cols)))==len(cols)
 inv={i:r for r,i in owner.items()};return [inv[i] for i in range(len(cols))]
def det_bareiss(a):
 a=[row[:] for row in a];n=len(a);sign=1;prev=1
 for k in range(n-1):
  if a[k][k]==0:
   p=next((i for i in range(k+1,n) if a[i][k]),None)
   if p is None:return 0
   a[k],a[p]=a[p],a[k];sign=-sign
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):a[i][j]=(a[i][j]*pivot-a[i][k]*a[k][j])//prev
  prev=pivot
 return sign*a[-1][-1]

cols=component(16,12,40); primary_rows=hall_rows(cols)
primary=[[c.get(r,0) for c in cols] for r in primary_rows]
alternate_rows=[3 if r==1 else r for r in primary_rows]
alternate=[[c.get(r,0) for c in cols] for r in alternate_rows]
primary_det=det_bareiss(primary);alternate_det=det_bareiss(alternate)
cocircuit_relation=all((2*16+7)*c.get(1,0)==(3*16+7)*c.get(0,0) for c in cols)
family_cocircuit=[]
for family_g in range(2,17,2):
 family_q=2*family_g+8;family_k=family_g//2+4;family_cols=component(family_g,family_k,family_q)
 family_cocircuit.append({"g":family_g,"q":family_q,"k":family_k,"relation":all((2*family_g+7)*c.get(1,0)==(3*family_g+7)*c.get(0,0) for c in family_cols)})
alternate_family=[]
for family_g in range(2,31,2):
 family_q=2*family_g+8;family_k=family_g//2+4;family_cols=component(family_g,family_k,family_q)
 family_rows=[3 if row==1 else row for row in hall_rows(family_cols)]
 family_det=det_bareiss([[c.get(row,0) for c in family_cols] for row in family_rows])
 alternate_family.append({"g":family_g,"nonzero":family_det!=0,"sign":1 if family_det>0 else -1 if family_det<0 else 0})
all_rows=sorted(set().union(*(c.keys() for c in cols)))
# A nonzero 26x26 alternate minor proves the full 26-column rank directly.
full_rank=26 if alternate_det else None
confirmed=primary_det==0 and alternate_det!=0 and full_rank==26
result={"schema":"marici.strominger.capcl-prediction-outcome.v1","prediction_id":"capcl-magnetic-chart-r8-003","outcome":"confirmed" if confirmed else "falsified","primary_det":str(primary_det),"alternate_det":str(alternate_det),"alternate_row_exchange":{"drop":1,"add":3},"full_row_count":len(all_rows),"full_column_rank":full_rank,"presentation_obstruction":primary_det==0,"observation_obstruction":full_rank!=26,"primitive_row_cocircuit":"(2g+7)R1=(3g+7)R0","target_cocircuit_verified":cocircuit_relation,"family_cocircuit_checks":family_cocircuit,"alternate_family_exact_nonzero_through_g30":all(x["nonzero"] for x in alternate_family),"alternate_family_checks":alternate_family,"remaining_unbounded_obstruction":"nonvanishing_of_2_by_2_boundary_Schur_determinant_after_invertible_triangular_interior_core"}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({**result,"alternate_det":"nonzero" if alternate_det else "zero"},indent=2))
raise SystemExit(0 if confirmed else 1)
