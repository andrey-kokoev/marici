"""Exact interface gate for transferring a comb reference into flavor units."""

import json
from pathlib import Path

import sympy as sp


site_root = Path(__file__).resolve().parents[2]
flavor_root = site_root / "flavor"
aspect_root = site_root / "aspect"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


wp544 = load(flavor_root / "results" / "wp544_typed_source_instrument_pencil.json")
aspect = load(aspect_root / "results" / "calibrated_six_port_scale_identification_instrument.json")

weights = [sp.Integer(x) for x in (1, 2, 3, 5, 7, 11)]

# Coordinates are physical flavor scale tau, flavor detector unit u_F, and
# comb unit u_C. Without an interface, the two unit coordinates are distinct.
flavor_rows = sp.Matrix([[c, -c, 0] for c in weights])
comb_row = sp.Matrix([[0, 0, 1]])
separate_loci = flavor_rows.col_join(comb_row)
interface_row = sp.Matrix([[0, 1, -1]])
joined_loci = separate_loci.col_join(interface_row)

flavor_scale_kernel = sp.Matrix([1, 1, 0])
comb_only_direction = sp.Matrix([0, 0, 1])

checks = {
    "dependencies_passed": bool(wp544["passed"]) and aspect["status"] == "pass",
    "aspect_abstract_rank_is_two": aspect["ranks"]["referenced_readout"] == 2,
    "wp544_unreferenced_kernel_is_one_dimensional": wp544["source_scale_confounder"]["rank"] == 1,
    "separate_loci_rank_is_two": separate_loci.rank() == 2,
    "separate_loci_leave_one_kernel_direction": len(separate_loci.nullspace()) == 1,
    "original_flavor_scale_kernel_survives_comb_row": separate_loci * flavor_scale_kernel
    == sp.zeros(7, 1),
    "comb_row_calibrates_only_comb_unit": (comb_row * comb_only_direction)[0] == 1,
    "named_interface_raises_rank_to_three": joined_loci.rank() == 3,
    "named_interface_kills_scale_kernel": len(joined_loci.nullspace()) == 0,
    "interface_row_identifies_unit_coordinates": (interface_row * flavor_scale_kernel)[0] == 1,
    "source_rank_remains_one": wp544["typed_factorization"]["fixed_control_source_image_rank"] == 1,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP548",
    "domain": "Composition of WP544's flavor/QCD scale coordinate with Aspect's independently referenced comb coordinate, without presupposing a cross-locus calibration map.",
    "coordinate_order": ["physical flavor log scale", "flavor detector log unit", "comb log unit"],
    "separate_loci_jacobian": [[str(x) for x in row] for row in separate_loci.tolist()],
    "separate_loci_rank": separate_loci.rank(),
    "separate_loci_kernel": [str(x) for x in flavor_scale_kernel],
    "required_interface_row": [str(x) for x in interface_row.tolist()[0]],
    "joined_loci_rank": joined_loci.rank(),
    "interface_constructor": {
        "type": "P_scale: comb-referenced frequency standard -> flavor/QCD detector energy unit",
        "must_supply": [
            "a named physical transfer chain",
            "traceable calibration coefficients in common units",
            "uncertainty and drift covariance",
            "support and bandwidth limits",
            "a readback proving the same unit coordinate enters the six flavor ports",
        ],
        "examples_requiring_separate_derivation": [
            "clock-referenced field metrology followed by charged-beam momentum calibration",
            "experimentally calibrated hadron mass followed by lattice-spacing scale setting",
        ],
    },
    "theorem": "Aspect's reference row removes the unit kernel only after the comb and flavor instruments share one admitted unit coordinate. With distinct unit coordinates, the seven-row Jacobian has rank two and exact kernel (1,1,0), so the physical flavor scale remains unidentified. A separately derived interface row (0,1,-1) raises rank to three and removes the kernel.",
    "classification": "Exact cross-locus interface gate. The abstract reference architecture transfers, but an experimentally calibrated flavor-scale instrument is not yet admitted.",
    "selector": bool(wp544["selector"]),
    "instrument": "Conditional. The comb reference is a physical instrument in its own locus; the flavor/QCD scale transfer requires a named calibrated interface constructor.",
    "smallest_exact_falsifier": "Let physical flavor scale and flavor detector unit shift together while the comb unit is fixed: (1,1,0). All six flavor rows and the independent comb row remain unchanged.",
    "remaining_gate": "Derive and execute P_scale with common-unit readback and covariance. This repairs identification only; a source-derived transverse selector equation remains independently required.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = flavor_root / "results" / "wp548_cross_locus_scale_reference_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
