#!/usr/bin/env python3
"""Check supplied shell jets while enforcing the Stokes/transverse section firewall."""
import argparse
import json
from pathlib import Path

PORTS = ["ordinary_tail", "regular_derivative", "wall", "reciprocal", "ordered_link"]
KINDS = {"canonical_stokes", "transverse_evans"}


def cv(value):
    if isinstance(value, list) and len(value) == 2:
        return complex(value[0], value[1])
    return complex(value)


def pair(value):
    return [value.real, value.imag]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("packet", type=Path)
    parser.add_argument("--tol", type=float, default=1e-12)
    args = parser.parse_args()
    packet = json.loads(args.packet.read_text(encoding="utf-8"))
    errors = []
    kind = packet.get("section_kind")
    if kind not in KINDS:
        errors.append("section_kind_must_be_canonical_stokes_or_transverse_evans")
    m = packet.get("multiplicity")
    rows = packet.get("jet_rows", [])
    if not isinstance(m, int) or m < 1:
        errors.append("invalid_multiplicity")
    if not isinstance(rows, list) or (isinstance(m, int) and len(rows) != m):
        errors.append("jet_row_count_mismatch")
    provenance = packet.get("provenance", {})
    if provenance.get("source_frozen_before_Xi_specialization") is not True:
        errors.append("source_not_frozen_before_Xi_specialization")
    if kind == "transverse_evans" and not provenance.get("independent_of_canonical_stokes_construction"):
        errors.append("transverse_section_not_independent_of_canonical_stokes_construction")
    jets = []
    for j, row in enumerate(rows if isinstance(rows, list) else []):
        missing = [port for port in PORTS if row.get(port) is None]
        if missing:
            errors.append(f"jet_{j}_missing:" + ",".join(missing))
            continue
        values = {port: cv(row[port]) for port in PORTS}
        total = sum(values.values())
        jets.append({
            "jet": j,
            "ordinary_nonzero": abs(values[PORTS[0]]) > args.tol,
            "total": pair(total),
            "vanishes": abs(total) <= args.tol,
        })
    numerical_pass = not errors and len(jets) == m and all(jet["vanishes"] for jet in jets)
    xi_detection_admissible = numerical_pass and kind == "transverse_evans"
    result = {
        "section_kind": kind,
        "complete": not errors,
        "errors": errors,
        "jets": jets,
        "numerical_vanishing": numerical_pass,
        "xi_detection_admissible": xi_detection_admissible,
        "canonical_global_identity_only": kind == "canonical_stokes" and numerical_pass,
        "passed": numerical_pass,
        "claim_boundary": (
            "Canonical Stokes vanishing is a global identity and is never promoted to Xi detection. "
            "Transverse-Evans vanishing is eligible for further spectral tests only when its source is "
            "independent of the canonical construction. This checker does not establish provenance, "
            "completion, determinant-class control, all-shell validity, or RH."
        ),
    }
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if numerical_pass else (2 if errors else 1))


if __name__ == "__main__":
    main()
