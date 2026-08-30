"""Exact flip-protected kinetic interface for the disjoint two-triplet branch."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
Zn, Zm = sp.symbols("Zn Zm", positive=True)
Zx = sp.symbols("Zx", real=True)
K = sp.Matrix([[Zn, Zx], [Zx, Zm]])
Pn, Pm = sp.diag(-1, 1), sp.diag(1, -1)
parity_equations = list(Pn.T*K*Pn-K)+list(Pm.T*K*Pm-K)
solution = sp.solve(parity_equations, [Zx], dict=True)
Kdiag = K.subs(Zx, 0)
C = sp.diag(1/sp.sqrt(Zn), 1/sp.sqrt(Zm))
canonical = sp.simplify(C.T*Kdiag*C)

Khostile = sp.Matrix([[2, 1], [1, 2]])
y1, y2 = sp.symbols("y1 y2", positive=True)
canonical_strengths = sp.Matrix([y1/sp.sqrt(Zn), y2/sp.sqrt(Zm)])

checks = {
    "both_flips_force_zero_kinetic_mixing": solution == [{Zx: 0}],
    "positive_diagonal_gram_canonicalizes": canonical == sp.eye(2),
    "canonicalization_preserves_species_labels": C[0, 1] == 0 and C[1, 0] == 0,
    "without_flips_positive_mixing_is_allowed": Khostile.det() == 3 and (Pn.T*Khostile*Pn-Khostile) != sp.zeros(2),
    "canonical_yukawas_remain_two_free_coordinates": canonical_strengths.jacobian([y1, y2]).rank() == 2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP667", "status": "PASS", "checks": checks,
    "kinetic_gram": "K=[[Z_n,Z_x],[Z_x,Z_m]] tensor identity_3",
    "protecting_symmetry": "independent n and m sign flips",
    "forced_shape": "Z_x=0 with Z_n,Z_m>0 free",
    "canonical_map": "diag(Z_n^-1/2,Z_m^-1/2)",
    "hostile_unprotected_gram": [[2, 1], [1, 2]],
    "classification": "the kinetic interface exists conditionally on extending the flips to the disjoint messenger source, but it fixes no canonical Yukawa",
    "smallest_exact_falsifier": "a nonzero off-diagonal kinetic coefficient compatible with both admitted flips",
    "remaining_gate": "declare messenger flip charges and derive canonical Yukawa running and threshold decoupling",
}
(ROOT / "results" / "wp667_flip_protected_kinetic_interface.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
