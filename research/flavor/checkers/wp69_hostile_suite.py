#!/usr/bin/env python3
"""WP69: exact hostile-pair and reference-port suite for surviving routes."""

from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp69_hostile_suite.json"
def load(n): return json.loads((ROOT/f"research/flavor/results/{n}.json").read_text())

def main():
 d={k:load(v) for k,v in {
  "projection":"wp52_source_selector_audit","rg":"wp61_full_rg_local_diffeomorphism",
  "boundary":"wp62_uv_boundary_normalization_gate","threshold":"wp63_threshold_schur_selector_gate",
  "spurion":"wp65_spurion_relation_descent","positive":"wp66_positive_channel_inventory",
  "probe":"wp67_experimental_probe_algebra","reference":"wp55_relational_reference_port"}.items()}
 tests={
  "H1_measured10_collision_repaired_only_by_quotient_complement":d["projection"]["gates"]["hostile_pair_collapsed_by_measured10_exactly"] and d["probe"]["gates"]["experimental_algebra_separates_measured10_hostile_pair"],
  "H2_chart_spurion_data_fail_same_orbit_descent":d["projection"]["gates"]["chart_probe_fails_full_weak_basis_descent"] and d["spurion"]["gates"]["same_scalar_spurion_relation_fails_after_q_rotation"],
  "H3_rg_preserves_partition_without_proper_image":d["rg"]["gates"]["flow_differential_is_invertible_at_zero_time"],
  "H4_threshold_kernel_does_not_force_proper_image":d["threshold"]["gates"]["noninjective_does_not_imply_proper_image"],
  "H5_boundary_selects_only_with_frozen_normalization":d["boundary"]["gates"]["frozen_boundary_selects_one_hostile_point"] and d["boundary"]["gates"]["ir_fitted_normalization_is_circular"],
  "H6_reference_repairs_descent_only_on_changed_groupoid":d["reference"]["gates"]["fixed_reference_readout_fails_original_quotient_descent"] and d["reference"]["gates"]["simultaneous_state_reference_action_restores_descent"],
  "H7_positive_proper_image_channels_fail_authority_or_data":all(d["positive"]["gates"].values()),
 }
 assert all(tests.values()),tests
 result={
  "schema":"marici.flavor.hostile-suite.v1","tests":tests,
  "survivor_dispositions":{
   "physical16_probe_algebra":"faithful separator/readout; not selector",
   "full_one_loop_rg":"descending local transport; not selector",
   "independent_uv_boundary":"mathematically sufficient selector template; absent from source",
   "threshold_schur_map":"noninjective but surjective; not selector",
   "positive_expectations":"proper mathematical images; unauthorized and data-failing",
   "reference_port":"new relational stabilizer-groupoid experiment",
   "chart_phase_and_scalar_spurion":"presentation rigidifiers failing descent"},
  "conclusion":"Every surviving route is typed without ambiguity under all hostile pairs; none becomes a genuine physical selector on the original quotient.",
 }
 OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"passed":sum(tests.values()),"total":len(tests),"output":str(OUT.relative_to(ROOT))}))
if __name__=="__main__": main()
