import hashlib
import json
from pathlib import Path

import sympy as sp


hsp, hsm, htp, htm = sp.symbols("h_s_plus h_s_minus h_t_plus h_t_minus", positive=True)
tp, tm, u, v = sp.symbols("t_plus t_minus u v", positive=True)

P_source = hsp / hsm
P_target = htp / htm

preserving_plus_gain = tp * htp / hsp
preserving_minus_gain = tm * htm / hsm
preserving_relative = sp.simplify(preserving_plus_gain / preserving_minus_gain)
preserving_expected = sp.simplify((tp / tm) * P_target / P_source)
assert sp.simplify(preserving_relative - preserving_expected) == 0

exchanging_plus_gain = u * htp / hsm
exchanging_minus_gain = v * htm / hsp
exchanging_relative = sp.simplify(exchanging_plus_gain / exchanging_minus_gain)
exchanging_expected = sp.simplify((u / v) * P_target * P_source)
assert sp.simplify(exchanging_relative - exchanging_expected) == 0

# Perturbing only the plus amplitude multiplies the anomaly by lambda.
lam = sp.symbols("lambda", positive=True)
perturbed_relative = sp.simplify(preserving_relative.subs(tp, lam * tp))
assert sp.simplify(perturbed_relative / preserving_relative) == lam

payload = {
    "status": "pass",
    "theorem": "relative_determinant_metric_generates_twisted_potential_but_leaves_unimodularity_anomaly",
    "vertex_metric_ratio": "P_v=h_v_plus/h_v_minus",
    "vertex_potential": "phi_v=log(P_v)",
    "preserving_gain": "Gamma_e=A_e*P_t/P_s",
    "exchanging_gain": "Gamma_e=A_e*P_t*P_s",
    "unified_log_law": "ell_e=phi_t-epsilon_e*phi_s+a_e",
    "edge_anomaly": "a_e=log(relative determinant amplitude)",
    "metric_alone_implies_unimodularity": False,
    "plus_amplitude_perturbation": "a_e -> a_e+log(lambda)",
    "required_source_packet": ["relative character-line metric", "relative determinant transport"],
    "theta_character_lines_derived": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "relative-determinant-metric.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
