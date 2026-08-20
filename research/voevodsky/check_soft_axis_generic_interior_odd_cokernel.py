"""Generic-point fibers of the orbit-completed odd exact cokernel."""

import importlib.util
from pathlib import Path

P = 2305843009213693951
path = Path(__file__).with_name("check_soft_axis_deck_orbit_completion.py")
spec = importlib.util.spec_from_file_location("deck", path)
deck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(deck)


def ff(x):
    return x.numerator * pow(x.denominator, P - 2, P) % P


def rank(columns):
    basis = {}
    for column in columns:
        vector = dict(column)
        while vector:
            pivot = min(vector)
            if pivot in basis:
                factor = vector[pivot]
                for row, value in basis[pivot].items():
                    vector[row] = (vector.get(row, 0) - factor * value) % P
                    if not vector[row]:
                        vector.pop(row, None)
            else:
                inverse = pow(vector[pivot], P - 2, P)
                basis[pivot] = {row: value * inverse % P for row, value in vector.items()}
                break
    return len(basis)


def evaluate(poly, b_value):
    out = {}
    for (u_degree, a_degree, b_degree), coefficient in poly.items():
        key = (u_degree, a_degree)
        out[key] = (out.get(key, 0) + ff(coefficient) * pow(b_value % P, b_degree, P)) % P
    return {m: c for m, c in out.items() if c}


def census(cutoff, b_value, character=-1):
    start = 1 if character == -1 else 0
    special_rows = [(0, a) for a in range(start, cutoff + 1, 2)]
    dual_rows = [(u, a) for u in (0, 1) for _, a in special_rows]
    spos = {m: i for i, m in enumerate(special_rows)}
    dpos = {m: i for i, m in enumerate(dual_rows)}
    special_columns = []
    dual_columns = []

    for sector in ((1, 1), (1, 0), (0, 1), (0, 0)):
        for total in range(cutoff + 1):
            for a_degree in range(total + 1):
                f = deck.mul(deck.power(deck.a, a_degree), deck.power(deck.b, total - a_degree))
                for plus in (False, True):
                    for is_q in (False, True):
                        p = evaluate(deck.exact(sector, f, is_q, plus), b_value)
                        if not p or max(a for _, a in p) > cutoff:
                            continue
                        special = {spos[m]: c for m, c in p.items() if m[0] == 0 and m in spos}
                        dual = {dpos[m]: c for m, c in p.items() if m in dpos}
                        up = {(1, a): c for (u, a), c in p.items() if u == 0 and (1, a) in dpos}
                        udual = {dpos[m]: c for m, c in up.items()}
                        if special:
                            special_columns.append(special)
                        if dual:
                            dual_columns.append(dual)
                        if udual:
                            dual_columns.append(udual)

    special_cokernel = len(special_rows) - rank(special_columns)
    dual_cokernel = len(dual_rows) - rank(dual_columns)
    return special_cokernel, dual_cokernel


for b_value in (0, 2, 3):
    results = []
    for cutoff in (12, 16, 20, 24):
        special, dual = census(cutoff, b_value)
        results.append((special, dual))
        print(f"b={b_value},D={cutoff}: special_odd={special},dual_odd={dual}")
    assert len(set(results)) == 1
    print(f"b={b_value}: stable={results[0]}")

for b_value in (0, 2, 3):
    results = []
    for cutoff in (12, 16, 20, 24):
        special, dual = census(cutoff, b_value, character=1)
        results.append((special, dual))
        print(f"even b={b_value},D={cutoff}: special_even={special},dual_even={dual}")
    assert len(set(results)) == 1
    assert results[0] == (2, 4)
    print(f"even b={b_value}: stable={results[0]}")
