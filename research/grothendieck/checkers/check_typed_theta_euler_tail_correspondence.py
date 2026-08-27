#!/usr/bin/env python3
"""Finite typed model of theta-source incidence and Euler-current evaluation."""

from fractions import Fraction


# A finite theta forcing belongs to a source space E. Boundary currents are
# covectors on E; the tail map has a different codomain.
f = (Fraction(1, 2), Fraction(1, 8), Fraction(1, 32))
nu = (Fraction(1), Fraction(2), Fraction(3))


def evaluate(row, vector):
    return sum(a * b for a, b in zip(row, vector))


def source_incidence(c):
    return tuple(c * x for x in f)


def tail_resolvent(vector):
    # A separate target space, represented by cumulative source tails.
    return tuple(sum(vector[j:]) for j in range(len(vector)))


checks = {}
c = Fraction(5, 7)
checks["transpose_identity"] = evaluate(nu, source_incidence(c)) == c * evaluate(nu, f)

scalar = evaluate(nu, f)
typed_tail = tail_resolvent(source_incidence(scalar))
checks["typed_composition_exists"] = len(typed_tail) == len(f) and typed_tail[0] != 0

# A current is not a tail vector: applying the tail resolver directly to nu
# produces a different object from the authorized composition.
untyped_tail = tail_resolvent(nu)
checks["direct_current_to_tail_is_not_the_source_path"] = untyped_tail != typed_tail

# Scalarization loses current identity: two distinct rows can agree on f.
nu2 = (Fraction(0), Fraction(6), Fraction(3))
checks["distinct_currents_same_scalar_readout"] = nu != nu2 and evaluate(nu, f) == evaluate(nu2, f)

# Retaining the row detects the distinction even when the scalar control line
# does not; hence the control line mediates but does not replace Euler typing.
checks["labelled_current_retention"] = any(a != b for a, b in zip(nu, nu2))

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))
