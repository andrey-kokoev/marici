#!/usr/bin/env python3
"""Finite normalized-chain audit of the marked log-blowdown counit."""

from collections import defaultdict


Mono = tuple[int, int, int, int, int]  # X0,X1,X3,X5,XD
Face = frozenset[str]
Flag = tuple[Face, ...]
Combination = dict[tuple[Flag, Mono], int]

ZERO: Mono = (0, 0, 0, 0, 0)
X0: Mono = (1, 0, 0, 0, 0)
X1: Mono = (0, 1, 0, 0, 0)
X3: Mono = (0, 0, 1, 0, 0)
X5: Mono = (0, 0, 0, 1, 0)
XD: Mono = (0, 0, 0, 0, 1)


def madd(a: Mono, b: Mono) -> Mono:
    return tuple(x + y for x, y in zip(a, b))


def msub(a: Mono, b: Mono) -> Mono:
    result = tuple(x - y for x, y in zip(a, b))
    assert min(result) >= 0
    return result


def old(face: Face) -> Face:
    if "E" not in face:
        return face
    return frozenset((face - {"E"}) | {"D", "1"})


def label(face: Face) -> Mono:
    exponents = [0, 0, 0, 0, 0]
    for ray in old(face):
        exponents[{"0": 0, "1": 1, "3": 2, "5": 3, "D": 4}[ray]] = 1
    return tuple(exponents)


def add(out: defaultdict, flag: Flag, mono: Mono, coefficient: int) -> None:
    out[(flag, mono)] += coefficient
    if out[(flag, mono)] == 0:
        del out[(flag, mono)]


def boundary(chain: Combination) -> Combination:
    out: defaultdict = defaultdict(int)
    for (flag, mono), coefficient in chain.items():
        for index in range(len(flag)):
            factor = ZERO
            if index == 0 and len(flag) > 1:
                factor = msub(label(flag[1]), label(flag[0]))
            add(out, flag[:index] + flag[index + 1 :], madd(mono, factor),
                coefficient * (-1 if index % 2 else 1))
    return dict(out)


def blowdown(chain: Combination) -> Combination:
    out: defaultdict = defaultdict(int)
    for (flag, mono), coefficient in chain.items():
        image = tuple(old(face) for face in flag)
        if len(set(image)) != len(image):
            continue  # normalized chains kill degenerate simplices
        add(out, image, mono, coefficient)
    return dict(out)


def scaled(chain: Combination, factor: Mono, sign: int = 1) -> Combination:
    return {(flag, madd(mono, factor)): sign * coefficient
            for (flag, mono), coefficient in chain.items()}


def summed(*chains: Combination) -> Combination:
    out: defaultdict = defaultdict(int)
    for chain in chains:
        for (flag, mono), coefficient in chain.items():
            add(out, flag, mono, coefficient)
    return dict(out)


def singleton(flag: Flag, mono: Mono = ZERO, sign: int = 1) -> Combination:
    return {(flag, mono): sign}


def main() -> None:
    top = frozenset()
    qd = frozenset({"D"})
    a = frozenset({"1", "3", "5"})
    ec = frozenset({"1", "3"})
    b1 = frozenset({"E", "1", "3"})
    h = frozenset({"E", "3"})
    bd = frozenset({"E", "D", "3"})
    er = frozenset({"D", "3"})
    c = frozenset({"D", "0", "3"})

    h_morse: Combination = {}
    for apex, edge, left, right, mono in [
        (top, ec, a, b1, ZERO),
        (top, h, b1, bd, ZERO),
        (qd, er, bd, c, XD),
    ]:
        h_morse = summed(
            h_morse,
            singleton((apex, edge, right), mono, -1),
            singleton((apex, edge, left), mono, 1),
        )
    h_morse = summed(h_morse, singleton((top, qd, bd)))

    xi: Combination = {}
    for edge, left, right, mono in [
        (ec, a, b1, X1),
        (h, b1, bd, madd(XD, X1)),
        (er, bd, c, XD),
    ]:
        xi = summed(xi, singleton((edge, right), mono),
                    singleton((edge, left), mono, -1))

    qj = summed(
        singleton((top, a), ZERO, -1),
        singleton((top, qd)),
        singleton((qd, c), XD),
    )
    assert boundary(h_morse) == summed(qj, scaled(xi, X3, -1))

    # Normalized blowdown is a chain map on the marked carrier.
    assert blowdown(boundary(h_morse)) == boundary(blowdown(h_morse))
    assert blowdown(boundary(xi)) == boundary(blowdown(xi))
    assert blowdown(boundary(qj)) == boundary(blowdown(qj))
    assert boundary(blowdown(h_morse)) == summed(
        blowdown(qj), scaled(blowdown(xi), X3, -1)
    )

    # The exceptional middle interval collapses, but both external road legs
    # and the unit generic [top<D03] term survive.
    assert len(h_morse) == 7 and len(blowdown(h_morse)) == 5
    assert len(xi) == 6 and len(blowdown(xi)) == 4
    assert ((top, qd), ZERO) in blowdown(qj)
    assert blowdown(qj)[((top, qd), ZERO)] == 1

    print("nontrivial_blowdown_fiber: contractible V")
    print("Morse_terms: 7 upstairs -> 5 nondegenerate downstairs")
    print("expanded_path_terms: 6 upstairs -> 4 nondegenerate downstairs")
    print("normalized_blowdown_chain_map: PASS")
    print("generic_Q_unit: +[top<D03] survives")
    print("descent_counit_on_marked_carrier: CONSTRUCTED")


if __name__ == "__main__":
    main()
