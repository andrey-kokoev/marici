"""WP391: exact cross-context and RG coherence audit for one channel."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    g1, g2, h1, h2 = sp.symbols("g1 g2 h1 h2", real=True)
    chi1, chi2, z = sp.symbols("chi1 chi2 z", positive=True)
    gamma1, gamma2 = sp.symbols("gamma1 gamma2", real=True)
    v, w = sp.Matrix([g1, g2]), sp.Matrix([h1, h2])
    K1, K2 = chi1*v*v.T, chi2*w*w.T
    wedge = sp.factor(g1*h2-g2*h1)
    joint_det = sp.factor((K1+K2).det())
    aligned_K2 = sp.simplify(K2.subs({h1: z*g1, h2: z*g2}, simultaneous=True))
    norm_v = (v.T*v)[0]
    P1 = sp.simplify(v*v.T/norm_v)
    P2_aligned = sp.simplify(aligned_K2/sp.trace(aligned_K2))
    orthogonal = {g1: 1, g2: 0, h1: 0, h2: 1, chi1: 1, chi2: 1}
    commutator = sp.simplify(K1*K2-K2*K1)
    A = sp.diag(gamma1, gamma2)
    Av = A*v
    rg_wedge = sp.factor(g1*Av[1]-g2*Av[0])
    ratio_rate = sp.factor((Av[1]*g1-g2*Av[0])/g1**2)
    checks = {
        "first_context_rank_one": sp.factor(K1.det()) == 0,
        "second_context_rank_one": sp.factor(K2.det()) == 0,
        "joint_determinant_is_context_wedge": sp.simplify(joint_det-chi1*chi2*wedge**2) == 0,
        "aligned_transport_preserves_normalized_projector": sp.simplify(P2_aligned-P1) == sp.zeros(2),
        "orthogonal_contexts_individually_rank_one": K1.subs(orthogonal).rank() == 1 and K2.subs(orthogonal).rank() == 1,
        "orthogonal_contexts_jointly_rank_two": (K1+K2).subs(orthogonal).rank() == 2,
        "commutation_is_insufficient_hostile_case": commutator.subs(orthogonal) == sp.zeros(2),
        "rg_alignment_wedge_exact": sp.simplify(rg_wedge-g1*g2*(gamma2-gamma1)) == 0,
        "rg_ratio_rate_exact": sp.simplify(ratio_rate-g2*(gamma2-gamma1)/g1) == 0,
        "equal_anomalous_dimensions_preserve_direction": rg_wedge.subs(gamma2, gamma1) == 0,
        "unequal_anomalous_dimensions_rotate_benchmark": rg_wedge.subs({g1: 1, g2: 1, gamma1: 0, gamma2: 1}) == 1,
        "single_component_eigenchannel_survives_unequal_running": rg_wedge.subs(g2, 0) == 0,
        "common_direction_deletion_loses_cross_context_test": joint_det.subs(chi2, 0) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP391",
        "admitted_state_domain": "two calibrated response coordinates observed in two source-generated contexts and transported into one declared common frame",
        "faithful_quotient_coordinate": "the family of normalized rank-one response projectors on the physical16 tangent plane",
        "source_authorized_probe_family": "per-context Gram matrices, joint determinant, calibrated projector overlap, and RG direction transport",
        "contextual_partition": "all contexts share one channel exactly when their coupling vectors are collinear after authorized parallelization; per-context rank one alone is insufficient",
        "classification": "cross-context coherence test for the single-channel explanation, not a new numerical selector",
        "joint_determinant": str(joint_det),
        "rg_alignment_obstruction": str(rg_wedge),
        "ratio_running": str(ratio_rate),
        "smallest_exact_falsifier": "two orthogonal contexts each have rank one and commuting projectors, but their joint response has rank two",
        "remaining_physical_instrument_gate": "derive the source/readout parallelization and measure normalized response directions at two contexts or scales with a calibrated metric and uncertainty on their wedge",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp391_cross_context_channel_coherence.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
