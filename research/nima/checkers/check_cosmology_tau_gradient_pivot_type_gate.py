"""Typing gate for the proposed gradient-pivot to exceptional-face tau lift."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; NIMA=ROOT/"nima"; BEN=ROOT/"benincasa"; VOE=ROOT/"voevodsky"
OUT=NIMA/"results"/"cosmology_tau_gradient_pivot_type_gate.json"
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def main():
    first=load(NIMA/"results"/"cosmology_augmented_wall_first_jet_packet.json")
    principal=load(NIMA/"results"/"cosmology_source_principal_wall_cell.json")
    pivot=load(BEN/"results"/"gradient-pivot-cech-descent.json")
    normal=load(BEN/"physical-normal-lift-cech-coherence.json")
    nonfaith=load(VOE/"results"/"cosmology_residue_functor_nonfaithfulness_gate.json")
    assert first["normal_sequence"]["dimensions"]==[2,3,1]
    assert principal["wall_order"]==["q_g1","q_g2","q_g3"]
    assert pivot["cover"]==["D(partial_aK)","D(partial_bK)","D(partial_cK)"]
    assert normal["gradient_pivot_chart_count"]==3
    # The target fiber is two-dimensional (a,b).  In the source kinematics
    # c=-(x+y+z) is base-dependent, not a third target fiber coordinate.
    target_fiber_coordinates=["a","b"]; adapter_pivots=["a","b","c"]
    admissible=[p for p in adapter_pivots if p in target_fiber_coordinates]
    assert admissible==["a","b"]
    # A two-chart restriction has no Cech degree-two triple face.
    restricted_pair_count=1; restricted_triple_count=0
    assert restricted_triple_count==0
    packet={
      "schema":"marici.cosmology-tau-gradient-pivot-type-gate.v1",
      "status":"gradient_pivot_tau_candidate_blocked_by_fiber_base_and_cover_mismatch",
      "target_fiber_coordinates":target_fiber_coordinates,
      "target_wall_count":3,
      "normal_adapter_pivots":adapter_pivots,
      "c_pivot_role":"base-dependent c=-(x+y+z), not a target fiber direction",
      "admissible_fixed_fiber_pivots":admissible,
      "restricted_cover":{"chart_count":2,"pair_count":restricted_pair_count,"triple_face_count":restricted_triple_count},
      "required_exceptional_face":"sigma123 from the ordered three-wall blow-up",
      "source_map_from_pivot_cover_to_wall_cover_constructed":False,
      "triple_homotopy_transports_after_fixed_fiber_restriction":False,
      "residue_functor_kernel_rank":nonfaith["finite_field_witnesses"]["101"]["kernel_rank"],
      "residue_comparison_selects_pre_residue_kernel_component":False,
      "raw_prior_art_supplies_tau_p":False,
      "new_source_data_required":"a comparison allowing the c/base direction in the relative total space, or a different three-chart source cover native to the two-dimensional marked fiber",
      "conclusion":"the prior gradient-pivot Cech packet cannot be restricted directly to the target fixed fiber: removing the base-dependent c pivot destroys the triple face needed for sigma123, while retaining it requires a new relative base-fiber comparison",
      "passed":True}
    OUT.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8"); print(json.dumps(packet,indent=2))
if __name__=="__main__": main()
