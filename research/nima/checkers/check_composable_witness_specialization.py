"""Validate fresh composition/coherence receipts; never launch a compiler."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MODULES = ("ComposableWitnessSpecialization", "CoherentWitnessSpecialization", "DisplayedWitnessSpecialization")
RESULT = ROOT / "research/nima/results/composable-witness-specialization-check.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root):
    return {str(p.relative_to(root)).replace("\\", "/"): digest(p)
            for p in sorted(root.rglob("*.agda"))}


def validate(receipt, module):
    failures = []

    def require(condition, reason):
        if not condition:
            failures.append(reason)

    require(receipt.get("schema") == "marici.nima.agda-check.v1", "receipt schema")
    require(receipt.get("module") == module, "receipt module")
    require(receipt.get("passed") is True and receipt.get("exit_code") == 0, "Agda exit")
    require(receipt.get("inputs_stable_during_check") is True, "input stability")
    require(receipt.get("ignore_interfaces") is True, "fresh closure")
    require(set(["--safe", "--cubical", "--guardedness", "--ignore-interfaces"])
            <= set(receipt.get("args", [])), "safe Cubical flags")
    require(receipt.get("source_sha256") == digest(ROOT / f"research/nima/agda/{module}.agda"),
            "module changed since check")
    require(receipt.get("checker_sha256") == digest(ROOT / "research/nima/checkers/check_cubical_agda.ps1"),
            "launcher changed since check")
    for key, directory in [
        ("owner_source_inventory_sha256", ROOT / "research/nima/agda"),
        ("adapter_source_inventory_sha256", ROOT / "research/nima/adapters"),
        ("library_source_inventory_sha256", Path(receipt["library"])),
    ]:
        require(directory.is_dir(), f"missing inventory root: {directory}")
        require(receipt.get(key) == inventory(directory), f"inventory mismatch: {key}")
    require(receipt.get("compiler_sha256") == digest(Path(receipt["command"])),
            "compiler changed since check")
    return failures


def main():
    failures = []
    for module in MODULES:
        try:
            path = ROOT / f"research/nima/results/agda-{module}.json"
            receipt = json.loads(path.read_text(encoding="utf-8-sig"))
            failures.extend(f"{module}: {f}" for f in validate(receipt, module))
            # Fail-closed controls: neither an incremental receipt nor one
            # for a different module may pass as this module's certificate.
            for changed, diagnostic in [
                (dict(receipt, ignore_interfaces=False), "fresh closure"),
                (dict(receipt, module="WrongModule"), "receipt module"),
            ]:
                if diagnostic not in validate(changed, module):
                    failures.append(f"{module}: negative control failed: {diagnostic}")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            failures.append(f"{module}: receipt unavailable or invalid: {exc}")
    result = {
        "schema": "marici.nima.composable-witness-specialization-check.v1",
        "status": "pass" if not failures else "fail",
        "classification": "displayed_refinement_and_coherent_composition_checked" if not failures else "unverified",
        "failures": failures,
        "scope": "Receipt freshness for safe Agda indexed composition and coherence, displayed graph/history identification, and conditional hom-set library CategoryD bridge; no general comprehension category or fibration.",
        "receipts": [f"research/nima/results/agda-{module}.json" for module in MODULES],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
