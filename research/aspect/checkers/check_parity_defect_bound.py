"""Exact saturation audit for the parity-defect cross-pairing bound."""
from fractions import Fraction as F
from pathlib import Path
import json

def dot(a,b):return sum((a[i]*b[i] for i in range(len(a))),F(0))
def mv(a,v):return [sum((a[i][j]*v[j] for j in range(len(v))),F(0)) for i in range(len(a))]
U=[[F(1),0],[0,F(-1)]]
bp=[F(4),F(3)];bm=[F(5),F(12)]
dp=[mv(U,bp)[i]-bp[i] for i in range(2)]
dm=[mv(U,bm)[i]+bm[i] for i in range(2)]
# Norms are exact integers from Pythagorean data.
Bp=F(5);Bm=F(13);ep=F(6);em=F(10);goodp=F(4);goodm=F(12)
c=dot(bp,bm)
sharp=(goodp*em+ep*goodm)/2
coarse=(Bp*em+ep*Bm)/2
checks={"defects_match_spectral_components":dp==[0,F(-6)] and dm==[F(10),0],"cross_pairing_is_56":c==56,"sharp_bound_saturates":abs(c)==sharp,"coarse_bound_holds":abs(c)<=coarse,"exact_symmetry_limit_vanishes":(goodp*0+0*goodm)/2==0}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"cross_pairing":str(c),"sharp_bound":str(sharp),"coarse_bound":str(coarse),"conclusion":"the spectral parity-defect bound is sharp; quantitative confinement requires measured route norms and both parity defects"}
out=Path("research/aspect/results/parity_defect_bound.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
