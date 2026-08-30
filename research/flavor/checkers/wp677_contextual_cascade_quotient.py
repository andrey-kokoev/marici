"""Exact contextual quotient audit for the finite-mass cascade analyzer."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
u, v, eps = sp.symbols("u v eps", positive=True)
A, C, L = sp.symbols("A C L", positive=True)
phi = sp.symbols("phi", real=True)

W = A*(u+v) + C*sp.sqrt(u*v)*sp.cos(phi)
N = L*(u-v)
Juv = sp.Matrix([W.subs(phi, 0), N]).jacobian([u, v])
det_uv = sp.factor(Juv.det())
gram = sp.simplify(Juv.T*sp.diag(1, eps)*Juv)

# Same unsigned endpoint distribution before the signed analyzer, distinct fibers.
swap_1 = {u: 4, v: 1, A: 3, C: 4, L: 1, phi: 0}
swap_2 = {u: 1, v: 4, A: 3, C: 4, L: 1, phi: 0}

# Same complete two-port record, but inequivalent complex-phase points.
phase_1 = {u: 4, v: 1, A: 3, C: 4, L: 1, phi: sp.pi/3}
phase_2 = {u: 4, v: 1, A: 3, C: 4, L: 1, phi: -sp.pi/3}

# Same composite record from two physically realizable, distinct mass packets.
factor_1 = {u: 1, v: 1, A: 33, C: 60, L: sp.sqrt(189), phi: 0}
factor_2 = {u: sp.Rational(9, 5), v: sp.Rational(9, 5), A: 19, C: 32, L: sp.sqrt(105), phi: 0}

checks = {
    "real_positive_analyzer_rank_two": det_uv != 0,
    "unsigned_endpoint_has_swap_fiber": W.subs(swap_1) == W.subs(swap_2),
    "signed_analyzer_breaks_swap_fiber": N.subs(swap_1) == -N.subs(swap_2) and N.subs(swap_1) != 0,
    "complex_conjugation_survives_two_ports": W.subs(phase_1) == W.subs(phase_2) and N.subs(phase_1) == N.subs(phase_2),
    "complex_domain_cannot_be_locally_faithful": sp.Matrix([W, N]).jacobian([u, v, phi]).rank() == 2,
    "positive_detector_metric_preserves_gram_rank": sp.factor(gram.det() - eps*det_uv**2) == 0,
    "vanishing_chirality_precision_erases_rank": gram.subs(eps, 0).rank() == 1,
    "full_algebraic_rank_has_no_uniform_uncalibrated_gain": sp.limit(gram.det(), eps, 0, dir="+") == 0,
    "ordered_factorization_is_not_identified": W.subs(factor_1) == W.subs(factor_2) and N.subs(factor_1) == N.subs(factor_2),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP677",
    "status": "PASS",
    "checks": checks,
    "endpoint_level": "unsigned endpoint rate has the exact u<->v fiber; a signed chirality analyzer breaks it away from u=v",
    "analyzer_level": "on the real-positive open-threshold slice the (W,N) Jacobian has rank two",
    "phase_frame_level": "on the complex coupling domain two real ports leave at least the exact conjugation stabilizer phi<->-phi and a generic one-dimensional fiber",
    "factorization_level": "physical mass packets (5,3,1) and (4,2,1), with balanced coupling strengths 1 and 9/5, both give (W,N)=(126,0)",
    "detector_gate": "with W_det=diag(1,eps), det Gram=eps(det J)^2; algebraic rank survives every eps>0 but minimum gain is not uniformly certified as eps approaches zero",
    "context_saturation": "the currently declared preparation family is only the identity on the WP675 slice; closure under any additional source-authorized preparation must be computed before compositional quotient authority",
    "maximal_uniformly_observable_domain": "not presently authorized; it requires a calibrated positive lower bound on detector precision and a context-saturated compact domain separated from Kallen=0",
    "existence": "algebraic two-port analyzer exists on the real-positive interior",
    "synthesis": "source cascade is specified abstractly, but must be rebuilt in the physical pole basis after WP676",
    "physical_instrument_execution": "not established",
    "fault": "complex phase, detector precision, and ordered factorization remain nonfaithful",
    "completion": "negative for physical recovery authority; positive only for the conditional algebraic slice",
    "smallest_exact_falsifiers": {
        "endpoint": "(u,v)=(4,1) and (1,4) have equal unsigned rate",
        "phase": "phi=pi/3 and phi=-pi/3 have equal complete two-port records",
        "calibration": "eps=0 makes the detector Gram rank one",
        "factorization": "mass packets (5,3,1) and (4,2,1), with u=v=1 and u=v=9/5 respectively, both give (W,N)=(126,0)",
    },
}
(ROOT / "results" / "wp677_contextual_cascade_quotient.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
