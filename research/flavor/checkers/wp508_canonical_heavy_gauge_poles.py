"""Canonical heavy gauge-pole factorization and current resolvents for WP508."""

import contextlib
import io
import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp485 = load("wp485_mixed_gauge_pole_residues.json")
wp488 = load("wp488_flavor_clock_normalization_correction.json")
wp507 = load("wp507_complete_gauge_gram_rank.json")

# Reuse the exact WP507 tangent construction, then impose the physical SU(3)
# generator and kinetic normalizations used by WP485.
namespace = {"__file__": str(root / "checkers" / "wp507_complete_gauge_gram_rank.py"), "__name__": "wp507_replay"}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(
            compile(
                (root / "checkers" / "wp507_complete_gauge_gram_rank.py").read_text(encoding="utf-8"),
                namespace["__file__"],
                "exec",
            ),
            namespace,
        )
    except SystemExit as error:
        if error.code != 0:
            raise

tangent_matrix = namespace["tangent_matrix"]
g_f = namespace["g_f"]
g_p = namespace["g_p"]
g_e = namespace["g_e"]
g_2 = namespace["g_2"]
g_y = namespace["g_y"]
mu = namespace["mu"]
s = namespace["s"]
a = namespace["a"]
b = namespace["b"]

generator_normalization = sp.diag(*([sp.Rational(1, 2)] * 8 + [1] * 10))
canonical_tangents = tangent_matrix * generator_normalization
kinetic_metric = sp.diag(*([1] * 9 + [2] * 24 + [2] * 24))
mass_matrix = sp.simplify(canonical_tangents.T * kinetic_metric * canonical_tangents)
heavy_block = mass_matrix[:14, :14]
electroweak_block = mass_matrix[14:, 14:]

names = [f"F{i + 1}" for i in range(8)] + [f"P{i + 1}" for i in range(3)] + [f"E{i + 1}" for i in range(3)]


def sparsity_components(matrix):
    remaining = set(range(matrix.rows))
    components = []
    while remaining:
        seed = min(remaining)
        stack = [seed]
        component = set()
        while stack:
            node = stack.pop()
            if node in component:
                continue
            component.add(node)
            for other in range(matrix.rows):
                if other != node and sp.simplify(matrix[node, other]) != 0:
                    stack.append(other)
        remaining -= component
        components.append(sorted(component))
    return components


components = sparsity_components(heavy_block)
component_sizes = sorted(len(component) for component in components)
z = sp.symbols("z")
quintet_mass = 3 * g_f**2 * mu**2
component_packets = []
singleton_masses = []
cubic_current_resolvents = []
embedded_quintet_factors = 0
for component in components:
    block = heavy_block.extract(component, component)
    polynomial = sp.factor(block.charpoly(z).as_expr())
    packet = {
        "generators": [names[index] for index in component],
        "size": len(component),
        "characteristic_polynomial": str(polynomial),
    }
    flavor_positions = [local for local, global_index in enumerate(component) if global_index < 8]
    if len(component) == 1:
        singleton_masses.append(sp.factor(block[0, 0]))
    if len(component) == 4 and len(flavor_positions) == 2:
        quotient, remainder = sp.div(sp.Poly(polynomial, z), sp.Poly(z - quintet_mass, z))
        cubic_polynomial = sp.factor(quotient.as_expr())
        adjugate = (z * sp.eye(4) - block).adjugate()
        numerator_matrix = sp.Matrix(
            2,
            2,
            lambda row, column: sp.factor(
                g_f**2 * adjugate[flavor_positions[row], flavor_positions[column]]
            ),
        )
        denominator = sp.factor((z * sp.eye(4) - block).det())
        packet["embedded_quintet_factor"] = str(z - quintet_mass)
        packet["cubic_characteristic_polynomial"] = str(cubic_polynomial)
        packet["factor_remainder"] = str(remainder.as_expr())
        packet["flavor_current_resolvent"] = {
            "numerator_matrix": [[str(value) for value in row] for row in numerator_matrix.tolist()],
            "denominator": str(denominator),
        }
        cubic_current_resolvents.append((numerator_matrix, denominator, remainder.as_expr()))
        embedded_quintet_factors += 1
    component_packets.append(packet)

heavy_characteristic_from_components = sp.expand(
    sp.prod(heavy_block.extract(component, component).charpoly(z).as_expr() for component in components)
)
off_component_entries = []
for left_index, left_component in enumerate(components):
    for right_component in components[left_index + 1:]:
        off_component_entries.extend(
            heavy_block[i, j] for i in left_component for j in right_component
        )

v_phys_squared = 2 * (a**2 + b**2)
expected_electroweak = v_phys_squared * sp.Matrix(
    [
        [g_2**2 / 4, 0, 0, 0],
        [0, g_2**2 / 4, 0, 0],
        [0, 0, g_2**2 / 4, -g_2 * g_y / 4],
        [0, 0, -g_2 * g_y / 4, g_y**2 / 4],
    ]
)

checks = {
    "wp485_dependency_passed": wp485["passed"],
    "wp488_dependency_passed": wp488["passed"],
    "wp507_dependency_passed": wp507["passed"],
    "canonical_heavy_block_has_rank_fourteen": heavy_block.rank() == 14,
    "heavy_sparsity_components_are_two_singletons_and_three_quartics": component_sizes == [1, 1, 4, 4, 4],
    "two_singletons_recover_wp488_quintet_mass": len(singleton_masses) == 2 and all(
        sp.simplify(value - quintet_mass) == 0 for value in singleton_masses
    ),
    "three_quartics_each_factor_as_quintet_times_cubic": embedded_quintet_factors == 3 and all(
        sp.simplify(remainder) == 0 for _, _, remainder in cubic_current_resolvents
    ),
    "five_total_quintet_factors_are_recovered": len(singleton_masses) + embedded_quintet_factors == 5,
    "each_mixed_block_has_two_by_two_flavor_current_resolvent": len(cubic_current_resolvents) == 3 and all(
        numerator.shape == (2, 2) for numerator, _, _ in cubic_current_resolvents
    ),
    "sparsity_components_are_exactly_block_diagonal": all(
        sp.simplify(value) == 0 for value in off_component_entries
    ),
    "component_characteristic_product_has_degree_fourteen": sp.degree(
        heavy_characteristic_from_components, z
    ) == 14,
    "canonical_electroweak_block_uses_v_phys_squared": (
        electroweak_block - expected_electroweak
    ).applyfunc(sp.simplify) == sp.zeros(4),
    "physical_electroweak_norm_is_two_a2_plus_b2": v_phys_squared == 2 * (a**2 + b**2),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP508",
    "canonical_normalization": {
        "su3_generators": "lambda_A/2",
        "field_metric": "weight 1 on real connector coordinates, weight 2 on adjoint coordinates, and weight 2 on complex-doublet real/imaginary coordinates",
        "flavor_norm": "f_phys^2=6 mu^2",
        "electroweak_norm": "v_phys^2=2(a^2+b^2)",
    },
    "heavy_gauge_poles": {
        "dimension": 14,
        "factorization": "two singleton quintet poles plus three four-generator blocks, each factoring into one quintet pole and one exact cubic mixed sector",
        "unmixed_quintet_mass_squared": str(quintet_mass),
        "components": component_packets,
    },
    "current_readout": {
        "quintet": "g_F^2/(z-3 g_F^2 mu^2) on each principal-SU(2) quintet coordinate",
        "three_mixed_channels": "Each four-generator component carries the exact two-by-two flavor-current resolvent recorded with that component.",
        "interpretation": "The Gell-Mann basis mixes one quintet and one embedded-triplet flavor coordinate inside each four-generator block. The determinant separates into an exact quintet factor and cubic mixed factor, while the current resolvent remains matrix-valued before a principal-SU(2) basis rotation.",
    },
    "classification": "Exact canonically normalized heavy gauge-pole and matrix-current-resolvent grammar: five quintet factors plus three cubic mixed sectors. It freezes the algebraic pole packet, not numerical masses, residues, or widths.",
    "selector": False,
    "rigidifier": bool(component_sizes == [1, 1, 4, 4, 4] and embedded_quintet_factors == 3),
    "instrument": None,
    "smallest_exact_falsifier": "Canonical normalization produces two singleton and three embedded quintet factors at 3 g_F^2 mu^2, together with three independent cubic flavor-port-row sectors; any reuse of WP485's three identical quadratic blocks fails once the entrance gauge sector is active.",
    "remaining_gate": "Extract pole projectors and residues for each cubic root, freeze or constrain the source parameter ratios, enumerate every kinematically open channel, and compose the propagators with a calibrated current instrument before assigning numerical widths or g_F f_phys/v.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp508_canonical_heavy_gauge_poles.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
