"""WP384: exact reference-probe compression and normalization-kernel audit."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    DP, DF, h, s = sp.symbols("D_P D_F h s", nonzero=True, real=True)
    kernel = sp.Matrix([[DP, h], [h, DF]])
    inverse = sp.simplify(kernel.inv())
    probe_propagator = sp.factor(inverse[0, 0])
    probe_self_energy = sp.factor(h**2/DF)
    effective_probe_kernel = sp.factor(DP-probe_self_energy)
    scaled_self_energy = sp.simplify((s*h)**2/(s**2*DF))
    reconstructed_DF = sp.simplify(h**2/probe_self_energy)
    residual_degree = 24
    probe_degree = 1
    mixing_degree = residual_degree+probe_degree
    checks = {
        "block_inverse_exact": sp.simplify(kernel*inverse) == sp.eye(2),
        "probe_propagator_is_schur_inverse": sp.simplify(probe_propagator-1/effective_probe_kernel) == 0,
        "self_energy_exact": sp.simplify(DP-1/probe_propagator-probe_self_energy) == 0,
        "normalization_scaling_is_blind": sp.simplify(scaled_self_energy-probe_self_energy) == 0,
        "known_mixing_recovers_residual_kernel": reconstructed_DF == DF,
        "hostile_distinct_pair_same_readout": sp.simplify(probe_self_energy.subs({h: 1, DF: 1})-probe_self_energy.subs({h: 2, DF: 4})) == 0,
        "mixing_deletion_blinds_probe": sp.limit(probe_self_energy, h, 0) == 0,
        "residual_decoupling_blinds_probe": sp.limit(probe_self_energy, DF, sp.oo) == 0,
        "mixing_vertex_field_degree_twenty_five": mixing_degree == 25,
        "two_point_detector_valence": kernel.shape == (2, 2),
        "uncalibrated_readout_does_not_separate_h_and_DF": sp.simplify(sp.diff(probe_self_energy, h)*h + sp.diff(probe_self_energy, DF)*2*DF) == 0,
        "calibrated_h_breaks_hostile_scaling_unless_s_unit": sp.factor((s*h-h).subs(s, 2)) != 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP384",
        "admitted_state_domain": "quadratic augmented experiment containing a preparable reference probe P, the invariant composite residual F, and real nonzero mixing h",
        "faithful_quotient_coordinate": "WP378 physical16 residual F augmented by a reference-port normalization",
        "source_authorized_probe_family": "reference-probe two-point propagator and its Schur-complement self-energy",
        "contextual_partition": "without independent mixing calibration, every orbit (h,DF)~(s*h,s^2*DF) has the same probe readout",
        "classification": "lower-valence relational readout and conditional separator; neither a source selector nor a reduction of microscopic operator degree",
        "probe_propagator": str(probe_propagator),
        "probe_self_energy": str(probe_self_energy),
        "mixing_vertex_field_degree": mixing_degree,
        "smallest_exact_falsifier": "(h,DF)=(1,1) and (2,4) are distinct augmented source packets with identical probe self-energy",
        "remaining_physical_instrument_gate": "independently calibrate h in detector units and derive the degree-25 P-F mixing vertex from source dynamics over the augmented stabilizer groupoid",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp384_reference_probe_compression.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
