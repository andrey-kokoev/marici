# The order-three determinant is the finite three-stratum totalization law

## The totalization is multiplicative

For a finite-rank operator \(K\), define the first two additive currents

\[
P_1(K)=\operatorname{Tr}K,
\qquad
P_2(K)=\frac12\operatorname{Tr}K^2.
\]

The connected order-three logarithm is

\[
C_3(K)=\sum_{m\ge3}\frac1m\operatorname{Tr}K^m.
\]

The full determinant logarithm decomposes exactly as

\[
-\log\det(I-K)=P_1(K)+P_2(K)+C_3(K).
\]

Equivalently,

\[
\det(I-K)^{-1}
=
\exp(P_1(K)+P_2(K))\det_3(I-K)^{-1}.
\]

Thus the three Green-boundary strata are not added by an arbitrary scalar sum.
They are combined by a typed multiplicative totalization:

- the primitive current enters through first-order exponentiation;
- the square current enters through second-order exponentiation;
- the connected tail enters through the order-three determinant.

## Categorical form

At finite cutoff, the three-stratum carrier maps into a determinant line:

\[
\mathcal B^{(1)}\times
\mathcal B^{(2)}	imes
\mathcal B^{(3)}
\longrightarrow
\mathcal L_{\det}.
\]

Direct sum of labelled operators is sent to tensor product in the determinant
line.  The first two logarithmic currents are additive, while the connected
determinant is multiplicative.  The totalization is therefore a monoidal
functor only after the modalities are respected.

This supplies the finite dynamic operation that the previous stratification
left abstract.  It is the algebraic reason the first two currents must remain
as boundary anomaly data rather than being deleted from the order-three tail.

## Global obstruction

For the completed arithmetic operator, the connected part may exist as a
Schatten-three determinant while \(P_1\) and \(P_2\) do not exist as ordinary
scalar traces.  The finite identity then does not yield a scalar global
determinant.

Instead, \(P_1\) and \(P_2\) define boundary or anomaly-line data that must be
trivialized by the source-derived endpoint, seam, and archimedean Green law.
Until those trivializations are constructed, the total object is a section of
a relative determinant line, not a canonical scalar.

The finite scalar product remains exact at every cutoff.  The missing global
cell is the compatibility between:

- cutoff inclusions;
- the three regularity completions;
- anomaly-line trivialization;
- reciprocal dagger sewing;
- the completed theta section.

## Frame ambiguity

Knowing only the final scalar does not recover the three components.  A finite
counterterm can be moved between the first two anomaly channels while leaving
their exponentiated sum unchanged.  Source grading by operator degree fixes the
canonical finite decomposition, but a completed boundary trivialization must
preserve that grading.

Therefore the totalization law supplies provenance, not automatic orientation.
The RH-bearing content remains in the boundary law that fixes the anomaly
frame and identifies scalar zeros with states of the completed mixed complex.

## DPC verdict

The finite three-stratum totalization is already canonical: it is the
order-three determinant identity.  The unresolved constructor is not another
regularized product.  It is the source-derived trivialization of the primitive
and square anomaly lines through the full Green boundary presentation.

The smallest falsifier is a proposed global scalar totalization for which
either first- or second-order counterterms can be changed without changing any
declared source datum.  Such a scalar has an unfixed determinant frame.

## Verification

`check_rh_det3_three_stratum_totalization.py` verifies the logarithmic identity
coefficientwise through degree twelve, direct-sum composition for multiple
labelled blocks, and an explicit counterterm-transfer ambiguity when source
grading is forgotten.
