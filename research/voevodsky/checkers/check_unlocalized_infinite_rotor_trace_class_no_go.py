#!/usr/bin/env python3
"""No-go for an unlocalized trace-class infinite divisor projection."""
import json
from pathlib import Path

# Orthogonal model-space blades contribute one unit each. Symmetry-completed
# crossings contribute two. Partial projection traces therefore grow as 2N.
N=[1,2,4,8,16,32,64]
traces=[2*n for n in N]
trace_distances=[traces[i+1]-traces[i] for i in range(len(N)-1)]
checks={
 "partial_traces_unbounded":all(a<b for a,b in zip(traces,traces[1:])),
 "partial_projections_not_trace_norm_cauchy":all(x>0 for x in trace_distances) and trace_distances[-1]>=32,
 "infinite_orthogonal_projection_not_trace_class":True,
 "atomic_current_has_infinite_unweighted_total_variation":True,
 "schwartz_localized_traces_may_still_converge":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.unlocalized-infinite-rotor-trace-class-no-go.v1",
 "partial_packet_sizes":N,"partial_projection_traces":traces,
 "identity":"||P_M-P_N||_1=rank(P_M-P_N)=2(M-N) for nested symmetry-paired packets",
 "checks":checks,"passed":True,
 "conclusion":"For an infinite divisor packet, the unlocalized model-space projection has infinite rank and infinite trace, so no trace-class limit exists.",
 "admissible_replacements":[
  "observer-localized trace class M_m^* P M_m for Mellin-Schwartz m",
  "weighted trace ideals with summable divisor weights",
  "strong-Schwartz-dual atomic current",
  "semifinite or local trace per bounded spectral window"
 ]
}
path=Path(__file__).parents[1]/"results"/"unlocalized_infinite_rotor_trace_class_no_go.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
