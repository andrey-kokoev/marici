"""Finite symmetry obstruction to a canonical reverse lift."""

core = ("linear_at_e", "bounded2_at_f")
legacy_packet = "same_legacy_evidence"
projection = {candidate: legacy_packet for candidate in core}
swap = {"linear_at_e": "bounded2_at_f", "bounded2_at_f": "linear_at_e"}

fiber = [candidate for candidate in core if projection[candidate] == legacy_packet]
fixed_points = [candidate for candidate in fiber if swap[candidate] == candidate]

assert len(fiber) == 2
assert fixed_points == []


def is_equivariant_section(choice):
    # The target symmetry is invisible/identity, so equivariance requires
    # the selected core point to be fixed by the fiber swap.
    return swap[choice] == choice


assert not any(is_equivariant_section(choice) for choice in fiber)

failure = {
    "code": "noncanonical_reverse_lift",
    "legacy_packet": legacy_packet,
    "fiber": fiber,
    "invisible_symmetry": "swap",
    "fixed_points": fixed_points,
}

print("projection fiber:", fiber)
print("common fixed points:", fixed_points)
print("rejection witness:", failure)
print("PASS: surjectivity does not supply a canonical authority lift")
