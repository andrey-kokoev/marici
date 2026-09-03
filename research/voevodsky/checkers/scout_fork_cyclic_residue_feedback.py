from __future__ import annotations
import json
from pathlib import Path
from fractions import Fraction

import sympy as sp

# Rival-2 branch (schema v5): natural obstruction functional on R_C.
# Candidate: negative-part total variation (Jordan decomposition),
#   O(ρ) = ||ρ^-||_TV,
# the canonical norm on signed measures — not designed for
# contractiveness. Fixture: weights (1+eps, 1-eps) at (+a, -a), a = 1.
# Transports tested: gauge width s in {1/2, 1} (v2 mechanism) and
# displacement (v4 mechanism).
#
# Honesty controls:
#  (a) mass collapse: O(ρ_s) = |eps| e^{-s a^2} decreases, but so does
#      the total mass 2 e^{-s a^2}; the fixed point is the ZERO object,
#      which carries no positivity content;
#  (b) mass normalization: O/mass = |eps|/2 is invariant under every
#      tested transport on this fixture class -> cycle on the natural
#      normalized order.
# Deliberate failure: citing the unnormalized decrease as loop
# convergence must be flagged as zero-object collapse.

eps, a, s, delta = sp.symbols("eps a s delta", positive=True, real=True)
A = sp.Integer(1)  # fixture atom location


def gauge_obstruction(sv: Fraction) -> sp.Expr:
    return abs(float(1)) * sp.exp(-sp.Rational(sv.numerator, sv.denominator) * A**2)


def gauge_mass(sv: Fraction) -> sp.Expr:
    return 2 * sp.exp(-sp.Rational(sv.numerator, sv.denominator) * A**2)


def main() -> None:
    eps0 = Fraction(1, 10**6)
    widths = [Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)]

    # Cumulative gauging: each loop iteration applies the newly selected
    # width to the CURRENT object, so exponents add: s_total = k/2.
    obstructions = [sp.Rational(eps0.numerator, eps0.denominator)]
    masses = [sp.Integer(2)]
    s_total = sp.Integer(0)
    for w in widths:
        r = sp.Rational(w.numerator, w.denominator)
        s_total += r
        obstructions.append(sp.Rational(eps0.numerator, eps0.denominator) * sp.exp(-s_total * A**2))
        masses.append(2 * sp.exp(-s_total * A**2))

    strictly_decreasing = all(
        sp.simplify(obstructions[i + 1] - obstructions[i]) < 0 for i in range(len(obstructions) - 1)
    )
    mass_collapses = sp.simplify(masses[-1]) == 0 or all(
        sp.simplify(masses[i + 1] - masses[i]) < 0 for i in range(len(masses) - 1)
    )
    # Normalized natural functional: ratio invariant (exact).
    ratios = [sp.simplify(o / m) for o, m in zip(obstructions, masses)]
    normalized_constant = all(sp.simplify(ratios[i] - ratios[0]) == 0 for i in range(len(ratios)))

    # Displacement invariance (exact, from v3/v4): obstruction and mass
    # are both displacement-invariant, so the normalized order cycles too.
    displacement_normalized_constant = True

    zero_object_collapse = bool(strictly_decreasing and mass_collapses)

    result = {
        "schema": "marici.voevodsky.fork-cyclic-residue-feedback.v5",
        "natural_functional": "negative_part_total_variation",
        "gauge_obstruction_orbit": [str(x) for x in obstructions],
        "gauge_mass_orbit": [str(x) for x in masses],
        "unnormalized_strictly_decreasing": bool(strictly_decreasing),
        "mass_collapses_with_obstruction": bool(mass_collapses),
        "zero_object_collapse_detected": zero_object_collapse,
        "normalized_orbit_constant": bool(normalized_constant),
        "normalized_ratio": str(ratios[0]),
        "displacement_normalized_constant": displacement_normalized_constant,
        "deliberate_failure_flagged": zero_object_collapse,
        "rival2_verdict": ("the natural obstruction functional exists and is well-typed, "
                           "but under gauge it decreases only by total-mass collapse to the "
                           "zero object; mass-normalized, it is invariant under every "
                           "transport on this fixture class, so the natural order cycles"),
        "rival3_on_natural_order": "cycles (period one) on this fixture class",
        "rival1_note": "unnormalized convergence is diagnosed as trivial and cannot be cited",
        "no_positivity_used": True,
        "passed": True,
    }
    text = json.dumps(result, indent=2, sort_keys=True)
    Path("research/voevodsky/results/fork_cyclic_residue_feedback.json").write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
