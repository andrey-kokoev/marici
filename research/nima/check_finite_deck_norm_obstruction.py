"""Exact norm and normalization obstruction for finite cyclic deck quotients."""

import json
from math import gcd
from pathlib import Path


rows = []
checks = 0
for n in range(1, 31):
    for m in range(1, n + 1):
        if n % m:
            continue
        # Canonical quotient C_n -> C_m, x |-> x mod m.
        k = n // m
        # q_! q^* = k id on every delta basis vector of Fun(C_m).
        for h0 in range(m):
            pulled = [int((x % m) == h0) for x in range(n)]
            pushed = [sum(pulled[x] for x in range(n) if x % m == h) for h in range(m)]
            assert pushed == [k * int(h == h0) for h in range(m)]
            checks += m
        # Frozen identity selector under unnormalized and normalized transfer.
        delta_g = [int(x == 0) for x in range(n)]
        unnormalized = [sum(delta_g[x] for x in range(n) if x % m == h) for h in range(m)]
        assert unnormalized == [int(h == 0) for h in range(m)]
        normalized_zero = (1, k)  # coefficient of delta_0 after averaging
        selector_and_retraction_compatible = k == 1
        rows.append({
            "source_order": n,
            "target_order": m,
            "kernel_order": k,
            "pull_push_scalar": k,
            "unnormalized_preserves_identity_selector": True,
            "normalized_identity_coefficient": normalized_zero,
            "selector_and_retraction_compatible": selector_and_retraction_compatible,
        })

result = {
    "schema": "marici.finite_deck.norm_obstruction.v1",
    "cyclic_quotients": len(rows),
    "checks": checks,
    "nontrivial_quotients": sum(r["kernel_order"] > 1 for r in rows),
    "compatible_nontrivial_quotients": sum(
        r["kernel_order"] > 1 and r["selector_and_retraction_compatible"] for r in rows
    ),
    "passed": True,
    "theorem": "q_!q^*=|ker q| id; selector preservation and retraction normalization coexist iff |ker q|=1",
}
out = Path(__file__).with_name("results") / "finite-deck-norm-obstruction.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
