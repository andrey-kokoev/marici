# Endpoint rank-one Schur gate

## Question

How does the raw endpoint channel alter the single Hausdorff localizer, and which exact finite-rank conditions determine whether gamma and prime data compensate it?

## Claim boundary

The rank-one subtraction theorem and normalization fork are verified. The RH-equivalent normalization, gamma--prime positivity, and arithmetic Schur bound remain open.

## Raw endpoint localizer

For the raw endpoint contribution

\[
H_E(t)=e^{t/4},
\]

the sampled coordinate is

\[
y_E=e^{h/4}>1.
\]

Its Hankel matrix is positive rank one. Its localizer is

\[
L_E(t)
=
M_E(t)-M_E(t+h)
=
-(y_E-1)vv^*.
\]

Thus the endpoint lies outside the compact Hausdorff interval and contributes one negative rank-one channel.

Writing

\[
L_{\mathrm{full}}
=
L_{\Gamma+P}-c vv^*,
\qquad c>0,
\]

makes the compensation problem exact.

## Rank-one subtraction theorem

Let \(L\geq0\). Then

\[
L-cvv^*\geq0
\]

if and only if

\[
v\in\operatorname{ran}L
\]

and

\[
c\langle v,L^\dagger v\rangle\leq1.
\]

Here \(L^\dagger\) is the Moore--Penrose pseudoinverse.

If \(v\) has a component in \(\ker L\), subtraction is immediately negative on that component. If \(v\in\operatorname{ran}L\), factor through \(L^{1/2}\); the residual becomes an identity minus one rank-one operator, whose unique nontrivial threshold is the displayed scalar bound.

## Three hostile gates

The full localizer cannot be positive if any of the following holds:

1. \(L_{\Gamma+P}\) has a negative direction orthogonal to \(v\);
2. \(v\notin\operatorname{ran}L_{\Gamma+P}\);
3. the scalar leverage exceeds one:
   \[
   c\langle v,L_{\Gamma+P}^\dagger v\rangle>1.
   \]

The first is an inertia obstruction. The second is a support obstruction. The third is the remaining quantitative endpoint-capacity obstruction.

## Normalization fork

For the normalized target

\[
F(t)=e^{-t/4}H(t),
\]

the endpoint contribution becomes constant:

\[
e^{-t/4}H_E(t)=1.
\]

Its first localizer then vanishes. Consequently, the raw rank-one repair problem and the normalized compact-Hausdorff problem are not the same presentation.

The source-derived RH equivalence must determine which target is legitimate:

- retain raw \(H\): prove the gamma--prime PSD, range, and Schur conditions;
- use normalized \(F\): prove that the spectral shift preserves the exact RH criterion and then work with a zero endpoint localizer.

Silently switching between them would move the endpoint residual rather than prove its control.

## Exact fixtures

The checker verifies:

- the sharp Schur threshold for a positive definite matrix;
- the range obstruction for a singular PSD matrix;
- persistence of a negative direction on \(v^\perp\);
- negativity of the raw endpoint localizer;
- vanishing of the normalized endpoint localizer.

## Categorical interpretation

The endpoint vector defines a one-dimensional object attached to the gamma--prime cone. The range condition asks whether it admits a lift through \(L_{\Gamma+P}^{1/2}\). The Schur inequality asks whether that lift is contractive after scaling by \(c^{1/2}\).

Thus endpoint compensation is a lifting problem:

\[
\mathbb C
\longrightarrow
\overline{\operatorname{ran}L_{\Gamma+P}^{1/2}},
\]

with norm at most one. This is the finite localizer analogue of the global Douglas contraction.

## Disposition

The raw endpoint channel reduces to a source-forced rank-one Schur gate. But normalization can remove that localizer entirely by shifting the spectral coordinate. The first unresolved decision is therefore not the Schur estimate; it is the source-typed identification of the RH-equivalent normalization. Only after that decision is the correct positivity target fixed.

## Verification

- `research/voevodsky/endpoint-rank-one-schur-gate-v1.json`
- `research/voevodsky/checkers/check_endpoint_rank_one_schur_gate.py`
- `research/voevodsky/results/endpoint_rank_one_schur_gate.json`
