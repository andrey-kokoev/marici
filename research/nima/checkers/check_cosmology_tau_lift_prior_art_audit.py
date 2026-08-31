"""Audit prior constructions for a source-derived lift of the universal tau_p cell."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; NIMA=ROOT/"nima"; BEN=ROOT/"benincasa"; VOE=ROOT/"voevodsky"
OUT=NIMA/"results"/"cosmology_tau_lift_prior_art_audit.json"
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def main():
    normal=load(BEN/"physical-normal-lift-cech-coherence.json")
    pivot=load(BEN/"results"/"gradient-pivot-cech-descent.json")
    second=load(BEN/"results"/"second-covariant-cech-homotopy.json")
    raw=load(BEN/"results"/"raw_rees_adapter_no_go.json")
    exceptional=load(VOE/"results"/"cosmology_blowup_exceptional_cell_gate.json")
    monic=load(VOE/"results"/"cosmology_residue_monic_comparison.json")
    total=load(NIMA/"results"/"cosmology_p_normal_total_lift_exhaustion.json")
    assert normal["status"]=="passed" and normal["triple_cocycle_checks"]==3
    assert pivot["status"]=="pass" and pivot["cech_intersections"]["2"]
    assert second["status"]=="pass" and second["checks"]["all_triple_boundaries"]
    assert exceptional["exceptional_cell_column_rows_Xi_minusSigma"]==[0,1]
    assert exceptional["required_tau_column_rows_Xi_minusSigma"]==[1,1]
    assert monic["residue_sum"]==[0,0,0]
    assert raw["checks"]["coefficient_is_not_rees_gauge_invariant"]
    packet={
      "schema":"marici.cosmology-tau-lift-prior-art-audit.v1",
      "status":"internal_comparison_test_reopened_no_tau_lift_constructed",
      "universal_target":"tau_p with differential column (1,1) in (Xi_log,-sigma123)",
      "sourced_exceptional_face_leg":{"column":[0,1],"constructed":True},
      "residue_level_Xi_comparison":{"unique_after_orientation":True,"pre_residue_lift_constructed":False},
      "best_existing_bulk_candidate":{
        "source":"physical normal-lift gradient-pivot Cech class",
        "mechanism":"Cartan primitives i_W(omega) on pair overlaps plus second Cech triple homotopy",
        "three_chart_cover":True,"pairwise_exactness":True,"triple_homotopy":True,
        "target_wall_cover_comparison_constructed":False},
      "candidate_constructor":"mapping cone of the source gradient-pivot normal-adapter Cech complex restricted to the ordered blow-up exceptional wall face",
      "required_gates":[
        "construct a source map from gradient-pivot charts to ordered wall/blow-up charts",
        "strict-transform the Cartan overlap primitives to the exceptional face",
        "verify the cone cell has integral differential column (1,1)",
        "verify invariance under admitted Rees shears",
        "rerun full total d^2 and two-prime nonboundary test"],
      "hostiles":[
        "pure Cartan contraction in the ordinary Laurent carrier has zero double residue and cannot supply Xi_log",
        "the exceptional face alone has column (0,1)",
        "a raw Rees coefficient is continuously variable under admitted shears",
        "a nonunit multiple of tau_p does not kill the primitive integral class"],
      "currently_open_internal_test":True,
      "new_external_source_authority_required_for_test":False,
      "tau_p_source_map_constructed":False,
      "relative_bockstein_constructed":False,
      "physical_period_constructed":False,
      "conclusion":"prior work suggests one bounded internal comparison test: cone the existing source normal-adapter Cech class against the sourced exceptional face; none of the prior constructions alone supplies tau_p",
      "passed":True}
    OUT.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8"); print(json.dumps(packet,indent=2))
if __name__=="__main__": main()
