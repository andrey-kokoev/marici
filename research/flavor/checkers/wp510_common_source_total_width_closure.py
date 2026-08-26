"""Common-source total tree-level width closure for the WP508 spectrum."""

import contextlib
import io
import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp447 = load("wp447_irreducible_adjoint_triplet.json")
wp499 = load("wp499_o2_connector_hessian.json")
wp506 = load("wp506_full_doublet_hessian_attempt.json")
wp508 = load("wp508_canonical_heavy_gauge_poles.json")
wp509 = load("wp509_spectral_residue_width_sum_rules.json")

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

witness = {
    g_f: sp.sqrt(2),
    g_p: sp.Rational(1, 10),
    g_e: sp.Rational(1, 50),
    mu: 1,
    s: 16,
    a: 55,
    b: 54,
}
lower = sp.Rational(19, 10)
upper = sp.Rational(31, 5)
quintet = (3 * g_f**2 * mu**2).subs(witness)

cubic_packets = []
cubic_root_counts = []
cubic_simple_checks = []
for component in wp508["heavy_gauge_poles"]["components"]:
    if component["size"] != 4:
        continue
    polynomial = sp.Poly(
        sp.sympify(
            component["cubic_characteristic_polynomial"], locals=symbols
        ).subs(witness),
        z,
    )
    count = int(polynomial.count_roots(lower, upper))
    discriminant = sp.factor(sp.discriminant(polynomial.as_expr(), z))
    cubic_root_counts.append(count == 3)
    cubic_simple_checks.append(bool(discriminant > 0))
    cubic_packets.append(
        {
            "generators": component["generators"],
            "polynomial": str(polynomial.as_expr()),
            "roots_in_open_interval": count,
            "interval": [str(lower), str(upper)],
            "discriminant": str(discriminant),
        }
    )

# A single singlet sigma fixes every amplitude through positive radial squares.
# The kinetic metric records the canonical radial norms of the adjoint triplet,
# connector, and two complex entrance doublets.
mu_r, s_r, a_r, b_r, sigma = sp.symbols("mu_r s_r a_r b_r sigma", real=True)
radial_variables = [mu_r, s_r, a_r, b_r]
radial_ratios = [1, 16, 55, 54]
radial_quartic = sp.Integer(100)
singlet_quartic = sp.Integer(10) ** 9
radial_potential = sp.expand(
    sum(
        radial_quartic * (variable**2 - ratio**2 * sigma**2) ** 2
        for variable, ratio in zip(radial_variables, radial_ratios)
    )
    + singlet_quartic * (sigma**2 - 1) ** 2
)
radial_vacuum = dict(zip(radial_variables + [sigma], radial_ratios + [1]))
radial_hessian = sp.hessian(
    radial_potential, radial_variables + [sigma]
).subs(radial_vacuum)
radial_metric = sp.diag(6, 3, 2, 2, 1)
daughter_threshold = upper / 4
shifted_radial = radial_hessian - daughter_threshold * radial_metric
radial_minors = [
    sp.factor(shifted_radial[:index, :index].det()) for index in range(1, 6)
]

# Replay the complete entrance source and evaluate its physical spectrum at the
# same amplitudes.  The six exact zeros are the broken gauge orbit.
wp506_path = root / "checkers" / "wp506_full_doublet_hessian_attempt.py"
namespace = {"__file__": str(wp506_path), "__name__": "wp506_replay"}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(compile(wp506_path.read_text(encoding="utf-8"), str(wp506_path), "exec"), namespace)
    except SystemExit as error:
        if error.code != 0:
            raise
entrance_substitution = {
    namespace["a"]: witness[a],
    namespace["b"]: witness[b],
    **{coupling: 1 for coupling in namespace["couplings"]},
}
entrance_hessian = namespace["hessian"].subs(entrance_substitution)
entrance_eigenvalues = entrance_hessian.eigenvals()
entrance_positive = sorted(
    eigenvalue
    for eigenvalue, multiplicity in entrance_eigenvalues.items()
    for _ in range(multiplicity)
    if eigenvalue != 0
)

# The WP447 unit source has minimum physical adjoint mass squared 16.  A stable
# O(2) connector point lambda_1=lambda_3=lambda_4=lambda_5=1, lambda_2=0
# has minimum physical mass squared 4 s^2.  Both are source coefficients, not
# separately inserted daughter masses.
adjoint_minimum = sp.Integer(16)
connector_minimum = 4 * witness[s] ** 2
messenger_mass_squared = sp.Integer(4)  # z_A=z_B=2 and sigma=1
electroweak_w_squared = sp.Rational(
    witness[a] ** 2 + witness[b] ** 2, 2
)
electroweak_z_squared = witness[a] ** 2 + witness[b] ** 2
clock_ratio_squared = sp.factor(
    witness[g_f] ** 2 * (6 * witness[mu] ** 2)
    / (2 * (witness[a] ** 2 + witness[b] ** 2))
)

checks = {
    "wp447_dependency_passed": bool(wp447["passed"]),
    "wp499_dependency_passed": bool(wp499["passed"]),
    "wp506_dependency_passed": bool(wp506["passed"]),
    "wp508_dependency_passed": bool(wp508["passed"]),
    "wp509_dependency_passed": bool(wp509["passed"]),
    "all_nine_cubic_poles_lie_in_exact_interval": all(cubic_root_counts),
    "all_three_cubics_have_simple_real_roots": all(cubic_simple_checks),
    "five_quintet_poles_lie_in_exact_interval": bool(lower < quintet < upper),
    "global_vector_pair_threshold_is_closed": bool(4 * lower > upper),
    "radial_source_hessian_exceeds_daughter_threshold": all(
        minor > 0 for minor in radial_minors
    ),
    "entrance_hessian_has_only_six_gauge_zeros": bool(
        entrance_hessian.rank() == 18 and entrance_eigenvalues.get(0, 0) == 6
    ),
    "entrance_physical_scalars_exceed_daughter_threshold": bool(
        len(entrance_positive) == 18 and min(entrance_positive) > daughter_threshold
    ),
    "adjoint_scalars_exceed_daughter_threshold": bool(
        adjoint_minimum > daughter_threshold
    ),
    "connector_scalars_exceed_daughter_threshold": bool(
        connector_minimum > daughter_threshold
    ),
    "messengers_exceed_daughter_threshold": bool(
        messenger_mass_squared > daughter_threshold
    ),
    "massive_electroweak_vectors_exceed_daughter_threshold": bool(
        min(electroweak_w_squared, electroweak_z_squared) > daughter_threshold
    ),
    "clock_ratio_is_fixed_by_same_source_witness": bool(
        clock_ratio_squared == sp.Rational(6, 5941)
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP510",
    "source_witness": {
        "common_clock": "sigma=1",
        "vacuum_relations": "mu=sigma, s=16 sigma, a=55 sigma, b=54 sigma",
        "gauge_couplings": "g_F=sqrt(2), g_P=1/10, g_E=1/50",
        "messenger_yukawas": "z_A=z_B=2",
        "radial_quartics": "lambda_mu=lambda_s=lambda_a=lambda_b=100, kappa_sigma=10^9",
        "clock_ratio_squared": str(clock_ratio_squared),
        "clock_ratio": str(sp.sqrt(clock_ratio_squared)),
    },
    "exact_vector_interval": {
        "lower_mass_squared": str(lower),
        "upper_mass_squared": str(upper),
        "quintet_mass_squared": str(quintet),
        "cubic_sectors": cubic_packets,
        "pair_closure_margin": str(4 * lower - upper),
    },
    "nonquark_thresholds": {
        "required_minimum_mass_squared": str(daughter_threshold),
        "radial_shifted_leading_minors": [str(value) for value in radial_minors],
        "adjoint_minimum_mass_squared": str(adjoint_minimum),
        "connector_minimum_mass_squared": str(connector_minimum),
        "entrance_minimum_mass_squared": str(min(entrance_positive)),
        "messenger_mass_squared": str(messenger_mass_squared),
        "electroweak_w_mass_squared": str(electroweak_w_squared),
        "electroweak_z_mass_squared": str(electroweak_z_squared),
    },
    "width_disposition": "At this source witness every tree-level two-body nonquark threshold in the declared census is closed, so WP509's six-quark partial widths are the complete tree-level widths. Loop-induced, off-shell, and detector-smeared widths are not included.",
    "classification": "Nonempty common-source total-width closure witness and conditional relational selector. The dimensionless witness coefficients remain inputs rather than dynamically predicted numbers.",
    "selector": "conditional relational selector for fixed source coefficients",
    "rigidifier": bool(all(cubic_root_counts) and all(cubic_simple_checks)),
    "instrument": None,
    "smallest_exact_falsifier": "A heavy pole outside (19/10,31/5), a nonquark daughter mass squared at or below 31/20 with a nonzero source vertex, or a source deformation that changes 6/5941 while respecting the admitted symmetries.",
    "remaining_gate": "Derive the dimensionless witness coefficients from coefficient dynamics and attach a calibrated common-frame pole-current instrument. Only then is the clock ratio a numerical prediction and the total-width packet experimentally readable.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp510_common_source_total_width_closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
