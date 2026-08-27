"""Exact exchange-balance selector and its failure to select low-energy flavor."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
A, B, y, z, p, M = sp.symbols("A B y z p M", positive=True)
j = sp.symbols("j", real=True)
mass = sp.Matrix([[A, y*j], [z*j, B]])
swap = sp.Matrix([[0, 1], [1, 0]])
exchange_defect = sp.expand(swap*mass*swap-mass)
solutions = sp.solve(list(exchange_defect), [B, z], dict=True)

erosion = y**4+z**4
product = y*z
balanced_erosion = erosion.subs(z, y)
matched_coefficient = -p/M
response = sp.Matrix([matched_coefficient]).jacobian([p])

checks = {
    "exchange_forces_equal_masses_and_vertices": solutions == [{B: A, z: y}],
    "exchange_selects_balance_subspace": balanced_erosion == 2*y**4,
    "balance_saturates_fixed_product_minimum": sp.simplify(erosion-2*product**2-(y**2-z**2)**2) == 0,
    "matched_coefficient_remains_one_free_coordinate": response.rank() == 1,
    "two_balanced_source_points_give_distinct_matching": matched_coefficient.subs({p: 1, M: 1}) != matched_coefficient.subs({p: 2, M: 1}),
    "bare_exchange_basis_is_not_a_split_pole_basis": mass.subs({B: A, z: y}).eigenvals() == {A-j*y: 1, A+j*y: 1},
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP676", "status": "PASS", "checks": checks,
    "source_symmetry": "A<->B exchange",
    "selected_uv_subspace": "M_A=M_B and y=z",
    "erosion_on_selected_subspace": "y^4+z^4=2(yz)^2",
    "low_energy_map": "c=-p/M with p=y^2 still free",
    "pole_warning": "after the frame background, exchanged bare fields diagonalize to eigenvalues M+-yj and are not the physical decay labels used in WP674",
    "classification": "conditional internal-block rigidifier and erosion minimizer; WP681 shows that fixed entrance/exit endpoints break the exchange, so it is not a full-grammar source selector",
    "smallest_exact_falsifier": "an exchange-invariant mass matrix with M_A!=M_B or y!=z",
    "remaining_gate": "closed negative by WP681: the balanced fluctuation is pole diagonal and the full endpoint grammar is not exchange invariant",
}
(ROOT / "results" / "wp676_exchange_balance_uv_selector.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
