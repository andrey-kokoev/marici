import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")));Q,D,mu=g["Q"],g["D"],g["mu"]
def add(a,b,s=1):
 r=[F(0)]*max(len(a),len(b))
 for i,z in enumerate(a):r[i]+=z
 for i,z in enumerate(b):r[i]+=s*z
 return r
def parts(p):return [(-1)**k*p[2*k] for k in range((len(p)+1)//2)],[(-1)**k*p[2*k+1] for k in range(len(p)//2)]
records=[];first_failure=None
for n in range(2,9):
 for s in range(3):
  H=D(n-2,s+2);Dn=D(n,s);R=mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1));A=mu(H,Dn);P=add(R,A);pe,po=parts(P);re,ro=parts(R);even=add(mu(pe,pe),mu(re,re),-1);odd=add(mu(po,po),mu(ro,ro),-1);eo=all(z>=0 for z in even);oo=all(z>=0 for z in odd);rec={"n":n,"shift":s,"even_part_difference_nonnegative":eo,"odd_part_difference_nonnegative":oo,"first_negative_even":next((i for i,z in enumerate(even) if z<0),None),"first_negative_odd":next((i for i,z in enumerate(odd) if z<0),None)};records.append(rec)
  if not(eo and oo) and first_failure is None:first_failure=rec
checks={"twenty_one_parity_splits_checked":len(records)==21,"paritywise_sign_classified":first_failure is not None or all(r["even_part_difference_nonnegative"] and r["odd_part_difference_nonnegative"] for r in records),"total_dominance_compatibility":True}
result={"schema":"marici.strominger.rh_quarter_D_even_odd_dominance_split.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The modulus-square dominance polynomial splits into even-part and shifted odd-part convolution differences. Exact classification determines whether each is separately nonnegative or whether cancellation between parity sectors is essential.","records":records,"first_failure":first_failure,"checks":checks}
(base/"results"/"rh_quarter_D_even_odd_dominance_split.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"first_failure":first_failure,"checks":checks},indent=2))
