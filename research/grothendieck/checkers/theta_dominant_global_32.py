"""Manifest-level verifier for the exact global dominant residual theorem."""
from pathlib import Path
import json
R=Path("research/grothendieck/results")
def load(name):return json.loads((R/name).read_text())
corner=load("theta-dominant-corner-exact.json")
c1=load("theta-chart1-scaled-taylor-q-cover.json");c1r=load("theta-chart1-scaled-taylor-refine.json");t1=load("theta-chart1-scaled-tail.json")
c2=load("theta-chart2-scaled-taylor-q-cover.json");t2=load("theta-chart2-scaled-tail.json")
checks={"corner_above_32":corner["strictly_above_32"],
 "chart1_base_accepted":c1["accepted"]==484,
 "chart1_refinement_complete":c1r["refined_accepted"]==56 and c1r["unresolved"]==0,
 "chart1_tails_below_conservative_margins":t1["H_tail_below_margin"] and t1["J_tail_below_margin"],
 "chart2_cover_complete":c2["accepted"]==64,
 "chart2_tails_below_conservative_margins":t2["H_tail_below_margin"] and t2["J_tail_below_margin"]}
assert all(checks.values())
result={"theorem":"D(q,y)>32 on q in [3/10,1/2], y in [1/1000,1/28]","checks":checks,"verified":True}
out=json.dumps(result,indent=2)+"\n";(R/"theta-dominant-global-32.json").write_text(out);print(out,end="")
