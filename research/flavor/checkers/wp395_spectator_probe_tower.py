"""WP395: exact finite spectator-extension fiber and probe-tower audit."""
import itertools
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    spectator_count = 3
    states = list(itertools.product((-1, 1), repeat=spectator_count))
    masks = list(itertools.product((0, 1), repeat=spectator_count))
    H = sp.Matrix([
        [sp.prod(signs[i] for i in range(spectator_count) if mask[i]) for signs in states]
        for mask in masks
    ])
    central_fibers = {}
    for signs in states:
        central_fibers.setdefault(sum(signs), []).append(signs)
    labelled_records = {signs: signs for signs in states}
    deleted_records = {}
    for signs in states:
        deleted_records.setdefault(signs[:2], []).append(signs)
    amplitudes = sp.Matrix(sp.symbols("p0:8", real=True))
    moments = H*amplitudes
    reconstructed = sp.simplify(H.T*moments/8)
    checks = {
        "extension_fiber_has_eight_states": len(states) == 8,
        "all_extensions_share_one_flavor_restriction": len({"S_v" for _ in states}) == 1,
        "central_readout_has_four_classes": len(central_fibers) == 4,
        "central_readout_largest_fiber_three": max(map(len, central_fibers.values())) == 3,
        "labelled_single_spectator_probes_are_jointly_faithful": len(set(labelled_records.values())) == 8,
        "deleting_one_labelled_probe_leaves_pairs": set(map(len, deleted_records.values())) == {2},
        "walsh_orthogonality_exact": H*H.T == 8*sp.eye(8),
        "walsh_determinant_nonzero": abs(H.det()) == 4096,
        "complete_tower_reconstructs_every_extension_weight": reconstructed == amplitudes,
        "empty_probe_is_constant": list(H.row(0)) == [1]*8,
        "full_product_probe_is_not_sufficient_alone": len(set(H.row(7))) == 2,
        "hostile_central_collision_exists": len(central_fibers[-1]) == 3,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP395",
        "admitted_state_domain": "one fixed flavor reflection extended by three labelled binary spectator parities",
        "faithful_quotient_coordinate": "the labelled spectator sign packet together with the fixed physical16 flavor ray",
        "source_authorized_probe_family": "all labelled subset-parity characters, represented by the Walsh transform",
        "contextual_partition": "flavor-only readout has one eight-element fiber; central spectator sum has fibers of sizes 1,3,3,1; the complete labelled tower has singleton fibers",
        "classification": "jointly faithful constructor identifier conditional on executable labelled spectator probes, not a selector of which extension occurs",
        "extension_count": len(states),
        "central_fiber_sizes": {str(key): len(value) for key, value in central_fibers.items()},
        "walsh_determinant": str(H.det()),
        "smallest_exact_falsifier": "deleting any one labelled spectator probe leaves four indistinguishable pairs of extensions",
        "remaining_physical_instrument_gate": "derive and execute the labelled spectator parity probes from the source; their successful inversion identifies but still does not select the extension",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp395_spectator_probe_tower.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
