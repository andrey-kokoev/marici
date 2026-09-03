from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/infinitesimal-dirichlet-conjecture-audit-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    h, s, t, u = sp.symbols("h s t u", positive=True, real=True)
    finite_multiplier = sp.exp(-t * u**2) * (1 - sp.exp(-h * u**2))
    infinitesimal_multiplier = u**2 * sp.exp(-(t + s) * u**2)
    assert sp.simplify(finite_multiplier - sp.integrate(infinitesimal_multiplier, (s, 0, h))) == 0
    assert sp.simplify(sp.limit(finite_multiplier / h, h, 0, dir="+") - u**2 * sp.exp(-t * u**2)) == 0

    # Mesh composition is additivity of adjacent integration intervals.
    h1, h2 = sp.symbols("h1 h2", positive=True, real=True)
    total = sp.exp(-t * u**2) * (1 - sp.exp(-(h1 + h2) * u**2))
    pieces = sp.exp(-t * u**2) * (1 - sp.exp(-h1 * u**2)) + sp.exp(-(t + h1) * u**2) * (1 - sp.exp(-h2 * u**2))
    assert sp.simplify(total - pieces) == 0

    result = {
        "schema":"marici.voevodsky.infinitesimal-dirichlet-conjecture-audit-check.v1",
        "status":"finite_infinitesimal_equivalence_identity_verified",
        "mesh_integral_identity":True,
        "small_mesh_derivative":True,
        "mesh_composition":True,
        "explicit_source_R_t":False,
        "conjecture_explanatory_content":"rejected",
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
