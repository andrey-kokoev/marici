# Localized \(SU(6)\) clock-alignment gate: WP1058

## Question

Does WP1056's localized \(SU(6)\) bulk cell derive a common pole clock?

## Reducible bulk cell

After localizing one quartet, the bulk cell is

\[
6+8+1+4+2+2,
\qquad C=23.
\]

These are distinct residual-group sectors. An invariant mass-squared operator
therefore has one independent real eigenvalue on each block:

\[
(m_6^2,m_8^2,m_1^2,m_4^2,m_{2a}^2,m_{2b}^2).
\]

The exchange symmetry between the two \(\overline6\) parents identifies only

\[
m_{2a}^2=m_{2b}^2.
\]

It does not align the doublet mass with the \(6\), \(8\), \(1\), or retained
\(4\). Thus the localized cell has six mass blocks before exchange and five
after exchange, not one common clock.

## Exact hostiles

The unit vector is the desired clock:

\[
(1,1,1,1,1,1),
\qquad
\langle M^2\rangle_C=1.
\]

An exchange-even hostile shifts only the retained quartet:

\[
(1,1,1,2,1,1),
\qquad
\langle M^2\rangle_C=\frac{27}{23}.
\]

An exchange-breaking hostile shifts one doublet:

\[
(1,1,1,1,2,1),
\qquad
\langle M^2\rangle_C=\frac{25}{23}.
\]

The first hostile preserves the two-port exchange symmetry but still is not a
common pole clock. Localization and exchange alone therefore cannot authorize
\(M^2=1\).

## Relation to the irreducible spin cell

WP1054's irreducible spin-11 cell forces an invariant mass operator to be
scalar. WP1056's localized \(SU(6)\) cell is reducible, so Schur's lemma does
not apply. The two cells cannot be identified as clock cells without a new
projection or alignment law.

## Boundary

The next source must derive one of:

1. a common \(SU(6)\) parent mass surviving localization;
2. a branch-alignment theorem for the six residual sectors; or
3. a projection from the localized \(SU(6)\) cell to the irreducible spin-11
   pole cell while preserving the two ports.

Only then can \(M^2=1\) and \(p^2/M^2\) be source-derived. This packet does
not reject such a future law; it rejects declaring the common clock from
localization alone.

## Classification

Negative common-clock gate. WP1056 derives \((C,k)=(23,2)\), but its bulk cell
has five exchange-even independent mass blocks.

Checker: `research/flavor/checkers/wp1058_localized_su6_clock_alignment_gate.py`

Result: `results/wp1058_localized_su6_clock_alignment_gate.json`
