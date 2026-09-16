#!/usr/bin/env python3
"""Check the polynomial exponent condition giving a uniform angular tail."""
import json
from pathlib import Path

# Representative integer growth parameters; the formula below is symbolic.
samples=[]
for a in range(5):
  for q in range(1,6):
    M=a+q//2+2
    exponent=2*a-2*M+q-1  # shell multiplicity times energy decay
    assert exponent < -1
    samples.append({"phase_growth_a":a,"shell_dimension_q":q,"schwartz_order_M":M,"shell_exponent":exponent})

out={
 "schema":"marici.voevodsky.angular-phase-energy-uniform-tail.v1",
 "energy_bound":"E_g(chi)<=C_B,M (1+|chi|)^(2a-2M), uniformly for g in bounded Schwartz packet B",
 "shell_growth":"#shell(n)<=C(1+n)^(q-1)",
 "summability_condition":"2M>2a+q",
 "tail_bound":"sum_|chi|>F E_g(chi) <= C'_B,M (1+F)^(2a-2M+q)",
 "samples":samples,
 "passed":True,
 "conclusion":"Angular/conductor removal is uniform on bounded Schwartz observer packets once M is chosen beyond the polynomial phase and shell-growth threshold.",
 "remaining_gate":"uniform outer-regulator removal for the exact recentered transported physical regulator and the placement cross term"
}
path=Path(__file__).parents[1]/"results"/"angular_phase_energy_uniform_tail.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!='samples'},indent=2))
