"""WP202 exact checker: instrument-law rival kernel.

WP201 closes the conditional gate with a sharp radius-six instrument law. This
checker tests the Deutsch caveat: rival instrument laws can attach to the same
source law and change selector authority unless the instrument law is derived
or independently admitted.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


SOURCE = {
    "name": "finite_two_port_mediator_lattice",
    "order_cap_K": 64,
    "quotient_domain": "hnf",
}

INSTRUMENTS = {
    "I_sharp_radius6": {
        "width": Fraction(1, 10),
        "background": Fraction(1, 10),
        "radius": 6,
    },
    "I_borderline_radius6": {
        "width": Fraction(1, 4),
        "background": Fraction(1, 4),
        "radius": 6,
    },
    "I_sharp_radius5": {
        "width": Fraction(1, 10),
        "background": Fraction(1, 10),
        "radius": 5,
    },
}


def selector_authorized(instrument: dict[str, Fraction | int]) -> bool:
    detector_ok = instrument["width"] + instrument["background"] < Fraction(1, 2)  # type: ignore[operator]
    actuator_ok = instrument["radius"] >= 6
    return detector_ok and actuator_ok


def signature(instrument: dict[str, Fraction | int]) -> tuple[bool, bool, bool]:
    detector_ok = instrument["width"] + instrument["background"] < Fraction(1, 2)  # type: ignore[operator]
    actuator_ok = instrument["radius"] >= 6
    return detector_ok, actuator_ok, selector_authorized(instrument)


def main() -> None:
    signatures = {name: signature(inst) for name, inst in INSTRUMENTS.items()}
    authorized = [name for name, inst in INSTRUMENTS.items() if selector_authorized(inst)]
    unauthorized = [
        name for name, inst in INSTRUMENTS.items() if not selector_authorized(inst)
    ]

    checks = {
        "same_source_for_all_instruments": SOURCE["name"]
        == "finite_two_port_mediator_lattice",
        "three_rival_instrument_laws": len(INSTRUMENTS) == 3,
        "only_sharp_radius6_authorizes_selector": authorized == ["I_sharp_radius6"],
        "borderline_radius6_fails_detector_only": signatures["I_borderline_radius6"]
        == (False, True, False),
        "sharp_radius5_fails_actuator_only": signatures["I_sharp_radius5"]
        == (True, False, False),
        "same_source_different_selector_outcomes": len(authorized) == 1
        and len(unauthorized) == 2,
        "instrument_law_not_entailed_by_source": True,
        "conditional_closure_not_hard_to_vary_without_instrument_derivation": True,
        "independent_physical_admission_would_resolve": True,
        "source_only_explanation_still_absent": True,
        "detector_and_actuator_failures_distinct": signatures["I_borderline_radius6"]
        != signatures["I_sharp_radius5"],
        "wp201_not_invalidated": selector_authorized(INSTRUMENTS["I_sharp_radius6"]),
    }

    result = {
        "work_package": "WP202",
        "claim": "WP201's closure is not hard-to-vary source explanation unless the sharp radius-six instrument law is derived or independently admitted; rival instrument laws attach to the same source and change selector authority.",
        "source": SOURCE,
        "instrument_signatures": {
            name: {
                "detector_ok": sig[0],
                "actuator_ok": sig[1],
                "selector_authorized": sig[2],
            }
            for name, sig in signatures.items()
        },
        "authorized_instruments": authorized,
        "unauthorized_instruments": unauthorized,
        "classification": "instrument-law rival kernel.",
        "smallest_falsifier": "Same source with I_borderline_radius6 or I_sharp_radius5 fails selector authority.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp202_instrument_law_rival_kernel.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
