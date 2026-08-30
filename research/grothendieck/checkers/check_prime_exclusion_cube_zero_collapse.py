from fractions import Fraction
from itertools import combinations


def subsets(items):
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def main() -> None:
    # Stand-ins for the regular multiplier values p^(-1/2-z0).
    q = {2: Fraction(2, 3), 3: Fraction(-1, 4), 5: Fraction(3, 7), 7: Fraction(-2, 5)}
    primes = tuple(q)
    x_zero = Fraction(0)
    x_prime = Fraction(11, 13)

    multiplier = {}
    values = {}
    jets = {}
    for subset in subsets(primes):
        m = Fraction(1)
        for prime in subset:
            m *= 1 - q[prime]
        multiplier[subset] = m
        values[subset] = m * x_zero
        jets[subset] = m * x_prime

    checks = {
        "all_sixteen_boolean_vertices_present": len(multiplier) == 16,
        "all_multipliers_regular": all(m != 0 for m in multiplier.values()),
        "all_value_ports_collapse_at_zero": all(value == 0 for value in values.values()),
        "all_simple_zero_jets_survive": all(jet != 0 for jet in jets.values()),
        "normalized_jets_recover_only_common_derivative": all(
            jets[subset] / multiplier[subset] == x_prime for subset in multiplier
        ),
    }

    # Every square in the Boolean cube commutes and satisfies inclusion-exclusion.
    square_count = 0
    square_ok = True
    for base in subsets(primes):
        remaining = [p for p in primes if p not in base]
        for p, r in combinations(remaining, 2):
            base = tuple(sorted(base))
            bp = tuple(sorted(base + (p,)))
            br = tuple(sorted(base + (r,)))
            bpr = tuple(sorted(base + (p, r)))
            square_ok &= multiplier[bpr] == multiplier[base] * (1 - q[p]) * (1 - q[r])
            square_ok &= multiplier[bpr] == multiplier[bp] * (1 - q[r])
            square_ok &= multiplier[bpr] == multiplier[br] * (1 - q[p])
            square_count += 1
    checks["all_boolean_squares_commute"] = square_ok
    checks["twenty_four_boolean_squares_checked"] = square_count == 24

    # Explicit two-prime inclusion-exclusion coefficient.
    p, r = 2, 3
    expanded = 1 - q[p] - q[r] + q[p] * q[r]
    checks["two_prime_inclusion_exclusion_exact"] = expanded == multiplier[(p, r)]
    checks["cube_is_principal_over_multiplier_algebra"] = all(
        values[subset] == multiplier[subset] * values[()] for subset in multiplier
    )

    assert all(checks.values()), [name for name, ok in checks.items() if not ok]
    print(f"{len(checks)}/{len(checks)} exact gates passed; squares={square_count}")


if __name__ == "__main__":
    main()

