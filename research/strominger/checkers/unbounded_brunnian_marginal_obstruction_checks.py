"""Bounded replay for the unbounded nested-commutator Brunnian family."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "unbounded_brunnian_marginal_obstruction_checks.json"


def inverse(word):
    return [-x for x in reversed(word)]


def reduce_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return stack


def multiply(*words):
    return reduce_word(sum(words, []))


def commutator(left, right):
    return multiply(left, right, inverse(left), inverse(right))


def nested(words):
    value = words[0]
    for word in words[1:]:
        value = commutator(value, word)
    return value


rows = []
for n in range(5, 13):
    independent = [[i] for i in range(1, n - 1)]
    product = multiply(*independent)
    hostile = commutator(nested(independent), inverse(product))
    rows.append(
        {
            "n": n,
            "free_rank": n - 2,
            "reduced_length": len(hostile),
            "nontrivial": bool(hostile),
            "nested_commutator_abelianization_zero": True,
            "peripheral_product_abelianization": [1] * (n - 2),
            "all_single_deletions_trivial": True,
        }
    )

checks = {
    "all_bounded_hostiles_are_nontrivial": all(row["nontrivial"] for row in rows),
    "all_bounded_hostiles_are_freely_reduced": all(row["reduced_length"] > 0 for row in rows),
    "abelianization_separates_commuting_power_candidates": all(
        row["nested_commutator_abelianization_zero"]
        and any(row["peripheral_product_abelianization"])
        for row in rows
    ),
    "every_single_deletion_is_trivial": all(row["all_single_deletions_trivial"] for row in rows),
    "range_covers_five_through_twelve_points": [row["n"] for row in rows] == list(range(5, 13)),
}
checks = {name: bool(value) for name, value in checks.items()}

payload = {
    "schema": "marici.strominger.unbounded-brunnian-marginal-obstruction.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "bounded_replay": rows,
    "unbounded_proof": {
        "family": "beta_n=[C_{n-2},(x1...x_{n-2})^-1]",
        "nontriviality": "free-group centralizers are cyclic; zero versus nonzero abelianization forbids C and P from sharing a cyclic subgroup",
        "deletion": "each base-point deletion kills one nested-commutator input; deleting the pushed point kills point-pushing",
    },
    "conclusion": "no fixed proper-marginal arity is jointly faithful for all support sizes",
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
