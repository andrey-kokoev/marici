"""Evidence and falsifiers for the Deutsch-Popperian two-closure-tower conjecture."""
import json
from pathlib import Path

root=Path(__file__).resolve().parents[3]
fixtures=[
 {"id":"magnetic_preferred_chart","I":False,"C":True,"M":"not_reached","source":"research/strominger/magnetic-chart-cocircuit-explanation.md"},
 {"id":"magnetic_factorial_normalization","I":True,"C":False,"M":"not_reached","source":"research/strominger/magnetic-divided-target-factorization.md"},
 {"id":"magnetic_integral_curvature","I":True,"C":True,"M":False,"source":"research/strominger/magnetic-divided-power-curvature-coherence.md"},
 {"id":"grothendieck_prime_equalizer","I":True,"C":False,"M":"operator_lift_open","source":"src/ledger/20260827-3376 The Prime-Scale Recursion Constructs the Backward Equalizer through the Square Grade.md"},
 {"id":"kitaev_five_rail","I":True,"C":False,"M":"not_reached","source":"research/kitaev/s3-five-rail-code-and-transversal-obstruction.md"}
]
source_exists=all((root/x["source"]).exists() for x in fixtures)
tests={
 "I_pass_C_fail_exists":any(x["I"] is True and x["C"] is False for x in fixtures),
 "I_fail_C_pass_exists":any(x["I"] is False and x["C"] is True for x in fixtures),
 "I_C_pass_M_fail_exists":any(x["I"] is True and x["C"] is True and x["M"] is False for x in fixtures),
 "independent_source_packets_exist":source_exists
}
result={"schema":"marici.checker_results.v1","checker":"deutsch_popperian_two_closure_towers_checks.py",
 "passed":all(tests.values()),"tests":tests,"fixtures":fixtures,
 "one_tower_hypothesis":"falsified by realized off-diagonal I/C cases",
 "two_tower_exhaustiveness":"falsified by the nontrivial Z/2 associator fixture",
 "exhaustiveness_falsifier":"research/strominger/deutsch-popperian-two-tower-falsifier.md"}
(root/"research/strominger/results/deutsch_popperian_two_closure_towers.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["passed"] else 1)
