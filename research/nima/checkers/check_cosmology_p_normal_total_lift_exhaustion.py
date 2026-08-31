"""Current-source exhaustion gate for the p-normal total lift."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; NIMA=ROOT/"nima"; VOE=ROOT/"voevodsky"
OUT=NIMA/"results"/"cosmology_p_normal_total_lift_exhaustion.json"
def load(path): return json.loads(path.read_text(encoding="utf-8"))
def main():
    rel=load(NIMA/"results"/"cosmology_p_normal_relative_residue_cocycle.json")
    blocker=load(VOE/"results"/"cosmology_total_lift_blocker.json")
    universal=load(VOE/"results"/"cosmology_universal_total_lift_cell.json")
    D=rel["relative_differential"]; target=[1,1]
    assert [sum(row[j]*target[j] for j in range(2)) for row in D]==[0,0,0]
    assert blocker["incoming_generators_available_in_minimal_total_complex"]==[]
    assert universal["primitive_kernel_generator"]==target
    assert universal["universal_cell"]["differential"]=="d(tau_p)=Xi_log+minus_sigma123"
    for prime in (101,103):
        w=blocker["finite_field_witnesses"][str(prime)]
        assert (w["coefficient_rank"],w["augmented_rank_for_target_cocycle"],w["total_lift_exists"])==(0,1,False)
        u=universal["finite_field_witnesses"][str(prime)]
        assert (u["incoming_rank_before_tau"],u["incoming_rank_after_tau"])==(0,1)
    packet={
      "schema":"marici.cosmology-p-normal-total-lift-exhaustion.v1",
      "status":"current_source_total_lift_exhausted_universal_missing_cell_classified",
      "target_relative_cocycle":"Xi_log+minus_sigma123",
      "primitive_integral_kernel_generator":[1,1],
      "incoming_generators_current_source":[],
      "two_prime_total_lift_rank_pairs":{"101":[0,1],"103":[0,1]},
      "total_chain_level_lift_constructed":False,
      "universal_missing_cell":{"name":"tau_p","degree":1,"differential":"d(tau_p)=Xi_log+minus_sigma123","unit_coefficient_required":True,"source_derived":False},
      "abstract_tau_adjoined":False,
      "relative_bockstein_constructed":False,
      "physical_period_constructed":False,
      "currently_open_internal_route":False,
      "requires_new_source_data":True,
      "admissible_new_source_signatures":universal["admissible_next_source_tests"],
      "forbidden_shortcuts":universal["forbidden_shortcuts"],
      "conclusion":"the relative residue cocycle is constructed, but the current source complex has no incoming generator; tau_p classifies the missing unit cell and must not be invented",
      "passed":True}
    OUT.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8"); print(json.dumps(packet,indent=2))
if __name__=="__main__": main()
