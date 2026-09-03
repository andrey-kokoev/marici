# Falsification of the positive spectral-edge conjecture

## Problem

Test the conjecture that every finite remainder Hankel determinant has an unconditional single exponential asymptotic with positive coefficient and strictly faster remainder.

## Rank-one falsifier

The remainder localizer contains the extracted endpoint feature

\[
c(t,h)
=e^{t/4}(e^{h/4}-1).
\]

Therefore the rank-one determinant grows like

\[
D_1(t,h)\sim(e^{h/4}-1)e^{t/4},
\]

rather than decaying as a positive-rate exponential. In the notation

\[
D_1\sim C_1e^{-\alpha_1t},
\]

one has

\[
\alpha_1=-\frac14.
\]

Thus the conjecture is false as stated for every finite rank.

## Nonreal leading-shell obstruction

More importantly, before RH is known, a least-real-part spectral shell can contain conjugate complex rates

\[
\lambda=\sigma+i\omega,
\qquad
\bar\lambda=\sigma-i\omega.
\]

Their grouped contribution has the form

\[
e^{-\sigma t}
\left(Ae^{-i\omega t}+\bar A e^{i\omega t}\right).
\]

Even in the simplest real-residue case this is

\[
2Ae^{-\sigma t}\cos(\omega t).
\]

Renormalization by \(e^{\sigma t}\) leaves an oscillatory function, not a positive limit. It takes the values \(2A\) and \(-2A\) along two unbounded sequences.

Hence an unconditional leading term must initially be a finite exponential or trigonometric shell sum. It cannot be declared a single positive coefficient before phase cancellation or spectral reality is proved.

## Circular coefficient

The proposed coefficient

\[
\left(\prod_jw_j(h)\right)
\Delta(y_E,y_1,\ldots)^2
\]

is visibly positive only when the sampled bases are real and the grouped weights have the required signs. Those are spectral conclusions of the RH-strength cone.

Using this expression as unconditional source input silently inserts the property to be proved.

## Disposition

Reject the conjecture as stated for two independent reasons:

1. rank one has endpoint growth, not positive-rate decay;
2. an off-axis leading shell generally oscillates and has no positive real renormalized limit.

Conditional on RH, or on an independently proved reality and noncancellation theorem for the leading shell, the fixed-rank asymptotic remains valid and useful for certification.

## Replacement boundary

A valid conjecture must first produce

\[
D_r(t,h)
=
e^{-\sigma_rt}S_r(t,h)
+R_r(t,h),
\]

where \(S_r\) is the complete leading shell, possibly trigonometric, and \(R_r\) is strictly faster. It must then derive from source identities that \(S_r\) is constant and positive. Declaring that property is not a derivation.

## Verification

- `research/voevodsky/spectral-edge-asymptotic-conjecture-falsification-v1.json`
- `research/voevodsky/checkers/check_spectral_edge_asymptotic_conjecture.py`
- `research/voevodsky/results/spectral_edge_asymptotic_conjecture.json`
