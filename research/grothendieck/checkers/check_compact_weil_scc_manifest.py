from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "research/grothendieck/scc/compact-weil-source-identity.scc.json"

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert data["schema"] == "marici.scc.unimath-certificate.v1"
    assert data["backend"]["kind"] == "UniMath/Rocq"
    assert data["backend"]["kernel_check_status"] in {
        "not_run_coqc_not_installed",
        "passed_rocq_9.0.1_ocaml_4.14.2",
    }
    assert data["certifies_truth"] is False
    assert data["unresolved_target"] == "nonnegative_completed_weil_form_equivalent_to_RH"
    for source in data["source_files"]:
        assert digest(ROOT / source["path"]) == source["sha256"]
    coq = (ROOT / data["backend"]["source"]).read_text(encoding="utf-8")
    for token in ("Require Import UniMath.Foundations.All.", "centered_completed_xi_explicit_formula", "source_form_equals_endpoint_plus_gamma_plus_prime", "compact_support_has_finite_prime_packet", "positivity_is_not_assumed"):
        assert token in coq
    assert "Axiom positivity" not in coq
    result = {
        "schema": "marici.scc.unimath-certificate-check.v1",
        "passed": True,
        "manifest_sha256": digest(MANIFEST),
        "coq_source_sha256": digest(ROOT / data["backend"]["source"]),
        "source_digests_verified": True,
        "kernel_check_status": data["backend"]["kernel_check_status"],
        "external_assumptions_visible": data["externally_sourced_assumptions"],
        "analytic_obligations_not_formalized": data["analytic_obligations_not_formalized"],
        "unresolved_target": data["unresolved_target"]
    }
    out = ROOT / "research/grothendieck/results/compact-weil-scc-manifest.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
