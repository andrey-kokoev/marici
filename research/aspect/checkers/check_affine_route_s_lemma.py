"""Exact one-dimensional S-lemma certificate for an affine route ball."""
from fractions import Fraction as F
from pathlib import Path
import json

def psd2(a,b,c):return a>=0 and c>=0 and a*c-b*b>=0
q=F(1,2); r=F(1,4); rho2=F(9,16); lam=F(3,16)
a=rho2-q*q-lam; b=-q*r; c=lam-r*r
lower_rho2=F(1,2); lower_a=lower_rho2-q*q-lam
# Direct endpoint maximum for |w|<=1.
direct=max((q+r*w)**2 for w in (F(-1),F(1)))
checks={"sharp_block_psd":psd2(a,b,c),"sharp_block_determinant_zero":a*c-b*b==0,"direct_affine_maximum_matches":direct==rho2,"lower_target_fails_same_multiplier":not psd2(lower_a,b,c)}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"rho_squared":str(rho2),"multiplier":str(lam),"certificate_block":[[str(a),str(b)],[str(b),str(c)]],"conclusion":"one augmented positive-semidefinite block certifies the full affine route norm over a quadratic admissible set"}
out=Path("research/aspect/results/affine_route_s_lemma.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
