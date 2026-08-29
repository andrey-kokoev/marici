from dataclasses import dataclass


@dataclass(frozen=True)
class Parameter:
    name: str
    on_seam: bool


seam = Parameter("seam", True)
off_seam = Parameter("off_seam", False)
zeros = {seam, off_seam}


def aggregate_lift(z: Parameter) -> tuple[str, Parameter]:
    return ("regular_aggregate_tail", z)


common_source = {seam}


def common_lift(z: Parameter):
    if z not in common_source:
        return None
    return ("label_faithful_common_state", z)


aggregate_states = {z: aggregate_lift(z) for z in zeros}
assert set(aggregate_states) == zeros
assert aggregate_states[off_seam][0] == "regular_aggregate_tail"

typed_states = {z: common_lift(z) for z in zeros}
assert typed_states[seam] is not None
assert typed_states[off_seam] is None

# Existence in the ambient completion does not reflect the common source
# domain. A lift through the typed carrier does, but its existence for every
# scalar zero is the unresolved theorem.
aggregate_reflects_domain = all(
    state is None or z in common_source for z, state in aggregate_states.items()
)
typed_reflects_domain = all(
    state is None or z in common_source for z, state in typed_states.items()
)

assert aggregate_reflects_domain is False
assert typed_reflects_domain is True
assert not all(state is not None for state in typed_states.values())

print("aggregate lift: total but not domain-reflecting")
print("typed lift: domain-reflecting but not total on hostile zero locus")
print("unresolved gate: source-derived total typed lift")
