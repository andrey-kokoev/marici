# Hostile beta deformation shows that the current width is source-geometric

Replace the magnetic source coefficient

\[
(4-a)^{\overline j}
\]

by

\[
(\beta-a)^{\overline j},
\]

without claiming that \(\beta\ne4\) defines an authorized magnetic theory.
This is a counterfactual test of the proposed explanation.

The current-width law is not invariant under this replacement. At
\((g,q)=(3,1)\), with a sufficiently large tested cutoff, the quotient widths
are

\[
D^{(0)}_{3,1}=4,
\qquad
D^{(4)}_{3,1}=5,
\qquad
D^{(5)}_{3,1}=6.
\]

Thus the original formula is not produced by support geometry alone.

## Two source-selected boundary atoms

The deformation explains where \(\beta\) enters.

At \(a=0\), the source polynomial has only its upper coefficient:

\[
c_g=\beta^{\overline g}.
\]

The two-row cokernel functional generalizes immediately and detects the
zero-depth current with value

\[
-2g\,\beta^{\overline g}.
\]

For \(\beta=0\), this atom vanishes and the first current port disappears.

At \(a=\beta\), the source polynomial has only its lower coefficient

\[
c_0=(-1)^g\beta^{\overline g}.
\]

This second boundary atom belongs to the admitted depth lattice
\(\{0,2,4,\ldots\}\) exactly when \(\beta\) is a nonnegative even
integer.

Therefore changing \(\beta\) changes both endpoint data and, through parity,
whether the lower atom is constructible at all.

## Explanatory consequence

The native value \(4\) is not a fitted scalar decorating an otherwise fixed
graph. It locks a source zero to the admitted even pole-depth lattice. The
finite current width must be derived from interaction among:

- the upper atom at \(a=0\);
- the lower atom at \(a=\beta\);
- reflection-component overlap controlled by \((g,q)\);
- exceptional target circuits.

The hostile deformation supports the local-boundary explanation while
falsifying any claim that the native width formula depends only on interval
support.

A general closed formula \(D^{(\beta)}_{g,q}\) remains open.

Replay with: python research/strominger/checkers/magnetic_beta_deformation_checks.py
