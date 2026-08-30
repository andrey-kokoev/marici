# 2281 — The Spectral Residual Is Positive and the Gram Wall Is the Only Physical Rank Loss

## Residual quadratic form

Entry 2276 reduces every generic-orientation rank loss of the frozen spectral
Gaussian source to the Gram factor \(c\) and a residual quadratic form

\[
B=Aa^2+2Mab+Cb^2
+2c^2(w_1w_2+w_1w_3+w_2w_3),
\]

where

\[
A=3w_2w_3,
\qquad
M=\sqrt3w_1(w_2-w_3),
\]

\[
C=2w_1(w_2+w_3)-w_2w_3.
\]

The spectral weights are

\[
w_i=\frac1{d_i},
\qquad
d_i=2+t_i,
\qquad
t_i=|p_i+q|.
\]

## Exact positivity reduction

Since \(A>0\), positivity of the \((a,b)\) block is controlled by its
determinant.  Clearing the positive denominator gives

\[
\frac{d_1^2d_2^2d_3^2}{3}(AC-M^2)
=
4d_2d_3-(d_1-d_2-d_3)^2.
\]

This is positive exactly when

\[
(\sqrt{d_2}-\sqrt{d_3})^2
<d_1<
(\sqrt{d_2}+\sqrt{d_3})^2.
\]

## Lower inequality

The reverse triangle inequality for distances from \(-q\) to the second and
third equilateral vertices gives

\[
|t_2-t_3|\le|p_2-p_3|=2\sqrt3.
\]

Because \(d_2,d_3\ge2\),

\[
(\sqrt{d_2}-\sqrt{d_3})^2
=\frac{(d_2-d_3)^2}{(\sqrt{d_2}+\sqrt{d_3})^2}
\le\frac{12}{8}=\frac32<2\le d_1.
\]

## Upper inequality

The ordinary triangle inequality gives

\[
t_1\le t_2+|p_1-p_2|=t_2+2\sqrt3,
\]

so

\[
d_1\le d_2+2\sqrt3.
\]

Meanwhile

\[
(\sqrt{d_2}+\sqrt{d_3})^2
=d_2+d_3+2\sqrt{d_2d_3}
\ge d_2+6.
\]

Since \(6>2\sqrt3\), the upper inequality is strict.

Therefore \(AC-M^2>0\), the \((a,b)\) block is positive definite, and the
additional \(c^2\) term is nonnegative.  Hence

\[
\boxed{B>0}
\]

throughout the positive-energy source chamber.

## Complete finite-\(q\) classification

For the frozen spectral Gaussian source,

\[
\boxed{
\operatorname{rank}T(q)<3
\iff
q\cdot(p_1\times p_2)=0.
}
\]

Thus the only physical finite-\(q\) rank loss is the existing Gram/projection
wall.  There is no residual transport divisor and no new Carrier datum.

## Verification

- `research/benincasa/marici-gm/src/bin/generic_tensor_projection_determinant.rs`
  derives the determinant and residual.
- `research/benincasa/checkers/spectral_residual_positivity.rs` verifies the
  cleared-minor identity and the exact inequality ingredients.
