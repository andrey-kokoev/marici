# Source-to-generator audit — current disposition

## Supersession, 7 October 2026

This replaces the earlier selection narrative after the closure audit found
an incomplete commutant, confused source/spectral coordinates, and unsupported
claims from a print-driven checker. The original text, source and receipts
are hash-preserved in `quarantine/20261007-tick-evidence/manifest.json`.
Repair record: `tick-evidence-repair-20261007.md`.

Do not use `check_tick_selects_generator.py` or its old receipt as evidence.
That entrypoint now refuses execution with code 2. Iteration 3 also quarantines
`check_general_square_generator.py` and its receipt after finding false
continuous-parameter and post-selection candidate claims; their originals
are in `quarantine/20261007-general-square-generator/`.

The source-backed unitary implementation already exists in
`native-square-controlled-hamiltonian.md`. The new image comparison reuses its
checked algebra rather than the narrower numerical consistency checker.

## Start from the actual full source

For the fixed-source Bool/notEquiv specialization, the existing theorem is

\[
\operatorname{Tick}(s)\simeq\operatorname{Schedule}\times\operatorname{Schedule}.
\]

`agda/TickRetainedStructure.agda` includes the entire return-section function,
attachments and witness fields. Its reconstruction inverse and observation
factorization close the structural-information question on this specialization.
Syntactic omission of fields does not establish loss of distinguishable data.
This does not classify all WG sources or select an analytic interpretation.

## Keep three different questions separate

| Question | Current disposition | Evidence |
|---|---|---|
| Does the full Bool Tick have extra independent information beyond its ordered tags? | Closed negatively, at fixed source and up to the stated path equality. | `tick-full-structure-classification.md`; `TickRetainedStructure.agda`. |
| Do the source/schedule constraints uniquely select a retained stochastic interpolation, modulo parameter changes? | Closed negatively in the explicitly declared class. Straight and bowed paths have different images. | `tick-admissible-interpretations.md`; `check_tick_interpretation_nonuniqueness.py`; `TickConcreteImageObstruction.agda` at its stated completion-valued scope. |
| Do commuting unitary composition, positive axis generators, axis symmetry and the same corners/return law select an image up to parameters and phase? | Closed negatively in the declared retained unitary annotation class. A mixed-projector rival leaves the entire baseline product-state image. | `tick-unitary-image-nonuniqueness.md`; exact determinant 0 versus squared modulus 3/16. |
| Is a physical unitary Hamiltonian or its calibrated rate selected? | Not established by these results. Intermediate tensor locality and a native analytic-return interpretation were not assumed in the annotation class. | Requires independently justified source/readout constraints, not more examples in the closed class. |

These closures remain separate. A new selection attempt needs new constraints
or a distinct comparison, not another compatible construction or another proof
of source retention.

## Correct matrix statement

For the supplied four-dimensional bit-flip model, define

\[
P_L=(I-L)/2,\qquad P_R=(I-R)/2.
\]

These projectors commute but have overlapping ranges. If a Hermitian H is
additionally required to commute with both L and R, its general form is

\[
H=cI+aP_L+bP_R+dP_LP_R,
\]

with real coefficients. Its four joint eigenvalues are
\(c,c+a,c+b,c+a+b+d\). Requiring the exact matrix endpoint
\(\exp(-i\pi H)=LR\) in this class gives even integer c,d and odd integer a,b:
a discrete lattice, not four remaining continuous parameters.
The endpoint condition alone does not impose the individual commutations.
Dropping the mixed term requires a further assumption; it does not follow
from the two bit flips commuting.

The explicit supplied family

\[
U(\alpha,\beta)=\exp(-i\alpha P_L)\exp(-i\beta P_R)
\]

has the expected four corner operators and two ordered boundary routes.
The repaired `checkers/check_tick_to_square_realization.py` tests finite
numerical matrix consistency and derivative controls for that family. It
neither evaluates native Tick terms nor supplies a new formal analytic bridge.
In particular, computational-basis vectors must not be treated as joint
eigenvectors: \((P_L+P_R)e_{00}\ne0\).

## Evidence boundary

Historical diagnoses remain reproducible against their archived versions via
`checkers/check_closure_understanding_audit_20261007.py`. Current failure-gate
verification belongs to `checkers/check_tick_evidence_repair.py`, not to the
old expected-defect receipt. No physical generator-selection theorem is
inferred from either kind of checker.
