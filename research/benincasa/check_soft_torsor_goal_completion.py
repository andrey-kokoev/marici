#!/usr/bin/env python3
"""Requirement-by-requirement completion audit for the soft-torsor goal."""

import json
from pathlib import Path


def load(here: Path, name: str) -> dict:
    return json.loads((here / name).read_text(encoding="utf-8"))


def passed(packet: dict) -> bool:
    return packet.get("status") == "pass" and all(packet.get("checks", {}).values())


def main() -> None:
    here = Path(__file__).resolve().parent
    noncyclic = load(here, "soft-endpoint-pointing-noncyclic-naturality.json")
    moving = load(here, "soft-endpoint-full-a-cycle-compatibility.json")
    pushforward = load(here, "soft-endpoint-pushed-forward-pointing.json")
    regulator = load(here, "soft-endpoint-regulator-invariance.json")
    leray = load(here, "soft-endpoint-leray-tube-pairing.json")

    requirements = {
        "noncyclic_chart_transitions": {
            "satisfied": passed(noncyclic),
            "evidence": [
                "exact sigma_23 quotient transition and inverse",
                "C3 atlas plus verified S3 presentation",
                "orientation sign and physical occurrence transport",
            ],
        },
        "full_a_cycle_compatibility": {
            "satisfied": passed(moving) and passed(pushforward),
            "evidence": [
                "exact moving root interval and collapse at t=2",
                "rejection of fixed-a pointing",
                "Gauss-Manin pushforward before endpoint pointing",
            ],
        },
        "regulator_invariance": {
            "satisfied": passed(regulator),
            "evidence": [
                "source-fixed q_g1 normal and unit Jacobian",
                "exact finite-part transformation -L log(c)",
                "invariance for source-admissible c=1 deformations",
                "hostile failure for arbitrary endpoint-only reparametrization",
            ],
        },
        "leray_tube_pairing": {
            "satisfied": passed(leray),
            "evidence": [
                "published negative-imaginary boundary-value orientation",
                "physical positive occurrence covector",
                "Delta P equals 2*pi*i*L equals the positive tube integral",
            ],
        },
    }
    complete = all(item["satisfied"] for item in requirements.values())
    packet = {
        "schema": "marici.soft-torsor-goal-completion.v1",
        "status": "pass" if complete else "fail",
        "requirements": requirements,
        "scope": "generic transverse soft endpoint in the frozen homogeneous three-site marked family",
        "prohibited_inference": "does not assert a global physical period outside the frozen source-normal and generic transverse locus",
    }
    out = here / "soft-torsor-goal-completion.json"
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if complete else 1)


if __name__ == "__main__":
    main()

