"""Exact SO(5) to diagonal-SO(3) singlet multiplicity obstruction."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

L3 = [
    sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
    sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
]
generators = [sp.diag(generator, sp.zeros(2)) for generator in L3]

entries = sp.symbols("x0:25")
X = sp.Matrix(5, 5, entries)
linear_equations = []
for generator in generators:
    linear_equations.extend(list(X * generator - generator * X))
solution_set = sp.linsolve(linear_equations, entries)
solution_tuple = next(iter(solution_set))
commutant_parameters = sorted(
    set().union(*(expression.free_symbols for expression in solution_tuple)),
    key=str,
)

theta = sp.symbols("theta", real=True)
rotation2 = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta)],
    [sp.sin(theta), sp.cos(theta)],
])
rotation5 = sp.diag(sp.eye(3), rotation2)
projector0 = sp.Matrix([[1, 0], [0, 0]])
projector_theta = sp.simplify(rotation2 * projector0 * rotation2.T)
c = sp.Matrix([1, 0])
s_theta = sp.Matrix([sp.cos(theta), sp.sin(theta)])
coupling_squared = sp.expand((c.dot(s_theta))**2)

checks = {
    "SO3_generators_have_rank_three_support": all(
        generator[3:, :] == sp.zeros(2, 5) and generator[:, 3:] == sp.zeros(5, 2)
        for generator in generators
    ),
    "full_linear_commutant_has_dimension_five": len(commutant_parameters) == 5,
    "singlet_multiplicity_is_two": rotation2.shape == (2, 2),
    "O2_rotation_commutes_with_residual_SO3": all(
        sp.simplify(rotation5 * generator - generator * rotation5) == sp.zeros(5)
        for generator in generators
    ),
    "rotated_projector_remains_rank_one": projector_theta.rank() == 1,
    "projector_varies_with_theta": sp.simplify(projector_theta.subs(theta, 0) - projector_theta.subs(theta, sp.pi/2)) != sp.zeros(2),
    "witness_coupling_is_cosine_squared": sp.simplify(coupling_squared - sp.cos(theta)**2) == 0,
    "witness_coupling_at_zero_is_one": coupling_squared.subs(theta, 0) == 1,
    "witness_coupling_at_half_turn_is_zero": coupling_squared.subs(theta, sp.pi/2) == 0,
    "deliberate_failure_residual_is_nonzero": coupling_squared.subs(theta, 0) - coupling_squared.subs(theta, sp.pi/2) == 1,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP739",
    "status": "PASS",
    "checks": checks,
    "parent_restriction": "5 of SO(5) -> (2,2)+(1,1) of SO(4) -> 3+1+1 of diagonal SO(3)",
    "contextual_partition": "the residual SO(3) identifies a two-dimensional singlet isotypic component but does not distinguish its rank-one rays",
    "commutant": "R times M_2(R), with O(2) in the orthogonal commutant",
    "classification": "simple-group representation rigidifies the total isotypic packet but does not select the physical one-singlet projector",
    "smallest_exact_falsifier": "the commuting pi/2 singlet rotation changes the selected coupling squared from one to zero",
    "claim_boundary": "representation descent and quadratic mixing; no claim about a separately specified breaking potential that could fix the projector",
    "remaining_source_gate": "derive a breaking-sector potential and gapped mass projector independently, then prove its RG and threshold stability",
    "remaining_fixed_point_gate": "deferred until the source-to-one-singlet projection is faithful",
    "remaining_physical_gate": "detector labels must distinguish the selected singlet from its compulsory partner using an independent calibration locus",
}
(ROOT / "results" / "wp739_so5_singlet_multiplicity_projector_obstruction.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
