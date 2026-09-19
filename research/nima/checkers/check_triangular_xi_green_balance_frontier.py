from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/nima/contracts/triangular-xi-green-balance-candidate.v1.json"
OUT = ROOT / "research/nima/results/triangular-xi-green-balance-frontier.json"


def main() -> None:
    c = json.loads(CONTRACT.read_text(encoding="utf-8"))
    locators = {name: ROOT / path for name, path in c["source_locators"].items()}
    repair = json.loads(locators["positive_repair"].read_text(encoding="utf-8"))
    ledger = locators["ledger"].read_text(encoding="utf-8")
    odd = locators["odd_obstruction"].read_text(encoding="utf-8")
    checks = {
        "all_source_locators_resolve": all(path.exists() for path in locators.values()),
        "positive_kernel_repair_exact": repair["status"] == "exact_positive_repair_constructed_confinement_not_implied",
        "Xi_divisor_preserved": repair["triangular_realization"]["determinant"].startswith("det F_lift=det(E)det(F_Xi)"),
        "Xi_kernel_state_lifts": "if F_Xi x=0" in repair["triangular_realization"]["kernel_lift"],
        "green_identity_not_inferred_from_positivity": "not_yet_proved" in repair["critical_firewall"],
        "three_equation_ledger_exists": "Auxiliary diagonal" in ledger and "Mixed block" in ledger and "Xi diagonal" in ledger,
        "mixed_equation_is_first": "The mixed equation is logically first" in ledger,
        "odd_obstruction_source_native": "T_{\\rm hist}(z)" in odd,
        "quadratic_functoriality_still_required": "Green-form functoriality" in odd,
    }
    assert all(checks.values())
    missing = [name for name, value in c["required_materialization"].items() if value is None]
    out = {
        "schema": "marici.nima.triangular-xi-green-balance-frontier.v1",
        "status": "divisor_and_positive_repair_closed_mixed_wronskian_haar_identity_open",
        "checks": checks,
        "lift": c["lift"],
        "decisive_equation": c["three_equations"]["mixed"],
        "missing_common_basis_data": missing,
        "acceptance_test": "Materialize the six common-basis blocks and evaluate the mixed residual coefficientwise for generic (w,z), before tau(z)=0. A single nonzero entry falsifies conservative promotion; exact zero unlocks the Xi-diagonal Green test.",
        "consequence": "A source-derived divisor-preserving positive lift exists as a triangular candidate. The sole first conservative-coherence gate is its mixed Wronskian-Haar Green identity, not abstract positivity and not a positive symmetrizer of the original stable pencil.",
        "artifacts_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in locators.items()},
        "promotion_ready": False,
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
