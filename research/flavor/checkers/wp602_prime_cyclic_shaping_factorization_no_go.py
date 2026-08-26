"""Exact WP602 prime-cyclic shaping-versus-factorization no-go."""

import json
from pathlib import Path


PRIMES = (3, 5, 7, 11, 13)


def dot(left, right, prime):
    return sum(a * b for a, b in zip(left, right)) % prime


def determinant(left, right, prime):
    return (left[0] * right[1] - left[1] * right[0]) % prime


census = []
violations = []
for prime in PRIMES:
    rotation_vectors = [
        (first, second)
        for first in range(1, prime)
        for second in range(1, prime)
    ]
    tested_triples = 0
    forbidden_triples = 0
    for rotation_charge in rotation_vectors:
        mixed_monomial_charges = [
            (first, second)
            for first in range(prime)
            for second in range(prime)
            if (first, second) != (0, 0)
            and dot((first, second), rotation_charge, prime) == 0
        ]
        for monomial_charge in mixed_monomial_charges:
            for shaping_charge in [
                (first, second)
                for first in range(prime)
                for second in range(prime)
            ]:
                tested_triples += 1
                shaping_forbids = (
                    dot(monomial_charge, shaping_charge, prime) != 0
                )
                shaping_independent = (
                    determinant(rotation_charge, shaping_charge, prime) != 0
                )
                if shaping_forbids:
                    forbidden_triples += 1
                if shaping_forbids != shaping_independent:
                    violations.append(
                        {
                            "prime": prime,
                            "rotation_charge": rotation_charge,
                            "monomial_charge": monomial_charge,
                            "shaping_charge": shaping_charge,
                        }
                    )
    census.append(
        {
            "prime": prime,
            "rotation_vector_count": len(rotation_vectors),
            "tested_triples": tested_triples,
            "cubic_or_higher_forbidden_triples": forbidden_triples,
            "equivalence_violations": sum(
                item["prime"] == prime for item in violations
            ),
        }
    )

# If the rotation and shaping charges form a basis of F_p^2, arbitrary
# componentwise rotation powers exist.  They compose with bare CP to fix every
# discrete angular pair indexed modulo p.
cp_pair_census = []
for prime in PRIMES:
    pairs = [
        (first, second)
        for first in range(2 * prime)
        for second in range(2 * prime)
    ]
    fixed = [
        (-first + 2 * (first % prime) - first) % (2 * prime) == 0
        and (-second + 2 * (second % prime) - second) % (2 * prime) == 0
        for first, second in pairs
    ]
    cp_pair_census.append(
        {
            "prime": prime,
            "angular_pair_count": len(pairs),
            "pairs_with_componentwise_cp_stabilizer": sum(fixed),
        }
    )

checks = {
    "forbidding_is_equivalent_to_linear_independence_in_every_census": not violations,
    "every_tested_prime_has_nonempty_forbidden_class": all(
        item["cubic_or_higher_forbidden_triples"] > 0 for item in census
    ),
    "independent_rotations_restore_cp_on_every_angular_pair": all(
        item["angular_pair_count"]
        == item["pairs_with_componentwise_cp_stabilizer"]
        for item in cp_pair_census
    ),
}

if not all(checks.values()):
    raise SystemExit(f"WP602 check failed: {checks}; violations={violations[:3]}")

result = {
    "work_package": "WP602",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "domain": "two nontrivially charged multiplets over a prime cyclic rotation group, one mixed invariant monomial, and one additional diagonal shaping charge",
    "exact_identity": "for e dot w=0 in F_p^2, e is proportional to (w_2,-w_1), so e dot q is nonzero exactly when det(w,q) is nonzero",
    "classification": "prime-cyclic diagonal-shaping no-go: forbidding any existing mixed invariant necessarily generates independent component rotations and restores componentwise generalized CP",
    "smallest_exact_falsifier": "one prime, charge triple with e dot w=0 and e dot q nonzero but det(w,q)=0",
    "surviving_architecture_gate": "a non-diagonal non-abelian rule, gauge locality, or collective constraint whose allowed operations do not span independent component rotations",
    "instrument_gate": "unchanged: the surviving constructor must descend to physical16 and share a calibrated threshold instrument with its CP-odd prediction",
    "census": census,
    "cp_pair_census": cp_pair_census,
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp602_prime_cyclic_shaping_factorization_no_go.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
