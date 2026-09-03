"""Exact diagonal singular-value audit of block coercivity versus return margin."""
from fractions import Fraction as F
from pathlib import Path
import json

cases={"strict":[F(1,2),F(1,3)],"terminal":[F(1),F(1,3)]}
rows={}
for name,s in cases.items():
 eta=1-max(s); return_margin=1-max(x*x for x in s); determinant=(1-s[0]*s[0])*(1-s[1]*s[1]); lower=(eta*(2-eta))**2
 rows[name]={"eta":str(eta),"return_margin":str(return_margin),"determinant":str(determinant),"determinant_lower_bound":str(lower),"margin_identity":return_margin==2*eta-eta*eta,"determinant_bound":determinant>=lower}
checks={"strict_margin_identity":rows["strict"]["margin_identity"],"strict_determinant_bound":rows["strict"]["determinant_bound"],"terminal_block_has_zero_coercivity":rows["terminal"]["eta"]=="0","terminal_return_has_zero_margin":rows["terminal"]["return_margin"]=="0"}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"cases":rows,"conclusion":"normalized block coercivity eta is equivalent to return norm at most (1-eta)^2"}
out=Path("research/aspect/results/block_coercivity_return.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
