"""Exact WP865 audit of a minimal lossless portal colligation."""

import json
from pathlib import Path

import sympy as sp


def channel_data(z, q):
    root2 = sp.sqrt(2)
    e0 = sp.Matrix([1, 0, 0])
    dark = sp.Matrix([0, -z/root2, 1/root2])
    bright = sp.Matrix([0, 1/root2, sp.conjugate(z)/root2])
    pd = dark*dark.conjugate().T
    pb = bright*bright.conjugate().T
    a0 = pd + sp.sqrt(q)*pb
    a1 = sp.sqrt(1-q)*dark*bright.conjugate().T
    a2 = dark*e0.conjugate().T
    kraus = [a0, a1, a2]
    superoperator = sum((sp.kronecker_product(sp.conjugate(a), a)
                         for a in kraus), sp.zeros(9))
    return e0, dark, bright, pd, pb, kraus, superoperator


def main() -> None:
    z = sp.I
    q = sp.Rational(1, 4)
    e0, dark, bright, pd, pb, kraus, superoperator = channel_data(z, q)
    identity = sp.eye(3)
    completeness = sp.simplify(sum((a.conjugate().T*a for a in kraus),
                                   sp.zeros(3)))
    fixed = sp.simplify(sum((a*pd*a.conjugate().T for a in kraus),
                            sp.zeros(3)))
    spectrum = superoperator.eigenvals()
    _, dark_1, _, _, _, _, super_1 = channel_data(1, q)
    _, dark_i, _, _, _, _, super_i = channel_data(sp.I, q)
    _, _, _, _, _, _, super_q0 = channel_data(sp.I, sp.Integer(0))
    _, _, _, _, _, _, super_q4 = channel_data(sp.I, q)
    bright_row = sp.Matrix([[0, 1/sp.sqrt(2), z/sp.sqrt(2)]])
    dark_row = sp.Matrix([[0, -sp.conjugate(z)/sp.sqrt(2), 1/sp.sqrt(2)]])
    port_matrix = bright_row.col_join(dark_row)
    endpoint_projector = sp.diag(0, 1, 1, 0)
    cosine = sp.Rational(3, 4)
    sine = sp.sqrt(7)/4
    threshold = sp.eye(4)
    threshold[1, 1], threshold[1, 3] = cosine, sine
    threshold[3, 1], threshold[3, 3] = -sine, cosine
    commutator = sp.simplify(endpoint_projector*threshold
                            - threshold*endpoint_projector)
    embedded_dark = sp.Matrix([dark[0], dark[1], dark[2], 0])
    retained_norm = sp.simplify((endpoint_projector*threshold*embedded_dark).norm()**2)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("kraus_family_is_trace_preserving", completeness == identity,
          completeness)
    check("dark_ray_is_stationary", fixed == pd, fixed)
    check("stationary_state_is_unique", spectrum.get(1, 0) == 1, spectrum)
    check("global_basin_has_expected_nontrivial_spectrum",
          spectrum.get(sp.Rational(1, 2), 0) == 2
          and spectrum.get(sp.Rational(1, 4), 0) == 1, spectrum)
    check("complementary_rows_are_lossless",
          sp.simplify(port_matrix*port_matrix.conjugate().T-sp.eye(2))
          == sp.zeros(2), port_matrix)
    check("selected_ray_is_bright_dark_and_complement_visible",
          sp.simplify(bright_row*dark) == sp.zeros(1, 1)
          and sp.simplify(dark_row*dark) == sp.Matrix([[1]]),
          [bright_row*dark, dark_row*dark])
    check("junction_phase_is_not_fixed_by_channel_spectrum",
          super_1.charpoly().as_expr() == super_i.charpoly().as_expr()
          and dark_1 != dark_i, [dark_1, dark_i])
    check("basin_rate_is_not_fixed_by_lossless_minimality",
          super_q0.charpoly().as_expr() != super_q4.charpoly().as_expr(),
          [super_q0.eigenvals(), super_q4.eigenvals()])
    check("lossless_threshold_need_not_reduce_endpoint_sector",
          threshold.conjugate().T*threshold == sp.eye(4)
          and commutator != sp.zeros(4), commutator)
    check("hostile_threshold_attenuates_selected_ray",
          retained_norm != 1, retained_norm)
    check("detector_calibration_is_not_constructed", True,
          "unit source amplitude has no admitted physical16 detector-unit map")

    result = {
        "schema": "marici.flavor.minimal-lossless-colligation-source-audit.v1",
        "work_package": "WP865",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "state_domain": "absent state plus reciprocal two-endpoint portal",
        "source_operation": "three-Kraus channel and its minimal lossless Stinespring colligation",
        "selected_ray": "(-i,1)/sqrt(2) for the audited z=i branch",
        "channel_spectrum": {str(k): v for k, v in spectrum.items()},
        "contextual_partition": "singleton dark ray for fixed z; U(1) family when z is not source-fixed",
        "classification": "implements selector, basin, and source readout conditionally; explains none of their free source moduli",
        "smallest_exact_falsifiers": [
            "q=0 versus q=1/4 at fixed z=i",
            "z=1 versus z=i at fixed q=1/4",
            "unitary endpoint-heavy rotation with cosine 3/4",
        ],
        "remaining_physical_instrument_gate": "calibrated map from complementary source port to physical16 detector units",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp865_minimal_lossless_colligation_source_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
