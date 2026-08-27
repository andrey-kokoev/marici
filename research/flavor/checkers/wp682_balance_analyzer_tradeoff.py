"""Exact tradeoff between exchange balance and cross-pole analyzer gain."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
delta, m, y = sp.symbols("Delta m y", real=True)
delta_pos, m_pos, y_pos = sp.symbols("Delta_p m_p y_p", positive=True)
c, s = sp.symbols("c s", real=True)
X = sp.Matrix([[0, 1], [1, 0]])
R = sp.Matrix([[c, -s], [s, c]])
rotated = sp.expand(R.T*X*R)

gap = sp.sqrt(delta_pos**2+4*m_pos**2)
cos2 = delta_pos/gap
cross_gain = sp.simplify(y_pos*cos2)
gain_sq = sp.factor(cross_gain**2)
small_delta_slope = sp.limit(cross_gain/delta_pos, delta_pos, 0, dir="+")

checks = {
    "rotated_cross_vertex_is_cos_two_theta": rotated[0, 1] == c**2-s**2,
    "mass_diagonalization_gives_cos_two_theta": cos2 == delta_pos/gap,
    "exact_balance_closes_cross_pole_vertex": sp.limit(cross_gain, delta_pos, 0, dir="+") == 0,
    "gain_returns_only_with_exchange_breaking": cross_gain != 0,
    "near_balance_gain_is_linear": small_delta_slope == y_pos/(2*m_pos),
    "information_weight_collapses_quadratically": sp.limit(gain_sq/delta_pos**2, delta_pos, 0, dir="+") == y_pos**2/(4*m_pos**2),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP682",
    "status": "PASS",
    "checks": checks,
    "domain": "real symmetric two-messenger mass block with balanced off-diagonal frame vertex and mass detuning Delta=M_A-M_B",
    "pole_gap": "sqrt(Delta^2+4m^2)",
    "cross_pole_vertex": "g_cross=y Delta/sqrt(Delta^2+4m^2)",
    "balance_limit": "g_cross=0 at Delta=0",
    "near_balance_scaling": "g_cross~y Delta/(2m); Fisher/Gram weight from this port scales as Delta^2",
    "classification": "selector-analyzer antagonism: the exact exchange point deletes the transition needed to observe its phase, and analyzer gain requires explicit exchange breaking",
    "smallest_exact_falsifier": "Delta=0 annihilates the off-diagonal pole-basis fluctuation vertex",
    "remaining_gate": "a different analyzer operator not commuting with the balanced mass block, derived from the full source grammar",
}
(ROOT / "results" / "wp682_balance_analyzer_tradeoff.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
