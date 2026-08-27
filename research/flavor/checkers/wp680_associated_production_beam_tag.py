"""Exact source and descent typing for a qg -> A H beam-odd tag."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
gs, lam, eta, D = sp.symbols("g_s lambda eta D", positive=True)
u, v = sp.symbols("u v", positive=True)
phi = sp.symbols("phi", real=True)
b, ysys = sp.symbols("b y_sys", real=True, nonzero=True)

# Up-sector hypercharges for bar(Q_L) Htilde A_R and QCD color transport.
YbarQ = -sp.Rational(1, 6)
YHtilde = -sp.Rational(1, 2)
YA = sp.Rational(2, 3)
hypercharge_sum = sp.simplify(YbarQ+YHtilde+YA)

# Nonzero source support is proportional to the independently admitted QCD
# and entrance-Yukawa couplings. Normalization is intentionally not claimed.
source_weight = gs**2*lam**2

# Fixed detector beam label b and system rapidity sign t. Under physical beam
# exchange both reverse, so their product is relationally invariant.
t = sp.sign(ysys)
raw = D*b*sp.sqrt(u*v)*sp.sin(phi)
tagged = sp.expand(t*raw)
tagged_exchanged = tagged.xreplace({b: -b, ysys: -ysys})

# Mistag probability omega enters only through eta=1-2 omega.
Sobs = eta*D*sp.sqrt(u*v)*sp.sin(phi)
W = sp.symbols("A", positive=True)*(u+v) + sp.symbols("C", positive=True)*sp.sqrt(u*v)*sp.cos(phi)
N = sp.symbols("L", positive=True)*(u-v)
J = sp.Matrix([W, N, Sobs]).jacobian([u, v, phi])
witness = {u: 4, v: 1, phi: sp.pi/3, eta: sp.Rational(3, 5), D: 2,
           sp.symbols("A", positive=True): 3, sp.symbols("C", positive=True): 4,
           sp.symbols("L", positive=True): 1}

checks = {
    "entrance_vertex_is_hypercharge_invariant": hypercharge_sum == 0,
    "qcd_yukawa_source_weight_is_positive": source_weight > 0,
    "rapidity_tag_is_beam_odd": t.xreplace({ysys: -ysys}) == -t,
    "tagged_statistic_descends": sp.simplify(tagged_exchanged-tagged) == 0,
    "tagged_statistic_is_phase_odd": tagged.subs(phi, -phi) == -tagged,
    "nonzero_calibrated_dilution_restores_rank": J.det().subs(witness) != 0,
    "random_tag_collapses_phase_port": Sobs.subs(eta, 0) == 0 and J.det().subs(eta, 0) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP680",
    "status": "PASS",
    "checks": checks,
    "source_constructor": "q g -> A H through the admitted Q-H-A entrance Yukawa and A/q QCD color coupling",
    "source_support": "partonic weight proportional to g_s^2 lambda^2 is nonzero for positive admitted couplings",
    "beam_odd_tag": "t=sign(y_AH)",
    "relational_observable": "t times the beam-oriented triple product is invariant under exchange of identical proton beams",
    "diluted_phase_port": "S_obs=eta D sqrt(uv) sin(phi), eta=1-2 omega",
    "rank_condition": "eta D != 0 in addition to the WP675 open-threshold conditions",
    "classification": "source-derived associated-production tag exists algebraically; physical execution and calibration are not established",
    "smallest_exact_falsifier": "omega=1/2 gives eta=0 and collapses the phase port",
    "remaining_instrument_gates": ["finite qg matrix element and pole-basis cascade synthesis", "PDF-calibrated quark-direction dilution", "A-H reconstruction and sign assignment", "background and detector covariance", "context-saturated support away from threshold"],
}
(ROOT / "results" / "wp680_associated_production_beam_tag.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
