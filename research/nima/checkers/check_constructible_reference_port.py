"""Exact support threshold for a logical reference port in toric chain codes."""

import importlib.util
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "toric", HERE / "check_toric_code_chain_carrier.py"
)
toric = importlib.util.module_from_spec(spec)
spec.loader.exec_module(toric)


def vectors_of_weight(n, weight):
    for support in itertools.combinations(range(n), weight):
        value = 0
        for i in support:
            value |= 1 << i
        yield value


def audit(L):
    d1, d2 = toric.lattice(L)
    n1 = 2 * L * L
    local_repairs = toric.column_space(d2)
    first_nontrivial_weight = None
    first_nontrivial_count = None
    lower_weight_nontrivial = 0
    for weight in range(1, L + 1):
        count = 0
        for chain in vectors_of_weight(n1, weight):
            if toric.apply_columns(d1, chain) == 0 and chain not in local_repairs:
                count += 1
        if weight < L:
            lower_weight_nontrivial += count
        if count and first_nontrivial_weight is None:
            first_nontrivial_weight = weight
            first_nontrivial_count = count
    assert lower_weight_nontrivial == 0
    assert first_nontrivial_weight == L
    assert first_nontrivial_count == 2 * L
    return {
        "L": L,
        "edge_count": n1,
        "local_repair_space_size": len(local_repairs),
        "nontrivial_logical_cycles_below_distance": lower_weight_nontrivial,
        "first_nontrivial_logical_weight": first_nontrivial_weight,
        "minimum_logical_cycle_count": first_nontrivial_count,
    }


def main():
    audits = [audit(L) for L in range(2, 5)]
    print(
        json.dumps(
            {
                "schema": "marici.constructible-reference-port.v1",
                "audits": audits,
                "gates": {
                    "subdistance_support_cannot_access_logical_port": True,
                    "minimum_nonlocal_support_equals_code_distance": True,
                    "mathematical_port_does_not_imply_admitted_constructor": True,
                },
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
