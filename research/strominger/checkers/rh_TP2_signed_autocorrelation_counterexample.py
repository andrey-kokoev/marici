import json
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1]
def mu(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):r[i+j]+=a*b
 return r
def add(a,b,s=1):
 r=[F(0)]*max(len(a),len(b))
 for i,z in enumerate(a):r[i]+=z
 for i,z in enumerate(b):r[i]+=s*z
 return r
def modcross(a,b):
 # coefficients in y=w^2 of 2 Re(a(iw) conjugate(b(iw)))
 ae=[(-1)**k*a[2*k] for k in range((len(a)+1)//2)];ao=[(-1)**k*a[2*k+1] for k in range(len(a)//2)];be=[(-1)**k*b[2*k] for k in range((len(b)+1)//2)];bo=[(-1)**k*b[2*k+1] for k in range(len(b)//2)]
 return [2*z for z in add(mu(ae,be),[F(0)]+mu(ao,bo))]
def modsq(a):return [z/2 for z in modcross(a,a)]
def lc(a):return all(a[i]*a[i]>=a[i-1]*a[i+1] for i in range(1,len(a)-1))
a=[F(1),F(1)];b=[F(1),F(10),F(100)];total=add(modsq(a),modcross(a,b));mlr=b[1]*a[0]>=b[0]*a[1]
checks={"a_positive_log_concave":all(x>0 for x in a) and lc(a),"b_positive_log_concave":all(x>0 for x in b) and lc(b),"b_over_a_nondecreasing_on_common_support":mlr,"signed_autocorrelation_coefficient_is_negative":total[1]==-179}
result={"schema":"marici.strominger.rh_TP2_signed_autocorrelation_counterexample.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Log-concavity and monotone likelihood-ratio order do not imply the signed autocorrelation bound. For a(x)=1+x and b(x)=1+10x+100x^2, both sequences are positive and log-concave and b_i/a_i increases on common support, yet the omega^2 coefficient of |a(iw)|^2+2Re(a(iw)conjugate(b(iw))) is -179.","a":[str(x) for x in a],"b":[str(x) for x in b],"signed_coefficients":[str(x) for x in total],"checks":checks}
(base/"results"/"rh_TP2_signed_autocorrelation_counterexample.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
