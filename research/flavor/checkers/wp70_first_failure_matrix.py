#!/usr/bin/env python3
"""WP70: exact first-failed-gate and ensemble-survival matrix."""

from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp70_first_failure_matrix.json"

def main():
 rows={
  "measured10_projection":{"D":True,"P":False,"A":True,"I":True,"E":True,"first":"P"},
  "physical16_probe_algebra":{"D":True,"P":False,"A":True,"I":True,"E":True,"first":"P"},
  "full_one_loop_rg":{"D":True,"P":False,"A":True,"I":False,"E":True,"first":"P"},
  "threshold_schur_reduction":{"D":True,"P":False,"A":False,"I":False,"E":True,"first":"P"},
  "generation_exchange_deck_probe":{"D":False,"P":False,"A":True,"I":False,"E":True,"first":"D"},
  "z4_vacuum_picture":{"D":False,"P":False,"A":False,"I":False,"E":False,"first":"D"},
  "z8_scalar_spurion_relation":{"D":False,"P":False,"A":False,"I":False,"E":False,"first":"D"},
  "fixed_reference_port":{"D":False,"P":False,"A":False,"I":False,"E":True,"first":"D"},
  "spectral_pinching":{"D":True,"P":True,"A":False,"I":False,"E":False,"first":"A"},
  "center_expectation":{"D":True,"P":True,"A":False,"I":False,"E":False,"first":"A"},
  "purity_stationarity":{"D":True,"P":True,"A":False,"I":True,"E":False,"first":"A"},
  "independent_uv_boundary_template":{"D":True,"P":True,"A":False,"I":False,"E":False,"first":"A"},
 }
 order=list("DPAIE")
 first_ok=all(next(g for g in order if not r[g])==r["first"] for r in rows.values())
 ensemble=json.loads((ROOT/"research/flavor/results/wp68_fitted_ensemble_contextual_partitions.json").read_text())
 hostile=json.loads((ROOT/"research/flavor/results/wp69_hostile_suite.json").read_text())
 gates={
  "all_rows_have_exact_first_failure":first_ok,
  "no_row_passes_all_gates":not any(all(r[g] for g in order) for r in rows.values()),
  "all_proper_image_survivors_first_fail_authority":all(r["first"]=="A" for r in rows.values() if r["D"] and r["P"]),
  "stationarity_ensemble_failure_is_complete":ensemble["partitions"]["stationarity_selector"]["accepted_within_one_sigma"]==0,
  "hostile_suite_dependencies_pass":all(hostile["tests"].values()),
 }
 assert all(gates.values()),gates
 counts={g:sum(r["first"]==g for r in rows.values()) for g in order}
 result={"schema":"marici.flavor.first-failure-matrix.v1","gate_order":order,"gate_definitions":{"D":"original quotient descent","P":"proper physical16 reduction","A":"independent source authority","I":"typed physical implementation","E":"complete-ensemble survival"},"candidates":rows,"first_failure_counts":counts,"progressive":[],"gates":gates,"conclusion":"Every proper-image survivor first fails independent source authority; every source-authorized descending route fails proper reduction."}
 OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"candidates":len(rows),"first_failures":counts,"output":str(OUT.relative_to(ROOT))}))
if __name__=="__main__": main()
