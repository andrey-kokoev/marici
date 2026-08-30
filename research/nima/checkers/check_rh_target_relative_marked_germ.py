import json
from pathlib import Path


# Source coordinates are analytic, primitive, square, archimedean,
# zero-frequency, and one presentation-only hidden coordinate.
def joint_signature(v):
    return v[:5]


def analytic_only(v):
    return v[0]


def admitted_transport(v):
    analytic, primitive, square, archimedean, zero, hidden = v
    return (
        analytic + primitive,
        primitive + square,
        square,
        archimedean + zero,
        zero,
        -hidden,
    )


def factored_temporal_realization(v):
    signature = joint_signature(v)
    return signature[0] + signature[4]


def hidden_temporal_realization(v):
    return v[5]


def relative_target(signature):
    analytic, primitive, square, archimedean, zero = signature
    return analytic + primitive * square + archimedean + zero


base = (2, 3, 5, 7, 11, 13)
same_germ = (2, 3, 5, 7, 11, -19)
assert joint_signature(base) == joint_signature(same_germ)
assert relative_target(joint_signature(base)) == relative_target(joint_signature(same_germ))
assert joint_signature(admitted_transport(base)) == joint_signature(admitted_transport(same_germ))

# A proposed temporal realization is an additional target operation. It may
# factor through the existing germ or force a refinement.
assert factored_temporal_realization(base) == factored_temporal_realization(same_germ)
assert hidden_temporal_realization(base) != hidden_temporal_realization(same_germ)

# The hidden direction is safely removed because every declared target map
# ignores it.
hidden_direction = (0, 0, 0, 0, 0, 1)
assert joint_signature(hidden_direction) == (0, 0, 0, 0, 0)

# Analytic-only completion is too coarse: it identifies packets with distinct
# primitive incidence and distinct native-arity target values.
analytic_collision = (2, 4, 5, 7, 11, 13)
assert analytic_only(base) == analytic_only(analytic_collision)
assert joint_signature(base) != joint_signature(analytic_collision)
assert relative_target(joint_signature(base)) != relative_target(joint_signature(analytic_collision))

# Nonlinear full-fiber hostile: q(x)=x^2 and r(x)=x^3 have identical
# differential kernels at x=1 and x=-1, yet r is not constant on the q-fiber.
def q(x):
    return x * x


def r(x):
    return x * x * x


assert q(-1) == q(1)
assert r(-1) != r(1)
assert (-2 != 0) and (2 != 0)

# Descent does not select a source representative of the hidden fiber.
representatives = [base, same_germ]
assert len({joint_signature(v) for v in representatives}) == 1
assert len(set(representatives)) == 2

result = {
    "schema": "marici.rh.target-relative-marked-germ.v1",
    "target_ports": ["analytic", "primitive", "square", "archimedean", "zero_frequency"],
    "target_invisible_hidden_direction_removed": True,
    "hidden_direction_stays_invisible_under_admitted_transport": True,
    "factored_temporal_realization_descends": True,
    "hidden_fiber_temporal_realization_descends": False,
    "hidden_fiber_temporal_realization_requires_germ_refinement": True,
    "analytic_only_completion_rejected": True,
    "nonlinear_full_fiber_hostile_detected": True,
    "descent_selects_source_representative": False,
    "verdict": "form the full target-fiber germ before native-arity totalization and keep source selection separate",
}

out = Path(__file__).parents[1] / "results" / "rh-target-relative-marked-germ.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
