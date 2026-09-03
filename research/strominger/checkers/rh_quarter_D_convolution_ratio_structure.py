import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")));Q,D,mu=g["Q"],g["D"],g["mu"]
def lc(a):return all(a[i]*a[i]>=a[i-1]*a[i+1] for i in range(1,len(a)-1))
def ratio_orientation(a,b):
 # signs of b_i/a_i adjacent differences on common positive support
 z=[b[i+1]*a[i]-b[i]*a[i+1] for i in range(min(len(a),len(b))-1) if a[i]>0 and a[i+1]>0]
 return "nondecreasing" if all(x>=0 for x in z) else "nonincreasing" if all(x<=0 for x in z) else "mixed"
records=[]
for n in range(2,9):
 for s in range(3):
  H=D(n-2,s+2);Dn=D(n,s);HD=mu(H,Dn);R=mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1));records.append({"n":n,"shift":s,"HD_log_concave":lc(HD),"R_log_concave":lc(R),"R_over_HD_ratio_orientation":ratio_orientation(HD,R),"HD_degree":len(HD)-1,"R_degree":len(R)-1})
orientations=sorted(set(r["R_over_HD_ratio_orientation"] for r in records));checks={"twenty_one_pairs_checked":len(records)==21,"HD_coefficients_log_concave":all(r["HD_log_concave"] for r in records),"R_coefficients_log_concave":all(r["R_log_concave"] for r in records),"uniform_likelihood_ratio_orientation":len(orientations)==1 and orientations[0]!="mixed"}
result={"schema":"marici.strominger.rh_quarter_D_convolution_ratio_structure.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact coefficient tests classify whether log-concavity and monotone likelihood-ratio order provide the missing diagonal convolution inequality. A mixed ratio or failed log-concavity is an exact obstruction to that route, not to dominance itself.","orientations":orientations,"records":records,"first_failure":next((r for r in records if not(r["HD_log_concave"] and r["R_log_concave"] and r["R_over_HD_ratio_orientation"]!="mixed")),None),"checks":checks}
(base/"results"/"rh_quarter_D_convolution_ratio_structure.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"orientations":orientations,"first_failure":result["first_failure"],"checks":checks},indent=2))
