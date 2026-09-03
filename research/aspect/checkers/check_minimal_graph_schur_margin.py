"""Exact scalar-mode audit of the minimal arithmetic-analytic graph block."""
from fractions import Fraction as F
from pathlib import Path
import json

samples=[F(1),F(1,2),F(1,5),F(1,29)]
rows=[]
for s in samples:
    full=[[1+s*s,-s],[-s,F(1)]]
    residual=[[s*s,-s],[-s,F(1)]]
    det_full=full[0][0]*full[1][1]-full[0][1]*full[1][0]
    det_res=residual[0][0]*residual[1][1]-residual[0][1]*residual[1][0]
    schur_v=full[0][0]-full[0][1]*full[1][0]/full[1][1]
    schur_h=full[1][1]-full[1][0]*full[0][1]/full[0][0]
    graph=[F(1),s]
    residual_on_graph=sum(graph[i]*sum(residual[i][j]*graph[j] for j in range(2)) for i in range(2))
    rows.append({"s":str(s),"det_full":str(det_full),"det_without_identity":str(det_res),"schur_after_analytic":str(schur_v),"schur_after_arithmetic":str(schur_h),"residual_on_graph":str(residual_on_graph)})
checks={
 "full_determinant_is_tautological_unit":all(r["det_full"]=="1" for r in rows),
 "identity_schur_is_one":all(r["schur_after_analytic"]=="1" for r in rows),
 "identity_removed_block_is_singular":all(r["det_without_identity"]=="0" for r in rows),
 "matching_residual_vanishes_on_graph":all(r["residual_on_graph"]=="0" for r in rows),
}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"rows":rows,"conclusion":"the minimal graph has a uniform margin only through the arithmetic identity; after removing it, graph directions are exact nulls"}
out=Path("research/aspect/results/minimal_graph_schur_margin.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["status"]=="pass" else 1)
