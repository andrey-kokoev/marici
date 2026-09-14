#!/usr/bin/env python3
"""Verify the antipode variance mate from a left native endpoint orbit to the
right-precomposition conormal orbit.

For homogeneous operations q,g, the transported left action on the conormal
right module is y triangleleft q = (-1)^(|q||g|) y*S(q).  The checker uses the
recovered Branch B native operation algebra through total degree six.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "research/chatgpt/check_marici_primitive_conormal_column_20260908.py"


def load_source():
    spec = importlib.util.spec_from_file_location("primitive_conormal", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {SOURCE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(output: Path) -> None:
    b = load_source()
    checks = 0

    def check(value, tag):
        nonlocal checks
        if not value:
            raise AssertionError(tag)
        checks += 1

    def antipode(value):
        out = {}
        for word, coefficient in value.items():
            seq = b.flatten(word)
            # All six letters are odd primitive elements.  The graded
            # anti-algebra sign combines with S(x)=-x for every letter.
            reversed_term = b.normal_form(tuple(reversed(seq)))
            out = b.add(
                out,
                b.scale(reversed_term,
                        coefficient * b.pm(len(seq) * (len(seq) + 1) // 2)),
            )
        return out

    generators = {J: b.generator(J) for J in b.MIXED}
    check(len(generators) == 49, "all_49_relative_generators")
    for operation in generators.values():
        check(antipode(operation) == b.scale(operation, -1),
              "primitive_antipode_is_minus_identity")

    atom35 = b.normal_form((2,))
    checked_words = 0
    checked_actions = 0
    quadratic_signs = []

    for degree in range(7):
        for word in b.relative_words(degree):
            g = b.relative_image(word)
            sg = antipode(g)
            image = b.mul(atom35, sg)
            check(bool(image), "antipode_mate_conormal_image_nonzero")
            checked_words += 1

            for key, q in generators.items():
                qdegree = len(key)
                if qdegree + degree > 6:
                    continue
                source_action = b.mul(q, g)
                lhs = b.mul(atom35, antipode(source_action))
                target_right_action = b.mul(image, antipode(q))
                rhs = b.scale(target_right_action, b.pm(qdegree * degree))
                check(lhs == rhs, "graded_antipode_variance_equation")
                checked_actions += 1

                if degree == 0 and qdegree == 2:
                    expected = b.scale(b.mul(atom35, q), -1)
                    check(lhs == expected,
                          "quadratic_primitive_mate_requires_minus_sign")
                    quadratic_signs.append({
                        "operation_labels": [b.LABELS[i] for i in key],
                        "source": "q cup endpoint primitive",
                        "target": "minus (conormal primitive right-precomposed by q)",
                    })

    check(len(quadratic_signs) == 9,
          "nine_quadratic_primitive_signs_recorded")

    payload = {
        "status": "graded_antipode_variance_mate_verified_through_degree_six",
        "checks": checks,
        "source": str(SOURCE),
        "relative_words_checked": checked_words,
        "operation_actions_checked": checked_actions,
        "formula": {
            "mate": "Phi(g m_sigma) = j35(v) right-precomposed by S(g)",
            "transported_action": "Phi(q g m) = (-1)^(|q||g|) Phi(g m) right-precomposed by S(q)",
            "primitive_generators": "S(r)=-r",
        },
        "quadratic_primitive_images": quadratic_signs,
        "scope": {
            "operation_algebra": "native relative Hopf algebra",
            "conormal_side": "right precomposition orbit of j35(v)",
            "endpoint_side": "left cup orbit with operation coordinates",
            "verified_degree_bound": 6,
            "all_degree_reason": "graded antipode anti-algebra identity plus target orbit injectivity",
            "chain_homotopies_on_spatial_endpoint": False,
            "line_and_support_transport": False,
        },
        "next_gate": "combine this antipode sign with the primitive fine-frame chain mate and construct line/support-compatible spatial endpoint intertwiners",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "checks": checks,
        "relative_words": checked_words,
        "actions": checked_actions,
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "research/voevodsky/conormal-variance-antipode-mate.json",
    )
    main(parser.parse_args().output)
