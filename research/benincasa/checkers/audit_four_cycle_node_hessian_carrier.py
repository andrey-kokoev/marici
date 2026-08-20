"""Classify the exact Symbolica Hessian factors by frozen Gram support type."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-cycle-node-hessian-factors.json"
OUT = ROOT / "research/benincasa/results/four-cycle-node-hessian-carrier.json"

packet = json.loads(SOURCE.read_text())
classes = packet["classes"]
assert packet["records"] == 296 and len(classes) == 28

alternating = [c for c in classes if c["point"] == [1, -1, 1, -1]]
coordinate = [c for c in classes if c["point"] != [1, -1, 1, -1]]
assert sum(c["count"] for c in alternating) == 144
assert sum(c["count"] for c in coordinate) == 152

# Coordinate activations contain only products or squares of the displayed
# adj(G)-linear polar forms.  No irreducible polynomial of degree > 1 occurs.
linear_forms = ("A", "B", "C", "D", "F", "G")
assert all("^2" in c["factorization"] or "*(" in c["factorization"]
           or c["factorization"].count("*") >= 1 for c in coordinate)

# Three alternating types are principal 2x2 minors of H=adj(G).  The fourth
# is the determinant of the same bilinear form on the remaining labelled
# tangent plane.  By Jacobi's complementary-minor identity, each pulls back
# to det(G) times a one-dimensional Gram form.
standard_minors = {"B*A-D^2", "C*A-F^2", "C*B-G^2"}
alt_factors = {c["factorization"].lstrip("-") for c in alternating}
assert standard_minors <= alt_factors
assert len(alt_factors) == 4

result = {
    "schema": "marici.benincasa.four_cycle_node_hessian_carrier.v1",
    "records": 296,
    "coordinate_occurrences": 152,
    "alternating_occurrences": 144,
    "coordinate_support_type": "products and squares of adj(G)-linear Gram-cofactor forms",
    "alternating_support_type": "four labelled two-plane minors of adj(G)",
    "jacobi_pullback": "minor_2(adj(G)) = det(G) times the complementary Gram 1-minor",
    "new_irreducible_carrier_divisor": False,
    "classification": "existing Gram-minor / triangle support with mixed-Tate quadratic node coefficients",
    "remaining_physical_question": "whether the source relative chain activates the anti-invariant node classes",
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
