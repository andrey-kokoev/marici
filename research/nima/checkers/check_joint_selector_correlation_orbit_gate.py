"""Finite joint-orbit selector correlation witness."""

from itertools import product

orbit_a = ("A0", "A1")
orbit_b = ("B0", "B1")
required_joint = set(product(orbit_a, orbit_b))

shared_states = (0, 1)
shared_image = {(orbit_a[s], orbit_b[s]) for s in shared_states}
shared_marginal_a = {a for a, _ in shared_image}
shared_marginal_b = {b for _, b in shared_image}

assert shared_marginal_a == set(orbit_a)
assert shared_marginal_b == set(orbit_b)
assert shared_image != required_joint

independent_states = tuple(product((0, 1), repeat=2))
independent_image = {(orbit_a[a], orbit_b[b]) for a, b in independent_states}
assert independent_image == required_joint

missing = sorted(required_joint - shared_image)
failure = {
    "code": "joint_selector_correlation_deficit",
    "marginals_complete": True,
    "required_joint_size": len(required_joint),
    "actual_joint_size": len(shared_image),
    "missing_combinations": missing,
}

print("shared-bit joint image:", sorted(shared_image))
print("missing cross-combinations:", missing)
print("independent-bit joint image size:", len(independent_image))
print("rejection witness:", failure)
print("PASS: complete selector marginals do not imply complete joint authority")
