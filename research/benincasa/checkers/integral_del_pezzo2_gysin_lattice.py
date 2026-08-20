"""Integral Gysin lattice for a degree-two del Pezzo anticanonical complement."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/integral-del-pezzo2-gysin-lattice.json"

# In Pic(S)=Z<H,E1,...,E7>, the anticanonical boundary is
# D=-K_S=3H-E1-...-E7.
D = [3] + [-1] * 7
content = math.gcd(*(abs(x) for x in D))
assert content == 1

# The degree map alpha |-> alpha.D is surjective because E_i.D=1.
# Consequently the Gysin inclusion Z[D] -> H^2(S;Z) is primitive.
intersection_with_D = [3] + [1] * 7
degree_image_gcd = math.gcd(*intersection_with_D)
assert degree_image_gcd == 1

# Localization for U=S\D:
# 0 -> H2(S)/Z[D] -> H2(U) -> H1(D)(-1) -> 0.
algebraic_rank = 8 - 1
elliptic_rank = 2
complement_rank = algebraic_rank + elliptic_rank
assert (algebraic_rank, elliptic_rank, complement_rank) == (7, 2, 9)

packet = {
    "schema": "marici.benincasa.integral_del_pezzo2_gysin_lattice.v1",
    "picard_basis": ["H"] + [f"E{i}" for i in range(1, 8)],
    "anticanonical_class": D,
    "anticanonical_content": content,
    "intersection_degree_row": intersection_with_D,
    "intersection_degree_gcd": degree_image_gcd,
    "algebraic_kernel_rank": algebraic_rank,
    "elliptic_quotient_rank": elliptic_rank,
    "complement_rank": complement_rank,
    "algebraic_quotient_torsion": [],
    "abelian_group_extension_splits": True,
    "splitting_canonical": False,
    "interpretation": "The generic integral infinity-Gysin sequence has primitive rank-seven algebraic kernel and free rank-two elliptic quotient. Static lattice torsion cannot identify conductor parities with the elliptic cusp coinvariant; any interaction must arise from monodromy, support, or the noncanonically split variation.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))
