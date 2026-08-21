"""Exact finite causal-cone test for the future-probe speed conjecture."""
import json
from pathlib import Path

n=11
source=5
max_depth=5

# Dependency support of a local nearest-neighbor circuit/message rule.
supports=[{source}]
for _ in range(max_depth):
    prev=supports[-1]
    nxt=set(prev)
    for i in prev:
        if i>0:nxt.add(i-1)
        if i+1<n:nxt.add(i+1)
    supports.append(nxt)

local_checks=[]
for depth,supp in enumerate(supports):
    cone={j for j in range(n) if abs(j-source)<=depth}
    local_checks.append({
      "depth":depth,
      "support":sorted(supp),
      "causal_cone":sorted(cone),
      "within_bound":supp<=cone,
      "cone_saturated":supp==cone,
    })
assert all(x["within_bound"] and x["cone_saturated"] for x in local_checks)

# One admitted nonlocal interaction makes a distant probe distinguish the
# source in a single step, defeating every unit-speed spatial bound.
nonlocal_support={source,0}
nonlocal_violation=0 in nonlocal_support and abs(0-source)>1
assert nonlocal_violation

result={
 "schema":"marici.future-probe-causal-speed-gate.v1",
 "local_model":{
   "sites":n,"source_site":source,"max_depth":max_depth,
   "rule":"one nearest-neighbor composition layer expands distinguishability support by at most one edge",
   "checks":local_checks,
 },
 "hostile_control":{
   "rule":"admit one all-to-all source-to-site-0 interaction at depth one",
   "support":sorted(nonlocal_support),
   "violates_unit_speed_bound":nonlocal_violation,
 },
 "verdict":(
   "Future probing operationally defines where a perturbation is distinguishable. "
   "A finite propagation bound follows in the bounded model only after local "
   "composition is imposed; future probing alone permits instantaneous nonlocal support."
 )
}
out=Path(__file__).parents[1]/"results"/"future_probe_causal_speed_gate.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
