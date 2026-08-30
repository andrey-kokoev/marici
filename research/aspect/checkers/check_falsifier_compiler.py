import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "falsifier_compiler_combined.json"


def run(name):
    completed = subprocess.run([sys.executable, str(ROOT / "checkers" / name)],
                               capture_output=True, text=True, check=False)
    assert completed.returncode == 0, completed.stderr


def main():
    run("compile_falsifiers.py")
    run("check_falsifier_compiler_exhaustive.py")
    run("check_falsifier_compiler_generated_interventions.py")
    gaussian = json.loads((ROOT / "results" / "falsifier_compiler.json").read_text(encoding="utf-8"))
    exhaustive = json.loads((ROOT / "results" / "falsifier_compiler_exhaustive.json").read_text(encoding="utf-8"))
    generated = json.loads((ROOT / "results" / "falsifier_compiler_generated_interventions.json").read_text(encoding="utf-8"))
    gates = {
        "gaussian_compiler_passes": gaussian["status"] == "pass",
        "exhaustive_analyzer_passes": exhaustive["status"] == "pass",
        "independent_kernel_dimensions_agree": exhaustive["agrees_with_gaussian_kernel_dimensions"],
        "all_primitive_pairs_killed": gaussian["primitive_pair_kill_count"] == gaussian["primitive_pair_total"] == 28,
        "all_signed_primitive_pairs_killed": gaussian["signed_primitive_pair_kill_count"] == gaussian["signed_primitive_pair_total"] == 112,
        "tester_blinding_rejected": gaussian["self_blinding_meta_tester_rejected"],
        "metamorphic_transport_passes": gaussian["metamorphic_violations"] == 0,
        "compiler_finds_pre_repair_kernel": gaussian["unresolved_kernel_dimension"] == 8,
        "synthesized_interventions_close_declared_kernel": gaussian["post_repair_unresolved_kernel_dimension"] == 0,
        "generated_dual_rows_implemented_in_rung_two": generated["all_generated_interventions_operational"] and generated["implemented_dual_dimension"] == 8,
        "open_world_boundary_retained": bool(gaussian["open_world_boundary"]),
    }
    assert all(gates.values())
    out = {"schema": "marici.aspect.falsifier-compiler-combined-check.v1", "status": "pass",
           "gates": gates, "rung_3_operational": True,
           "scope": "exact closure relative to the frozen sixteen-dimensional mutation carrier"}
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
