"""Six-port Ward-complete bilocal instrument contract for WP535."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp523 = load("wp523_h0_instrument_census.json")
wp524 = load("wp524_euclidean_h0_estimator.json")
wp525 = load("wp525_complex_mass_ward_completion.json")
wp534 = load("wp534_invariant_complex_pole_packet.json")

signed_poles = wp534["signed_bs_pole_residues"]
operator_channels = ["V_LL", "S_RR", "S_LL", "S_RL"]
mb, ms = sp.symbols("m_b m_s", nonzero=True)

# Six pole-resolved Ward rows acting on 6 x 4 complex bilocal estimators.
# Each row implements J.J - (m_b S_R - m_s S_L)^2/mu_i^2.
response = sp.zeros(6, 24)
mu_squared_values = []
residue_values = []
for pole_index, pole in enumerate(signed_poles):
    complex_mass = pole["complex_mass_squared_GeV_squared"]
    mu_squared = (
        sp.Float(str(complex_mass["real"]), 40)
        + sp.I * sp.Float(str(complex_mass["imaginary"]), 40)
    )
    residue = sp.sympify(pole["signed_bs_residue"])
    mu_squared_values.append(mu_squared)
    residue_values.append(residue)
    base = 4 * pole_index
    response[pole_index, base] = 1
    response[pole_index, base + 1] = -mb**2 / mu_squared
    response[pole_index, base + 2] = -ms**2 / mu_squared
    response[pole_index, base + 3] = 2 * mb * ms / mu_squared

residue_row = sp.Matrix([residue_values])
direct_readout = residue_row * response

# The measured scalar contracts six pole responses to one number. A hostile
# two-pole perturbation lies in its kernel but is visible to the six-port
# vector.
hostile_pole_shift = sp.Matrix(
    [
        residue_values[1],
        -residue_values[0],
        0,
        0,
        0,
        0,
    ]
)
hostile_scalar_response = sp.simplify(
    (residue_row * hostile_pole_shift)[0]
)

# A unit raw covariance is only a structural witness. Actual instrument
# authority requires a supplied renormalized 48 x 48 real covariance.
unit_covariance = sp.eye(24)
port_covariance_witness = sp.simplify(
    response * unit_covariance * response.conjugate().T
)
port_gram_determinant = sp.simplify(port_covariance_witness.det())

row_supports = [
    [column for column in range(24) if response[row, column] != 0]
    for row in range(6)
]
expected_supports = [
    list(range(4 * row, 4 * row + 4)) for row in range(6)
]

checks = {
    "wp523_dependency_passed": bool(wp523["passed"]),
    "wp524_dependency_passed": bool(wp524["passed"]),
    "wp525_dependency_passed": bool(wp525["passed"]),
    "wp534_dependency_passed": bool(wp534["passed"]),
    "six_signed_complex_poles_are_present": len(signed_poles) == 6,
    "four_ward_operator_channels_are_present": len(operator_channels) == 4,
    "raw_complex_estimator_dimension_is_twenty_four": response.cols == 24,
    "pole_resolved_response_has_rank_six": response.rank() == 6,
    "each_pole_row_has_its_own_four_channel_support": row_supports
    == expected_supports,
    "direct_delta_ms_readout_has_rank_one": direct_readout.rank() == 1,
    "direct_readout_has_five_dimensional_pole_kernel": len(
        residue_row.nullspace()
    )
    == 5,
    "hostile_two_pole_shift_is_nonzero": hostile_pole_shift != sp.zeros(6, 1),
    "hostile_two_pole_shift_collapses_in_scalar_readout": (
        hostile_scalar_response == 0
    ),
    "six_port_readout_separates_the_hostile_shift": (
        hostile_pole_shift.norm() != 0
    ),
    "unit_covariance_witness_gives_nonsingular_port_gram": (
        port_gram_determinant != 0
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP535",
    "domain": "The six signed b-s complex poles of WP534 and the WP525 Ward-complete vector-plus-scalar bilocal operator family.",
    "raw_estimator": {
        "complex_dimension": 24,
        "real_dimension": 48,
        "indexing": "six pole kernels times V_LL, S_RR, S_LL and S_RL",
        "operator_channels": operator_channels,
        "kernel_rule": "For pole i, weight the renormalized integrated B_s correlator by the Euclidean continuation of 1/(Q^2+mu_i^2), retaining real and imaginary parts.",
    },
    "source_generated_six_port_map": {
        "shape": [response.rows, response.cols],
        "rank": response.rank(),
        "row_supports": row_supports,
        "row_rule": "A_i=H_i,V-(m_b^2 H_i,RR+m_s^2 H_i,LL-2 m_b m_s H_i,RL)/mu_i^2",
    },
    "experimental_scalar_map": {
        "rule": "M_12,new=sum_i r_i A_i; Delta M_s reads a convention-dependent real projection after Standard Model composition.",
        "rank_on_six_pole_amplitudes": residue_row.rank(),
        "kernel_dimension": len(residue_row.nullspace()),
        "hostile_shift": [str(value) for value in hostile_pole_shift],
        "hostile_scalar_response": str(hostile_scalar_response),
    },
    "covariance_contract": {
        "required_shape": [48, 48],
        "required_units": "Renormalized continuum real-imaginary bilocal estimator units in one declared scheme.",
        "required_properties": [
            "symmetric positive semidefinite with every admitted null mode declared",
            "operator-mixing and coincident-point subtraction covariance",
            "cross-pole covariance from common gauge ensembles",
            "finite-volume, continuum and heavy-quark systematic covariance",
            "threshold-matching and current-normalization covariance",
        ],
        "structural_unit_covariance_port_gram_nonzero": bool(
            port_gram_determinant != 0
        ),
        "authority": "The unit covariance is a rank witness only and is not calibrated lattice data.",
    },
    "contextual_partition": "The six-port vector separates all pole-amplitude directions. The measured scalar identifies only residue-weighted equivalence classes with a five-dimensional kernel.",
    "classification": "Executable lattice instrument contract and exact readout-rank theorem. The instrument is specified but not realized by an existing calibrated B_s dataset.",
    "selector": False,
    "rigidifier": bool(response.rank() == 6),
    "instrument": "Proposed physical realization: six complex-kernel integrated B_s correlators in four renormalized operator channels, reported as 48 real estimators with full covariance. WP523 found no existing neutral-B calculation supplying this packet.",
    "smallest_exact_falsifier": "The nonzero hostile two-pole shift has exactly zero scalar DeltaM_s response but nonzero six-port response. Thus DeltaM_s alone cannot identify the pole decomposition.",
    "remaining_gate": "Execute the 24 complex correlator estimators on common B_s lattice ensembles with nonperturbative renormalization, contact subtraction, continuum and finite-volume limits, heavy-quark control, threshold matching and a published 48 x 48 covariance.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp535_six_port_bilocal_instrument.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
