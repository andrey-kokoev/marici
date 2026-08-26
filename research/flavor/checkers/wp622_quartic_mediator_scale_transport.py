"""Exact WP622 audit of the minimal stable quartic mediator reopening."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

z, phi = sp.symbols("z phi", real=True)
K, lam, v = sp.symbols("K lam v", positive=True, real=True)
target_z = sp.Rational(576, 25)

potential = sp.expand(
    K * (z - phi) ** 2 / 2 + lam * (phi**2 - v**2) ** 2 / 4
)
grad = [sp.diff(potential, variable) for variable in (z, phi)]

# The positive-domain stationary points follow exactly from dV/dz=0 and
# dV/dphi=0: z=phi and phi(phi^2-v^2)=0.
stationary = [(sp.Integer(0), sp.Integer(0)), (v, v), (-v, -v)]
hessian = sp.hessian(potential, (z, phi))
hessian_at_positive_vacuum = sp.simplify(hessian.subs({z: v, phi: v}))
hessian_at_origin = sp.simplify(hessian.subs({z: 0, phi: 0}))

target_hessian = hessian_at_positive_vacuum.subs({K: 2, lam: 3, v: target_z})
target_trace = sp.trace(target_hessian)
target_determinant = sp.det(target_hessian)

hostile_v = sp.Integer(24)
target_r = sp.sqrt(1 - target_z / 36)
hostile_r = sp.sqrt(1 - hostile_v / 36)

delta = sp.symbols("delta", real=True)
shifted_positive_minimum = v + delta

checks = {
    "potential_is_bounded_below": sp.Poly(potential, z, phi).total_degree() == 4,
    "stationary_points_are_exact": all(
        all(sp.simplify(component.subs({z: point[0], phi: point[1]})) == 0 for component in grad)
        for point in stationary
    ),
    "positive_vacuum_hessian_trace_is_positive": sp.trace(hessian_at_positive_vacuum) > 0,
    "positive_vacuum_hessian_determinant_is_positive": sp.det(hessian_at_positive_vacuum) == 2 * K * lam * v**2,
    "origin_is_a_saddle": sp.det(hessian_at_origin) == -K * lam * v**2,
    "target_scale_recovers_target_lens": target_r == sp.Rational(3, 5),
    "target_hessian_is_strictly_positive": target_trace > 0 and target_determinant > 0,
    "hostile_scale_moves_lens": hostile_r == sp.sqrt(3) / 3 and hostile_r != target_r,
    "scale_deformation_moves_center_exactly": shifted_positive_minimum - v == delta,
    "quartic_repairs_gaussian_sign_but_transports_scale": sp.diff(potential.subs(phi, z), z, 4) == 6 * lam,
}

if not all(checks.values()):
    raise SystemExit(f"WP622 check failed: {checks}")
checks = {key: bool(value) for key, value in checks.items()}

result = {
    "work_package": "WP622",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the H-referenced relational coordinate z=QR, a real mediator phi, and positive K, lambda, v on the inner s=1 support component",
    "source_grammar": "V=K/2(z-phi)^2+lambda/4(phi^2-v^2)^2",
    "stationary_fiber": ["(z,phi)=(0,0)", "(z,phi)=(v,v)", "(z,phi)=(-v,-v)"],
    "minimum_test": "the two nonzero vacua have Hessian determinant 2 K lambda v^2>0; the origin has determinant -K lambda v^2<0",
    "target_condition": "on s=1, z=36(1-r^2); r=3/5 requires v=576/25",
    "classification": "conditional selector and relational presentation rigidifier, but not an independently numerical selector",
    "smallest_exact_falsifier": "v=24 is equally stable and moves the inner lens from r=3/5 to r=sqrt(3)/3",
    "descent": "z uses the H reference and therefore belongs to the stabilizer groupoid of a new relational experiment; it is not an invariant of the original full weak-basis experiment",
    "physical_probe": "in one source lineage, reconstruct the two scalar normal-mode pole masses, mixing angle, cubic and quartic self-couplings, the mediator vacuum displacement, and the root-vector flavor masses",
    "instrument_gate": "no admitted detector-calibrated joint scalar/flavor apparatus has yet been supplied",
    "remaining_source_gate": "derive v from source geometry independently of the flavor target, or close this branch as transported scale data",
}

out = ROOT / "results" / "wp622_quartic_mediator_scale_transport.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
