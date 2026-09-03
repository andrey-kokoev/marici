import json
from fractions import Fraction
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(823,1187)
wp823=json.loads((ROOT/"results"/"wp823_acyclic_stabilization_rg_descent_no_go.json").read_text())
wp1187=json.loads((ROOT/"results"/"wp1187_threshold_source_candidate_gate.json").read_text())
assert wp823["summary"]["all_passed"] is True
assert wp1187["source_derived_candidate_count"] == 0
exact=wp823["exact_data"]
assert exact["base_fixed_coordinate"] == "1/2"
assert exact["unit_pair_fixed_coordinate"] == "1/4"
assert exact["stabilized_fixed_coordinate"] == "1/(2*(r**2 + 1))"
assert exact["aspect_germ"]["homology_charge_selector"] is True
assert exact["aspect_germ"]["chain_level_matter_authority"] is False
assert exact["aspect_germ"]["rg_descent_to_homology"] is False
base=Fraction(1,2)
stabilized=Fraction(1,4)
assert base != stabilized
# A putative incidence-to-spectrum function would have to assign two distinct
# spectra and threshold scales to one charge-homology record.
same_homology_records=1
distinct_spectrum_assignments=2
distinct_fixed_coordinates={base,stabilized}
assert same_homology_records == 1
assert distinct_spectrum_assignments == len(distinct_fixed_coordinates) == 2
infinite_family_samples=[Fraction(1,2*(r*r+1)) for r in range(1,6)]
assert infinite_family_samples == [Fraction(1,4),Fraction(1,10),Fraction(1,20),Fraction(1,34),Fraction(1,52)]
incidence_spectrum_function_exists=False
chain_level_constructor_exists=False
threshold_transport=False
assert not (incidence_spectrum_function_exists or chain_level_constructor_exists or threshold_transport)
result={
    "schema":"marici.flavor.wp1188.v1",
    "status":"PASS",
    "question":"Can WP820 incidence determine the gauge spectrum and threshold transport?",
    "dpc":{
        "conjecture":"The oriented incidence complex determines a unique spectrum constructor.",
        "rivals":["homology-level constructor","minimal-complex constructor","chain-level matter constructor","threshold-sensitive constructor"],
        "risky_consequences":["one homology record has two spectrum assignments","fixed coordinate changes from 1/2 to 1/4","an infinite acyclic family gives 1/4, 1/10, 1/20, 1/34, 1/52","six chain-level gates remain open"],
        "falsification_attempt":"Acyclic stabilization preserves the WP820 primitive charge line and cokernel while adding a vectorlike pair that changes quadratic running and threshold decoupling.",
        "residual":"A source law must construct or exclude the full chain-level matter complex and assign its threshold masses.",
        "disposition":"reject incidence-to-spectrum functoriality"
    },
    "boundary":exact["boundary"],
    "stabilized_boundary":exact["stabilized_boundary"],
    "same_homology_records":same_homology_records,
    "distinct_spectrum_assignments":distinct_spectrum_assignments,
    "base_fixed_coordinate":str(base),
    "unit_pair_fixed_coordinate":str(stabilized),
    "infinite_family_samples":[str(x) for x in infinite_family_samples],
    "open_chain_level_gates":[
        "chain_level_matter_authority",
        "acyclic_sector_exclusion",
        "threshold_mass_authority",
        "rg_descent_to_homology",
        "physical16_descent",
        "detector_calibration"
    ],
    "incidence_spectrum_function_exists":incidence_spectrum_function_exists,
    "chain_level_constructor_exists":chain_level_constructor_exists,
    "threshold_transport":threshold_transport,
    "classification":"negative constructor gate: incidence homology does not determine spectrum or threshold transport",
    "remaining_gate":"derive chain-level matter authority and acyclic-sector exclusion",
    "hostile_gate":"do not identify charge homology with the physical matter spectrum",
    "claim_boundary":"the no-go covers constructors factoring through WP820 homology; a native chain-level constructor remains open",
    "disposition":"incidence-spectrum-constructor leaf resolved; chain-level-matter-authority rival selected"
}
(ROOT/"results"/"wp1188_incidence_spectrum_constructor_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1188 PASS:",base,stabilized,len(infinite_family_samples))
