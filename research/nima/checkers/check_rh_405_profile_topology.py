import itertools


scales = ("local", "packet", "finite_system", "pro_system", "completion")
carrier = ("absent", "split", "compatible")
action = ("absent", "typed", "faithful")
observation = ("absent", "natural", "faithful")
estimate = ("absent", "bounded", "uniform")

profiles = tuple(itertools.product(scales, carrier, action, observation, estimate))
assert len(profiles) == 405

completion_profiles = tuple(profile for profile in profiles if profile[0] == "completion")
assert len(completion_profiles) == 81


def first_gate(profile: tuple[str, ...]) -> str:
    _, c_value, a_value, o_value, e_value = profile
    if c_value != "compatible":
        return "carrier"
    if a_value != "faithful":
        return "action"
    if o_value != "faithful":
        return "observation"
    if e_value != "uniform":
        return "estimate"
    return "apex"


counts = {name: 0 for name in ("carrier", "action", "observation", "estimate", "apex")}
for profile in completion_profiles:
    counts[first_gate(profile)] += 1

assert counts == {
    "carrier": 54,
    "action": 18,
    "observation": 6,
    "estimate": 2,
    "apex": 1,
}

apex = ("completion", "compatible", "faithful", "faithful", "uniform")
assert first_gate(apex) == "apex"

current = ("pro_system", "compatible", "typed", "absent", "absent")
assert current in profiles
assert first_gate(current) == "action"

print("profile count:", len(profiles))
print("completion profile count:", len(completion_profiles))
print("first-failure stratification:", counts)
print("unique completion apex:", apex)
print("current theta/Tate profile:", current)
