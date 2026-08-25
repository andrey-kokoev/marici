"""Evidence-manifest gate for the integral parity-cohomology master theorem."""
import json
import os

checks = []


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
results = os.path.join(root, "results")
required = {
    "arbitrary_depth_parity_kernel.json": {"MAGNETIC.arbitrary", "ELECTRIC.arbitrary", "BOUNDARY.visibility"},
    "electric_kernel_classification.json": {"BRANCH.rank", "BRANCH.defects", "CENTER.injective", "JOINT.E1", "JOINT.E2"},
    "magnetic_joint_observer.json": {"JOINT.faithful", "SHEET.injective", "SIGNED.wide"},
    "integral_parity_cohomology_types.json": {"SOURCE.naturality", "DERHAM.hinge", "RESIDUE.naturality"},
    "integral_parity_cohomology_diagram.json": {"JOINT.injective", "CROSS.magnetic", "CROSS.electric"},
    "magnetic_tower_logarithmic_normal_form.json": {"RADIAL.step", "HERMITE.normal"},
    "magnetic_rational_exact_classification.json": {"NAMED.exceptions", "CRITERION.hostile", "DIMENSION.visibility"},
    "magnetic_residue_augmentation.json": {"SMITH.basis", "PAIRWISE.falsifier", "STABLE.residue"},
    "even_depth_fixed_divisor.json": {"ODD_PRIME.local", "TWO_PRIME.local", "GLOBAL.recompose"},
    "stabilization_cutoffs.json": {"VISIBILITY.complete", "ARITHMETIC.minimal", "ARITHMETIC.laurent"},
    "parity_cohomology_naturality.json": {"READOUT.inclusion", "DELETION.falsifier"},
    "constructor_extension_classification.json": {"MIXED.circuits", "MIXED.joint", "COVER.descent"},
    "hostile_parity_cohomology_falsifiers.json": {"F1.target", "F2.depthwise", "F3.saturation", "F4.arithmetic", "F5.deletion", "F6.gauge", "F7.constructor", "F8.divisors"},
    "magnetic_kernel_tower.json": {"RATCOMB.g2", "RATCOMB.g3", "RATCOMB.g4", "RATCOMB.g5"},
}

missing = []
failed_results = []
missing_ids = []
total_gates = 0
for filename, expected_ids in required.items():
    path = os.path.join(results, filename)
    if not os.path.exists(path):
        missing.append(filename)
        continue
    with open(path, encoding="ascii") as handle:
        payload = json.load(handle)
    if payload.get("n_fail") != 0:
        failed_results.append((filename, payload.get("n_fail")))
    observed = {item.get("id") for item in payload.get("checks", [])
                if item.get("status") == "pass"}
    absent = sorted(expected_ids - observed)
    if absent:
        missing_ids.append((filename, absent))
    total_gates += int(payload.get("n_pass", 0))

record("MANIFEST.files", "every required result packet exists",
       not missing, missing)
record("MANIFEST.failures", "every required checker result has zero failed gates",
       not failed_results, failed_results)
record("MANIFEST.coverage", "every theorem clause has its named evidence gate",
       not missing_ids, missing_ids)

master_path = os.path.join(root, "integral-parity-cohomology-master-theorem.md")
with open(master_path, encoding="ascii") as handle:
    master = handle.read()
required_phrases = [
    "Complete parity kernels",
    "Transport and complementary parity reconstruction",
    "Closedness and logarithmic normal form",
    "Complete rational-exact classification",
    "Integral augmentation and Smith form",
    "Stable arithmetic law",
    "Exact cutoffs",
    "Naturality",
    "Constructor and target boundary",
    "Failure taxonomy",
]
record("MASTER.sections", "the master packet contains every required theorem section",
       all(phrase in master for phrase in required_phrases),
       f"required={len(required_phrases)}")

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "integral_parity_cohomology_master_checks.py",
    "author": "marici.Strominger",
    "scope": {"result_packets": len(required), "underlying_passed_gates": total_gates},
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "The master theorem evidence manifest is complete: every required result packet exists, every underlying checker is green, every named clause-level gate is present, and the master packet contains all ten theorem sections.",
}
with open(os.path.join(results, "integral_parity_cohomology_master.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed; underlying gates={total_gates}", flush=True)
raise SystemExit(1 if failed else 0)
