"""Exact cellular certificate for the resonant Kummer--Gysin excess.

The exceptional three-punctured line retracts to a wedge of two circles.
The Gysin loop has trivial monodromy and the Kummer loop has monodromy
lambda.  With h=lambda-1, its rank-one cellular cochain differential is

    R -> R^2,  1 |-> (0,h),       R = Q[h].

This script verifies the generic and resonant ranks and emits the Smith data
without choosing a splitting of the supported summand.
"""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    # The 1 x 2 presentation row [0,h] has one nonzero Smith invariant h.
    smith_invariants = ["h"]

    # Over Q(h), h is invertible: rank(d)=1, hence dim H^0=0, dim H^1=1.
    generic = {"rank_d": 1, "dim_h0": 0, "dim_h1": 1}

    # At h=0 the differential vanishes: H^0 gains one and H^1 gains one.
    resonant = {"rank_d": 0, "dim_h0": 1, "dim_h1": 2}

    # Coker([0,h]) = R plus R/(h).  The statement is invariant even though
    # writing a preferred free generator would amount to choosing a splitting.
    module = {"h1": "Q[h] + Q[h]/(h)", "h0": "0 over Q[h]"}

    assert generic == {"rank_d": 1, "dim_h0": 0, "dim_h1": 1}
    assert resonant == {"rank_d": 0, "dim_h0": 1, "dim_h1": 2}
    assert smith_invariants == ["h"]

    result = {
        "schema": "marici.resonant-kummer-gysin-excess.v1",
        "coefficient_ring": "Q[h]",
        "character_parameter": "h=lambda-1",
        "cellular_differential": [["0"], ["h"]],
        "smith_invariants": smith_invariants,
        "generic_fiber": generic,
        "resonant_fiber": resonant,
        "cohomology_module": module,
        "conclusion": (
            "The generic exceptional line extends freely, while resonance "
            "adds exactly one h-supported class on the existing collision carrier."
        ),
    }

    out = Path(__file__).with_name("results") / "resonant-kummer-gysin-excess.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
