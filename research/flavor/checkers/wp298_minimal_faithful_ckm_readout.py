"""WP298: exact reconstruction from a compact faithful CKM readout."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def ckm_packet(cos_delta):
    sin_delta = sp.Rational(4, 5)
    phase = cos_delta + sp.I * sin_delta
    s12, c12 = sp.Rational(3, 5), sp.Rational(4, 5)
    s23, c23 = sp.Rational(5, 13), sp.Rational(12, 13)
    s13, c13 = sp.Rational(5, 13), sp.Rational(12, 13)
    matrix = sp.Matrix(
        [
            [c12 * c13, s12 * c13, s13 * sp.conjugate(phase)],
            [-s12 * c23 - c12 * s23 * s13 * phase, c12 * c23 - s12 * s23 * s13 * phase, s23 * c13],
            [s12 * s23 - c12 * c23 * s13 * phase, -c12 * s23 - s12 * c23 * s13 * phase, c23 * c13],
        ]
    )
    moduli2 = [sp.simplify(sp.expand_complex(value * sp.conjugate(value))) for value in matrix]
    signed_j = sp.simplify(c12 * c23 * c13**2 * s12 * s23 * s13 * sin_delta)
    return matrix, moduli2, signed_j


def reconstruct(readout):
    vus2, vub2, vcb2, vcd2, signed_j = readout
    s13 = sp.sqrt(vub2)
    c13 = sp.sqrt(1 - vub2)
    s12 = sp.sqrt(vus2 / c13**2)
    c12 = sp.sqrt(1 - s12**2)
    s23 = sp.sqrt(vcb2 / c13**2)
    c23 = sp.sqrt(1 - s23**2)
    normalization = sp.simplify(c12 * c23 * c13**2 * s12 * s23 * s13)
    sin_delta = sp.simplify(signed_j / normalization)
    cos_delta = sp.simplify((vcd2 - s12**2 * c23**2 - c12**2 * s23**2 * s13**2) / (2 * s12 * c12 * c23 * s23 * s13))
    reconstructed, reconstructed_moduli, reconstructed_j = ckm_from_parameters(s12, c12, s23, c23, s13, c13, sin_delta, cos_delta)
    return {
        "sines": [s12, s23, s13],
        "cosines": [c12, c23, c13],
        "sin_delta": sin_delta,
        "cos_delta": cos_delta,
        "matrix": reconstructed,
        "moduli2": reconstructed_moduli,
        "signed_j": reconstructed_j,
    }


def ckm_from_parameters(s12, c12, s23, c23, s13, c13, sin_delta, cos_delta):
    phase = cos_delta + sp.I * sin_delta
    matrix = sp.Matrix(
        [
            [c12 * c13, s12 * c13, s13 * sp.conjugate(phase)],
            [-s12 * c23 - c12 * s23 * s13 * phase, c12 * c23 - s12 * s23 * s13 * phase, s23 * c13],
            [s12 * s23 - c12 * c23 * s13 * phase, -c12 * s23 - s12 * c23 * s13 * phase, c23 * c13],
        ]
    )
    moduli2 = [sp.simplify(sp.expand_complex(value * sp.conjugate(value))) for value in matrix]
    signed_j = sp.simplify(c12 * c23 * c13**2 * s12 * s23 * s13 * sin_delta)
    return matrix, moduli2, signed_j


def main():
    packets = [ckm_packet(sp.Rational(3, 5)), ckm_packet(sp.Rational(-3, 5))]
    audits = []
    all_checks = []
    for matrix, moduli2, signed_j in packets:
        readout = [moduli2[1], moduli2[2], moduli2[5], moduli2[3], signed_j]
        recovered = reconstruct(readout)
        packet_checks = {
            "input_is_unitary": sp.simplify(matrix * matrix.conjugate().T) == sp.eye(3),
            "reconstructed_moduli_match_all_nine": recovered["moduli2"] == moduli2,
            "reconstructed_signed_j_matches": recovered["signed_j"] == signed_j,
            "reconstructed_phase_is_on_unit_circle": sp.simplify(recovered["sin_delta"] ** 2 + recovered["cos_delta"] ** 2) == 1,
        }
        all_checks.extend(packet_checks.values())
        audits.append(
            {
                "readout": [str(value) for value in readout],
                "reconstructed_sines": [str(value) for value in recovered["sines"]],
                "reconstructed_cosines": [str(value) for value in recovered["cosines"]],
                "reconstructed_sin_delta": str(recovered["sin_delta"]),
                "reconstructed_cos_delta": str(recovered["cos_delta"]),
                "checks": {name: bool(value) for name, value in packet_checks.items()},
            }
        )

    checks = {
        "both_exact_packets_reconstruct": all(all_checks),
        "vcd_probe_separates_wp297_pair": audits[0]["readout"][3] != audits[1]["readout"][3],
        "signed_j_alone_does_not_separate_pair": audits[0]["readout"][4] == audits[1]["readout"][4],
        "reconstructed_cosines_have_opposite_sign": audits[0]["reconstructed_cos_delta"] == "3/5" and audits[1]["reconstructed_cos_delta"] == "-3/5",
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP298",
        "admitted_state_domain": "standard CKM chart with ordered nondegenerate masses, angles in the open first quadrant, nonzero sines, and phase constrained by sin^2(delta)+cos^2(delta)=1",
        "faithful_quotient_coordinate": "physical16",
        "compact_faithful_readout": "six ordered masses plus |V_us|^2, |V_ub|^2, |V_cb|^2, |V_cd|^2, and signed J",
        "reconstruction": {
            "angles": "first-row and |V_cb| moduli recover s13, s12, and s23 in the declared quadrant",
            "sin_delta": "signed J divided by the positive Jarlskog angle normalization",
            "cos_delta": "the |V_cd|^2 interference term",
            "remaining_moduli": "standard CKM formula after phase reconstruction",
        },
        "packet_audits": audits,
        "contextual_partition": "generic equality of physical16 on the declared standard chart; singular angle and degeneracy loci are excluded",
        "descent": "every readout entry is a weak-basis invariant after ordered mass conventions",
        "classification": "faithful physical readout/separator on the declared domain; neither selector nor texture rigidifier",
        "smallest_exact_falsifier_for_the_predecessor": "the WP297 phase pair is separated by |V_cd|^2=285184/714025 versus 172864/714025",
        "remaining_physical_instrument_gate": "type and calibrate the individual decay instruments and their common-fit correlations; no readout instrument gains authority to select the reconstructed numerical point",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp298_minimal_faithful_ckm_readout.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
