---
id: 563
date: 2026-08-18
title: The Square-Root Sign Lattice Does Not Remove the Lower Index Two
authors:
  - marici.Nima
---

# The Square-Root Sign Lattice Does Not Remove the Lower Index Two

Entry 562 leaves a \(\mathbb Z/2\) obstruction when reconstructing the two
resolved sheets from their invariant sum and anti-invariant difference. This
entry tests whether the physical square-root coefficient canonically removes
that obstruction.

Let \(C_2=\langle\tau\rangle\) act by exchanging \(D_+\) and \(D_-\). The
trivial and sign generators map to the sheet lattice by

\[
s\longmapsto D_++D_-,
\qquad
d\longmapsto D_+-D_-.
\]

In sheet coordinates this is

\[
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\]

whose determinant is \(-2\). Therefore

\[
\boxed{
\mathbb Z_{\rm triv}\oplus\mathbb Z_{\rm sign}
\hookrightarrow
\mathbb Z[D_+,D_-]
}
\]

has index two.

The physical form \(1/w\) supplies the sign character and identifies the
anti-invariant line \(d\). It does not supply the half-integral character
projectors

\[
e_\pm=\frac{1\pm\tau}{2}.
\]

Indeed, modulo two the invariant and anti-invariant generators coincide:

\[
D_++D_-\equiv D_+-D_-\pmod2.
\]

Thus the sign local system records which character is physical but does not
split the integral regular representation.

## Verdict

\[
\boxed{
\text{square-root orientation}
\quad\not\Rightarrow\quad
\text{integral half-sum splitting}.
}
\]

The Čech comparison becomes canonically character-split only over

\[
\mathbb Z[1/2]
\]

or a field of characteristic different from two. An integral lift would
require additional source data furnishing a genuine half-lattice, not merely
the existing double cover or its sign coefficient.

This sharpens Entry 559: the physical anti-invariant boundary sector is
well-defined integrally, but combining it with the invariant sector into
individual sheet coordinates retains the two-primary extension.

## Next gate

Formulate the source-to-boundary comparison equivariantly, without splitting
the sheet lattice. Over \(\mathbb Z[C_2]\), test the invariant and
anti-invariant maps separately and retain the mod-two extension class. A
physical theorem should not require individual \(D_\pm\) coordinates.

The executable audit is
\`research/benincasa/check_generic_lower_deck_integral_splitting.py\`.
