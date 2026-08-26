# First-row plus signed-J kernel (WP296)

## Complementary CP-even readout

Extend WP295's signed-$J$ probe by the complete first row of CKM moduli and
the six ordered masses. These are weak-basis-invariant physical readouts. They
are not source operations merely because they are measurable.

## Exact hostile pair

Fix $s_{12},c_{12},s_{13},c_{13}$ and the CP phase at the exact WP295 values.
Compare

\[
(s_{23},c_{23})=(5/13,12/13)
\]

with its interchange. The first CKM row is independent of this exchange, and
the Jarlskog invariant depends on the symmetric product $s_{23}c_{23}$.
Therefore all six masses, all three first-row moduli, and signed $J$ agree.

The lower two CKM rows differ. Both matrices remain exactly unitary, so the
pair consists of physically inequivalent `physical16` points in one contextual
class of the enlarged probe family.

## Classification

The enlarged family is a physical partial separator, neither a selector nor a
texture rigidifier. Adding more readouts can eventually restore faithfulness,
but it does not explain or select their numerical values. The next missing
readout lies in a lower row or column; the missing selector remains a
source-derived operation on those CP-even degrees of freedom.

Run `uv run --with sympy python
research/flavor/checkers/wp296_first_row_signed_j_kernel.py` to regenerate the
exact hostile-pair audit.
