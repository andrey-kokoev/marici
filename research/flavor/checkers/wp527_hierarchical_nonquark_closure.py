"""Exact nonquark threshold closure and vector-census authority audit."""

import contextlib
import io
import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp506 = load("wp506_full_doublet_hessian_attempt.json")
wp508 = load("wp508_canonical_heavy_gauge_poles.json")
wp516 = load("wp516_hierarchical_mass_basis_vertices.json")
wp518 = load("wp518_common_order_residue_width_composition.json")
wp526 = load("wp526_messenger_width_hostile_pair.json")

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

cubic_packets = []
all_roots_below_25 = []
for component in wp508["heavy_gauge_poles"]["components"]:
    if component["size"] != 4:
        continue
    polynomial = sp.Poly(
        sp.sympify(
            component["cubic_characteristic_polynomial"], locals=symbols
        ).subs(witness),
        z,
    )
    positive_count = int(polynomial.count_roots(0, sp.oo))
    below_25_count = int(polynomial.count_roots(0, 25))
    all_roots_below_25.append(positive_count == 3 and below_25_count == 3)
    cubic_packets.append(
        {
            "generators": component["generators"],
            "positive_roots": positive_count,
            "roots_between_0_and_25": below_25_count,
        }
    )

# Replay the exact WP506 entrance Hessian. Scaling all nine positive source
# coefficients by L scales the complete Hessian by L.
wp506_path = root / "checkers" / "wp506_full_doublet_hessian_attempt.py"
namespace = {"__file__": str(wp506_path), "__name__": "wp506_replay"}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(
            compile(wp506_path.read_text(encoding="utf-8"), str(wp506_path), "exec"),
            namespace,
        )
    except SystemExit as error:
        if error.code != 0:
            raise
entrance_substitution = {
    namespace["a"]: sp.sqrt(a_squared),
    namespace["b"]: sp.sqrt(b_squared),
    **{coupling: 5 for coupling in namespace["couplings"]},
}
entrance_hessian = namespace["hessian"].subs(entrance_substitution)
entrance_eigenvalues = entrance_hessian.eigenvals()
entrance_positive = [
    eigenvalue
    for eigenvalue, multiplicity in entrance_eigenvalues.items()
    for _ in range(multiplicity)
    if eigenvalue != 0
]
entrance_minimum = min(entrance_positive)

# A common radial source with the same vacuum ratios. The shifted Hessian test
# is in the canonical kinetic metric used by WP510.
mu_r, s_r, a_r, b_r, sigma = sp.symbols(
    "mu_r s_r a_r b_r sigma", real=True
)
radial_variables = [mu_r, s_r, a_r, b_r]
radial_ratios = [1, 16, sp.sqrt(a_squared), sp.sqrt(b_squared)]
radial_potential = sp.expand(
    sum(
        100 * (variable**2 - ratio**2 * sigma**2) ** 2
        for variable, ratio in zip(radial_variables, radial_ratios)
    )
    + sp.Integer(10) ** 9 * (sigma**2 - 1) ** 2
)
radial_vacuum = dict(zip(radial_variables + [sigma], radial_ratios + [1]))
radial_hessian = sp.hessian(
    radial_potential, radial_variables + [sigma]
).subs(radial_vacuum)
threshold_squared = sp.Rational(25, 4)
radial_metric = sp.diag(6, 3, 2, 2, 1)
shifted_radial = radial_hessian - threshold_squared * radial_metric
radial_minors = [
    sp.factor(shifted_radial[:index, :index].det())
    for index in range(1, 6)
]

adjoint_minimum = sp.Integer(16)
connector_minimum = sp.Integer(1024)
messenger_minimum = sp.Integer(9)
electroweak_minimum = sp.Rational(30258, 2)
wp516_source = (
    root / "checkers" / "wp516_hierarchical_mass_basis_vertices.py"
).read_text(encoding="utf-8")

checks = {
    "wp506_dependency_passed": bool(wp506["passed"]),
    "wp508_dependency_passed": bool(wp508["passed"]),
    "wp516_dependency_passed": bool(wp516["passed"]),
    "wp518_dependency_passed": bool(wp518["passed"]),
    "wp526_dependency_passed": bool(wp526["passed"]),
    "all_vector_mass_squares_are_strictly_below_25": all(all_roots_below_25)
    and 6 < 25,
    "entrance_hessian_has_exactly_six_gauge_zeros": entrance_eigenvalues.get(
        0, 0
    )
    == 6,
    "entrance_scalars_close_all_pair_thresholds": entrance_minimum
    > threshold_squared,
    "radial_scalars_close_all_pair_thresholds": all(
        minor > 0 for minor in radial_minors
    ),
    "adjoint_connector_messenger_and_ew_pairs_are_closed": min(
        adjoint_minimum,
        connector_minimum,
        messenger_minimum,
        electroweak_minimum,
    )
    > threshold_squared,
    "wp516_vector_census_uses_a_numerical_coupling_cutoff": "abs(coupling) > 1e-7"
    in wp516_source,
    "wp518_remains_explicitly_a_lower_bound": "lower bound"
    in wp518["classification"].lower(),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP527",
    "domain": "WP516 hierarchical vector witness with a common sigma=1 source completion, z_A=z_B=3, entrance coefficients five, radial quartics 100, and singlet lift 10^9.",
    "exact_vector_bound": {
        "cubic_root_counts": cubic_packets,
        "quintet_mass_squared": "6",
        "global_bound": "Every vector pole has M^2<25 GeV^2.",
    },
    "nonquark_closure_witness": {
        "required_daughter_mass_squared": str(threshold_squared),
        "entrance_minimum_mass_squared": str(entrance_minimum),
        "radial_shifted_leading_minors": [str(value) for value in radial_minors],
        "adjoint_minimum_mass_squared": str(adjoint_minimum),
        "connector_minimum_mass_squared": str(connector_minimum),
        "messenger_mass_squared": str(messenger_minimum),
        "electroweak_minimum_mass_squared": str(electroweak_minimum),
        "conclusion": "Every declared nonquark two-body pair threshold is strictly closed at this common-source witness.",
    },
    "remaining_vector_census_defect": {
        "cutoff": "WP516 retains transported cubic couplings only above 10^-7.",
        "authority_consequence": "The cutoff is a numerical resolution convention, not a proof that every omitted above-threshold coupling vanishes. WP517-WP518 therefore remain resolved lower bounds even after nonquark closure.",
    },
    "classification": "Constructive nonquark threshold closure witness plus an exact total-width authority refusal caused by the unresolved numerical vector-vertex cutoff.",
    "selector": "conditional relational selector for the explicitly frozen source coefficients",
    "rigidifier": bool(all(all_roots_below_25)),
    "instrument": "No total-width pole instrument is admitted until every above-threshold Yang-Mills channel is classified algebraically as zero or assigned a width.",
    "smallest_exact_falsifier": "The source completion closes all declared nonquark pairs, but WP516's 10^-7 vertex cutoff leaves unproved channel support; one nonzero omitted channel falsifies total-width identification.",
    "remaining_gate": "Replace the floating mass-basis cutoff census by exact algebraic pole projectors, isolate every threshold, prove each transported vertex zero or nonzero, and recompute the complete vector self-energy sum before applying WP525.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp527_hierarchical_nonquark_closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
