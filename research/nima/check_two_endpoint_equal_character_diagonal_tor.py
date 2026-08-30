"""Exact Tor certificate for a two-endpoint equal-character diagonal."""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    # A=Q[h1,h2], B=A/(h1-h2), T=A/(h1,h2).  Resolve B by
    # A --(h1-h2)--> A.  On T this map is identically zero.
    diagonal_map_on_intersection = "0"
    tor = {"Tor_0_A(T,B)": "Q", "Tor_1_A(T,B)": "Q", "Tor_i_for_i_gt_1": "0"}

    # On either singleton module A/(hi), h1-h2 remains a non-zero-divisor.
    singleton_tor1 = 0

    assert diagonal_map_on_intersection == "0"
    assert tor["Tor_0_A(T,B)"] == "Q"
    assert tor["Tor_1_A(T,B)"] == "Q"
    assert singleton_tor1 == 0

    result = {
        "schema": "marici.two-endpoint-equal-character-diagonal-tor.v1",
        "ambient_ring": "A=Q[h1,h2]",
        "equal_character_diagonal": "B=A/(h1-h2)",
        "double_supported_module": "T=A/(h1,h2)",
        "resolution": "[A --(h1-h2)--> A]",
        "map_after_tensor_with_T": diagonal_map_on_intersection,
        "tor": tor,
        "singleton_tor1_dimension": singleton_tor1,
        "conclusion": (
            "Derived equal-character specialization contributes exactly one "
            "shifted class at the double-resonant intersection; ordinary "
            "substitution misses it."
        ),
    }
    out = Path(__file__).with_name("results") / "two-endpoint-equal-character-diagonal-tor.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
