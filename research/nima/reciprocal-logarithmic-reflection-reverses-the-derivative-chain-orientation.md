# Reciprocal logarithmic reflection reverses the derivative-chain orientation

## Scope

The boundary sewing classification left one genuine bit: reciprocal reflection either preserves or reverses the derivative incidence. The Mellin half-density formulas decide this bit directly.

Let

\[
(\mathcal Rg)(q)=\overline{g(-q)}
\]

be antiunitary logarithmic reflection.

On the primal sheet, the derivative bridge is

\[
\widehat{\mathsf D}_+
=
e^{-q}\left(\partial_q-\frac12\right).
\]

## Reflected derivative

A direct calculation gives

\[
\mathcal R\widehat{\mathsf D}_+\mathcal R
=
-e^q\left(\partial_q+\frac12\right).
\]

Define the reciprocal-sheet derivative bridge by

\[
\widehat{\mathsf D}_-
=
e^q\left(\partial_q+\frac12\right).
\]

Then the exact reflection law is

\[
\mathcal R\widehat{\mathsf D}_+\mathcal R
=
-\widehat{\mathsf D}_-.
\]

Equivalently,

\[
\widehat{\mathsf D}_-\mathcal R
=
-\mathcal R\widehat{\mathsf D}_+.
\]

Thus reciprocal reflection reverses the chain arrow.

## Boundary modes

The primal modes are

\[
w_0=e^{q/2},
\qquad
w_1=e^{3q/2},
\]

with

\[
\widehat{\mathsf D}_+w_1=w_0,
\qquad
\widehat{\mathsf D}_+w_0=0.
\]

Their reflected modes are

\[
v_0=e^{-q/2},
\qquad
v_1=e^{-3q/2}.
\]

On the reciprocal sheet,

\[
\widehat{\mathsf D}_-v_1=-v_0,
\qquad
\widehat{\mathsf D}_-v_0=0.
\]

The sign reversal is therefore visible already on the two-dimensional boundary module.

## Canonical coefficient sewing

If both source and target coefficient frames normalize the nilpotent incidence as

\[
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\]

then the target partner must be reoriented by a minus sign. The canonical antiunitary sewing is

\[
R_{\partial}
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}C.
\]

It satisfies

\[
R_{\partial}N=-NR_{\partial}
\]

in the antilinear sense, preserves the Krein boundary metric, and squares to the identity.

The previously classified preserving option \(C\) is not compatible with the actual reflected differential bridge.

## Original-coordinate interpretation

The logarithmic reflection corresponds to multiplicative inversion, together with the half-density transport. Additive differentiation changes orientation under inversion. The minus sign is therefore geometric, not a fitted reciprocal phase.

This is distinct from ordinary parity \(x\mapsto-x\). The reflection here exchanges multiplicative ends \(x\to0\) and \(x\to\infty\).

## Consequence for the odd port

The boundary partner changes sign while the constant wall does not. Hence the ordered odd coordinate lives in the relative orientation between the two module levels.

Any scalar sewing that identifies both coefficients with the same sign erases this reciprocal character even if it preserves endpoint magnitudes and the indefinite Green form.

## Result

The remaining local sewing bit is fixed:

\[
\mathcal R\widehat{\mathsf D}_+\mathcal R
=
-\widehat{\mathsf D}_-.
\]

Therefore the source-authorized canonical boundary sewing is the orientation-reversing antiunitary

\[
R_{\partial}
=
\operatorname{diag}(1,-1)C.
\]

The local wall sewing now has no free parameter. The next unresolved constructor is the positive causal/history polarization that must couple this fixed Krein boundary module to the bulk endpoint cell.
