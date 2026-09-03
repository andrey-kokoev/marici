# Periodic bad intervals have Dirichlet rather than quadratic endpoint energy

## Question

What cancellation was lost when the one-prime bad set was bounded by the square of its component count?

## Claim boundary

For an exactly periodic train of equal bad intervals, the Fourier kernel factors through a Dirichlet kernel. Its pointwise peak has size \(N\), but its mean squared size over a dual period is only \(N\), not \(N^2\). This explains the failure of the component envelope and identifies the correct cancellation mechanism. The actual intervals have slowly varying widths and centers, whose error remains to be bounded.

## Periodic fixture

Let

\[
\Omega_N
=
\bigcup_{j=0}^{N-1}
\left[jp-\frac w2,jp+\frac w2\right].
\]

Its Fourier kernel is

\[
k_N(t)
=
\frac{\sin(wt/2)}{\pi t}
\sum_{j=0}^{N-1}e^{ijpt}.
\]

The geometric sum is

\[
D_N(pt)
=
\frac{1-e^{iNpt}}{1-e^{ipt}}.
\]

Although

\[
|D_N(0)|^2=N^2,
\]

Fourier orthogonality gives

\[
\frac1{2\pi}
\int_0^{2\pi}|D_N(\theta)|^2d\theta
=N.
\]

Thus the quadratic component estimate describes only coherent peaks. Integrated energy scales linearly away from the weighting singularities.

## Relation to the one-prime bad set

For

\[
a_L(u)=m_\Gamma(u)-c_2\cos(u\log2),
\]

the bad intervals are arranged near the period

\[
p=\frac{2\pi}{\log2}.
\]

The monotone gamma term changes their widths gradually and shifts their endpoints within each period. Therefore the actual endpoint sum is a modulated Dirichlet kernel rather than an arbitrary sum of \(N\) phases.

## Required perturbation estimate

Write actual endpoints as

\[
a_j=jp-\frac{w_j}{2}+\epsilon_j^- ,
\qquad
b_j=jp+\frac{w_j}{2}+\epsilon_j^+.
\]

The transition trace should be decomposed into:

1. a periodic Dirichlet contribution;
2. width modulation \(w_j-w_*\);
3. center displacement \((\epsilon_j^++\epsilon_j^-)/2\);
4. edge truncation from the first and last intervals.

The next theorem must bound these errors using derivatives of the monotone gamma multiplier. Reapplying the triangle inequality to each endpoint would restore the rejected \(N^2\) loss.

## Disposition

The cancellation mechanism is exact in the periodic fixture: mean-square endpoint energy is linear in component count. Extending it to the source bad set requires a bounded-variation or summation-by-parts estimate for the slowly modulated interval train. The actual transition trace remains uncertified. No RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_periodic_bad_interval_cancellation.py`
- `research/voevodsky/results/periodic_bad_interval_cancellation.json`
