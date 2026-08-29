from dataclasses import dataclass


@dataclass(frozen=True)
class FixedLocalClass:
    multiplicity: int
    orientation_sign: int


def burnside_fixed_mark(classes: tuple[FixedLocalClass, ...]) -> int:
    return sum(local.multiplicity for local in classes)


def signed_lefschetz_trace(classes: tuple[FixedLocalClass, ...]) -> int:
    return sum(local.orientation_sign * local.multiplicity for local in classes)


opposite_pair = (
    FixedLocalClass(multiplicity=1, orientation_sign=1),
    FixedLocalClass(multiplicity=1, orientation_sign=-1),
)
positive_pair = (
    FixedLocalClass(multiplicity=1, orientation_sign=1),
    FixedLocalClass(multiplicity=1, orientation_sign=1),
)

assert burnside_fixed_mark(opposite_pair) == 2
assert signed_lefschetz_trace(opposite_pair) == 0
assert burnside_fixed_mark(positive_pair) == 2
assert signed_lefschetz_trace(positive_pair) == 2

# A free orbit has no fixed local classes and the same signed trace as the
# hostile opposite-sign fixed pair.
free_orbit_classes = ()
assert signed_lefschetz_trace(free_orbit_classes) == signed_lefschetz_trace(opposite_pair) == 0
assert burnside_fixed_mark(free_orbit_classes) == 0

print("signed Lefschetz trace: can cancel fixed points")
print("unsigned Burnside fixed mark: does not cancel")
print("required gate: source-fixed positive local orientation")
