"""Photon helicity determinant as pre-positive connected information."""

import json
from pathlib import Path
import sympy as sp


r, s, t = sp.symbols("r s t", real=True)
M = sp.Matrix([[r, t], [t, s]])
norm = sp.expand(sum(v**2 for v in M))
rho_a_num = sp.expand(M*M.T)

det_transport = sp.factor(M.det())
det_rho_num = sp.factor(rho_a_num.det())
assert sp.factor(det_rho_num - det_transport**2) == 0

# Product-state locus for a pure bipartite coefficient matrix is rank one.
assert det_transport == r*s - t**2

# An independent spectator vector does not change Schmidt/transport rank.
a, b = sp.symbols("a b", real=True)
spectator = sp.Matrix([[a, b]])
M_ext = sp.kronecker_product(M, spectator)
assert M_ext.rank(iszerofunc=lambda z: z == 0) == 2  # generic symbolic rank

result = {
    "status": "PASS",
    "helicity_kernel": [[str(v) for v in row] for row in M.tolist()],
    "exterior_square": str(det_transport),
    "norm_squared": str(norm),
    "reduced_density_determinant": f"({det_transport})^2/({norm})^2",
    "product_locus": f"{det_transport}=0",
    "generic_spectator_extended_rank": M_ext.rank(),
    "conclusion": (
        "For the source-defined pure two-photon helicity state, the "
        "coefficient-kernel exterior square is nonzero exactly off the product "
        "locus. Positive conjugate doubling turns its square into the reduced "
        "density determinant, hence into the support of nonzero connected "
        "helicity information."
    ),
}
out = Path(__file__).parents[1] / "results" / "photon_connected_transport_determinant.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
