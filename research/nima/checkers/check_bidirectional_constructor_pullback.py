from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/nima/results/bidirectional-constructor-pullback.json"


@dataclass(frozen=True)
class Constructor:
    constructor_id: str
    source_type: str
    target_type: str
    requirement_rules: dict[str, frozenset[str]]

    def pullback(self, requirements: frozenset[str]) -> frozenset[str]:
        missing_rules = sorted(requirements - self.requirement_rules.keys())
        if missing_rules:
            raise KeyError(
                f"{self.constructor_id}: undeclared target requirements {missing_rules}"
            )
        pulled: set[str] = set()
        for requirement in requirements:
            pulled.update(self.requirement_rules[requirement])
        return frozenset(pulled)


def compose_pullback(
    first: Constructor,
    second: Constructor,
    requirements: frozenset[str],
) -> frozenset[str]:
    assert first.target_type == second.source_type
    return first.pullback(second.pullback(requirements))


def residual(required: frozenset[str], supplied: frozenset[str]) -> list[str]:
    return sorted(required - supplied)


def monitor(x: Fraction) -> Fraction:
    return Fraction(1, 100) + Fraction(5, 4) * x - Fraction(1, 2) * x * x


def main() -> None:
    prepare = Constructor(
        constructor_id="prepare",
        source_type="source",
        target_type="carrier",
        requirement_rules={
            "typed_observer": frozenset({"source_incidence"}),
            "observer_authority": frozenset({"source_authority"}),
        },
    )
    observe = Constructor(
        constructor_id="observe",
        source_type="carrier",
        target_type="record",
        requirement_rules={
            "faithful_record": frozenset({"typed_observer", "observer_authority"})
        },
    )

    direct = compose_pullback(
        prepare, observe, frozenset({"faithful_record"})
    )
    staged = prepare.pullback(observe.pullback(frozenset({"faithful_record"})))
    assert direct == staged == frozenset({"source_incidence", "source_authority"})

    reverse_order_rejected = False
    try:
        observe.pullback(prepare.pullback(frozenset({"typed_observer"})))
    except KeyError:
        reverse_order_rejected = True
    assert reverse_order_rejected

    rh_compression = Constructor(
        constructor_id="rh_trace_compression",
        source_type="function_trace",
        target_type="scalar_record",
        requirement_rules={
            "fourier_faithful_observer": frozenset(
                {"full_function_trace", "completion_continuity"}
            )
        },
    )
    rh_required = rh_compression.pullback(
        frozenset({"fourier_faithful_observer"})
    )
    rh_supplied = frozenset({"moment_germ", "determinant_line", "completion_continuity"})
    rh_residual = residual(rh_required, rh_supplied)
    assert rh_residual == ["full_function_trace"]

    moment_view = {
        "zero": "zero_germ",
        "theta": "visible_germ",
        "flat_bump": "zero_germ",
    }
    full_trace_view = {
        "zero": "zero_trace",
        "theta": "theta_trace",
        "flat_bump": "flat_bump_trace",
    }
    assert moment_view["zero"] == moment_view["flat_bump"]
    assert full_trace_view["zero"] != full_trace_view["flat_bump"]

    flavor_response = Constructor(
        constructor_id="flavor_rank_nine_response",
        source_type="flavor_source",
        target_type="physical16_record",
        requirement_rules={
            "proper_selector": frozenset(
                {
                    "nonaligned_tensor",
                    "derived_linear_coefficients",
                    "rank9_all_sheets",
                }
            )
        },
    )
    flavor_required = flavor_response.pullback(frozenset({"proper_selector"}))
    flavor_supplied = frozenset({"rank9_all_sheets", "response_capacity"})
    flavor_residual = residual(flavor_required, flavor_supplied)
    assert flavor_residual == ["derived_linear_coefficients", "nonaligned_tensor"]

    optical_inverse = Constructor(
        constructor_id="quadratic_monitor_inverse",
        source_type="optical_source",
        target_type="monitor_record",
        requirement_rules={
            "unique_physical_inverse": frozenset(
                {"three_level_calibration", "monotone_source_domain"}
            )
        },
    )
    optical_required = optical_inverse.pullback(
        frozenset({"unique_physical_inverse"})
    )
    optical_supplied = frozenset({"three_level_calibration"})
    optical_residual = residual(optical_required, optical_supplied)
    assert optical_residual == ["monotone_source_domain"]

    x_left = Fraction(1, 4)
    x_right = Fraction(9, 4)
    y_left = monitor(x_left)
    y_right = monitor(x_right)
    assert x_left != x_right
    assert y_left == y_right == Fraction(233, 800)

    result = {
        "schema": "marici.bidirectional_constructor_pullback.v1",
        "status": "pass",
        "composition": {
            "direct_pullback": sorted(direct),
            "staged_pullback": sorted(staged),
            "contravariant_order_exact": direct == staged,
            "forward_order_used_for_backward_rejected": reverse_order_rejected,
        },
        "rh": {
            "required": sorted(rh_required),
            "supplied": sorted(rh_supplied),
            "residual": rh_residual,
            "collision": ["zero", "flat_bump"],
            "moment_view_collision": True,
            "full_trace_separates": True,
        },
        "flavor": {
            "required": sorted(flavor_required),
            "supplied": sorted(flavor_supplied),
            "residual": flavor_residual,
            "classification": "capacity_not_selector",
        },
        "optics": {
            "required": sorted(optical_required),
            "supplied": sorted(optical_supplied),
            "residual": optical_residual,
            "collision_inputs": [str(x_left), str(x_right)],
            "collision_record": str(y_left),
        },
        "claim_boundary": (
            "Finite atomic requirement compiler with three exact pilots; "
            "no general predicate language or DPC integration."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
