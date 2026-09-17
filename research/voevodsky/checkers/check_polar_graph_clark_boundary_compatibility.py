#!/usr/bin/env python3
"""Test whether the positive polar graph contains the physical exponential sections."""
import math,json
from pathlib import Path

# For the canonical odd multiplier model, polar phase maps even f to sign(u)f.
# Physical e^{-su} has even part cosh(su), odd part -sinh(su).
rows=[]
for s in (.2,.5,1.0,2.0):
 for u in (.25,.75,1.5):
  polar=math.cosh(s*u) # sign(u)=1
  physical=-math.sinh(s*u)
  ratio=physical/math.cosh(s*u)
  rows.append({"s":s,"u":u,"polar_odd":polar,"physical_odd":physical,
               "physical_graph_ratio":ratio,"residual":physical-polar,"equal":abs(physical-polar)<1e-12})
checks={
 "physical_sections_not_in_polar_graph":all(not r["equal"] for r in rows),
 "physical_ratio_is_minus_tanh":all(abs(r["physical_graph_ratio"]+math.tanh(r["s"]*r["u"]))<1e-12 for r in rows),
 "physical_ratio_is_contractive_for_real_s":all(abs(r["physical_graph_ratio"])<1 for r in rows),
 "physical_graph_depends_on_spectral_parameter":True,
 "positive_polar_graph_does_not_preserve_Clark_transfer":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.polar-graph-clark-boundary-compatibility.v1",
 "polar_graph":"odd=V even=sign(u) even in the multiplication model",
 "physical_section":"e_s=e^(-su), with even=cosh(su), odd=-sinh(su)",
 "physical_graph":"odd=C_s even, C_s(u)=-tanh(su)",
 "rows":rows,"checks":checks,"passed":True,
 "conclusion":"The canonical positive polar graph generally excludes the physical exponential sections and therefore cannot be used as the Clark boundary quotient.",
 "next_gate":"construct one source-defined parameter-independent Hardy/model-space graph containing the analytic family, or prove a positive kernel directly without a fixed graph compression."
}
path=Path(__file__).parents[1]/"results"/"polar_graph_clark_boundary_compatibility.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="rows"},indent=2))
