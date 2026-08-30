"""Exact anomaly-descent, tadpole-selection, and flux-stability audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
wp777 = json.loads(
    (ROOT / "results" / "wp777_flux_three_index_spectral_degeneracy.json").read_text(
        encoding="utf-8"
    )
)

m, anomaly_6d, tadpole_c, localized_charge = sp.symbols(
    "m anomaly_6d tadpole_c localized_charge", integer=True
)

# Integrating one internal flux insertion in a local 6D anomaly polynomial is
# linear in the first Chern number.  Parent cancellation therefore leaves the
# whole integer flux lattice in the kernel.
descended_anomaly = sp.expand(m * anomaly_6d)
cancelled_descents = [descended_anomaly.subs({anomaly_6d: 0, m: value}) for value in range(-5, 6)]

# The smallest integrated Bianchi/tadpole equation that could select a flux.
tadpole_solution = sp.solve(sp.Eq(tadpole_c * m + localized_charge, 0), m)[0]
selected_three_charge = sp.solve(
    sp.Eq(tadpole_solution, 3), localized_charge
)[0]
source_free_flux = tadpole_solution.subs({localized_charge: 0, tadpole_c: 1})

# A charged vector in a constant internal magnetic field has a gyromagnetic
# shift.  The aligned lowest Landau state is tachyonic.
abs_qB = sp.symbols("abs_qB", positive=True)
landau_level = 0
vector_spin_shift = -2
lowest_vector_mass_sq = sp.expand((2 * landau_level + 1 + vector_spin_shift) * abs_qB)
external_u1_su6_vector_charge = 0
external_u1_vector_mass_sq = external_u1_su6_vector_charge * abs_qB

# A parity-even flux energy cannot orient the sector.
alpha = sp.symbols("alpha", positive=True)
even_flux_energy = alpha * m**2

checks = {
    "wp777_dependency_passed": wp777["status"] == "PASS" and all(wp777["checks"].values()),
    "anomaly_descent_is_linear_in_flux": sp.diff(descended_anomaly, m) == anomaly_6d,
    "parent_anomaly_cancellation_leaves_all_tested_fluxes": all(value == 0 for value in cancelled_descents),
    "bare_tadpole_selects_zero_not_three": source_free_flux == 0,
    "selecting_plus_three_requires_localized_charge_minus_three_c": selected_three_charge == -3 * tadpole_c,
    "tadpole_orientation_is_carried_by_source_charge": tadpole_solution.subs(localized_charge, -localized_charge) == -tadpole_solution,
    "internal_nonabelian_vector_flux_has_tachyonic_lowest_mode": lowest_vector_mass_sq == -abs_qB,
    "external_u1_leaves_su6_vectors_neutral": external_u1_vector_mass_sq == 0,
    "even_flux_energy_cannot_select_orientation": even_flux_energy.subs(m, 3) == even_flux_energy.subs(m, -3),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP778",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP777",
    "admitted_state_domain": "integer magnetic-flux sectors on a two-torus, a local six-dimensional anomaly-polynomial coefficient, the minimal integrated linear tadpole equation, and the charged-vector lowest Landau mode",
    "faithful_coordinate": "signed flux integer m together with the parent anomaly coefficient, localized tadpole charge, and lowest charged-vector mass squared",
    "source_authorized_probe": "anomaly-polynomial descent, integrated Bianchi/tadpole balance, and the full charged-vector quadratic spectrum",
    "contextual_partition": "parent anomaly cancellation identifies every integer m; an independently fixed nonzero localized tadpole charge can refine this to one signed flux; an even flux energy identifies m with -m",
    "anomaly_result": "local anomaly cancellation is homogeneous in m and therefore cannot select magnitude three or its orientation",
    "tadpole_result": "the minimal equation c m + Q_loc = 0 selects m=3 only when Q_loc=-3c; unless that charge is independently compulsory, the generation number has merely moved into source data",
    "stability_result": "a Cartan flux carried by the non-Abelian SU(6) gauge field has a tachyonic charged-vector lowest Landau mode and hence no admitted stable basin without an additional stabilization constructor",
    "escape_window": "place the index-generating flux in a distinct U(1) under which SU(6) vectors are neutral, then derive its charge embedding, oriented localized tadpole Q_loc=-3c, stabilization, and normalization independently",
    "classification": "anomaly cancellation is neither selector nor rigidifier of the flux integer; a sourced tadpole could be a selector, while the current internal SU(6) flux fails the stability gate",
    "smallest_exact_falsifier": "with the parent anomaly coefficient set to zero, both m=1 and m=3 have identical zero descended anomaly; moreover the internal charged-vector n=0 mode has mass squared -|qB|",
    "deutschian_status": "oriented flux three is not explained until the localized charge ratio -Q_loc/c=3 and its sign are consequences of a complete source theory rather than inputs",
    "next_source_gate": "construct the smallest anomaly-free external-U(1) charge and localized-source packet whose integrated Bianchi identity uniquely forces m=3 and whose complete scalar-vector spectrum has no tachyon",
    "instrument_gate": "no normalized physical16 detector map for the flux-selected generation channels has yet been derived",
    "primary_sources": [
        "https://arxiv.org/abs/1907.00536",
        "https://arxiv.org/abs/2306.00644"
    ],
}
(ROOT / "results" / "wp778_flux_anomaly_tadpole_stability_gate.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
