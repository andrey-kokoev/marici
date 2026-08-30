"""Exact endpoint noncommutation and coherent-reference gate."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
x, m, r = sp.symbols("x m r", real=True, nonzero=True)
rho, phi = sp.symbols("rho phi", positive=True, real=True)
I = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
PA = sp.diag(1, 0)
PB = sp.diag(0, 1)

commutator = PA*X-X*PA
G = sp.simplify((x*I-m*X).inv())
GAA = sp.factor(G[0, 0])
GAB = sp.factor(G[0, 1])
rate_cross = sp.factor(GAB**2)
interfering_rate = sp.expand((r+GAB)**2)
sign_difference = sp.factor(interfering_rate-interfering_rate.subs(m, -m))

# Hermitian complex mixing has phase in the transition amplitude but not its
# isolated probability or its pole denominator.
mc = rho*sp.exp(sp.I*phi)
complex_den = x**2-rho**2
complex_amp = mc/complex_den
complex_rate = sp.simplify(complex_amp*sp.conjugate(complex_amp))

checks = {
    "endpoint_projector_does_not_commute_with_mass_mixing": commutator != sp.zeros(2),
    "same_endpoint_propagator_is_even_in_mixing": GAA.subs(m, -m) == GAA,
    "cross_endpoint_amplitude_is_odd_in_mixing": GAB.subs(m, -m) == -GAB,
    "isolated_cross_rate_loses_mixing_sign": rate_cross.subs(m, -m) == rate_cross,
    "isolated_complex_rate_loses_phase": sp.simplify(complex_rate-rho**2/complex_den**2) == 0,
    "coherent_reference_restores_sign_response": sign_difference == 4*m*r/((x-m)*(x+m)),
    "reference_response_vanishes_without_reference": sign_difference.subs(r, 0) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP683",
    "status": "PASS",
    "checks": checks,
    "source_algebra": "the entrance projector P_A does not commute with balanced mixing sigma_x",
    "transition_amplitude": "G_AB=m/(x^2-m^2) for real mixing",
    "native_readout": "the isolated transition probability is even in m; for complex mixing it depends on |m| only",
    "reference_repair": "a coherent same-external-state amplitude r produces a sign-odd interference difference 4mr/(x^2-m^2)",
    "classification": "noncommuting endpoint algebra exists, but the admitted channel has no coherent reference amplitude and remains phase nonfaithful",
    "smallest_exact_falsifier": "|G_AB|^2 is invariant under m->-m and under complex phase rotation",
    "remaining_gate": "derive an independently normalized amplitude into the same QH-to-Xq external channel, including its absorptive phase and detector interference observable",
}
(ROOT / "results" / "wp683_endpoint_interference_reference_gate.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
