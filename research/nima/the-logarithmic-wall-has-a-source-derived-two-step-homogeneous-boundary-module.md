# The logarithmic wall has a source-derived two-step homogeneous boundary module

## Scope

The minimal Mellin chain has zero Hilbert traces at both logarithmic ends, so a nonzero wall requires a boundary extension. The transformed differential operators determine the smallest candidate extension algebraically: a two-step homogeneous module, not a freely added scalar wall.

Recall

\[
Q_-=
\left(\partial_q-\frac32\right)
\left(\partial_q-\frac12\right),
\]

\[
P_+=\partial_q^2-\frac14,
\]

and

\[
\widehat{\mathsf D}
=
e^{-q}\left(\partial_q-\frac12\right).
\]

## Indicial modes on one logarithmic end

The homogeneous equation

\[
Q_-g=0
\]

has the two solutions

\[
w_0(q)=e^{q/2},
\qquad
w_1(q)=e^{3q/2}.
\]

Their derivative incidences are

\[
\widehat{\mathsf D}w_0=0,
\]

\[
\widehat{\mathsf D}w_1=w_0.
\]

Moreover,

\[
P_+w_0=0.
\]

Therefore the chain closes on the two-dimensional boundary module

\[
\mathcal W_+
=
\operatorname{span}\{w_0,w_1\},
\]

with the nilpotent incidence pattern

\[
w_1
\longmapsto
w_0
\longmapsto
0.
\]

This is the minimal wall-plus-partner structure forced by the differential square.

## Original-coordinate meaning

Since

\[
(\mathcal Uf)(q)=e^{q/2}f(e^q),
\]

the mode \(w_0=e^{q/2}\) corresponds to the constant function

\[
f_0(x)=1.
\]

The mode \(w_1=e^{3q/2}\) corresponds to

\[
f_1(x)=x.
\]

Thus the familiar constant wall and its linear conjugate partner are not guessed auxiliary coordinates. They are precisely the two indicial modes of the shifted even-potential completion.

Ordinary differentiation gives

\[
\partial_x f_0=0,
\qquad
\partial_x f_1=1,
\]

which is the original-coordinate form of the same two-step module.

## Why one wall coordinate is insufficient

Adding only \(w_0\) creates a dark boundary coordinate:

\[
\widehat{\mathsf D}w_0=0.
\]

It survives in the boundary quotient but is invisible to the derivative incidence. The partner \(w_1\) supplies the incoming coordinate whose incidence lands in \(w_0\).

Therefore a faithful boundary constructor must retain at least:

- the wall coefficient of \(w_0\);
- the partner coefficient of \(w_1\);
- the incidence arrow \(w_1\mapsto w_0\).

This recovers the earlier abstract conclusion that a dynamic wall requires a conjugate partner, now directly from the source differential operator.

## Reciprocal end

Reflection \(q\mapsto-q\) produces the reciprocal indicial modes

\[
\widetilde w_0=e^{-q/2},
\qquad
\widetilde w_1=e^{-3q/2},
\]

with the conventionally reflected derivative arrow. These belong to the opposite logarithmic end and must not be identified with \(w_0,w_1\) before the reciprocal sewing map is supplied.

The completed boundary carrier is therefore at least a two-sheet object

\[
\mathcal W_+\oplus\mathcal W_-,
\]

followed by a source-authorized sewing relation.

## Affine extension

A candidate extended source space has the form

\[
\mathcal X_{\mathrm{ext}}
=
\mathcal X_{\min}
\dotplus
\mathcal W_+
\dotplus
\mathcal W_-,
\]

understood as an asymptotic or rigged boundary sum rather than an \(L^2\)-orthogonal sum. The wall modes are not Hilbert vectors on the full line.

To make this construction rigorous, one must provide:

1. cutoff-independent asymptotic coefficient maps;
2. a topology on the boundary module;
3. the Green boundary form pairing the two coefficients;
4. reciprocal reflection and sewing;
5. proof that the chain operators descend modulo the minimal domain.

## No automatic positivity

The indicial calculation determines the dimension and incidence of the boundary module. It does not determine its Hermitian Green metric, orientation sign, or positive loading margin. Those still require the causal-history or source boundary form.

## Result

The smallest source-derived nonzero wall extension is not rank one. On each logarithmic end it is the two-step module

\[
w_1\mapsto w_0\mapsto0,
\]

corresponding in original coordinates to

\[
x\mapsto1\mapsto0.
\]

This identifies the exact boundary carrier on which the missing wall Green form must be constructed.
