"""Derived-flatness certificate for the two-normal rank-one Gram corner."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-rank-one-derived-fiber.json"

# A = Q[s,t,x1,x2,x3].  Since F=W^2-f is monic in W,
# A[W]/(F) = A*1 direct-sum A*W.  It is therefore A-flat and Q[s,t]-flat.
# Tensoring with Q[s,t]/(s,t) produces Q[x][W]/(W^2), with no higher Tor.
degrees = list(range(0, 9))
# Hilbert function in fiber degree for Q[x1,x2,x3] plus W times the same ring,
# assigning degree(W)=1 only to display the square-zero two-layer structure.
base_hilbert = [(d + 2) * (d + 1) // 2 for d in degrees]
double_hilbert = [base_hilbert[d] + (base_hilbert[d-1] if d else 0) for d in degrees]
assert double_hilbert[:5] == [1, 4, 9, 16, 25]

packet = {
    "schema": "marici.benincasa.four_site_qg_rank_one_derived_fiber.v1",
    "base_ring": "A=Q[s,t,x1,x2,x3]",
    "family_ring": "A[W]/(W^2-st*x1^2-t*x2^2-s*x3^2)",
    "free_A_basis": ["1", "W"],
    "flat_over_Q_s_t": True,
    "higher_tor_at_s_t_zero": 0,
    "derived_special_fiber": "Q[x1,x2,x3,W]/(W^2)",
    "cartier_grades": ["Q[x1,x2,x3]", "W*Q[x1,x2,x3]"],
    "sample_hilbert_function": double_hilbert,
    "new_corner_extension": False,
    "qualification": "The square-zero W layer is retained; this does not assert a physical-chain pairing with it.",
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"free_rank": 2, "higher_tor": 0, "special_fiber": "W^2=0"}))
