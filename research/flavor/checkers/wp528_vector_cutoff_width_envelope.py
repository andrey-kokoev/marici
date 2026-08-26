"""Conservative width envelope for WP516's unresolved vector-coupling cutoff."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp516 = load("wp516_hierarchical_mass_basis_vertices.json")
wp517 = load("wp517_unequal_vector_partial_widths.json")
wp518 = load("wp518_common_order_residue_width_composition.json")
wp527 = load("wp527_hierarchical_nonquark_closure.json")

z = sp.symbols("z")
g_f, g_p, g_e, mu, s, a, b = sp.symbols(
    "g_F g_P g_E mu s a b", positive=True
)
symbols = {
    "z": z,
    "g_F": g_f,
    "g_P": g_p,
    "g_E": g_e,
    "mu": mu,
    "s": s,
    "a": a,
    "b": b,
}
wp508 = load("wp508_canonical_heavy_gauge_poles.json")
b_squared = sp.Rational(30258, 160001)
a_squared = 160000 * b_squared
witness = {
    g_f: sp.sqrt(2),
    g_p: sp.Rational(1, 10),
    g_e: sp.Rational(1, 50),
    mu: 1,
    s: 16,
    a: sp.sqrt(a_squared),
    b: sp.sqrt(b_squared),
}

# Certify a common positive lower bound on every vector mass squared.
minimum_mass_squared = sp.Rational(1, 10000)
no_root_below_floor = []
for component in wp508["heavy_gauge_poles"]["components"]:
    if component["size"] != 4:
        continue
    polynomial = sp.Poly(
        sp.sympify(
            component["cubic_characteristic_polynomial"], locals=symbols
        ).subs(witness),
        z,
    )
    no_root_below_floor.append(
        polynomial.count_roots(0, minimum_mass_squared) == 0
        and polynomial.count_roots(0, sp.oo) == 3
    )

# For an open V -> V V channel, lambda <= M^4, |p| <= M/2, and the
# six-term polynomial in WP517 is <= 33 M^4. Therefore
# Gamma <= 11 g^2 M^5/(64 pi m_min^4).
state_count = 14
maximum_candidate_channels = state_count * sp.binomial(state_count, 2)
coupling_cutoff = sp.Rational(1, 10**7)
maximum_parent_mass = sp.Integer(5)
minimum_daughter_mass = sp.Rational(1, 100)
per_channel_bound = sp.factor(
    11
    * coupling_cutoff**2
    * maximum_parent_mass**5
    / (64 * sp.pi * minimum_daughter_mass**4)
)
global_envelope = sp.factor(maximum_candidate_channels * per_channel_bound)

reported_couplings = [
    abs(sp.Float(channel["cubic_coupling"], 30))
    for channel in wp516["open_cubic_vector_channels"]
]
smallest_reported = min(reported_couplings)
largest_lower_bound = max(
    sp.Float(state["quark_plus_resolved_vector_width_lower_bound_GeV"], 30)
    for state in wp518["common_mass_ordering"]
)

checks = {
    "wp516_dependency_passed": bool(wp516["passed"]),
    "wp517_dependency_passed": bool(wp517["passed"]),
    "wp518_dependency_passed": bool(wp518["passed"]),
    "wp527_dependency_passed": bool(wp527["passed"]),
    "all_vector_masses_exceed_one_hundredth_GeV": all(no_root_below_floor),
    "candidate_channel_count_is_1274": maximum_candidate_channels == 1274,
    "smallest_retained_coupling_is_above_cutoff": smallest_reported
    > coupling_cutoff,
    "conservative_omitted_width_envelope_exceeds_one_fifth_GeV": global_envelope
    > sp.Rational(1, 5),
    "envelope_is_not_small_against_reported_width_scale": global_envelope
    > largest_lower_bound / 2,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP528",
    "domain": "WP516's full fourteen-state vector decay candidate set, conditional on every omitted transported coupling having magnitude at most the declared 10^-7 cutoff.",
    "exact_kinematic_bounds": {
        "maximum_parent_mass_GeV": str(maximum_parent_mass),
        "minimum_daughter_mass_GeV": str(minimum_daughter_mass),
        "maximum_candidate_channels": int(maximum_candidate_channels),
        "per_channel_width_bound_GeV": str(per_channel_bound),
        "global_omitted_width_envelope_GeV": str(global_envelope),
        "global_omitted_width_envelope_decimal_GeV": float(sp.N(global_envelope, 20)),
    },
    "cutoff_gap": {
        "declared_cutoff": str(coupling_cutoff),
        "smallest_retained_coupling": str(smallest_reported),
        "qualification": "The gap confirms numerical separation among retained entries but does not prove omitted entries are exact zeros.",
    },
    "classification": "Hostile robustness audit. Even granting the cutoff as an upper bound on every omitted coupling, the available uniform kinematic estimate is 7007/(10240 pi) GeV, above 0.2 GeV. This loose upper bound does not prove a large omitted width; it proves the cutoff alone supplies no negligible-width certificate.",
    "selector": False,
    "rigidifier": False,
    "instrument": "A detector resolution could define a coarse-grained lineshape, but no detector metric is authorized here and coarse graining would not turn the source self-energy into an exact total width.",
    "smallest_exact_falsifier": "A channel-specific exact enumeration or rigorous tighter bound below the independently declared width tolerance would defeat this cutoff-authority criticism.",
    "remaining_gate": "Compute exact algebraic spectral projectors or rigorous channel-specific interval bounds, especially for channels containing the lightest longitudinal vectors, before summing the complete WP525 complex self-energy.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp528_vector_cutoff_width_envelope.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
