# The combined positive tetrahedral lift is equivalent to vanishing of the interior Krein--Langer defect

## Tetrahedral location

The relevant oriented horn is

\[
H_{124}
\circ
(H_{234}*\eta_{12})
=
H_{134}
\circ
(\eta_{34}*H_{123}).
\]

Its signed realization already closes. The remaining question is whether this equality lifts through the positive-to-signed forgetful functor.

On the completed source graph, the metric residual of that lift is

\[
R_r
=
A_{S,r}^*A_{S,r}
-
A_{B,r}^*A_{B,r}.
\]

A positive filler exists exactly when

\[
R_r\succeq0.
\]

Thus the Douglas inequality is the metric lift of the combined \(H_{234}\)--\(H_{134}\) horn, not a separate face identity.

## Totality of the source image

Fix \(r\ge1\). The degree-\(r\) translated Gaussian amplitudes are

\[
m_{a,r}(t)
=c_re^{-r\tau t^2}e^{iat},
\qquad a\in\mathbb R.
\]

Their span is total in the Hardy boundary carrier.

Indeed, if \(f\in H^2\) is orthogonal to every \(m_{a,r}\), then

\[
\int_{\mathbb R}
\overline{f(t)}
e^{-r\tau t^2}
e^{iat}
\,dt
=0
\]

for every \(a\in\mathbb R\). The Gaussian-weighted boundary function belongs to \(L^1\), so Fourier uniqueness implies \(f=0\).

Therefore the completed physical observation subspace is dense in the full Hardy carrier. It is not a proper compression capable of hiding an interior negative square.

## Extension of the inequality

Assume the Schur and Blaschke feature maps are bounded in their canonical Hardy realizations and that

\[
\|A_{B,r}p\|
\le
\|A_{S,r}p\|
\]

for every degree-\(r\) source observer \(p\).

By density and continuity, the inequality extends from the source image to the full Hardy carrier. Hence the reflected kernel

\[
K_\Theta
=
\frac{K_S-K_B}
{B\overline B}
\]

is positive semidefinite on every finite point packet.

## Krein--Langer consequence

Under the coprime Krein--Langer factorization

\[
\Theta=B^{-1}S,
\]

nonconstant \(B\) contributes exactly

\[
\dim K_B
\]

negative squares in the finite-index case. Since the source is total, none of these squares disappears under observation.

Consequently

\[
R_r\succeq0
\]

implies

\[
K_B=\{0\}.
\]

Equivalently, \(B\) is constant and \(\Theta\) is Schur.

Conversely, if \(B\) is constant, then the interior defect feature vanishes and

\[
R_r
=A_{S,r}^*A_{S,r}
succeq0.
\]

Thus, for the interior Krein--Langer sector,

\[
R_r\succeq0
\quad\Longleftrightarrow\quad
K_B=\{0\}.
\]

## Degree independence

The totality argument holds separately for every positive convolution degree. Therefore positivity at one full translated-Gaussian degree already forces the interior defect to vanish.

Higher convolution degrees and successor coherence do not weaken or strengthen this criterion. They transport the same decision through the graded system.

## Endpoint convention

The preceding equivalence concerns the interior Blaschke model space.

If the odd endpoint line is retained as a separate boundary-graph summand, the total metric residual is

\[
R_r^{aug}
=
A_{S,r}^*A_{S,r}
-
A_{B,r}^*A_{B,r}
-
b_r^*b_r.
\]

After the interior conclusion \(K_B=0\), one still needs the endpoint leverage estimate

\[
b_r^*b_r
\preceq
A_{S,r}^*A_{S,r}.
\]

If the endpoint direction is incorporated into a generalized Krein--Langer denominator, then positivity forces the corresponding generalized defect to vanish in the same combined statement.

## Positive-fiber interpretation

The signed tetrahedral class is zero before this argument. Positivity asks whether that zero class has a representative in the positive fiber.

Because the source image is Hardy-total, a positive representative exists only when the interior negative model space is absent. The kernel of positive-to-signed forgetfulness therefore contains the complete interior divisor obstruction.

The positive lift cannot be produced by changing tetrahedral coordinates, adding successor coherence, or choosing another Kolmogorov gauge.

## Hostile fixture

For

\[
\Theta=B^{-1}
\]

with nonconstant \(B\), the signed horn still closes, but

\[
A_S=0,
\qquad
A_B\ne0.
\]

Hence its positive fiber is empty. This explicitly distinguishes signed tetrahedral coherence from a positive tetrahedral filler.

## Disposition

The combined \(H_{234}\)--\(H_{134}\) inequality is not a weaker source-compressed positivity statement. The translated-Gaussian source is total in the Hardy carrier.

Therefore the interior positive tetrahedral lift exists exactly when the Krein--Langer interior defect vanishes. After that interior gate, only the separately retained odd endpoint leverage estimate remains.
