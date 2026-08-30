import itertools
import json
from pathlib import Path

import sympy as sp


I = sp.I
R = I
double_braid = sp.simplify(R * R)


def omega(a, b, c):
    return -1 if a == b == c == 1 else 1


def cocycle_residual(a, b, c, d):
    left = omega(b, c, d) * omega(a, (b + c) % 2, d) * omega(a, b, c)
    right = omega((a + b) % 2, c, d) * omega(a, b, (c + d) % 2)
    return left - right


cocycle_checks = [cocycle_residual(*bits) == 0 for bits in itertools.product([0, 1], repeat=4)]

# A normalized U(1)-valued 2-cochain on Z2 has only beta(1,1)=u free.
# Its coboundary at (1,1,1) is always one, so omega(1,1,1)=-1 is nontrivial.
u = sp.symbols("u", nonzero=True)
delta_beta_111 = sp.simplify(u * 1 / (1 * u))

checks = {
    "semion_braid_is_unitary": sp.simplify(sp.conjugate(R) * R - 1) == 0,
    "semion_double_braid_is_minus_one": double_braid == -1,
    "symmetric_law_fails": double_braid != 1,
    "z2_associator_is_normalized": all(
        omega(a, b, c) == 1 if 0 in (a, b, c) else True
        for a, b, c in itertools.product([0, 1], repeat=3)
    ),
    "z2_associator_obeys_pentagon": all(cocycle_checks),
    "normalized_coboundary_at_111_is_one": delta_beta_111 == 1,
    "associator_is_not_a_normalized_coboundary": omega(1, 1, 1) != delta_beta_111,
}

result = {
    "schema": "marici.aspect.bivariant-network-semion-falsifier.v1",
    "status": "falsified_as_stated" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "falsified_clause": "Every physical presentation lies in a symmetric monoidal double category.",
    "repair": "Use a dagger braided/ribbon higher equipment; impose symmetry only on sectors with trivial double braiding.",
}

out = Path(__file__).parents[1] / "results" / "bivariant_network_semion_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "falsified_as_stated" else 1)
