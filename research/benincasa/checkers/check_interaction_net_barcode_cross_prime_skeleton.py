#!/usr/bin/env python3
"""Compare exact barcode exports at two good primes before rational reconstruction."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
R=ROOT/"research"/"benincasa"/"results"
a=json.loads((R/"interaction-net-barcode-basis-export-p32003.json").read_text())
b=json.loads((R/"interaction-net-barcode-basis-export-p32009.json").read_text())
def supports(rows):return [x["indices"] for x in rows]
def adapted(p):
 q=p["adapted_depth3_quotient_basis"]
 return {k:supports(q[k]) for k in ("first_death_rows","second_death_rows","through_depth6_rows")}
def transitions(p):return {k:supports(v["rows"]) for k,v in p["transition_matrices"].items()}
def duals(p):return {k:supports(v) for k,v in p["dual_pairing_matrices"].items()}
def charts(p):return {k:supports(v["rows"]) for k,v in p["chart_transports"].items()}
checks={
 "distinct_primes":a["prime"]==32003 and b["prime"]==32009,
 "source_label_order_depth3_equal":a["source_label_order_depth3"]==b["source_label_order_depth3"],
 "source_label_order_depth4_equal":a["source_label_order_depth4"]==b["source_label_order_depth4"],
 "adapted_supports_equal":adapted(a)==adapted(b),
 "emergence_supports_equal":supports(a["depth4_emergence_complement_rows"])==supports(b["depth4_emergence_complement_rows"]),
 "transition_supports_equal":transitions(a)==transitions(b),
 "dual_supports_equal":duals(a)==duals(b),
 "chart_transport_supports_equal":charts(a)==charts(b),
 "embedded_checks_equal":a["checks"]==b["checks"],
}
out={"schema":"marici.interaction-net-barcode-cross-prime-skeleton.v1",
 "primes":[32003,32009],"checks":checks,"passed":all(checks.values()),
 "conclusion":"the_complete_labelled_support_skeleton_is_stable_across_two_good_primes" if all(checks.values()) else "support_skeleton_prime_dependence_detected"}
path=R/"interaction-net-barcode-cross-prime-skeleton-p32003-p32009.json"
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
if not out["passed"]:raise SystemExit(1)
