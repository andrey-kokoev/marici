# Quarter-shift normalized localizer

## Question

Does the raw endpoint rank-one subtraction survive in the normalized Hausdorff chart, or is it an artifact of applying the localizer before the spectral quarter-shift?

## Claim boundary

The normalization and matrix congruences are exact. The source-derived equivalence with the RH criterion and positivity of the normalized completed remainder remain open.

## Spectral shift

Set

\[
F(t)=e^{-t/4}H(t).
\]

A raw Laplace atom transforms as

\[
e^{-t\lambda}
\longmapsto
 e^{-t(\lambda+1/4)}.
\]

Thus normalization translates the spectral coordinate by \(1/4\). The raw endpoint atom

\[
H_E(t)=e^{t/4}
\]

has \(\lambda=-1/4\) and becomes the constant atom at zero:

\[
e^{-t/4}H_E(t)=1.
\]

Translation preserves the signs of spectral coefficients. It changes support but cannot turn a signed measure into a positive one.

## Hankel congruence

For step \(h\), let

\[
D_h=\operatorname{diag}
\left(1,e^{-h/4},e^{-2h/4},\ldots\right).
\]

At every finite rank,

\[
M_F(t)
=
e^{-t/4}D_hM_H(t)D_h.
\]

Therefore raw and normalized Hankel matrices are related by a positive diagonal congruence and have the same inertia.

## Localizer transformation

The normalized localizer is

\[
L_F(t)
=M_F(t)-M_F(t+h).
\]

Substitution gives

\[
L_F(t)
=
e^{-t/4}D_h
\left[
M_H(t)-e^{-h/4}M_H(t+h)
\right]
D_h.
\]

This is not congruent to the raw localizer

\[
M_H(t)-M_H(t+h).
\]

For the endpoint channel, this weak \(1-y\) bracket vanishes exactly. But it permits a rate-zero atom. The RH-equivalent shifted rates are bounded below by \(1/4\), so the Hausdorff coordinate satisfies

\[
y\leq q=e^{-h/4}<1.
\]

The sharp normalized localizer is therefore

\[
L_F^{(q)}(t)=qM_F(t)-M_F(t+h).
\]

It satisfies

\[
L_F^{(q)}(t)
=
e^{-t/4}qD_h
\left[M_H(t)-M_H(t+h)\right]
D_h.
\]

Thus the sharp normalized localizer is a positive diagonal congruence of the raw localizer. It retains the negative rank-one endpoint channel and the Schur gate.

## Consequence for the rank-one scan

The prior raw scan does address the sharp normalized cone up to this congruence. The weak normalized \(1-y\) scan tests a larger support interval and can hide the endpoint defect by admitting a spurious zero-rate atom.

## Categorical interpretation

Normalization is a gauge on the Hankel object but not on the localizer arrow. It preserves objects by congruence while changing the transition map from

\[
M_H(t)
\longrightarrow
M_H(t+h)
\]

to a weighted transition. Thus it preserves Hankel inertia but changes the residual attached to scale translation.

The lesson is general: a gauge can preserve vertices while changing face residuals. Residual comparisons must be transported with the arrows, not only with the objects.

## Remaining source gate

The source explicit formula must prove that the quarter-shifted target is exactly the one entering the RH-equivalent positivity criterion. This requires tracking:

- the spectral coordinate before and after the shift;
- endpoint, gamma, and prime normalizations;
- support of the shifted measure;
- the map from normalized complete monotonicity back to Weil positivity.

Only then can the raw rank-one route be retired or retained.

## Disposition

Normalization removes the endpoint only from the weak \(1-y\) localizer. The sharp support localizer \(q-y\) retains it and is congruent to the raw rank-one problem. The active target is therefore the gamma--prime cone together with the endpoint range and Schur conditions; weak normalized positivity is insufficient.

## Verification

- `research/voevodsky/quarter-shift-normalized-localizer-v1.json`
- `research/voevodsky/checkers/check_quarter_shift_normalized_localizer.py`
- `research/voevodsky/results/quarter_shift_normalized_localizer.json`
