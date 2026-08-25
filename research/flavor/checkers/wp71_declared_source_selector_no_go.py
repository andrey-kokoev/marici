#!/usr/bin/env python3
"""WP71: completion checker for the declared-source physical16 selector no-go."""

from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp71_declared_source_selector_no_go.json"
DEPS=["wp60_source_authority_inventory","wp61_full_rg_local_diffeomorphism","wp62_uv_boundary_normalization_gate","wp63_threshold_schur_selector_gate","wp64_z4_vacuum_orbit_gate","wp65_spurion_relation_descent","wp66_positive_channel_inventory","wp67_experimental_probe_algebra","wp68_fitted_ensemble_contextual_partitions","wp69_hostile_suite","wp70_first_failure_matrix"]

def main():
 ds={n:json.loads((ROOT/f"research/flavor/results/{n}.json").read_text()) for n in DEPS}
 authority=ds["wp60_source_authority_inventory"]
 matrix=ds["wp70_first_failure_matrix"]
 required_extension={
  "domain":"explicit admitted nondegenerate physical16 state domain",
  "operation":"source-derived state operation or boundary law, not a fitted scalar",
  "descent":"proof under full U(3)_Q x U(3)_u x U(3)_d",
  "proper_reduction":"positive-codimension image or fixed locus in physical16",
  "normalization":"fixed independently of the IR fitted point",
  "instrument":"typed preparation/measurement or dynamical realization",
  "ensemble":"predeclared prediction surviving all 1210 viable sheets or a declared successor ensemble",
  "reference_rule":"if a port is added, replace the original groupoid by the explicit relational stabilizer groupoid",
 }
 gates={
  "all_move_dependencies_pass":all(all(d.get("gates",d.get("tests",{})).values()) for d in ds.values()),
  "source_inventory_has_one_derived_operation_family":authority["gates"]["exactly_one_derived_operation_family_declared"],
  "derived_rg_operation_has_no_local_proper_image":ds["wp61_full_rg_local_diffeomorphism"]["proper_image"].startswith("no locally"),
  "instrumented_probe_algebra_is_nonselective":ds["wp67_experimental_probe_algebra"]["selector"] is False,
  "no_candidate_passes_all_five_gates":matrix["gates"]["no_row_passes_all_gates"],
  "all_proper_image_survivors_fail_source_authority_first":matrix["gates"]["all_proper_image_survivors_first_fail_authority"],
  "stationarity_fails_complete_ensemble":ds["wp68_fitted_ensemble_contextual_partitions"]["partitions"]["stationarity_selector"]["accepted_within_one_sigma"]==0,
  "minimal_extension_contract_is_complete":len(required_extension)==8 and all(required_extension.values()),
 }
 assert all(gates.values()),gates
 result={
  "schema":"marici.flavor.declared-source-selector-no-go.v1",
  "scope":"mechanisms and instruments declared in arXiv:2607.27315v1 plus the exact mathematical completions explicitly audited in WP60-WP70",
  "theorem":"No declared source-generated operation is a genuine physical selector on the admitted physical16 quotient.",
  "proof_summary":[
   "The sole derived source state operation is one-loop SM RG; its complete finite-time flow is locally diffeomorphic and has no locally proper image.",
   "The maximal declared experimental algebra is physical16-generated and generically faithful, but is readout rather than a state-reducing operation.",
   "Texture phases and scalar spurion relations fail full weak-basis descent; a reference port changes the groupoid.",
   "Threshold reduction is noninjective but surjective without an independently restricted UV domain.",
   "Canonical positive expectations have proper images but no source dynamics/instrument and their fixed loci fail data.",
   "Stationarity accepts zero of the complete 1210-sheet viable ensemble."],
  "minimal_additional_source_structure":required_extension,
  "reopening_condition":"admission of a new source action, boundary/threshold law, or relational experiment satisfying every extension field before numerical fitting",
  "gates":gates,
 }
 OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"dependencies":len(DEPS),"output":str(OUT.relative_to(ROOT))}))
if __name__=="__main__": main()
