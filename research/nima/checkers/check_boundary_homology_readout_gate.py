"""Exact finite tests for the boundary--homology--readout typing gate."""

import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "toric", HERE / "check_toric_code_chain_carrier.py"
)
toric = importlib.util.module_from_spec(spec)
spec.loader.exec_module(toric)


def combined_rank(columns_a, columns_b, width_a, width_b):
    columns = [a | (b << width_a) for a, b in zip(columns_a, columns_b)]
    return toric.rank_gf2(columns, width_a + width_b)


def audit_l2():
    d1, d2 = toric.lattice(2)
    n0, n1 = 4, 8
    rank_r = toric.rank_gf2(d2, n1)
    rank_s = toric.rank_gf2(d1, n0)
    syndrome_kernel_dim = n1 - rank_s

    probe_h = [int(i < 4 and (i // 2) == 0) for i in range(n1)]
    probe_v = [int(i >= 4 and ((i - 4) % 2) == 0) for i in range(n1)]
    probes = [probe_h[i] | (probe_v[i] << 1) for i in range(n1)]
    full_rank = combined_rank(d1, probes, n0, 2)
    full_kernel_dim = n1 - full_rank

    return {
        "complex_condition": all(toric.apply_columns(d1, face) == 0 for face in d2),
        "repair_rank": rank_r,
        "residue_rank": rank_s,
        "homology_dimension": syndrome_kernel_dim - rank_r,
        "syndrome_only_kernel_dimension": syndrome_kernel_dim,
        "complete_probe_kernel_dimension": full_kernel_dim,
        "complete_probe_kernel_equals_repair_image": full_kernel_dim == rank_r,
    }


def hostile_same_rank_noncomplex():
    # R -> H -> S with the same dimensions and rank-one arrows as a complex,
    # but s(r(1))=1. Rank data alone cannot type homology.
    r = [0b01]
    s = [0b1, 0b0]
    return {
        "rank_r": toric.rank_gf2(r, 2),
        "rank_s": toric.rank_gf2(s, 1),
        "composition_nonzero": toric.apply_columns(s, r[0]) != 0,
        "homology_is_untyped": True,
    }


def main():
    l2 = audit_l2()
    hostile = hostile_same_rank_noncomplex()
    assert l2["complex_condition"]
    assert l2["homology_dimension"] == 2
    assert not (l2["syndrome_only_kernel_dimension"] == l2["repair_rank"])
    assert l2["complete_probe_kernel_equals_repair_image"]
    assert hostile["rank_r"] == hostile["rank_s"] == 1
    assert hostile["composition_nonzero"]
    payload = {
        "schema": "marici.boundary-homology-readout-gate.v1",
        "toric_l2": l2,
        "hostile_same_rank_noncomplex": hostile,
        "gates": {
            "rank_data_does_not_type_a_complex": True,
            "residue_alone_does_not_classify_mod_repairs": True,
            "residue_plus_global_probes_can_be_jointly_faithful": True,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
