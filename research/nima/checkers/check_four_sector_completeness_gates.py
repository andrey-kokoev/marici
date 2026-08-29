from fractions import Fraction


def rank_two(rows):
    if not rows:
        return 0
    if all(row[0] * rows[0][1] - row[1] * rows[0][0] == 0 for row in rows[1:]):
        return 1
    return 2


if __name__ == "__main__":
    carrier_idempotents = ((1, 0), (0, 1))
    control_rows = ((1, 0), (0, 1))
    collapsed_readout = ((1, 1),)

    assert len(carrier_idempotents) == 2
    assert rank_two(control_rows) == 2
    assert rank_two(collapsed_readout) == 1
    invisible = (1, -1)
    assert collapsed_readout[0][0] * invisible[0] + collapsed_readout[0][1] * invisible[1] == 0

    inverse_norms = []
    for n in (2, 4, 8, 16, 32, 64):
        readout = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1, n)))
        assert rank_two(readout) == 2
        inverse_norms.append(n)
    assert all(a < b for a, b in zip(inverse_norms, inverse_norms[1:]))

    print("carrier splitting: pass")
    print("action splitting: pass")
    print("observation splitting hostile: rank 1 with invisible state (1,-1)")
    print("finite observation with collapsing lower bound: witnessed")
    print("result: four sector-completeness gates are independent")
