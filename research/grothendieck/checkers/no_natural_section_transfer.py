G = tuple((a, b) for a in range(2) for b in range(2))
H = (0, 1)


def q(x):
    return x[0]


def shear(x):
    return (x[0], (x[0] + x[1]) % 2)


assert all(q(shear(x)) == q(x) for x in G)
assert all(shear(shear(x)) == x for x in G)

sections = []
for lift in ((1, 0), (1, 1)):
    s = {0: (0, 0), 1: lift}
    assert all(q(s[h]) == h for h in H)
    sections.append(s)

assert len(sections) == 2
assert {shear(sections[0][h]) for h in H} == {sections[1][h] for h in H}
assert {shear(sections[1][h]) for h in H} == {sections[0][h] for h in H}
assert not any(all(shear(s[h]) == s[h] for h in H) for s in sections)

# Both are group-homomorphic sections, so splitting alone does not select one.
for s in sections:
    assert all(s[(a + b) % 2] == ((s[a][0] + s[b][0]) % 2, (s[a][1] + s[b][1]) % 2) for a in H for b in H)

print({
    "surjection": "C2xC2->C2",
    "identity_preserving_sections": [[s[0], s[1]] for s in sections],
    "both_group_homomorphisms": True,
    "base_preserving_shear_swaps_sections": True,
    "automorphism_natural_section_count": 0,
    "checks": "pass",
})
