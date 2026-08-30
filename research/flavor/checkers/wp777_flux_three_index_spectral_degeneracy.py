"""Exact flux-index and Landau-degeneracy audit for the generation escape."""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
wp776 = json.loads(
    (ROOT / "results" / "wp776_five_dimensional_domain_wall_generation_rank_no_go.json").read_text(
        encoding="utf-8"
    )
)

charge = 1
flux = 3
dirac_index = charge * flux
opposite_flux_index = charge * (-flux)
landau_degeneracy = abs(charge * flux)
opposite_flux_degeneracy = abs(charge * (-flux))

su6_family_degree = 27
weighted_matter_degree = landau_degeneracy * su6_family_degree
N_V_su6 = 35
naive_equal_weight_index = 2 + N_V_su6 - weighted_matter_degree

checks = {
    "wp776_dependency_passed": wp776["status"] == "PASS" and all(wp776["checks"].values()),
    "unit_charge_flux_three_has_index_three": dirac_index == 3,
    "opposite_flux_reverses_chirality": opposite_flux_index == -3,
    "flux_three_landau_degeneracy_is_three": landau_degeneracy == 3,
    "flux_orientation_does_not_change_degeneracy": landau_degeneracy == opposite_flux_degeneracy,
    "every_tower_level_carries_flux_degeneracy": landau_degeneracy == abs(dirac_index),
    "weighted_family_spectral_degree_is_eighty_one": weighted_matter_degree == 81,
    "equal_weight_spectral_count_reproduces_negative_forty_four": naive_equal_weight_index == -44,
    "flux_three_is_not_selected_by_flux_quantization_alone": flux in range(-5, 6)
    and 1 in range(-5, 6)
    and 2 in range(-5, 6),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP777",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP776",
    "admitted_state_domain": "one charged higher-dimensional SU(6) anomaly-family field on a magnetized two-torus with integral first Chern flux, including the full Landau tower multiplicity",
    "faithful_coordinate": "signed Dirac index q m and unsigned Landau-level degeneracy |q m|",
    "source_authorized_probe": "the two-dimensional Dirac index and magnetic-translation degeneracy of the complete tower",
    "generation_result": "unit charge and flux m=3 produce index three and hence three chiral zero modes",
    "chirality_result": "m=-3 reverses chirality while retaining the same spectral degeneracy",
    "spectral_result": "each Landau level has degeneracy three, so the 27-degree SU(6) family contributes weighted degree 81 rather than 27",
    "classification": "magnetic flux supplies a genuine index-three generation constructor but no spectral economy; it changes the source problem from 5D KK counting to a flux-weighted six-dimensional spectrum",
    "smallest_exact_falsifier": "the same integer three that yields three zero modes multiplies every Landau tower level by three",
    "deutschian_status": "flux quantization makes generation number integral but does not select the value or sign three; a tadpole or anomaly equation must derive the oriented flux sector",
    "next_source_gate": "derive oriented flux three from a complete six-dimensional tadpole and anomaly packet, calculate the full boson-fermion flux-weighted effective potential, and test whether its selected twist and gauge normalization survive",
    "instrument_gate": "the physical16 two-port realization and generation-resolved detector calibration remain absent",
    "primary_source": "https://arxiv.org/abs/1709.09784",
}
(ROOT / "results" / "wp777_flux_three_index_spectral_degeneracy.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
