"""Audit an R-linear finite truncation of the labelled total complex."""

from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path

dependency = Path(__file__).parents[1] / "voevodsky" / "check_soft_axis_deck_orbit_completion.py"
spec = importlib.util.spec_from_file_location("deck", dependency)
deck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(deck)

SECTORS = ((1, 1), (1, 0), (0, 1), (0, 0))
CUTOFFS = (12, 16, 20, 24)


def monomial(ad, bd, ud=0):
    return deck.mul(deck.power(deck.u, ud), deck.mul(deck.power(deck.a, ad), deck.power(deck.b, bd)))


def support_within(poly, cutoff):
    return all(ud < 2 and ad + bd <= cutoff for ud, ad, bd in poly)


def dot(left, right):
    return deck.add(*(deck.mul(x, y) for x, y in zip(left, right)))


GRADIENT = tuple(deck.derivative(deck.K, coordinate) for coordinate in (1, 2, 0))
EULER = (deck.scale(deck.a, Q(1, 4)), {}, deck.scale(deck.u, Q(1, 2)))
assert dot(GRADIENT, EULER) == deck.K


def labelled_map(f, sa, sb, conjugate, label):
    ea, eb = 2 - sa, 2 - sb
    l2 = deck.L2_plus if conjugate else deck.L2_minus
    base = deck.mul(deck.power(deck.L1, ea), deck.power(l2, eb))
    m = deck.mul(f, base)
    if label == "p":
        coefficient = deck.scale(deck.mul(deck.derivative(f, 2), base), -1)
        if sa:
            coefficient = deck.add(
                coefficient,
                deck.scale(
                    deck.mul(f, deck.power(deck.L1, ea - 1), deck.power(l2, eb)),
                    sa,
                ),
            )
        homotopy = ({}, deck.scale(m, Q(3, 2)), {})
    else:
        coefficient = deck.mul(deck.derivative(f, 1), base)
        if sb:
            coefficient = deck.add(
                coefficient,
                deck.scale(
                    deck.mul(f, deck.power(deck.L1, ea), deck.power(l2, eb - 1)),
                    -sb,
                ),
            )
        homotopy = (deck.scale(m, Q(-3, 2)), {}, {})
    lift = tuple(deck.add(homotopy[i], deck.mul(coefficient, EULER[i])) for i in range(3))
    scalar = deck.add(deck.mul(coefficient, deck.K), dot(GRADIENT, homotopy))
    assert dot(GRADIENT, lift) == scalar
    return scalar, lift


def audit(cutoff):
    source_generators = 0
    principal_generators = 0
    chain_checks = 0
    linearity_checks = 0

    for sa, sb in SECTORS:
        ea, eb = 2 - sa, 2 - sb
        source_cutoff = cutoff - 3 - ea - eb
        for conjugate in (False, True):
            for label in ("p", "q"):
                for total in range(source_cutoff + 1):
                    for ad in range(total + 1):
                        f = monomial(ad, total - ad)
                        scalar, lift = labelled_map(f, sa, sb, conjugate, label)
                        scalar_u, lift_u = labelled_map(deck.mul(deck.u, f), sa, sb, conjugate, label)
                        assert scalar_u == deck.mul(deck.u, scalar)
                        assert lift_u == tuple(deck.mul(deck.u, part) for part in lift)
                        assert support_within(scalar, cutoff)
                        assert all(support_within(part, cutoff - 3) for part in lift)
                        assert deck.add(scalar, deck.scale(dot(GRADIENT, lift), -1)) == {}
                        source_generators += 1
                        chain_checks += 1
                        linearity_checks += 1

    principal_cutoff = cutoff - 4
    for total in range(principal_cutoff + 1):
        for ad in range(total + 1):
            p = monomial(ad, total - ad)
            scalar = deck.mul(deck.K, p)
            lift = tuple(deck.mul(p, part) for part in EULER)
            assert support_within(scalar, cutoff)
            assert all(support_within(part, cutoff - 3) for part in lift)
            assert deck.add(scalar, deck.scale(dot(GRADIENT, lift), -1)) == {}
            assert deck.mul(deck.u, scalar) == deck.mul(deck.K, deck.mul(deck.u, p))
            principal_generators += 1
            chain_checks += 1
            linearity_checks += 1

    return {
        "D": cutoff,
        "A_rank_over_R": source_generators,
        "P_rank_over_R": principal_generators,
        "B_cutoff": cutoff,
        "G_cutoff": cutoff - 3,
        "chain_checks": chain_checks,
        "u_linearity_checks": linearity_checks,
    }


def main():
    results = [audit(cutoff) for cutoff in CUTOFFS]
    for result in results:
        print(
            f"D={result['D']}: rank_R(A)={result['A_rank_over_R']} "
            f"rank_R(P)={result['P_rank_over_R']} D0D-1={result['chain_checks']} "
            f"u-linear={result['u_linearity_checks']}"
        )
    print(json.dumps({
        "schema": "marici.benincasa.labelled_total_truncation.v1",
        "ring": "Q[u]/(u^2)",
        "generator_cutoffs": "B:D,G:D-3,P:D-4,A(sector):D-3-ea-eb",
        "results": results,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
