import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "four_rung_tower.json"


def run(script):
    completed = subprocess.run([sys.executable, str(ROOT / "checkers" / script)],
                               capture_output=True, text=True, check=False)
    assert completed.returncode == 0, completed.stderr


def main():
    run("check_three_wing_associator_preregistration.py")
    run("check_falsifier_compiler.py")
    run("check_ontology_falsifier.py")
    rung2 = json.loads((ROOT / "results" / "three_wing_associator_preregistration.json").read_text())
    rung3 = json.loads((ROOT / "results" / "falsifier_compiler_combined.json").read_text())
    rung4 = json.loads((ROOT / "results" / "ontology_falsifier.json").read_text())
    gates = {
        "rung_2_has_34_passing_gates": rung2["status"] == "pass" and len(rung2["positive_gates"]) == 34,
        "rung_3_closes_frozen_16d_kernel": rung3["status"] == "pass" and rung3["gates"]["synthesized_interventions_close_declared_kernel"],
        "rung_4_breaks_absolute_carrier_closure": rung4["status"] == "pass" and not rung4["absolute_finite_ontology_closure"],
        "rung_4_closes_frozen_ontology_challenge": rung4["relative_frozen_challenge_closure"],
        "open_world_successor_is_exhibited": rung4["diagonal_successor_outside_enlarged_carrier"],
    }
    assert all(gates.values())
    out = {
        "schema": "marici.aspect.four-rung-tower-check.v1",
        "status": "pass", "gates": gates,
        "tower": ["realization", "tester", "falsifier compiler", "ontology falsifier"],
        "disposition": "The tower is recursively extensible, not finitely terminal. Each closure certificate is indexed by its declared hostile language.",
        "physical_apparatus_qualified": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
