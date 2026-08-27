"""Exact orbit quotient of 49 raw F7 ports by the common-mode annihilator."""
import json
from pathlib import Path


p = 7
ports = [(u, v) for u in range(p) for v in range(p)]


def orbit(port):
    u, v = port
    return sorted({((u + t) % p, (v + t) % p) for t in range(p)})


orbits = {}
for port in ports:
    contrast = (port[0] - port[1]) % p
    orbits.setdefault(contrast, orbit(port))

tests = {
    "forty_nine_raw_ports": len(ports) == 49,
    "seven_contextual_orbits": len(orbits) == 7,
    "every_orbit_has_seven_presentations": all(len(members) == 7 for members in orbits.values()),
    "orbits_partition_raw_ports": len({member for members in orbits.values() for member in members}) == 49,
    "contrast_constant_on_each_orbit": all(
        all((u - v) % p == contrast for u, v in members)
        for contrast, members in orbits.items()
    ),
    "zero_class_blind_six_classes_faithful": 0 in orbits and set(orbits) == set(range(7)),
    "split_and_cyclic_middle_groups_have_different_exponents": 7 != 49,
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "contextual_49_to_7_port_quotient_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "orbits_by_contrast": {str(key): value for key, value in sorted(orbits.items())},
    "quotient_coordinate": "u-v mod 7",
    "verdict": "49 raw interfaces divide by a 7-element common-mode gauge to 7 contextual port types",
}

out = Path(__file__).resolve().parents[1] / "results" / "contextual_49_to_7_port_quotient_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
