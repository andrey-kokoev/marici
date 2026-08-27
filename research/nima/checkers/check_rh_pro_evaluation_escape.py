import json
from pathlib import Path


cutoffs = {}
for n in (1, 2, 4, 8, 16, 32):
    # M_N=I_N and R_N=(1,...,1), so L_N=R_N is an exact factor.
    cutoffs[str(n)] = {
        "kernel_inclusion": True,
        "factor_squared_hilbert_norm": n,
        "constant_packet_partial_sum": n,
    }

assert all(item["kernel_inclusion"] for item in cutoffs.values())
assert cutoffs["32"]["factor_squared_hilbert_norm"] == 32
assert cutoffs["32"]["constant_packet_partial_sum"] == 32

result = {
    "schema": "marici.rh-pro-evaluation-escape.v1",
    "finite_bordered_operator": "M_N=I_N",
    "finite_carrier_port": "R_N=(1,...,1)",
    "finite_factorization": "R_N=L_N M_N with L_N=R_N",
    "truncation_compatible": True,
    "cutoffs": cutoffs,
    "inverse_limit_carrier": "product_of_coordinate_lines",
    "formal_limit_readout": "sum_n x_n",
    "constant_packet_readout_diverges": True,
    "continuous_dual_contains_formal_limit": False,
    "required_gate": "source_topology_making_evaluation_summable_and_uniformly_continuous",
}

out = Path(__file__).parents[1] / "results" / "rh-pro-evaluation-escape.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
