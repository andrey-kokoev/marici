import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "five_rung_tower.json"


def run(script):
    completed = subprocess.run([sys.executable, str(ROOT / "checkers" / script)],
                               capture_output=True, text=True, check=False)
    assert completed.returncode == 0, completed.stderr


def main():
    run("check_four_rung_tower.py")
    run("check_admissibility_governance_falsifier.py")
    four = json.loads((ROOT / "results" / "four_rung_tower.json").read_text())
    five = json.loads((ROOT / "results" / "admissibility_governance_falsifier.json").read_text())
    gates = {
        "four_rung_tower_passes": four["status"] == "pass",
        "all_64_evidence_profiles_classified": five["profile_count"] == 64,
        "legitimate_theta_extension_admitted": five["theta_two_port_ternary_disposition"] == "admit",
        "unconstructed_arity_four_extension_deferred": five["variable_amplitude_arity_four_disposition"] == "defer",
        "all_governance_hostiles_rejected": all(five["adversarial_policies"].values()),
        "policy_is_renaming_invariant": five["renaming_invariant"],
        "policy_is_evidence_monotone": five["evidence_monotone"],
        "authority_does_not_substitute_for_evidence": five["authority_independent"],
    }
    assert all(gates.values())
    out = {
        "schema": "marici.aspect.five-rung-tower-check.v1", "status": "pass",
        "gates": gates,
        "tower": ["realization", "tester", "falsifier compiler", "ontology falsifier", "admissibility-governance falsifier"],
        "disposition": "Ontology extension is corrigible but governed: admit constructed distinctions, defer incomplete ones, reject untyped, redundant, or authority-substituted growth.",
        "terminal_completeness_claimed": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
