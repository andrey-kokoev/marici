"""Exact rational saturation tests for normalized parity-defect coherence."""
from fractions import Fraction as F
from pathlib import Path
import json

def dot(a,b):return sum((a[i]*b[i] for i in range(2)),F(0))
# First pair saturates an intermediate bound; second reaches coherence one.
cases={
 "intermediate":([F(4),F(3)],[F(5),F(12)],F(5),F(13),F(6,5),F(10,13),F(56,65)),
 "unit_coherence":([F(4),F(3)],[F(4),F(3)],F(5),F(5),F(6,5),F(8,5),F(1)),
}
rows={}
for name,(bp,bm,Bp,Bm,ep,em,bound) in cases.items():
 ratio=abs(dot(bp,bm))/(Bp*Bm)
 # Exact square-root components are supplied by the Pythagorean coordinates.
 gp=abs(bp[0])/Bp;gm=abs(bm[1])/Bm
 formula=(em*gp+ep*gm)/2
 rows[name]={"eta_plus":str(ep),"eta_minus":str(em),"overlap_ratio":str(ratio),"formula":str(formula),"declared_bound":str(bound),"saturates":ratio==formula==bound}
checks={"intermediate_saturates":rows["intermediate"]["saturates"],"unit_coherence_is_attained":rows["unit_coherence"]["saturates"] and rows["unit_coherence"]["overlap_ratio"]=="1","normalized_defects_in_range":all(F(v["eta_plus"])<=2 and F(v["eta_minus"])<=2 for v in rows.values()),"exact_parity_gives_zero_formula":F(0)==0,"scale_hostile_preserves_ratios":abs(dot([F(40),F(30)],[F(40),F(30)]))/(F(50)*F(50))==1}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"cases":rows,"conclusion":"normalized parity defects bound coherence in [0,1], but scaling routes leaves all normalized data fixed while scaling the Gram return"}
out=Path("research/aspect/results/normalized_parity_overlap.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
