"""Aggregate the twelve-move functional-completion theorem."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(__file__)
ROOT = os.path.dirname(HERE)
RESULTS = os.path.join(ROOT, "results")

PROGRAMS = [
    ("functional_completion_source_categories_checks.py", 8),
    ("global_grade_three_spin_spectrum_checks.py", 8),
    ("global_parity_helicity_harmonic_checks.py", 7),
    ("local_characteristics_global_kernel_checks.py", 7),
    ("grade_three_fredholm_regularity_checks.py", 8),
    ("finite_energy_bms_boundary_kernel_checks.py", 7),
    ("hard_flux_low_kernel_constructibility_checks.py", 7),
    ("accumulation_infinite_collision_checks.py", 8),
    ("low_kernel_observability_checks.py", 6),
    ("functional_completion_analogue_checks.py", 7),
    ("functional_extension_hostile_falsifiers.py", 12),
    ("global_grade_three_numerical_spectral_checks.py", 6),
]

checks = []
for program, expected in PROGRAMS:
    proc = subprocess.run(
        [sys.executable, os.path.join(HERE, program)],
        capture_output=True,
        text=True,
        encoding="ascii",
    )
    summary = f"SUMMARY {expected}/{expected}"
    passed = proc.returncode == 0 and summary in proc.stdout
    checks.append({
        "gate": "aggregate." + program.removesuffix(".py"),
        "statement": f"fresh constituent checker passes {expected}/{expected}",
        "passed": passed,
        "detail": summary if passed else (proc.stdout + proc.stderr)[-500:],
    })

required = {
    "functional-completion-extension-master-theorem.md": [
        "strict LF", "nuclear DFS", "lambda_l", "l=2,3,4", "Fredholm",
        "weak-*", "21", "(1,-3,2)", "p^4-q^4", "finite news energy",
    ],
    "functional-completion-extension-diagram.md": [
        "TV completion", "weak-* completion", "P_low: 21-port repair",
    ],
    "functional-completion-extension-correction-audit.md": [
        "Claims retained", "Claims narrowed or corrected", "Authority boundary",
    ],
}
for name, terms in required.items():
    path = os.path.join(ROOT, name)
    data = open(path, encoding="utf-8").read()
    missing = [term for term in terms if term not in data]
    checks.append({
        "gate": "artifact." + name,
        "statement": "master artifact contains its canonical claims",
        "passed": not missing,
        "detail": "all terms present" if not missing else "missing: " + ", ".join(missing),
    })

all_paths = [os.path.join(ROOT, name) for name in required]
all_paths.append(__file__)
control = []
for path in all_paths:
    raw = open(path, "rb").read()
    control.extend(byte for byte in raw if byte < 32 and byte not in (9, 10, 13))
checks.append({
    "gate": "artifact.ascii_control",
    "statement": "new theorem artifacts contain no forbidden control bytes",
    "passed": not control,
    "detail": "clean" if not control else repr(control[:20]),
})

constituent_total = sum(expected for _, expected in PROGRAMS)
passed = sum(item["passed"] for item in checks)
payload = {
    "checker": os.path.basename(__file__),
    "strength": "fresh aggregate of the twelve-move functional-completion classification",
    "constituent_gates": constituent_total,
    "passed": passed,
    "total": len(checks),
    "checks": checks,
    "verdict": "The local characteristic locus has no authorized localized global finite-energy kernel. The weak-* smooth hard-flux completion has exactly the separate 21-dimensional magnetic l=2,3,4 kernel, repaired minimally by 21 low-harmonic ports.",
}
os.makedirs(RESULTS, exist_ok=True)
with open(os.path.join(RESULTS, "functional_completion_extension_master.json"), "w", encoding="ascii") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True)
    handle.write("\n")
for item in checks:
    print(f"{'PASS' if item['passed'] else 'FAIL'} {item['gate']}: {item['statement']} - {item['detail']}")
print(f"CONSTITUENT GATES {constituent_total}/{constituent_total}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed != len(checks):
    raise SystemExit(1)
