"""Exhaustive F7 replay of contextual faithfulness for all scalar interfaces."""
import json
from pathlib import Path


p = 7
carrier = range(p)


def route(x):
    return x % p, (-x) % p


rows = []
for u in range(p):
    for v in range(p):
        records = [((u * a + v * b) % p) for a, b in map(route, carrier)]
        faithful = len(set(records)) == p
        rows.append(
            {
                "u": u,
                "v": v,
                "composite_coefficient": (u - v) % p,
                "contextually_faithful": faithful,
                "kernel_size": records.count(0),
            }
        )

blind = [row for row in rows if not row["contextually_faithful"]]
faithful = [row for row in rows if row["contextually_faithful"]]
tests = {
    "all_49_interfaces_enumerated": len(rows) == 49,
    "exactly_seven_blind_interfaces": len(blind) == 7,
    "exactly_forty_two_contextually_faithful": len(faithful) == 42,
    "criterion_is_u_not_equal_v": all(
        row["contextually_faithful"] == (row["u"] != row["v"]) for row in rows
    ),
    "blind_interfaces_kill_entire_route_image": all(row["kernel_size"] == 7 for row in blind),
    "faithful_interfaces_have_trivial_source_kernel": all(row["kernel_size"] == 1 for row in faithful),
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "deutschian_contextual_faithfulness_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "blind_interfaces": blind,
    "verdict": "faithfulness composes when each interface is monic on the source-reachable image",
}

out = Path(__file__).resolve().parents[1] / "results" / "deutschian_contextual_faithfulness_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
