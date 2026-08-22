"""Audit the canonical absolute-to-common localization map at finite cutoff."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
import physical_four_mark_residue_twisted_derham as m

NAMES = ("g1", "g2", "g3", "g23", "g31")
GAMMA = int(os.environ.get("MARICI_TWIST_GAMMA", "5")) % m.PRIME
AMBIENT = int(os.environ.get("MARICI_AMBIENT_DEGREE", "10"))
CUTOFF = int(os.environ.get("MARICI_CUTOFF_DEGREE", "5"))
RESULT_NAME = (
    "physical_common_half_twist_absolute_comparison.json"
    if GAMMA == (m.PRIME - 1) // 2
    else "physical_common_rank9_absolute_comparison.json"
)
OUT = Path(__file__).resolve().parents[1] / "results" / RESULT_NAME


def add_scaled(target, vector, scale=1):
    for column, value in vector.items():
        m.add_value(target, column, scale * value)


def main() -> None:
    a_low, a_columns, a_pivots, a_free = m.presentation(
        (), GAMMA, AMBIENT, CUTOFF, minimum_q_level=0
    )
    c_low, c_columns, c_pivots, c_free = m.presentation(
        NAMES, GAMMA, AMBIENT, CUTOFF, minimum_q_level=0
    )
    a_label_by_column = {column: label for label, column in a_columns.items()}
    c_label_by_column = {column: label for label, column in c_columns.items()}

    def common_label(absolute_label):
        k_pole, monomial = absolute_label
        return (k_pole, 0, 0, 0, 0, 0, monomial)

    def map_ambient(vector):
        image = {}
        for column, coefficient in vector.items():
            target = common_label(a_label_by_column[column])
            add_scaled(image, {c_columns[target]: 1}, coefficient)
        return image

    def common_quotient(vector):
        reduced = m.reduce_row(vector, c_pivots)
        return {column: reduced[column] for column in c_free if column in reduced}

    # A quotient map is typed only if every retained absolute relation maps to
    # zero in the common quotient.  Checking only free-basis images is weaker.
    relation_failures = 0
    relation_failure_support = 0
    for relation in a_pivots.values():
        residual = common_quotient(map_ambient(relation))
        relation_failures += int(bool(residual))
        relation_failure_support += len(residual)

    image_span = {}
    absolute_basis_images = {}
    for column in a_free:
        label = a_label_by_column[column]
        image = common_quotient({c_columns[common_label(label)]: 1})
        absolute_basis_images[column] = image
        m.add_pivot(dict(image), image_span)

    intrinsic_core = {}
    for label in c_low:
        if all(level == 0 for level in label[1:-1]):
            m.add_pivot(m.quotient_coordinates(label, c_columns, c_pivots, c_free), intrinsic_core)

    image_outside_core = sum(
        bool(m.reduce_row(row, intrinsic_core)) for row in image_span.values()
    )

    def absolute_connection(vector, axis):
        image = {}
        for column, coefficient in vector.items():
            add_scaled(
                image,
                m.connection_image(a_label_by_column[column], (), GAMMA, axis, a_columns),
                coefficient,
            )
        reduced = m.reduce_row(image, a_pivots)
        return {column: reduced[column] for column in a_free if column in reduced}

    def common_connection(vector, axis):
        image = {}
        for column, coefficient in vector.items():
            add_scaled(
                image,
                m.connection_image(c_label_by_column[column], NAMES, GAMMA, axis, c_columns),
                coefficient,
            )
        return common_quotient(image)

    def map_absolute_quotient(vector):
        image = {}
        for column, coefficient in vector.items():
            add_scaled(image, absolute_basis_images[column], coefficient)
        return image

    intertwining_failures = [0, 0]
    for column in a_free:
        source = {column: 1}
        mapped = absolute_basis_images[column]
        for axis in range(2):
            left = common_connection(mapped, axis)
            right = map_absolute_quotient(absolute_connection(source, axis))
            add_scaled(left, right, -1)
            intertwining_failures[axis] += int(bool(left))

    packet = {
        "schema": "marici.physical-common-rank9-absolute-comparison.v1",
        "prime": m.PRIME,
        "ambient": AMBIENT,
        "cutoff": CUTOFF,
        "twist_gamma_mod_prime": GAMMA,
        "absolute_dimension": len(a_free),
        "common_intrinsic_core_dimension": len(intrinsic_core),
        "absolute_image_dimension": len(image_span),
        "absolute_relation_failures": relation_failures,
        "absolute_relation_failure_support": relation_failure_support,
        "absolute_image_outside_intrinsic_core": image_outside_core,
        "connection_intertwining_failures": intertwining_failures,
    }
    half_twist = GAMMA == (m.PRIME - 1) // 2
    packet["canonical_isomorphism_at_tested_cutoff"] = (
        packet["absolute_dimension"] == 9
        and packet["common_intrinsic_core_dimension"] == 9
        and packet["absolute_image_dimension"] == 9
        and packet["absolute_relation_failures"] == 0
        and packet["absolute_image_outside_intrinsic_core"] == 0
        and packet["connection_intertwining_failures"] == [0, 0]
    )
    packet["physical_half_twist_failure_signature"] = (
        packet["absolute_dimension"] == 9
        and packet["common_intrinsic_core_dimension"] == 6
        and packet["absolute_image_dimension"] == 6
        and packet["absolute_relation_failures"] == 0
        and packet["absolute_image_outside_intrinsic_core"] == 0
        and packet["connection_intertwining_failures"] == [3, 3]
    )
    packet["passed"] = (
        packet["physical_half_twist_failure_signature"]
        if half_twist
        else packet["canonical_isomorphism_at_tested_cutoff"]
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
