from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FIXTURE = ROOT / "research/nima/six-point-nmhv-triangulation-fixture.json"
RESULT = ROOT / "research/nima/results/six-point-nmhv-triangulation-fixture.json"


def boundary(simplex: list[int]) -> Counter[tuple[int, ...]]:
    out: Counter[tuple[int, ...]] = Counter()
    for i in range(len(simplex)):
        out[tuple(simplex[:i] + simplex[i + 1 :])] += -1 if i % 2 else 1
    return out


def chain_boundary(cells: list[list[int]]) -> Counter[tuple[int, ...]]:
    total: Counter[tuple[int, ...]] = Counter()
    for cell in cells:
        total.update(boundary(cell))
    return Counter({face: coefficient for face, coefficient in total.items() if coefficient})


def internal_faces(cells: list[list[int]]) -> list[tuple[int, ...]]:
    occurrences: dict[tuple[int, ...], list[int]] = {}
    for cell in cells:
        for face, sign in boundary(cell).items():
            occurrences.setdefault(face, []).append(sign)
    return sorted(face for face, signs in occurrences.items() if len(signs) == 2 and sum(signs) == 0)


def main() -> None:
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    left = fixture["triangulations"]["left"]
    right = fixture["triangulations"]["right"]
    left_boundary = chain_boundary(left)
    right_boundary = chain_boundary(right)
    expected_left = sorted(map(tuple, fixture["expected_internal_facets"]["left"]))
    expected_right = sorted(map(tuple, fixture["expected_internal_facets"]["right"]))

    checks = {
        "left_internal_facets_cancel": internal_faces(left) == expected_left,
        "right_internal_facets_cancel": internal_faces(right) == expected_right,
        "triangulation_boundaries_equal": left_boundary == right_boundary,
    }

    mutated = [cell[:] for cell in left]
    mutation_boundary = chain_boundary(mutated)
    mutation_boundary.subtract({face: 2 * coefficient for face, coefficient in boundary(mutated[0]).items()})
    mutation_boundary = Counter({f: c for f, c in mutation_boundary.items() if c})
    mutation_residual = mutation_boundary - right_boundary
    reverse_residual = right_boundary - mutation_boundary
    mutation_nonzero = bool(mutation_residual or reverse_residual)
    checks["orientation_flip_has_nonzero_residual"] = mutation_nonzero

    result = {
        "schema": "marici.nima.six_point_nmhv_triangulation_fixture.result.v1",
        "status": "passed" if all(checks.values()) else "failed",
        "checks": checks,
        "left_boundary": {"".join(map(str, k)): v for k, v in sorted(left_boundary.items())},
        "right_boundary": {"".join(map(str, k)): v for k, v in sorted(right_boundary.items())},
        "left_internal_facets": ["".join(map(str, f)) for f in internal_faces(left)],
        "right_internal_facets": ["".join(map(str, f)) for f in internal_faces(right)],
        "orientation_mutation_residual_nonzero": mutation_nonzero,
        "claim_boundary": "This checks the authored oriented simplex chains only. It does not verify canonical forms, the super five-bracket identity, source normalization, or physical boundary interpretation."
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if result["status"] != "passed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
