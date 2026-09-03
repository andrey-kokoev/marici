import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")));Q,D,mu=g["Q"],g["D"],g["mu"]
def add(a,b,s=1):
 r=[F(0)]*max(len(a),len(b))
 for i,z in enumerate(a):r[i]+=z
 for i,z in enumerate(b):r[i]+=s*z
 while len(r)>1 and r[-1]==0:r.pop()
 return r
def negx(p):return [(-1)**i*z for i,z in enumerate(p)]
records=[];first_failure=None
for n in range(2,9):
 for s in range(3):
  H=D(n-2,s+2);Dn=D(n,s);A=mu(H,Dn);R=mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1));P=add(R,A);difference=add(mu(P,negx(P)),mu(R,negx(R)),-1);factored=add(mu(A,negx(P)),mu(R,negx(A)));identity=difference==factored;odd_zero=all(difference[i]==0 for i in range(1,len(difference),2));even_sign=all(((-1)**k)*difference[2*k]>0 for k in range((len(difference)+1)//2));rec={"n":n,"shift":s,"factorization_exact":identity,"odd_coefficients_zero":odd_zero,"even_coefficients_strictly_alternating":even_sign,"even_coefficient_count":(len(difference)+1)//2};records.append(rec)
  if not(identity and odd_zero and even_sign) and first_failure is None:first_failure=rec
checks={"twenty_one_reflected_factorizations":len(records)==21 and all(r["factorization_exact"] for r in records),"all_odd_coefficients_cancel_exactly":all(r["odd_coefficients_zero"] for r in records),"all_even_coefficients_have_required_sign":all(r["even_coefficients_strictly_alternating"] for r in records)}
result={"schema":"marici.strominger.rh_quarter_D_reflected_product_factorization.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The adjacent parity pairing is the even coefficient of the exact reflected-product identity P(x)P(-x)-R(x)R(-x)=H(x)D_n(x)P(-x)+R(x)H(-x)D_n(-x). Odd coefficients cancel algebraically. Imaginary-axis coefficient positivity is equivalent to strict alternating sign of the even coefficients of this product.","records":records,"first_failure":first_failure,"checks":checks}
(base/"results"/"rh_quarter_D_reflected_product_factorization.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"first_failure":first_failure,"checks":checks},indent=2))
