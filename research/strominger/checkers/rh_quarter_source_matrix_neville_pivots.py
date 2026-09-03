import json
from fractions import Fraction as F
from functools import reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def rise(x,k):
 r=F(1)
 for j in range(k):r*=x+j
 return r
def entry(i,j,a):return reduce(lambda z,s:z*rise(s+a+i,j),ss,F(1))
def neville(A):
 A=[r[:] for r in A];n=len(A);multipliers=[]
 for j in range(n-1):
  for i in range(n-1,j,-1):
   if A[i-1][j]==0:return None,None
   m=A[i][j]/A[i-1][j];multipliers.append(m)
   for k in range(j,n):A[i][k]-=m*A[i-1][k]
 return multipliers,[A[i][i] for i in range(n)]
N=10;records=[];all_values=[]
for a in range(7):
 A=[[entry(i,j,a) for j in range(N)] for i in range(N)];m,p=neville(A);mt,pt=neville([list(r) for r in zip(*A)]);vals=m+p+mt+pt;all_values.extend(vals);records.append({"shift":a,"row_multiplier_count":len(m),"column_multiplier_count":len(mt),"minimum_positive":str(min(vals)),"first_diagonal_pivots":[str(x) for x in p[:4]]})
A=[[entry(i,j,0) for j in range(4)] for i in range(4)];A[0],A[1]=A[1],A[0];badm,badp=neville(A);bad=(badm or [])+(badp or [])
checks={"all_neville_values_strictly_positive":all(v>0 for v in all_values),"tested_size_ten":all(r["row_multiplier_count"]==45 for r in records),"tested_matrix_and_transpose":all(r["column_multiplier_count"]==45 for r in records),"tested_seven_shifts":len(records)==7,"deliberate_row_reversal_breaks_positive_neville_data":badm is None or any(v<=0 for v in bad),"unit_leading_pivot":all(r["first_diagonal_pivots"][0]=="1" for r in records)}
result={"schema":"marici.strominger.rh_quarter_source_matrix_neville_pivots.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact Neville elimination of size-10 source matrices and their transposes tests positivity of every elimination multiplier and diagonal pivot. Passing supplies finite factorization evidence, not an all-size formula.","records":records,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_source_matrix_neville_pivots.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
