"""Exact classification checks for linear rows on a rank-one terminal graph."""

from fractions import Fraction
import json


def terminal(F, c):
    return (F * c, c)


def row(alpha, beta, state):
    G0, c = state
    return alpha * G0 + beta * c


F_regular = Fraction(3)
F_zero = Fraction(0)
c = Fraction(1)

regular = terminal(F_regular, c)
zero_state = terminal(F_zero, c)

checks = {
    "terminal_graph_regular": regular == (3, 1),
    "terminal_graph_zero": zero_state == (0, 1),
    "evans_row_vanishes_at_zero": row(1, 0, zero_state) == 0,
    "faithful_constant_port_detects_zero_state": row(0, 1, zero_state) == 1,
    "graph_syzygy_regular": row(1, -F_regular, regular) == 0,
    "graph_syzygy_zero": row(1, -F_zero, zero_state) == 0,
    "evans_multiple_adds_no_force": row(7, 0, zero_state) == 0,
    "independent_row_excludes_nonzero_amplitude": row(2, 5, zero_state) != 0,
}

result = {
    "schema": "marici.grothendieck.rank-one-terminal-row-classification.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "zero_state": [str(x) for x in zero_state],
}

print(json.dumps(result, indent=2, sort_keys=True))
