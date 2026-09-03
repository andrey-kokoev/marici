import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")));Q,D,mu=g["Q"],g["D"],g["mu"]
def add(a,b,s=1):
 r=[F(0)]*max(len(a),len(b))
 for i,z in enumerate(a):r[i]+=z
 for i,z in enumerate(b):r[i]+=s*z
 return r
def modsq(p):
 e=[(-1)**k*p[2*k] for k in range((len(p)+1)//2)];o=[(-1)**k*p[2*k+1] for k in range(len(p)//2)];return add(mu(e,e),[F(0)]+mu(o,o))
records=[];all_same_index=True;all_strict=True
for n in range(2,9):
 for s in range(3):
  H=D(n-2,s+2);Dn=D(n,s);R=mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1));HD=mu(H,Dn);P=add(R,HD);square=modsq(HD);cross=add(add(modsq(P),modsq(R),-1),square,-1);neg=[]
  for k,x in enumerate(cross):
   if x<0:
    cap=square[k] if k<len(square) else F(0);ratio=(-x)/cap if cap else None;neg.append({"index":k,"capacity_nonzero":cap>0,"strictly_covered":cap>-x,"demand_over_capacity":None if ratio is None else str(ratio)});all_same_index &= cap>0;all_strict &= cap>-x
  records.append({"n":n,"shift":s,"negative_cross_count":len(neg),"negative_indices":[z["index"] for z in neg],"same_index_all_covered":all(z["capacity_nonzero"] and z["strictly_covered"] for z in neg),"matches":neg})
checks={"twenty_one_profiles_checked":len(records)==21,"every_negative_cross_coefficient_has_same_index_capacity":all_same_index,"every_same_index_match_is_strict":all_strict,"some_negative_cross_coefficient_present":any(r["negative_cross_count"] for r in records)}
result={"schema":"marici.strominger.rh_quarter_D_negative_cross_capacity_profile.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Every negative cross coefficient in the tested D family is strictly dominated by the square coefficient at the same omega-squared index. No transport between indices is needed in the bounded cases; the uniform theorem reduces to a diagonal coefficient inequality.","records":records,"checks":checks}
(base/"results"/"rh_quarter_D_negative_cross_capacity_profile.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"checks":checks,"negative_counts":[r["negative_cross_count"] for r in records]},indent=2))
