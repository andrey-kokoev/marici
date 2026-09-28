"""Exact endpoint-reversal counts for the exploratory 137 feedback model.

No target-dependent coefficients. Counts are combinatorial; the conversion
from retained-path fraction to loop gain is an explicit toy-model assumption.
Run directly; writes no artifacts.
"""
from fractions import Fraction
from itertools import product

paths = list(product(range(11), range(11), range(4), range(4)))

def reverse(path):
    i, j, a, b = path
    return j, i, b, a

fixed = sum(reverse(p) == p for p in paths)
orbits = {min(p, reverse(p)) for p in paths}
pairs = (len(paths) - fixed) // 2
assert len(paths) == 1936
assert fixed == 44
assert len(orbits) == 990
assert pairs == 946
assert all(reverse(reverse(p)) == p for p in paths)

# Dimensions of +/- eigenspaces of the permutation involution.
assert len(orbits) + pairs == len(paths)
base_gain = Fraction(1, len(paths))
fractions = {
    "all_returns": Fraction(1),
    "symmetric_projector_rank_fraction": Fraction(len(orbits), len(paths)),
    "antisymmetric_projector_rank_fraction": Fraction(pairs, len(paths)),
}
print(f"paths={len(paths)}, fixed={fixed}, reversal_pairs={pairs}, orbits={len(orbits)}")
for name, fraction in fractions.items():
    # Assumes incoherent uniform path input, survival by projector rank,
    # and unchanged original normalization after projection.
    gain = base_gain * fraction
    inverse = Fraction(137) / (1 - gain)
    print(f"{name}: retained={fraction}, gain={gain}, alpha_inverse={float(inverse):.12f}")

# A coherent uniform vector is already symmetric: projection does not halve it.
uniform = {p: Fraction(1, len(paths)) for p in paths}
assert all((uniform[p] + uniform[reverse(p)]) / 2 == uniform[p] for p in paths)
assert all((uniform[p] - uniform[reverse(p)]) / 2 == 0 for p in paths)
print("coherent uniform input: symmetric survival=1, antisymmetric survival=0")
# Proposed reference port: inject into and read from the arrow block.
a = Fraction(1, 121)
p = Fraction(45, 88)
b = Fraction(1, 16) * p
g = a * b
assert g == Fraction(45, 170368)
# x = u + a*y, y = b*x. A unit arrow-side input has x = 1/(1-g).
x = 1 / (1 - g)
y = b * x
assert x == 1 + a * y
assert y == b * x
print(f"same arrow port: inverse={float(137*x):.12f}, state response={float(y):.12f}")
print(f"mixed readout x+y: inverse={float(137*(x+y)):.12f}")
print(f"slot-weighted readout (121*x+16*y)/121: inverse={float(137*(121*x+16*y)/121):.12f}")

# Distinguish memory reset from a persistent symmetric/antisymmetric sector.
# Independent survival selection at each loop gives p^n at loop n.
reset_response = 1 / (1 - p * base_gain)
# Persistent sector: selected fraction p survives every loop, others never return.
persistent_response = (1 - p) + p / (1 - base_gain)
assert reset_response == x
assert persistent_response > reset_response
assert g == p * base_gain  # identical first-return term
assert p * base_gain**2 != (p * base_gain)**2  # different second returns
print(f"persistent-sector average: inverse={float(137*persistent_response):.12f}")
print(f"averaging-order difference={float(137*(persistent_response-reset_response)):.12f}")
# Positive-return memory family: initial symmetric survival p; conditional
# survival after an accepted return r in [0,1]. nth return: p*g0**n*r**(n-1).
# Response = 1 + p*g0/(1-r*g0), increasing in r on this interval.
def memory_inverse(r):
    return 137 * (1 + p * base_gain / (1 - r * base_gain))

first_only = memory_inverse(Fraction(0))
assert memory_inverse(p) == 137 * reset_response
assert memory_inverse(Fraction(1)) == 137 * persistent_response
rounded_target = Fraction(137036, 1000)
assert first_only > rounded_target
required_r = (1 - 137*p*base_gain/(rounded_target-137)) / base_gain
assert required_r < 0
print(f"positive-return family lower bound={float(first_only):.12f}")
print(f"rounded-target implied conditional survival={float(required_r):.12f} (outside [0,1])")
print("Thus changing positive-return memory cannot reach the rounded target.")
# Endpoint-fixed paths are labels i=j and a=b; the direct arrow was excluded
# before this path domain was formed. Test explicit subtraction hypotheses,
# rather than identifying endpoint-fixed paths with the direct reference.
for label, removed_rank in [("no embedded reference", 0),
                            ("one symmetric reference direction", 1),
                            ("entire endpoint-fixed subspace", fixed)]:
    remaining_rank = len(orbits) - removed_rank
    retained = Fraction(remaining_rank, len(paths))
    trial_gain = retained * base_gain
    first = 137 * (1 + trial_gain)
    reset = 137 / (1 - trial_gain)
    print(f"{label}: rank={remaining_rank}, first={float(first):.12f}, reset={float(reset):.12f}")
assert len(orbits) - fixed == pairs
# A normalized uniform reference vector is symmetric. Subtracting its
# rank-one projector from P+ leaves an idempotent rank-(990-1) projector.
# But a source in that very reference direction is then annihilated.
# This is a structural identity, not an implementation of carrier injection.
def centered_symmetric(v):
    mean = sum(v.values(), Fraction(0)) / len(paths)
    return {q: (v[q] + v[reverse(q)]) / 2 - mean for q in paths}

assert all(value == 0 for value in centered_symmetric(uniform).values())
for selected in [paths[0], paths[1], paths[-1]]:
    basis = {q: Fraction(q == selected) for q in paths}
    projected = centered_symmetric(basis)
    assert centered_symmetric(projected) == projected
    assert sum(projected.values()) == 0
print("Centered symmetric projector: idempotence and uniform-source annihilation checked.")
print("Reference subtraction needs an embedding; slot labels do not supply it.")
print("Counts and port equations checked. Reference-port assignment, positive gains,")
print("and reset versus persistent path ensemble remain physical model choices.")
