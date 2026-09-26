"""Exact finite hostile for the conditional RH physical-readout bridge.

This checks coordinate identities only. It does not compute zeta zeros, prove RH,
or construct an arithmetic-to-apparatus map.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
OWN = Path(__file__).resolve().parent
OUT = OWN / "rh-physical-readout-bridge.json"
PACKET = OWN / "rh-physical-readout-bridge.md"
MANIFEST = OWN / "scc-models/rh-physical-readout-bridge-v1.json"
DIAGRAM = OWN / "rh-physical-readout-diagram.json"
sys.path.insert(0, str(ROOT / "research/aspect/scc"))
from categorical_compiler import compile_diagram, inverse_design

checks = {}

def check(name, condition):
    assert condition, name
    checks[name] = True


def modulus_squared(beta, gamma):
    """|((rho-1)/rho)|^2 for rho=beta+i*gamma, exactly."""
    return ((beta - 1) ** 2 + gamma ** 2) / (beta ** 2 + gamma ** 2)


def predicted_defect(beta, gamma):
    return (1 - 2 * beta) / (beta ** 2 + gamma ** 2)


betas = [Q(1, 10), Q(1, 3), Q(49, 100), Q(1, 2), Q(51, 100), Q(2, 3), Q(9, 10)]
gammas = [Q(1), Q(3, 2), Q(14), Q(10**6)]
rows = []

for beta in betas:
    for gamma in gammas:
        g = modulus_squared(beta, gamma)
        defect = g - 1
        reflected = modulus_squared(1 - beta, gamma)
        check(f"defect_identity_{beta}_{gamma}", defect == predicted_defect(beta, gamma))
        check(f"reflection_reciprocity_{beta}_{gamma}", g * reflected == 1)
        check(f"unit_circle_iff_critical_{beta}_{gamma}", (g == 1) == (beta == Q(1, 2)))
        check(f"real_spectral_coordinate_iff_critical_{beta}_{gamma}",
              (-beta + Q(1, 2) == 0) == (beta == Q(1, 2)))
        if beta != Q(1, 2):
            check(f"reciprocal_gain_loss_{beta}_{gamma}",
                  (g > 1 and reflected < 1) or (g < 1 and reflected > 1))
        rows.append({
            "beta": str(beta),
            "gamma": str(gamma),
            "gain_squared": str(g),
            "reflected_gain_squared": str(reflected),
            "modulus_defect": str(defect),
            "centered_spectral_imaginary_part": str(Q(1, 2) - beta),
        })

# Deliberate failures: both false promotions must be detected on a hostile point.
hostile_beta, hostile_gamma = Q(2, 3), Q(14)
hostile_gain = modulus_squared(hostile_beta, hostile_gamma)
check("deliberate_failure_off_critical_unitarity", hostile_gain != 1)
check("deliberate_failure_off_critical_self_adjoint_spectrum", Q(1, 2) - hostile_beta != 0)

# At huge ordinate the defect is tiny but remains exactly nonzero.
large_defect = modulus_squared(Q(51, 100), Q(10**6)) - 1
check("large_ordinate_defect_nonzero", large_defect != 0)
check("large_ordinate_defect_has_expected_sign", large_defect < 0)

# Compile the readout-descent diagram. Its lower reciprocity cell closes, while
# inverse design must retain every upstream physical witness as missing.
diagram = json.loads(DIAGRAM.read_text(encoding="utf-8"))
compiled = compile_diagram(diagram)
claim_id = "off_critical_zero_has_observable_passivity_defect"
inverse = inverse_design(diagram, claim_id)
expected_missing = {
    "calibrated_positive_apparatus_readout",
    "complete_prime_shell_adjoint_residual_family",
    "evans_to_conservative_green_chain_map",
    "global_fourier_poisson_response_intertwining",
}
check("categorical_diagram_valid", compiled["errors"] == [])
check("lower_li_reciprocity_cell_closes", compiled["cells"][0]["passed"])
check("physical_promotion_not_admitted", not compiled["promotions"][0]["admitted"])
check("physical_claim_has_missing_witnesses", inverse["status"] == "missing_witnesses")
check("physical_claim_missing_set_exact", set(inverse["missing"]) == expected_missing)
check("each_missing_witness_has_discriminating_test",
      {x for e in inverse["ranked_experiments"] for x in e["separates"]} == expected_missing)

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
result = {
    "schema": "marici.voevodsky.rh-physical-readout-bridge.v1",
    "status": "passed",
    "classification": "conditional_coordinate_theorem_not_rh_proof_not_physical_prediction",
    "obligation": "readout descent",
    "grid_cases": len(rows),
    "checks": len(checks),
    "identities": {
        "li_phase_modulus_defect": "|1-1/rho|^2-1=(1-2 beta)/(beta^2+gamma^2)",
        "reflection": "|u(1-rho)|^2=1/|u(rho)|^2",
        "centered_coordinate": "Im((rho-1/2)/i)=1/2-beta",
    },
    "missing_constructors": sorted(expected_missing),
    "categorical_compilation": {
        "lower_cell_passed": compiled["cells"][0]["passed"],
        "physical_promotion_admitted": compiled["promotions"][0]["admitted"],
        "claim_status": inverse["status"],
        "ranked_experiments": inverse["ranked_experiments"],
    },
    "scope": "Exact arithmetic coordinate identities and missing-witness compilation. No zeta-zero computation, RH proof, self-adjoint realization, or physical source authorization.",
    "hostile_large_ordinate_defect": str(large_defect),
    "rows": rows,
    "artifact_sha256": {
        str(PACKET.relative_to(ROOT)): sha(PACKET),
        str(Path(__file__).relative_to(ROOT)): sha(Path(__file__)),
        str(MANIFEST.relative_to(ROOT)): sha(MANIFEST),
        str(DIAGRAM.relative_to(ROOT)): sha(DIAGRAM),
    },
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(f"passed=True checks={len(checks)} cases={len(rows)} obligation=readout-descent")
