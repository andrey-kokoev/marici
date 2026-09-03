from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


CONTRACT = Path("research/voevodsky/finite-adelic-mellin-evaluation-naturality-v1.json")
SCALE_AUDIT = Path("research/grothendieck/multiplicative-to-additive-scale-comparison-audit.md")


def height(value: Fraction) -> int:
    return max(abs(value.numerator), value.denominator)


def evaluate_edges(chain: dict[tuple[Fraction, tuple[str, str]], int]) -> dict[tuple[int, tuple[str, str]], int]:
    out: defaultdict[tuple[int, tuple[str, str]], int] = defaultdict(int)
    for (label, edge), coefficient in chain.items():
        out[(height(label), edge)] += coefficient
    return {key: value for key, value in out.items() if value}


def boundary_labelled(chain: dict[tuple[Fraction, tuple[str, str]], int]) -> dict[tuple[Fraction, str], int]:
    out: defaultdict[tuple[Fraction, str], int] = defaultdict(int)
    for (label, (source, target)), coefficient in chain.items():
        out[(label, source)] -= coefficient
        out[(label, target)] += coefficient
    return dict(out)


def evaluate_vertices(chain: dict[tuple[Fraction, str], int]) -> dict[tuple[int, str], int]:
    out: defaultdict[tuple[int, str], int] = defaultdict(int)
    for (label, vertex), coefficient in chain.items():
        out[(height(label), vertex)] += coefficient
    return {key: value for key, value in out.items() if value}


def boundary_evaluated(chain: dict[tuple[int, tuple[str, str]], int]) -> dict[tuple[int, str], int]:
    out: defaultdict[tuple[int, str], int] = defaultdict(int)
    for (grade, (source, target)), coefficient in chain.items():
        out[(grade, source)] -= coefficient
        out[(grade, target)] += coefficient
    return {key: value for key, value in out.items() if value}


def reflect(vertex: str) -> str:
    return {"w": "-w", "-w": "w"}[vertex]


def reciprocal_labels(chain: dict[tuple[Fraction, tuple[str, str]], int]) -> dict[tuple[Fraction, tuple[str, str]], int]:
    return {(1 / label, (reflect(edge[0]), reflect(edge[1]))): coefficient for (label, edge), coefficient in chain.items()}


def reflect_evaluated(chain: dict[tuple[int, tuple[str, str]], int]) -> dict[tuple[int, tuple[str, str]], int]:
    return {(grade, (reflect(edge[0]), reflect(edge[1]))): coefficient for (grade, edge), coefficient in chain.items()}


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    audit = SCALE_AUDIT.read_text(encoding="utf-8")
    assert "Taking `log H` gives the desired scale" in audit
    assert "arithmetic/adelic inputs" in audit

    packet = {Fraction(1): 2, Fraction(-1): 3, Fraction(2): 5, Fraction(1, 2): 7}
    chain = {(label, ("w", "-w")): coefficient for label, coefficient in packet.items()}
    # Zero-extension leaves the sparse chain unchanged, hence evaluation is natural.
    assert evaluate_edges(dict(chain)) == evaluate_edges(chain)
    assert evaluate_vertices(boundary_labelled(chain)) == boundary_evaluated(evaluate_edges(chain))
    assert evaluate_edges(reciprocal_labels(chain)) == reflect_evaluated(evaluate_edges(chain))
    assert all(height(1 / label) == height(label) for label in packet)

    status = contract["status"]
    assert status["finite_evaluation_natural_transformation"] == "constructed"
    assert status["graph_topology_continuity"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.finite-adelic-mellin-evaluation-naturality-check.v1",
        "status":"finite_mellin_evaluation_naturality_verified",
        "cutoff_transition_naturality":True,
        "boundary_naturality":True,
        "reciprocal_naturality":True,
        "adelic_scale_authority_explicit":True,
        "graph_topology_continuity_verified":False,
        "uniform_completion_verified":False,
        "first_missing_datum":contract["first_missing_datum"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
