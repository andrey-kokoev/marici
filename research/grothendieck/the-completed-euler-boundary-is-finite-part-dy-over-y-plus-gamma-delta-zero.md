# The Completed Euler Boundary Is Finite-Part dy/y Plus Gamma Delta-Zero

## Primitive finite-part limit

Let

\[
\nu_X=
\sum_{p\le X}\frac1p
\delta_{\log p/\log X}
\]

be the tangent measures from Entry 3941.  Let \(f\) be continuously
differentiable on \([0,1]\).  Split

\[
\int f\,d\nu_X
=f(0)H_X
+\sum_{p\le X}\frac1p
\left[
f\!\left(\frac{\log p}{\log X}\right)-f(0)
\right].
\]

The Meissel--Mertens asymptotic is

\[
H_X-\log\log X\longrightarrow B_1.
\]

The bracketed function vanishes at the singular endpoint, so the tangent
limit from Entry 3941 applies and gives

\[
\sum_{p\le X}\frac1p
\left[
f\!\left(\frac{\log p}{\log X}\right)-f(0)
\right]
\longrightarrow
\int_0^1\frac{f(y)-f(0)}{y}\,dy.
\]

Therefore

\[
\lim_{X\to\infty}
\left[
\int f\,d\nu_X-f(0)\log\log X
\right]
=B_1f(0)
+\int_0^1\frac{f(y)-f(0)}{y}\,dy.
\]

This is the canonical primitive boundary distribution

\[
\mathcal T_1
=\operatorname{Fp}\!\left(\frac{dy}{y}\right)
+B_1\delta_0.
\]

The Mertens finite part is exactly the connecting coefficient between the
grade-zero corona and its positive-grade tangent chart.

## Square and higher currents collapse to the endpoint

The remaining Euler logarithm grades have finite total mass

\[
C_{\ge2}
=\sum_p\sum_{k\ge2}\frac1{k p^k}.
\]

Because this sum is absolutely convergent, every fixed prime-power label moves
to \(y=0\) as \(X\to\infty\), and dominated convergence gives

\[
\mathcal T_{\ge2}(f)=C_{\ge2}f(0).
\]

Thus the square and connected-tail currents become an endpoint delta channel
on the tangent blowup.  They do not contribute to the diffuse \(dy/y\) part.

Entry 3924 established the exact scalar identity

\[
\gamma=B_1+C_{\ge2}.
\]

Adding all Euler grades therefore produces one completed distribution:

\[
\mathcal T_{\mathrm{Euler}}(f)
=\int_0^1\frac{f(y)-f(0)}{y}\,dy
+\gamma f(0).
\]

Equivalently,

\[
\mathcal T_{\mathrm{Euler}}
=\operatorname{Fp}\!\left(\frac{dy}{y}\right)
+\gamma\delta_0.
\]

This is the distributional upgrade of the scalar sewing identity.  It
simultaneously retains the divergent primitive tangent current, every positive
jet moment, and the endpoint contribution of the square and higher grades.

## Checks

For the constant test function,

\[
\mathcal T_{\mathrm{Euler}}(1)=\gamma.
\]

For \(f(y)=y^r\), \(r\ge1\),

\[
\mathcal T_{\mathrm{Euler}}(y^r)=\frac1r.
\]

Thus the endpoint constant and tangent jet tower are two faces of one
boundary-bearing distribution.

No independent normalization is chosen at each grade.  The source cutoff,
Mertens subtraction, and absolutely convergent Euler remainder fix the entire
functional.

## Fourier--Tate typing

Reciprocal reflection reverses the oriented logarithmic coordinate but not its
magnitude.  The correct completed object therefore requires two copies of the
tangent chart:

\[
(\varepsilon,y),
\qquad
\varepsilon\in\{+1,-1\},
\qquad
0<y\le1,
\]

with oriented generator \(\varepsilon y\).  Fourier--Tate reflection exchanges
the two sheets and reverses the generator.

The scalar distribution \(\mathcal T_{\mathrm{Euler}}\) is identical on both
sheets.  It fixes magnitude and normalization but not relative orientation.
This agrees with Nima's hostile two-prime phase audit: Haar, trace, and positive
rank-one data cannot distinguish opposite cross-prime phases.

Therefore the distribution derived here is the scalar connecting map, not the
final RH orientation law.  The missing datum is a source-rooted incidence
between the two endpoint deltas or an archimedean channel that assigns their
relative sign before Haar projection.

## Next gate and falsifier

Construct the doubled boundary object

\[
\mathcal T_+\oplus\mathcal T_-
\]

together with the Fourier--Tate sheet swap and archimedean endpoint incidence.
The finite-part distribution must be preserved, while the oriented generator
must reverse.

The smallest falsifier is Nima's two-prime pair of opposite residual phases.
If the proposed endpoint incidence gives the same oriented readout on both,
it supplies only scalar magnitude and cannot contribute to RH confinement.

Source phase audit:
`research/nima/the-mellin-corona-module-preserves-coherence-but-cannot-orient-it.md`
