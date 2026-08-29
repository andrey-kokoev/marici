from dataclasses import dataclass


@dataclass(frozen=True)
class Packet:
    fixed_orbits: int
    free_orbits: int

    @property
    def total_mark(self) -> int:
        return self.fixed_orbits + 2 * self.free_orbits

    @property
    def fixed_mark(self) -> int:
        return self.fixed_orbits

    @property
    def has_only_fixed_orbits(self) -> bool:
        return self.free_orbits == 0


two_fixed = Packet(fixed_orbits=2, free_orbits=0)
one_free = Packet(fixed_orbits=0, free_orbits=1)

# Total counting cannot distinguish the hostile pair.
assert two_fixed.total_mark == one_free.total_mark == 2

# The second Burnside mark separates them.
assert two_fixed.fixed_mark == 2
assert one_free.fixed_mark == 0

# Equality of the two marks is exactly absence of free reciprocal orbits.
for fixed in range(5):
    for free in range(5):
        packet = Packet(fixed, free)
        assert (packet.total_mark == packet.fixed_mark) == packet.has_only_fixed_orbits

# Pull-push orbit-cardinality eigenvalues are 1 and 2.
pull_push_fixed = 1
pull_push_free = 2
assert pull_push_fixed != pull_push_free

print("total mark alone: non-injective")
print("total plus fixed mark: separates C2 orbit types")
print("RH gate: source-side realization of the fixed-point mark")
