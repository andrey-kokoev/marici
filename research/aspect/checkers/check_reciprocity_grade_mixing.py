"""Exact Gaussian-integer audit of reciprocity versus grade mixing."""
from pathlib import Path
import json

# Gaussian integers are pairs (real, imaginary).
Z=(0,0); O=(1,0); I=(0,1); MI=(0,-1)
X=[[Z,O],[O,Z]]
Y=[[Z,I],[MI,Z]]
Pp=[[O,Z],[Z,Z]]
Pm=[[Z,Z],[Z,O]]
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def mm(a,b):return [[sum_gauss([mul(a[i][k],b[k][j]) for k in range(2)]) for j in range(2)] for i in range(2)]
def sum_gauss(xs):
 out=Z
 for x in xs:out=add(out,x)
 return out
def conj(a):return [[(x[0],-x[1]) for x in row] for row in a]
def zero(a):return all(x==Z for row in a for x in row)
reverse=mm(mm(Pm,X),Pp)
checks={"X_is_reciprocity_even":conj(X)==X,"Y_is_reciprocity_odd":conj(Y)==[[Z,MI],[I,Z]],"reciprocal_X_has_reverse_grade_block":not zero(reverse),"reciprocity_does_not_force_grade_commutation":not zero(reverse)}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"Gaussian integer pairs","checks":checks,"reverse_block":[[str(x) for x in row] for row in reverse],"conclusion":"conjugation reciprocity excludes the Y coefficient but permits the real symmetric X route, so it does not imply grade confinement"}
out=Path("research/aspect/results/reciprocity_grade_mixing.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
