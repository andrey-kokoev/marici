"""Finite kernel-reference completion theorem over F_2."""

from itertools import product


vectors = list(product((0, 1), repeat=2))


def syndrome(v):
    # Loses the common second-coordinate mode.
    return (v[0],)


def derived_reference(v):
    # Any post-processing of this one-bit syndrome still loses the kernel.
    return syndrome(v)


def independent_reference(v):
    return (v[1],)


def fibers(observation):
    grouped = {}
    for v in vectors:
        grouped.setdefault(observation(v), []).append(v)
    return grouped


lossy = fibers(syndrome)
internally_completed = fibers(
    lambda v: syndrome(v) + derived_reference(v)
)
independently_completed = fibers(
    lambda v: syndrome(v) + independent_reference(v)
)

assert max(map(len, lossy.values())) == 2
assert max(map(len, internally_completed.values())) == 2
assert max(map(len, independently_completed.values())) == 1

witness = {
    "code": "reference_factors_through_lossy_projection",
    "kernel_dimension": 1,
    "reference_rank_on_kernel": 0,
    "largest_fiber_before": 2,
    "largest_fiber_after_internal_reference": 2,
    "largest_fiber_after_independent_reference": 1,
}

print("lossy fibers:", lossy)
print("internal-reference fibers:", internally_completed)
print("independent-reference fibers:", independently_completed)
print("witness:", witness)
print("PASS: only a reference injective on the invisible kernel restores faithfulness")
