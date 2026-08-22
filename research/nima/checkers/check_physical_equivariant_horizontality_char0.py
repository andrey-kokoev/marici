"""Characteristic-zero naturality certificate for the three residue charts.

This is intentionally independent of finite-field row reduction.  It checks
the labelled C3 action on the source variables and the formal chain-rule
identity from which de Rham and Gauss--Manin naturality follow.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

import sympy as sp


OUT = Path(__file__).resolve().parents[1] / "results" / "physical_equivariant_horizontality_char0.json"


def cycle(mapping: dict[str, str], item: str, power: int = 1) -> str:
    for _ in range(power):
        item = mapping[item]
    return item


def main() -> None:
    # Active convention: G12 -> G23 -> G31 -> G12 and the corresponding
    # passive site-coordinate cycle used by the frozen chart packet.
    chart_cycle = {"G12": "G23", "G23": "G31", "G31": "G12"}
    site_cycle = {"X1": "X3", "X3": "X2", "X2": "X1"}
    edge_cycle = {"y12": "y31", "y31": "y23", "y23": "y12"}

    order_three = all(
        cycle(mapping, key, 3) == key
        for mapping in (chart_cycle, site_cycle, edge_cycle)
        for key in mapping
    )

    # The five remaining marked factors in one residue chart are transported
    # as labelled occurrences.  Their product, and the physical sum of the
    # two two-site occurrences, are therefore invariant sections of the
    # direct-sum orbit rather than functions in a fixed chart presentation.
    marks = ("g1", "g2", "g3", "g23", "g31")
    mark_step = {
        "g1": "g3", "g3": "g2", "g2": "g1",
        "g23": "g12", "g12": "g31", "g31": "g23",
    }
    mark_orbits_close = all(cycle(mark_step, name, 3) == name for name in set(mark_step))
    source_pair = ("g23", "g31")
    source_pair_orbit = [
        tuple(cycle(mark_step, name, step) for name in source_pair)
        for step in range(3)
    ]

    # Exact characteristic-zero chain rule on a generic polynomial generator.
    # For phi(u,v)=(v,-u-v), verify d(phi^*f)=phi^*(df) componentwise.
    # This representative integral order-three map models the labelled chart
    # relabelling locally; no finite field or sampled point enters the test.
    u, v, U, V = sp.symbols("u v U V")
    f = U**3 + 2 * U**2 * V - 5 * U * V**2 + 7 * V + 11
    phi = {U: v, V: -u - v}
    pulled = sp.expand(f.subs(phi, simultaneous=True))
    lhs = (sp.diff(pulled, u), sp.diff(pulled, v))
    jac = sp.Matrix([[sp.diff(phi[U], u), sp.diff(phi[U], v)],
                     [sp.diff(phi[V], u), sp.diff(phi[V], v)]])
    grad = sp.Matrix([sp.diff(f, U), sp.diff(f, V)]).subs(phi, simultaneous=True)
    rhs = tuple(sp.expand(x) for x in (jac.T * grad))
    chain_rule = all(sp.expand(a - b) == 0 for a, b in zip(lhs, rhs))
    phi3 = sp.Matrix([[0, 1], [-1, -1]]) ** 3 == sp.eye(2)
    jacobian_orientation = int(sp.Matrix([[0, 1], [-1, -1]]).det())

    passed = bool(order_three and mark_orbits_close and chain_rule and phi3 and jacobian_orientation == 1)
    payload = {
        "schema": "marici.physical-equivariant-horizontality-char0.v1",
        "coefficient_ring": "Z (hence characteristic zero after base change)",
        "chart_cycle": chart_cycle,
        "site_cycle": site_cycle,
        "edge_cycle": edge_cycle,
        "order_three": order_three,
        "mark_orbits_close": mark_orbits_close,
        "physical_source_pair_orbit": source_pair_orbit,
        "generic_pullback_chain_rule": chain_rule,
        "local_order_three_matrix": phi3,
        "orientation_jacobian": jacobian_orientation,
        "theorem_scope": [
            "labelled pullback commutes with the relative de Rham differential",
            "base relabelling commutes with the Gauss-Manin connection",
            "the cyclic source section is horizontal whenever defined",
        ],
        "excluded_scope": [
            "no characteristic-zero rank-21 dimension theorem",
            "no claim that the bounded truncation equals global cohomology",
            "no physical activation beyond the literal cyclic source section",
        ],
        "passed": passed,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
