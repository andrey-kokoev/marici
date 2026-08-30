"""Exact port-family hostile on the degree-seven attachment residue."""
import json
import math
from pathlib import Path


ports = []
for k in range(7):
    image = sorted({(k * x) % 7 for x in range(7)})
    kernel = [x for x in range(7) if (k * x) % 7 == 0]
    ports.append(
        {
            "port": f"r_{k}",
            "multiplier": k,
            "image": image,
            "kernel": kernel,
            "faithful": len(kernel) == 1,
        }
    )

tests = {
    "seven_linear_labelled_ports": len(ports) == 7,
    "zero_port_is_blind": ports[0]["kernel"] == list(range(7)) and not ports[0]["faithful"],
    "six_nonzero_ports_are_faithful": all(port["faithful"] for port in ports[1:]),
    "same_carrier_supports_different_capabilities": len({len(port["kernel"]) for port in ports}) == 2,
    "faithful_ports_are_record_frame_units": all(math.gcd(port["multiplier"], 7) == 1 for port in ports[1:]),
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "deutschian_instrument_selection_falsifier.py",
    "passed": all(tests.values()),
    "tests": tests,
    "ports": ports,
    "verdict": "exact attachment data do not select or authorize an observation port",
    "missing_constructor": "source-authorized instrument functor with a kernel theorem",
}

out = Path(__file__).resolve().parents[1] / "results" / "deutschian_instrument_selection_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
