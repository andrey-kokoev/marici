"""Exact robustness arithmetic for relative physical-form coercivity."""
from fractions import Fraction as F
from pathlib import Path
import json

eta_hat=F(1,4); eps_h=F(1,10)
cases={"strict":F(1,20),"boundary":F(9,40),"failed":F(1,4)}
rows={}
for name,eps_g in cases.items():
 eta=eta_hat*(1-eps_h)-eps_g
 margin=2*eta-eta*eta if eta>0 else F(0)
 rows[name]={"form_error":str(eps_g),"certified_eta":str(eta),"return_margin_lower":str(margin),"strict":eta>0}
checks={"strict_eta_exact":rows["strict"]["certified_eta"]=="7/40","strict_margin_positive":F(rows["strict"]["return_margin_lower"])>0,"boundary_eta_zero":rows["boundary"]["certified_eta"]=="0","failed_certificate_detected":not rows["failed"]["strict"]}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","formula":"eta=eta_hat*(1-epsilon_H)-epsilon_G","checks":checks,"cases":rows}
out=Path("research/aspect/results/relative_form_error_certificate.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
