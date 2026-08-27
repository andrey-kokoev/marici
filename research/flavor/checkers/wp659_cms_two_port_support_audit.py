"""Exact WP659 coverage audit of published CMS VLQ searches."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    "standard_vertex_port",
    "exotic_scalar_vertex_port",
    "simultaneous_two_port_fit",
    "free_two_width_parameterization",
    "common_constructor_frame",
    "background_control",
    "two_efficiency_controls",
    "public_joint_covariance",
    "finite_width_response",
]
candidates = {
    "CMS-B2G-23-009": {
        "standard_vertex_port": True,
        "exotic_scalar_vertex_port": True,
        "simultaneous_two_port_fit": False,
        "free_two_width_parameterization": False,
        "common_constructor_frame": False,
        "background_control": True,
        "two_efficiency_controls": False,
        "public_joint_covariance": False,
        "finite_width_response": False,
    },
    "CMS-B2G-22-001": {
        "standard_vertex_port": True,
        "exotic_scalar_vertex_port": True,
        "simultaneous_two_port_fit": False,
        "free_two_width_parameterization": False,
        "common_constructor_frame": False,
        "background_control": True,
        "two_efficiency_controls": False,
        "public_joint_covariance": False,
        "finite_width_response": True,
    },
}
missing = {name: [gate for gate in required if not row[gate]]
           for name, row in candidates.items()}
checks = {
    "coverage_rows_are_complete": all(set(row) == set(required) for row in candidates.values()),
    "no_candidate_binds_all_required_records": all(missing[name] for name in candidates),
    "both_candidates_cover_each_decay_hypothesis": all(
        row["standard_vertex_port"] and row["exotic_scalar_vertex_port"]
        for row in candidates.values()),
    "neither_candidate_performs_simultaneous_two_width_fit": all(
        not row["simultaneous_two_port_fit"] for row in candidates.values()),
    "neither_candidate_identifies_both_vertex_magnitudes": all(
        not row["free_two_width_parameterization"] for row in candidates.values()),
}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP659", "status": "PASS", "checks": checks,
    "required_gates": required,
    "candidate_coverage": candidates,
    "missing_gates": missing,
    "classification": "published CMS searches constrain single production times an assumed decay branching fraction; no admitted analysis realizes WP658's simultaneous five-record instrument",
    "smallest_exact_falsifier": "a published likelihood with both partial widths free in one constructor frame and independent background/efficiency controls plus joint covariance",
    "remaining_gate": "a dedicated simultaneous standard-plus-exotic decay analysis or a validated reinterpretation workspace exposing the joint likelihood and detector controls",
}
(ROOT / "results" / "wp659_cms_two_port_support_audit.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
