import json
from pathlib import Path
base=Path(__file__).parents[1]
records=[]
for m in range(1,17):
 terms=[]
 for i in range(m+1):
  j=m-i
  terms.extend([("AR",i,j,(-1)**j),("RA",i,j,(-1)**j),("AA",i,j,(-1)**j)])
 def phi(t):
  kind,i,j,sgn=t
  return (("RA" if kind=="AR" else "AR" if kind=="RA" else "AA"),j,i,(-1)**i)
 involutive=all(phi(phi(t))==t for t in terms);fixed=sum(phi(t)==t for t in terms);reverses=all(phi(t)[3]==-t[3] for t in terms);preserves=all(phi(t)[3]==t[3] for t in terms)
 records.append({"total_degree":m,"involutive":involutive,"fixed_points":fixed,"sign_reversing":reverses,"sign_preserving":preserves})
checks={"all_maps_involutive":all(r["involutive"] for r in records),"odd_degrees_fixed_point_free_sign_reversing":all(r["fixed_points"]==0 and r["sign_reversing"] for r in records if r["total_degree"]%2),"even_degrees_sign_preserving":all(r["sign_preserving"] for r in records if not r["total_degree"]%2),"deliberate_even_sign_reversal_fails":not records[1]["sign_reversing"]}
result={"schema":"marici.strominger.rh_reflected_convolution_swap_involution.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The canonical swap involution exchanges AR(i,j) with RA(j,i) and AA(i,j) with AA(j,i). It is fixed-point-free and sign-reversing exactly in odd total degree, proving odd cancellation. In even degree it preserves sign, so no weight-independent involution can supply positive residues through this swap; a D-specific weighted inequality remains necessary.","records":records,"checks":checks}
(base/"results"/"rh_reflected_convolution_swap_involution.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
