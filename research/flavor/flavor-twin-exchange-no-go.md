# Twin-branch exchange no-go: WP1147

## Question

Does the selected localized \(SU(6)\) cell carry a physical twin-branch
exchange symmetry?

## DPC resolution

- **Problem:** determine whether equal-weight twin branches have physical
  exchange symmetry after localization.
- **Conjecture:** the twin branches have an unbroken exchange symmetry in the
  selected cell.
- **Rivals:** prelocalization multiplicity exchange; postlocalization
  unbroken exchange; equal algebraic weights only; quartet-choice quotient.
- **Risky consequences:** exchange must fix the selected quartet cell, leave
  the production kernel invariant, preserve gain \(3/2\), and make the three
  matching orbits physical.
- **Falsification attempt:** WP1056's exchange swaps the two one-quartet
  cells rather than fixing either selected cell. No post-localization
  exchange or kernel-invariance certificate is sourced.
- **Residual:** a quotient of the symmetric quartet choice or a new production
  packet may restore exchange.
- **Disposition:** reject unbroken physical twin exchange and record the typed
  blocker.

## Typed blocker

`post_localization_exchange_certificate` must derive an exchange that fixes
the selected quartet localization, leaves the production kernel invariant,
and preserves gain \(3/2\).

Checker: `research/flavor/checkers/wp1147_twin_exchange_no_go.py`

Result: `results/wp1147_twin_exchange_no_go.json`
