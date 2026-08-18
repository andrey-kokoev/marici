"""Test whether the Euler homotopy is recoverable from target image columns."""

import importlib.util
from pathlib import Path

P = 2305843009213693951
source = Path(__file__).with_name("check_soft_axis_deck_orbit_completion.py")
spec = importlib.util.spec_from_file_location("deck", source)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)


def finite(x):
    return x.numerator * pow(x.denominator, P - 2, P) % P


def rank(columns):
    basis = {}
    for column in columns:
        vector = {k: finite(v) for k, v in column.items() if v}
        while vector:
            pivot = min(vector)
            if pivot not in basis:
                inv = pow(vector[pivot], P - 2, P)
                basis[pivot] = {k: v * inv % P for k, v in vector.items()}
                break
            factor = vector[pivot]
            for k, v in basis[pivot].items():
                vector[k] = (vector.get(k, 0) - factor * v) % P
                if not vector[k]:
                    vector.pop(k, None)
    return len(basis)


def audit(cutoff):
    target_columns = []
    graph_columns = []
    for sector in ((1, 1), (1, 0), (0, 1), (0, 0)):
        sa, sb = sector
        ea, eb = 2 - sa, 2 - sb
        base = d.mul(d.power(d.L1, ea), d.power(d.L2_minus, eb))
        for total in range(cutoff + 1):
            for ai in range(total + 1):
                f = d.mul(d.power(d.a, ai), d.power(d.b, total - ai))
                for is_q in (False, True):
                    exact = d.exact(sector, f, is_q, False)
                    h_a = (d.scale(d.mul(d.power(d.a, 2), f, base), d.Q(1, 2))
                           if is_q else {})
                    support = [m[1] + m[2] for m in (*exact.keys(), *h_a.keys())]
                    if not support or max(support) > cutoff:
                        continue
                    target = {(0, *m): c for m, c in exact.items()}
                    graph = dict(target)
                    graph.update({(1, *m): c for m, c in h_a.items()})
                    target_columns.append(target)
                    graph_columns.append(graph)
    rd = rank(target_columns)
    rg = rank(graph_columns)
    assert rg > rd
    print(f"D={cutoff}: rank(d)={rd}, rank(d,H)={rg}, provenance_excess={rg-rd}")
    return rg - rd


excesses = [audit(cutoff) for cutoff in (12, 16, 20, 24)]
assert all(x > 0 for x in excesses)
print("verdict: H is not reconstructible from the target image matrix")
print("required next model: retain labelled source columns and gradient rows")
