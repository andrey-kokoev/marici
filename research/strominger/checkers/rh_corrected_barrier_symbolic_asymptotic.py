import json
from fractions import Fraction as F
from pathlib import Path
M=8
def add(a,b):return [a[i]+b[i] for i in range(M)]
def mul(a,b):return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(M)]
def inv(a):
 q=[F(0)]*M;q[0]=1/a[0]
 for i in range(1,M):q[i]=-sum(a[j]*q[i-j] for j in range(1,i+1))/a[0]
 return q
def scale(a,c):return [c*x for x in a]
def ratio_leading_x(a,b):
 return mul(a[1:]+[F(0)],inv(b[1:]+[F(0)]))
def critical(k,c,r2=F(10),r3=F(0),r4=F(0)):
 x=[F(0),F(1)]+[F(0)]*(M-2)
 def shifted(sign):
  y=[F(0)]+[F((-sign)**(j-1)) for j in range(1,M)]
  den=add([F(1)]+[F(0)]*(M-1),scale(y,k));y2=mul(y,y)
  return mul(mul(y,inv(den)),add([F(1)]+[F(0)]*(M-1),scale(y2,c)))
 v=shifted(0);vp=shifted(1);vm=shifted(-1);r=[F(1),F(-4),r2,r3,r4]+[F(0)]*(M-5);one=[F(1)]+[F(0)]*(M-1)
 return add(add(one,r),scale(add(ratio_leading_x(vp,v),mul(r,ratio_leading_x(vm,v))),-1))
base=critical(F(0),F(0));khalf=critical(F(1,2),F(0));c1=critical(F(0),F(1));r3one=critical(F(0),F(0),r3=F(1))
checks={
 "leading_defect_is_two":base[2]==2,
 "kappa_absent_through_third_order":all(khalf[j]==base[j] for j in range(2,4)),
 "kappa_changes_fourth_order":khalf[4]!=base[4],
 "c_absent_through_third_order":all(c1[j]==base[j] for j in range(2,4)),
 "c_changes_fourth_order":c1[4]!=base[4],
 "r3_changes_fourth_order":r3one[4]!=base[4],
}
result={"schema":"marici.strominger.rh_corrected_barrier_symbolic_asymptotic.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact truncated-series algebra shows kappa, c, and the unknown r3 coefficient of a_n/a_(n+1) all first change the critical defect at n^-4. Thus the observed fourth-order slack constrains only a combination of these three quantities and cannot source the fitted barrier parameters separately.","checks":checks,"baseline_coefficients":{str(j):str(base[j]) for j in range(2,7)},"fourth_order_kappa_half_increment":str(khalf[4]-base[4]),"fourth_order_c_increment":str(c1[4]-base[4]),"fourth_order_r3_increment":str(r3one[4]-base[4]),"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
basepath=Path(__file__).parents[1];(basepath/"results"/"rh_corrected_barrier_symbolic_asymptotic.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
