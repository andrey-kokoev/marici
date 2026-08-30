"""Finite lift-dependence test for the affine C8 fold Betti generator."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
CONTOUR = ROOT / "results" / "eight-site-canonical-contour-packet.json"
PAIRING = ROOT / "results" / "eight-site-rank4-os-fold-sewing.json"
TARGET = ROOT / "results" / "eight-site-rank4-fold-betti-selection.json"


def main() -> None:
    contour = json.loads(CONTOUR.read_text())
    pairing = json.loads(PAIRING.read_text())
    s, h = sp.symbols("s h")
    cover = s**2 - h

    # One positive loop in the external fold normal h exchanges the two roots.
    deck = {s: -s, h: h}
    odd_generator = s
    even_generator = sp.Integer(1)
    assert sp.expand(cover.subs(deck)) == cover
    assert sp.expand(odd_generator.subs(deck)) == -odd_generator
    assert sp.expand(even_generator.subs(deck)) == even_generator

    # Primary-source Eq. (4.19), omitted from the earlier packet schema,
    # supplies the negative-imaginary tube x_s,y_e -> x_s,y_e-i epsilon.
    # It does not identify a unique positive epsilon vector or a vanishing
    # path from that tube to a particular complex fold.
    source_selects_external_tube = True
    source_selects_unique_vanishing_path = False

    checks = {
        "local_fold_equation": str(cover),
        "one_external_loop_preserves_fold_cover": True,
        "fold_deck_character_on_odd_line": -1,
        "fold_deck_character_on_even_line": 1,
        "projective_odd_line_is_preserved": True,
        "affine_odd_generator_is_preserved": False,
        "primary_source_selects_negative_imaginary_tube": source_selects_external_tube,
        "primary_source_selects_unique_vanishing_path": source_selects_unique_vanishing_path,
        "algebraically_sewn_nonzero_occurrence_count": pairing["checks"]["status_counts"]["activated_in_os_degree_four"],
    }
    packet = {
        "schema": "marici.eight_site_rank4_fold_betti_selection.v1",
        "typing": {
            "tested_choice": "external-parameter lift to the local A1 fold cover",
            "source_fixed_data": "integration-variable contour plus the external negative-imaginary energy tube of primary-source Eq. (4.19)",
            "source_missing_data": "a unique positive regulator ray or vanishing path from that tube to the complex fold",
            "conclusion": "projective coefficient line canonical; affine Betti selection remains open pending tube-to-fold path analysis",
        },
        "checks": checks,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
