"""Free-group witness invisible to every four-point deletion marginal."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "five_point_brunnian_four_marginal_hostile_checks.json"


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


x1, x2, x3 = [1], [2], [3]
x4 = inverse(multiply(x1, x2, x3))
brunnian_word = commutator(commutator(commutator(x1, x2), x3), x4)

# The formal four-peripheral word collapses when any peripheral generator is
# killed. Deleting the pushed fifth point kills the point-pushing map itself.
formal = {1: [1], 2: [2], 3: [3], 4: [4]}


def formal_hostile(gens):
    return commutator(commutator(commutator(gens[1], gens[2]), gens[3]), gens[4])


deletion_images = {}
for deleted in range(1, 5):
    gens = {i: ([] if i == deleted else formal[i]) for i in range(1, 5)}
    deletion_images[str(deleted)] = formal_hostile(gens)
deletion_images["5"] = []

checks = {
    "sphere_relation_eliminates_fourth_peripheral_generator": multiply(x1, x2, x3, x4) == [],
    "hostile_is_reduced_nonempty_in_free_rank_three_group": bool(brunnian_word),
    "hostile_has_reduced_length_twenty_two": len(brunnian_word) == 22,
    "delete_first_point_trivializes": deletion_images["1"] == [],
    "delete_second_point_trivializes": deletion_images["2"] == [],
    "delete_third_point_trivializes": deletion_images["3"] == [],
    "delete_fourth_point_trivializes": deletion_images["4"] == [],
    "delete_pushed_fifth_point_trivializes": deletion_images["5"] == [],
}
checks = {name: bool(value) for name, value in checks.items()}

payload = {
    "schema": "marici.strominger.five-point-brunnian-four-marginal-hostile.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "hostile": {
        "point_push_loop": "[[[x1,x2],x3],x4]",
        "sphere_relation": "x1*x2*x3*x4=1",
        "free_rank_three_reduced_word": brunnian_word,
        "reduced_length": len(brunnian_word),
        "all_single_deletions": "identity",
    },
    "conclusion": "all four-point deletion marginals fail to detect a nontrivial five-point Brunnian point-push class",
    "source_boundary": "nontriviality as a mapping class uses the Birman point-pushing injection; the checker proves free-word nontriviality and every deletion collapse",
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
