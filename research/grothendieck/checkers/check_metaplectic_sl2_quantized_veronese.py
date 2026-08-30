#!/usr/bin/env python3
"""Exact monomial checks for the metaplectic quantization of the conic."""

from fractions import Fraction


State = dict[int, Fraction]


def add(*states: State) -> State:
    out: State = {}
    for state in states:
        for degree, coefficient in state.items():
            out[degree] = out.get(degree, Fraction(0)) + coefficient
    return {degree: coefficient for degree, coefficient in out.items() if coefficient}


def scale(state: State, coefficient: Fraction) -> State:
    return {degree: coefficient * value for degree, value in state.items() if coefficient * value}


def E(state: State) -> State:
    return {degree + 2: coefficient / 2 for degree, coefficient in state.items()}


def F(state: State) -> State:
    return {degree - 2: -coefficient * degree * (degree - 1) / 2
            for degree, coefficient in state.items() if degree >= 2}


def H(state: State) -> State:
    return {degree: coefficient * (Fraction(degree) + Fraction(1, 2))
            for degree, coefficient in state.items()}


def commutator(a, b, state):
    return add(a(b(state)), scale(b(a(state)), Fraction(-1)))


def main():
    gates = []
    for degree in range(21):
        state = {degree: Fraction(1)}
        gates.append((f"HE commutator at degree {degree}", commutator(H, E, state) == scale(E(state), Fraction(2))))
        gates.append((f"HF commutator at degree {degree}", commutator(H, F, state) == scale(F(state), Fraction(-2))))
        gates.append((f"EF commutator at degree {degree}", commutator(E, F, state) == H(state)))

        omega = add(H(H(state)), scale(H(state), Fraction(2)), scale(F(E(state)), Fraction(4)))
        gates.append((f"Casimir at degree {degree}", omega == scale(state, Fraction(-3, 4))))

    # Classical principal-symbol relation h^2+4ef=0, tested on exact samples.
    for q, p in ((1, 1), (2, 3), (-3, 5), (7, -2)):
        e = Fraction(q * q, 2)
        f = Fraction(-p * p, 2)
        h = Fraction(q * p)
        gates.append((f"classical conic at ({q},{p})", h * h + 4 * e * f == 0))

    for name, passed in gates:
        if not passed:
            print(f"FAIL: {name}")
    passed_count = sum(ok for _, ok in gates)
    print(f"SUMMARY: {passed_count}/{len(gates)} gates passed")
    if passed_count != len(gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
