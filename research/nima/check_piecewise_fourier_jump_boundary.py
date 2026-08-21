"""Exact coefficient-vector audit for one internal Fourier-support jump."""

from __future__ import annotations

import json
from pathlib import Path


def add(*vectors: tuple[int, int]) -> tuple[int, int]:
    return tuple(sum(v[i] for v in vectors) for i in range(2))  # type: ignore[return-value]


def evaluate(vector: tuple[int, int], a: int, b: int) -> int:
    return vector[0] * a + vector[1] * b


def main() -> None:
    # Density a on [0,c] and b on [c,Lambda].
    residues = {
        "q=0": (-1, 0),       # -a
        "q=-c": (1, -1),     # a-b
        "q=-Lambda": (0, 1), # b
    }
    total = add(*residues.values())

    assert total == (0, 0)
    assert evaluate(residues["q=-c"], 1, 1) == 0
    assert evaluate(residues["q=-c"], 3, 2) == 1

    result = {
        "schema": "marici.piecewise-fourier-jump-boundary.v1",
        "density": "a*1_[0,c] + b*1_[c,Lambda]",
        "pushforward": (
            "-a*log(q) + (a-b)*log(q+c) + b*log(q+Lambda)"
        ),
        "oriented_residue_vectors_in_(a,b)": {
            key: list(value) for key, value in residues.items()
        },
        "total_residue_vector": list(total),
        "internal_residue": "a-b",
        "internal_residue_when_a_equals_b": 0,
        "conclusion": (
            "The internal logarithmic class is exactly the coefficient jump. "
            "It cancels under subdivision when adjacent densities agree."
        ),
    }
    out = Path(__file__).with_name("results") / "piecewise-fourier-jump-boundary.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
