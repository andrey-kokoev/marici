"""Exact extreme-point audit for a convex admissible lift set."""
from fractions import Fraction as F
from pathlib import Path
import json

vertices=[(F(1),0),(F(-1),0),(0,F(2)),(0,F(-2))]
samples=[(0,0),(F(1,2),F(1)),(F(-1,4),F(3,2))]
def route(w):return F(1,5)*w[0]+F(1,10)*w[1]
def width(points):return max(abs(route(w)) for w in points)
vertex_width=width(vertices); sample_width=width(samples)
# Convex-combination witness: (1/2,1)=1/2(1,0)+1/2(0,2).
w=(F(1,2),F(1)); combo=(F(1,2)*vertices[0][0]+F(1,2)*vertices[2][0],F(1,2)*vertices[0][1]+F(1,2)*vertices[2][1])
checks={"extreme_width_exact":vertex_width==F(1,5),"interior_samples_do_not_exceed_extremes":sample_width<=vertex_width,"convex_combination_witness_exact":w==combo,"route_norm_is_convex_on_witness":abs(route(w))<=F(1,2)*abs(route(vertices[0]))+F(1,2)*abs(route(vertices[2]))}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"vertex_width":str(vertex_width),"sample_width":str(sample_width),"conclusion":"for a source-certified compact convex hull, omitted-route norm width is attained on its extreme lifts"}
out=Path("research/aspect/results/convex_lift_width.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
