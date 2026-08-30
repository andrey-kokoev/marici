"""Exact beam-exchange no-go for orienting the WP678 reference at a pp source."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
u, v = sp.symbols("u v", positive=True)
phi = sp.symbols("phi", real=True)
D, b, t = sp.symbols("D b t", real=True)

# b is the signed beam orientation. Identical-beam exchange sends b -> -b.
S = D*b*sp.sqrt(u*v)*sp.sin(phi)
beam_average = sp.simplify((S + S.subs(b, -b))/2)
unsigned = sp.simplify(S**2)

# A source-derived beam-odd tag t can make the product t*S exchange even.
tagged = sp.expand(t*S)
tagged_exchanged = sp.expand(tagged.subs({b: -b, t: -t}, simultaneous=True))

checks = {
    "signed_cp_port_is_beam_exchange_odd": sp.simplify(S.subs(b, -b)+S) == 0,
    "untagged_identical_beam_average_vanishes": beam_average == 0,
    "squaring_erases_phase_sign": unsigned.subs(phi, -phi) == unsigned,
    "beam_odd_tag_repairs_exchange_descent": sp.simplify(tagged_exchanged-tagged) == 0,
    "tagged_port_retains_phase_sign": tagged.subs(phi, -phi) == -tagged,
    "repair_requires_nonzero_tag_and_gain": tagged.subs(t, 0) == 0 and tagged.subs(D, 0) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP679",
    "status": "PASS",
    "checks": checks,
    "source_domain": "unpolarized identical-beam pp preparation with no beam-odd event tag",
    "groupoid": "beam exchange b<->-b",
    "candidate_port": "S=D b sqrt(uv) sin(phi)",
    "descent_result": "S is odd and its untagged pp expectation vanishes exactly",
    "false_repair": "S^2 descends but is even in phi and cannot distinguish conjugate phases",
    "minimal_relational_repair": "a source-derived beam-odd tag t makes tS exchange-even while retaining odd phase response",
    "classification": "the existing identical-beam preparation does not orient the WP678 reference; a tagged production experiment changes the admitted context",
    "smallest_exact_falsifier": "[S(b)+S(-b)]/2=0",
    "remaining_instrument_gate": "derive a physical beam-odd tag from an admitted associated-production channel and calibrate its dilution and sign-assignment error",
}
(ROOT / "results" / "wp679_identical_beam_orientation_no_go.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
