"""Exact audit: isotropic implies radical only after positivity."""
from fractions import Fraction as F
from pathlib import Path
import json

def mv(a,v):return [sum((a[i][j]*v[j] for j in range(len(v))),F(0)) for i in range(len(a))]
def q(a,v):
 w=mv(a,v);return sum((v[i]*w[i] for i in range(len(v))),F(0))
PSD=[[F(1),0],[0,F(0)]]; IND=[[F(0),F(1)],[F(1),F(0)]]; v=[F(0),F(1)]; e=[F(1),F(0)]
checks={"psd_zero_quadratic_is_radical":q(PSD,v)==0 and mv(PSD,v)==[0,0],"indefinite_isotropic_not_radical":q(IND,e)==0 and mv(IND,e)!=[0,0],"indefinite_cross_pairing_survives":sum((v[i]*mv(IND,e)[i] for i in range(2)),F(0))==1,"full_operator_test_detects_both":mv(PSD,v)==[0,0] and mv(IND,e)!=[0,0]}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"conclusion":"basis quadratic zeros certify radical membership only after full-form positive semidefiniteness; otherwise test Qv=0 directly"}
out=Path("research/aspect/results/psd_radical_test.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
