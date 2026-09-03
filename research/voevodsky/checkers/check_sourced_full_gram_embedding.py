from __future__ import annotations

import json
from fractions import Fraction


def render(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    cyclic = Fraction(2)
    cross = Fraction(1, 2)
    auxiliary = Fraction(1)
    determinant = cyclic * auxiliary - cross * cross
    auxiliary_quotient = auxiliary - cross * cross / cyclic
    cyclic_quotient = cyclic - cross * cross / auxiliary

    assert cyclic > 0
    assert determinant == Fraction(7, 4) > 0
    assert auxiliary_quotient == Fraction(7, 8) > 0
    assert cyclic_quotient == Fraction(7, 4) > 0

    gauge_source_fields = {
        "exact_sequence": True,
        "identified_kernel": True,
        "canonical_section": False,
        "ambient_gram_form": False,
        "quotient_gram_form": False,
        "schur_quotient_asserted": False,
    }
    gauge_full_gram_embedding_defined = all(
        gauge_source_fields[field]
        for field in ("ambient_gram_form", "quotient_gram_form", "schur_quotient_asserted")
    )
    assert not gauge_full_gram_embedding_defined

    result = {
        "schema": "marici.voevodsky.sourced-full-gram-embedding.v1",
        "status": "green_embeds_gauge_comparison_undefined",
        "green_leading_principal_determinants": [render(cyclic), render(determinant)],
        "green_cyclic_principal_block_preserved": True,
        "green_auxiliary_schur_form": render(auxiliary_quotient),
        "green_cyclic_schur_form": render(cyclic_quotient),
        "green_full_gram_embedding_defined": True,
        "gauge_source_fields": gauge_source_fields,
        "gauge_full_gram_embedding_defined": gauge_full_gram_embedding_defined,
        "first_missing_gauge_datum": "source-derived positive Gram form on the total gauge-presentation space",
        "next_gate": "heterogeneous full-Gram and exact-sequence equipment with typed mixed cells",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
