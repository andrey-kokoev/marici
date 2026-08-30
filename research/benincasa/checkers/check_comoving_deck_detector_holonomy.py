"""Test the co-moving detector repair of the infinity sheet-selector path."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PORT = ROOT / "results" / "infinity-relative-port-integral-extension.json"
OUTPUT = ROOT / "results" / "comoving-deck-detector-holonomy.json"


def main() -> None:
    port = json.loads(PORT.read_text(encoding="utf-8"))
    theta = sp.symbols("theta", real=True)
    imaginary = sp.I
    identity = sp.eye(2)
    deck = sp.Matrix([[0, 1], [1, 0]])
    pauli_y = sp.Matrix([[0, -imaginary], [imaginary, 0]])
    selector_path = sp.diag(1, sp.exp(imaginary * theta))
    moving_deck = sp.simplify(selector_path * deck * selector_path.conjugate().T)
    expected_deck = sp.simplify(sp.cos(theta) * deck + sp.sin(theta) * pauli_y)

    checks = {
        "selector_endpoint_is_Z": selector_path.subs(theta, sp.pi) == sp.diag(1, -1),
        "moving_detector_is_conjugated_source_detector": moving_deck == expected_deck,
        "strict_covariance_holds": sp.simplify(moving_deck * selector_path - selector_path * deck) == sp.zeros(2),
        "moving_detector_is_involutive": sp.simplify(moving_deck * moving_deck) == identity,
        "moving_detector_is_hermitian": moving_deck.conjugate().T == moving_deck,
        "oriented_detector_returns_with_minus_sign": moving_deck.subs(theta, sp.pi) == -deck,
        "projective_detector_closes": (
            moving_deck.subs(theta, sp.pi) == deck
            or moving_deck.subs(theta, sp.pi) == -deck
        ),
        "projective_loop_has_odd_lift_parity": moving_deck.subs(theta, sp.pi) != moving_deck.subs(theta, 0),
        "parity_matches_integral_extension_order": port["obstruction_order"] == 2,
    }
    failed = [name for name, passed in checks.items() if not passed]
    result = {
        "schema": "marici.comoving_deck_detector_holonomy.v1",
        "selector_deformation": "U(theta)=diag(1,exp(i*theta)), 0<=theta<=pi",
        "moving_detector": "X(theta)=U(theta) X U(theta)^dagger=cos(theta)X+sin(theta)Y",
        "strict_covariance": "X(theta)U(theta)=U(theta)X",
        "endpoint": "X(pi)=-X(0), hence projectively closed but not closed as an oriented integral detector",
        "projective_winding": 1,
        "oriented_lift_holonomy": -1,
        "checks": checks,
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "conclusion": "Co-moving transport removes the local deck-unlocking defect but transfers the obstruction into an odd projective detector loop with sign holonomy on the oriented integral lift.",
        "scope": "explicit minimal selector deformation on the two-sheet branch-gap port; no source authorization for the moving detector is inferred",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
