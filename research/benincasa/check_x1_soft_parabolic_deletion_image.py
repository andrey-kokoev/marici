"""Identify the X1-soft invariant plane with the q_g23 deletion image."""

import json

import check_rank26_tangent_support_algebra as algebra

base = algebra.base
support = algebra.support
cyclic = support.cyclic


def main():
    point = (0, 3, 5)
    tangents = ((0, 1, 0), (0, 0, 1))
    record, five, invariant, _ = algebra.case_algebra(
        ("X1_soft", (point, tangents), True)
    )
    assert invariant is not None

    # q_g23=b on X1=0.  Cancelling that pole embeds a four-mark numerator P
    # as the five-mark numerator bP.  Generate the complete filtered image
    # through the same degree-six cutoff used by the rank-26 closure.
    deletion_image = {}
    labels_used = []
    for exponent in base.monomials_at_most(5):
        raised = (exponent[0], exponent[1] + 1)
        label = (0, 1, 1, 1, 1, 1, raised)
        vector = base.reduce_row({five["columns"][label]: 1}, five["pivots"])
        if vector:
            labels_used.append(label)
            base.add_pivot(vector, deletion_image)

    invariant_mod_deletion = 0
    for vector in invariant.values():
        if base.reduce_row(vector, deletion_image):
            invariant_mod_deletion += 1
    deletion_mod_invariant = 0
    for vector in deletion_image.values():
        if base.reduce_row(vector, invariant):
            deletion_mod_invariant += 1

    result = {
        "schema": "marici.benincasa.x1-soft-parabolic-deletion-image.v1",
        "field": base.PRIME,
        "point": list(point),
        "soft_wall": "q_g23=b=0",
        "four_to_five_mark_map": "P -> b P",
        "degree_before_multiplication": 5,
        "candidate_label_count": len(labels_used),
        "deletion_image_rank": len(deletion_image),
        "trace_radical_image_rank": len(invariant),
        "invariant_mod_deletion_failures": invariant_mod_deletion,
        "deletion_mod_invariant_failures": deletion_mod_invariant,
        "equality_verified": (
            len(deletion_image) == len(invariant)
            and invariant_mod_deletion == deletion_mod_invariant == 0
        ),
        "algebra_dimension": record["generated_algebra_dimension"],
    }
    assert result["equality_verified"]
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
