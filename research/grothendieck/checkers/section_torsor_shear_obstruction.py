controls = []

for p in (2, 3, 5):
    sections = {
        a: {h: ((a * h) % p, h) for h in range(p)}
        for a in range(p)
    }

    # Shear b sends section a to section a+b.
    action = {}
    for b in range(p):
        action[b] = {}
        for a, section in sections.items():
            transformed = {h: ((section[h][0] + b * h) % p, h) for h in range(p)}
            target = next(c for c, candidate in sections.items() if candidate == transformed)
            action[b][a] = target
            assert target == (a + b) % p

    fixed_by_all = [a for a in sections if all(action[b][a] == a for b in range(p))]
    assert fixed_by_all == []
    assert {action[b][0] for b in range(p)} == set(range(p))

    controls.append({
        "prime": p,
        "homomorphic_section_count": len(sections),
        "shear_count": len(action),
        "fixed_section_count": len(fixed_by_all),
        "shear_orbit_of_zero": sorted(action[b][0] for b in range(p)),
    })

print({"controls": controls, "torsor_and_no_fixed_point_checks": "pass", "checks": "pass"})
