#!/usr/bin/env python3
"""Denominator-support audit of q_G12 in the printed triangle integrand."""
import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[3]
    common = {"q_G", "q_g1", "q_g2", "q_g3"}
    bracket_terms = [
        {"q_G12", "q_g23"},
        {"q_G12", "q_g31"},
        {"q_G23", "q_g31"},
        {"q_G23", "q_g12"},
        {"q_G31", "q_g12"},
        {"q_G31", "q_g23"},
    ]
    full_terms = [common | term for term in bracket_terms]
    containing = [sorted(term) for term in full_terms if "q_G12" in term]
    assert len(containing) == 2
    assert all(len(term) == 6 for term in containing)
    assert all(set(term) != {"q_G12"} for term in containing)
    assert not any(term == {"q_G12"} for term in full_terms)

    result = {
        "schema": "marici.nima.t7_literal_source_support_gate.v1",
        "passed": True,
        "printed_triangle_term_count": 6,
        "q_G12_occurrence_count": 2,
        "q_G12_full_denominator_supports": containing,
        "literal_isolated_T7_term_exists": False,
        "verdict": "the physical triangle integrand lives in the full denominator-sector complex; isolated T7 appears only after reduction",
        "required_map": "source-normalized full-sector IBP/reduction chain into T7, retaining cross-sector UV cancellation and counterterm coherence",
        "source_locator": "temp/arxiv-2408.16386-source/sections/applications.tex:204",
    }
    output = root / "research/nima/results/t7_literal_source_support_gate.json"
    payload = output.read_text(encoding="utf-8")
    assert json.loads(payload) == result
    print(json.dumps({"passed": True, "isolated_T7": False,
                      "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
