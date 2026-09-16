# The local prolate defect density is a boundary tail, not a constant Plancherel density

## Purpose

Before attempting the nonpolynomial multiplier \(\eta(B_\Lambda)\), compute the diagonal density of the first exact prolate defect

\[
T_\Lambda
=B_\Lambda-B_\Lambda^2.
\]

This model determines whether logarithmic transition mass should be expected to have a constant local density.

## Real prolate pair

Let

\[
P_\Lambda=1_{[-\Lambda,\Lambda]},
\]

\[
Q_\Lambda=\mathcal FP_\Lambda\mathcal F^{-1}.
\]

The convolution kernel of \(Q_\Lambda\) is

\[
q_\Lambda(u)
=
\frac{\sin(\Lambda u)}{\pi u}.
\]

Set

\[
B_\Lambda=P_\Lambda Q_\Lambda P_\Lambda.
\]

## Exact diagonal density

For \(|x|<\Lambda\), the diagonal of \(B_\Lambda\) is

\[
B_\Lambda(x,x)
=q_\Lambda(0)
=
\frac{\Lambda}{\pi}.
\]

The diagonal of \(B_\Lambda^2\) is

\[
B_\Lambda^2(x,x)
=
\int_{-\Lambda}^{\Lambda}
|q_\Lambda(x-y)|^2dy.
\]

Since \(Q_\Lambda\) is a projection,

\[
\int_{\mathbb R}
|q_\Lambda(x-y)|^2dy
=q_\Lambda(0).
\]

Therefore the defect density is exactly

\[
\rho_\Lambda^{tr}(x)
=
T_\Lambda(x,x)
=
\int_{|y|>\Lambda}
|q_\Lambda(x-y)|^2dy.
\]

Equivalently,

\[
\rho_\Lambda^{tr}(x)
=
\frac1{\pi^2}
\int_{|y|>\Lambda}
\frac{
\sin^2(\Lambda(x-y))
}{(x-y)^2}
dy.
\]

This is a boundary-crossing tail density.

## Distance-to-boundary form

Let

\[
d_+(x)=\Lambda-x,
\qquad
d_-(x)=\Lambda+x.
\]

Changing variables on the two exterior half-lines gives

\[
\rho_\Lambda^{tr}(x)
=
\frac1{\pi^2}
\left[
\int_{d_+(x)}^\infty
\frac{
\sin^2(\Lambda u)
}{u^2}du
+
\int_{d_-(x)}^\infty
\frac{
\sin^2(\Lambda u)
}{u^2}du
\right].
\]

The density depends on distance to the two physical boundaries. It is not spatially constant.

## Interior estimate

If \(x\) remains in a fixed compact set while \(\Lambda\) grows, then

\[
d_+(x)\asymp\Lambda,
\qquad
d_-(x)\asymp\Lambda.
\]

Using \(\sin^2\le1\), one obtains

\[
0\le
\rho_\Lambda^{tr}(x)
\le
\frac1{\pi^2}
\left(
\frac1{d_+(x)}+
\frac1{d_-(x)}
\right)
=O(\Lambda^{-1}).
\]

Thus the local transition density vanishes in the fixed interior.

## Mesoscopic boundary tail

Away from the microscopic oscillatory region, averaging \(\sin^2(\Lambda u)\) gives the leading tail

\[
\rho_\Lambda^{tr}(x)
\sim
\frac1{2\pi^2}
\left(
\frac1{d_+(x)}+
\frac1{d_-(x)}
\right).
\]

Integrating \(1/d\) from the microscopic boundary scale to the window scale produces the logarithmic trace.

Therefore the \(\log\Lambda\) transition mass is spread over a scale-invariant boundary layer. It is not produced by a constant density across the whole interval.

## Recovery of the logarithmic trace

Integrating the exact density over \([-\Lambda,\Lambda]\) recovers

\[
\operatorname{Tr}
(B_\Lambda-B_\Lambda^2)
=
\frac{2}{\pi^2}
\log\Lambda+O(1).
\]

The logarithm comes from the two integrals of the boundary tail, not from interval length times a constant local density.

## Weighted consequence

For a multiplication observer \(a(x)\),

\[
\operatorname{Tr}
\left(
M_a^*T_\Lambda M_a
\right)
=
\int_{-\Lambda}^{\Lambda}
|a(x)|^2
\rho_\Lambda^{tr}(x)dx.
\]

If \(a\) is fixed and compactly supported near the center, this tends to zero at least as fast as \(\Lambda^{-1}\).

If \(a\) follows one moving boundary, the limit is a half-line boundary-tail functional.

If \(a\) remains approximately constant across the expanding interval, the full logarithmic Widom coefficient is recovered.

These are three different observer scalings.

## Implication for the Witt multiplier

The scalar trace law for \(\eta(B_\Lambda)\) has a logarithmic coefficient, but the first exact defect shows that one cannot infer a constant Plancherel density from that coefficient.

The likely local object is again a scale-invariant boundary profile. Its exact profile differs from the first defect, but its source Gram depends on how the observer is placed relative to the moving cutoff boundary.

Therefore the proposed formula

\[
G_{edge}
=2C_W(\log2)G_{Pl}
\]

is not justified without proving that the transported Mellin observer occupies the expanding-window scaling rather than the fixed-interior or boundary-following scaling.

## Required transport check

The exact physical-to-Hardy transport must determine which of the following occurs:

1. fixed observer in the interior;
2. observer translated with one Hardy boundary;
3. observer spread over the expanding physical window;
4. two-sided combination of boundary-following observers.

Only after this placement is fixed can the observer-weighted edge Gram be identified.

## Disposition

For the exactly computable first defect, the diagonal density is

\[
\rho_\Lambda^{tr}(x)
=
\int_{|y|>\Lambda}
|q_\Lambda(x-y)|^2dy.
\]

It is a boundary tail and vanishes in the fixed interior. Hence scalar logarithmic Widom growth does not imply a constant observer-weighted Plancherel density. The next step is to insert the exact transported observer placement before proposing the common edge Gram.
