"""Exact F7 hostile: faithful local routes, blind sum interface."""
import json
from pathlib import Path


p = 7
carrier = list(range(p))


def r_plus(x):
    return x % p


def r_minus(x):
    return (-x) % p


def route(x):
    return r_plus(x), r_minus(x)


def sum_interface(pair):
    return (pair[0] + pair[1]) % p


def difference_interface(pair):
    return (pair[0] - pair[1]) % p


def kernel(fn):
    return [x for x in carrier if fn(x) == 0]


tests = {
    "positive_route_faithful": kernel(r_plus) == [0],
    "negative_route_faithful": kernel(r_minus) == [0],
    "route_packet_faithful": len({route(x) for x in carrier}) == p,
    "sum_composite_completely_blind": kernel(lambda x: sum_interface(route(x))) == carrier,
    "difference_composite_faithful": kernel(lambda x: difference_interface(route(x))) == [0],
    "sum_and_difference_jointly_reconstruct_route_packet": len(
        {(sum_interface(route(x)), difference_interface(route(x))) for x in carrier}
    )
    == p,
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "deutschian_faithful_ports_blind_net.py",
    "passed": all(tests.values()),
    "tests": tests,
    "route_records": {str(x): route(x) for x in carrier},
    "sum_records": {str(x): sum_interface(route(x)) for x in carrier},
    "difference_records": {str(x): difference_interface(route(x)) for x in carrier},
    "verdict": "local port faithfulness does not survive an arbitrary authorized pairing",
    "missing_constructor": "typed observation-net wiring with a composite kernel theorem",
}

out = Path(__file__).resolve().parents[1] / "results" / "deutschian_faithful_ports_blind_net.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
