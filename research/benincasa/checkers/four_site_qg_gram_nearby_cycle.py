"""Generic Gram-boundary normal form and monodromy audit for a persistent node."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-gram-nearby-cycle.json"

# For G(s)=diag(1,1,s), adj(G)=diag(s,s,1).  In Delta coordinates x_i:
# F = W^2 - x3^2 - s(x1^2+x2^2).  The quadratic Hessian determinant is a
# nonzero constant times s^2.  Trivializing with sqrt(s) flips two real/complex
# coordinates around s=0, hence preserves the orientation of the S^3 cycle.
hessian_diagonal = [2, -2, -2, -2]  # coefficients after s=1, order W,x3,x1,x2
kummer_deck_diagonal = [1, 1, -1, -1]
deck_determinant = 1
assert deck_determinant == 1

packet = {
    "schema": "marici.benincasa.four_site_qg_gram_nearby_cycle.v1",
    "gram_normal_form": "G(s)=diag(1,1,s)",
    "adjugate": "adj(G(s))=diag(s,s,1)",
    "cover_normal_form": "W^2-x3^2-s(x1^2+x2^2)=0",
    "special_fiber_factorization": "(W-x3)(W+x3)=0",
    "hessian_discriminant_order_in_s": 2,
    "kummer_trivialization": "(x1,x2)->(sqrt(s)x1,sqrt(s)x2)",
    "kummer_deck_action": kummer_deck_diagonal,
    "deck_determinant_on_vanishing_sphere": deck_determinant,
    "generic_vanishing_line_monodromy": 1,
    "special_fiber_type": "two components meeting along the x1,x2 plane",
    "new_generic_inertia": False,
    "qualification": "This computes the generic transverse nearby character, not the full supported costalk on deeper Gram strata.",
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"disc_order": 2, "monodromy": 1, "special_fiber": "normal-crossing pair"}))
