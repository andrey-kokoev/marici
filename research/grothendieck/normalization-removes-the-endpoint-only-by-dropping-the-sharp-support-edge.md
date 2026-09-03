# Normalization removes the endpoint only by dropping the sharp support edge

## Question

Does `F(t)=e^(-t/4)H(t)` eliminate the endpoint rank-one repair from an RH-equivalent Hausdorff criterion?

## Two support cones

If raw heat rates satisfy `lambda>=0`, then normalized rates are

\[
a=\lambda+1/4\ge1/4.
\]

At mesh `h`, normalized Hausdorff coordinates obey

\[
y=e^{-ha}\le q_h=e^{-h/4}<1.
\]

Ordinary complete monotonicity of `F` tests only support in `[0,1]`. The RH-equivalent shifted criterion must retain the sharper support interval `[0,q_h]`.

## Endpoint behavior

The raw endpoint `H_E=e^(t/4)` becomes the constant

\[
F_E(t)=1.
\]

Its ordinary `1-y` localizer vanishes, so the endpoint appears removed. But this constant is an atom at `y=1`, outside the required interval `[0,q_h]`.

The sharp normalized localizer is

\[
L_{q-y}^F(t)_{ij}
=
q_hF(t+(i+j)h)
-F(t+(i+j+1)h).
\]

Substituting `F(s)=e^{-s/4}H(s)` gives

\[
L_{q-y}^F(t)
=
e^{-(t+h)/4}D_h
L_{1-y}^H(t)
D_h,
\]

where `D_h` is the positive diagonal normalization matrix. Thus the sharp normalized localizer is congruent to the raw localizer and has the same inertia.

For the endpoint alone it remains negative rank one. Normalization does not remove the defect when the support edge needed to recover RH is preserved.

## Scan result

The updated checker found the weaker normalized `1-y` gamma-plus-prime localizer positive at all nine sampled cases through rank four. Its minimum eigenvalues ranged from about `9.09e-2` to `1.20e-20`.

This confirms only complete-monotonicity compatibility for the shifted function. It does not test the sharp `q_h-y` support cone and cannot replace the endpoint Schur gate.

## Consequence

There are two distinct normalized claims:

1. `F` completely monotone, allowing a rate-zero endpoint atom;
2. `F` represented by rates at least `1/4`, equivalent to raw heat positivity after undoing the shift.

Only the second has the required RH force. It retains the endpoint rank-one support residual.

## Disposition

Do not use quarter normalization to declare the endpoint defect absent. Keep the sharp support localizer `q_hI-Y_h>=0`; it is congruent to the raw contraction localizer. The positive normalized scan is useful reconnaissance for a weaker cone only.