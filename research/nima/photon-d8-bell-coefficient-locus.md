# Dimension-eight photon Bell coefficient locus

Put

\[
r=\frac{f_2}{g_2},qquad
x=\sin^2\frac\theta2,qquad q(x)=1-x+x^2.
\]

The dimension-eight helicity map gives

\[
\frac{\Phi_2}{\Phi_1}=2r q(x),
\qquad q([0,1])=[3/4,1].
\]

For real coefficients the signed Bell function is

\[
I(x,r)=\frac{8\sqrt2,r q(x)}{1+4r^2q(x)^2}.
\]

## Exact locus

Writing \(y=2|r|q\), the condition \(|I|>2\) is

\[
y^2-2\sqrt2y+1<0,
\]

or

\[
\sqrt2-1<y<\sqrt2+1.
\]

Requiring this for every physical angle gives the strict locus

\[
\boxed{
\frac23(\sqrt2-1)<|r|<\frac{\sqrt2+1}{2}.
}
\]

The weak inequalities describe its closure, including Bell-saturating
boundaries.  Intersecting with the independently admitted photon positivity
cone

\[
g_2>0,qquad |f_2|\le g_2
\]

gives

\[
\boxed{
\frac23(\sqrt2-1)<|f_2/g_2|\le1.
}
\]

## What Bell identifies

Every normalized Bell observable is invariant under

\[
(g_2,f_2)\mapsto\lambda(g_2,f_2).
\]

Its differential therefore kills the radial vector \((g_2,f_2)\), and the
generic Jacobian has rank one.  Bell data cannot determine the EFT scale.

At one angle there is also the familiar duality \(y\leftrightarrow y^{-1}\).
Two distinct angles remove that dual branch because it would require
simultaneously

\[
rr'=\frac14,qquad rr'=\frac49.
\]

Thus signed two-angle data identifies \(r\) generically; using only
\(|I|\) leaves the unavoidable sign pair \(r\leftrightarrow-r\).

## Benchmarks

- One-loop QED has \(|r|=3/11\), strictly below the all-angle Bell boundary.
- The Bell boundary is \(|r|=\frac23(\sqrt2-1)\).
- Maximizing the worst-angle Bell value gives \(|r|=1/\sqrt3\); the two angular
  endpoints are then related by \(y_{\min}y_{\max}=1\).
- Born--Infeld has equal coefficients for \((F^2)^2\) and
  \((F\widetilde F)^2\), hence \(f_2=0\) in these conventions and zero Bell
  value for this incoming preparation.

These are distinct rays.  Proximity of QED to the Bell boundary is evidence to
investigate, not a derivation of the QED coefficient.

## Accepted events

For angular bins, integrate the unnormalized density against one common
nonnegative momentum-base weight and normalize once afterward.  Entry 1587
proves normalization and no-signalling for this pushforward.  Entry 1578's
outcome-dependent acceptance remains the hostile control.

Reproduce with:

```text
uv run --with sympy python research/nima/check_photon_d8_bell_coefficient_locus.py
```
