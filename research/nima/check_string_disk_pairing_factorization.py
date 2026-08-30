"""Count rank-one coefficient/Betti character factorizations of disk readout."""

import json
from pathlib import Path


def character_values(n):
    # A rank-one rational character is fixed by r,s in {+1,-1},
    # with r^n=1 and srs=r^-1.
    out = []
    for r in (-1, 1):
        for s in (-1, 1):
            if r**n == 1:
                out.append((r, s))
    return out


rows = []
checks = 0
for n in range(3, 17):
    chars = character_values(n)
    target = (1, (-1) ** n)
    factors = []
    for alpha in chars:
        for beta in chars:
            checks += 1
            if (alpha[0] * beta[0], alpha[1] * beta[1]) == target:
                factors.append({"coefficient": alpha, "betti": beta})
    assert len(factors) == len(chars)
    rows.append({
        "arity": n,
        "combined_character": target,
        "character_group_order": len(chars),
        "factorization_count": len(factors),
        "factorizations": factors,
    })

result = {
    "schema": "marici.string.disk_pairing_factorization.v1",
    "audited_arities": [r["arity"] for r in rows],
    "rows": rows,
    "checks": checks,
    "passed": True,
    "verdict": "combined disk character does not determine coefficient and Betti characters",
}
out = Path(__file__).with_name("results") / "string-disk-pairing-factorization.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"checks": checks, "counts": [r["factorization_count"] for r in rows], "passed": True}))
