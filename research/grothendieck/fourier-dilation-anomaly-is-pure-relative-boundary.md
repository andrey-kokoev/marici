# Fourier dilation anomaly is pure relative boundary

## Question

The seam-matched theta score produces a Mellin-label connection.  Its only
remaining curvature candidate was the generator-reversal anomaly of
Fourier--Tate sewing.  Does the smallest native archimedean model produce a
nonzero bulk anomaly?

## Exact Fourier reversal

Use the self-dual Fourier convention

\[
(\mathcal Ff)(\xi)
=
\int_{\mathbb R}f(x)e^{-2\pi ix\xi}\,dx
\]

and the centered dilation generator

\[
D=x\partial_x+\frac12.
\]

For every Schwartz function, differentiation under the integral and one
integration by parts give

\[
\mathcal F D=-D\mathcal F.
\]

Thus the typed generator-reversal residual vanishes identically in the
interior:

\[
D\mathcal F+\mathcal FD=0.
\]

Fourier sewing itself supplies no curvature.

## Mellin cutoff exposes the whole anomaly

On the positive ray, define the finite Mellin window

\[
M_{a,b}(f;s)
=
\int_a^b f(x)x^{s-1}\,dx,
\qquad
0<a<b<\infty.
\]

Direct integration by parts gives

\[
M_{a,b}(Df;s)
=
\left[x^sf(x)\right]_a^b
+\left(\frac12-s\right)M_{a,b}(f;s).
\]

Therefore the failure of centered dilation to act by its Mellin eigenvalue is
exactly the two-endpoint current

\[
\mathcal A_{a,b}(f;s)
=
b^sf(b)-a^sf(a).
\]

There is no residual bulk integral.

## Completion audit

For a Schwartz source at infinity and \(\Re s>0\) at the origin,

\[
\lim_{a\downarrow0,\ b\uparrow\infty}
\mathcal A_{a,b}(f;s)=0.
\]

Hence ordinary Schwartz completion restores exact generator reversal and
erases the finite-window anomaly.  Meromorphic continuation beyond the
initial Mellin chamber requires subtracting endpoint jets.  Those jets must
remain explicit relative boundary coordinates; they cannot be reclassified
as a positive bulk.

This matches the programme's typing rule:

- interior Fourier--Tate transport is flat;
- cutoff failure is an endpoint current;
- continuation is legitimate only with the removed jets retained as boundary
  data.

## Consequence for the theta collision lane

The identity is universal for Schwartz sources.  It therefore cannot
distinguish the completed theta source from a hostile self-Fourier carrier.
In particular, the phase-aligned score residual cannot acquire an RH-bearing
orientation merely from archimedean Fourier reversal.

Any surviving source-specific anomaly must involve the arithmetic observation
boundary or restricted-product completion.  Its finite form must reduce to
named primitive, prime-square, or archimedean jet currents and must not vanish
when those currents are reassembled.

## Next exact target

Let \(W_X\) be the full finite-Euler primal--dual comparison, including its
arithmetic boundary registers, and let \(Q_\pm\) be the oriented Mellin label
generators.  The remaining anomaly is

\[
\mathcal A_X=Q_-W_X+W_XQ_+.
\]

The archimedean calculation proves that the continuous bulk component of
\(\mathcal A_X\) must be zero.  The next audit need only compute its boundary
coefficients.  A nonzero bulk term signals a typing or domain error.

The route closes if all correctly retained boundary coefficients cancel in
the completed limit.  It remains live only if theta/Tate source grammar leaves
a nonzero boundary matrix coefficient that is absent for hostile sources and
controls the phase-aligned residual transform.

## Result

The Fourier--dilation anomaly is a pure relative-boundary phenomenon.  The
archimedean interior is exactly flat, and ordinary Schwartz completion kills
its cutoff anomaly.  The search is now confined to arithmetic and
continuation boundary currents.
