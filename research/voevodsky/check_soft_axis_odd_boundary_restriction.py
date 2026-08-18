"""Boundary restriction of the stable odd Bockstein generators."""

from fractions import Fraction


def rank(vectors):
    basis = {}
    for vector in vectors:
        vector = list(vector)
        while any(vector):
            pivot = next(i for i, value in enumerate(vector) if value)
            if pivot not in basis:
                q = vector[pivot]
                basis[pivot] = [value / q for value in vector]
                break
            q = vector[pivot]
            vector = [x - q * y for x, y in zip(vector, basis[pivot])]
    return len(basis)


for cutoff in (16, 20, 24, 28):
    # Coordinates are (+a^3,-a^3,+a^11,-a^11).
    h_orbit = []
    for j in range(cutoff - 3):
        at_plus = 3 * (1 + 1) * (1**j)
        at_minus = 3 * (1 - 1) * ((-1) ** j)
        h_orbit.append(tuple(map(Fraction, (at_plus, at_minus, 0, 0))))
    resonance = tuple(map(Fraction, (0, 0, 1, -1)))
    source_rank = cutoff - 2
    boundary_rank = rank(h_orbit + [resonance])
    kernel_rank = source_rank - boundary_rank
    assert boundary_rank == 2
    assert kernel_rank == cutoff - 4
    assert rank(h_orbit) == 1
    assert rank([resonance]) == 1
    print(
        f"cutoff_{cutoff}: source_rank={source_rank} "
        f"boundary_rank={boundary_rank} kernel_rank={kernel_rank}"
    )

print("h-tail boundary value: nonzero at b=+1, zero at b=-1")
print("resonance boundary value: nonzero at both endpoints")
print("ordinary boundary restriction leaves rank two, not rank one")
