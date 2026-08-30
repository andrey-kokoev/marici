# The Archimedean Tate Phase Is a Gamma Multiplier Times Reflection

## Diagonalizing the logarithmic Hankel operator

Write the even and odd kernels as

\[
k_+(u)=2e^{u/2}\cos(2\pi e^u),
\qquad
k_-(u)=-2i e^{u/2}\sin(2\pi e^u).
\]

Then

\[
(K_\pm g)(r)=\int_{\mathbb R}k_\pm(r+q)g(q)\,dq.
\]

Using logarithmic Fourier convention

\[
\widehat g(t)=\int_{\mathbb R}g(q)e^{-itq}\,dq,
\]

the sum dependence gives

\[
\widehat{K_\pm g}(t)=m_\pm(t)\widehat g(-t).
\]

Thus additive Tate Fourier is not a scalar multiplier in Mellin frequency. It
is a multiplier followed by spectral reflection.

## Exact gamma multipliers

Set

\[
s=\frac12-it.
\]

The Mellin integrals for cosine and sine give

\[
m_+(t)
=2(2\pi)^{-s}\Gamma(s)\cos\left(\frac{\pi s}{2}\right),
\]

\[
m_-(t)
=-2i(2\pi)^{-s}\Gamma(s)\sin\left(\frac{\pi s}{2}\right).
\]

These are precisely the even and odd archimedean Tate gamma multipliers in the
chosen Fourier normalization.

The squared sheet laws become cocycle identities:

\[
m_+(t)m_+(-t)=1,
\qquad
m_-(t)m_-(-t)=-1.
\]

On real (t\), unitarity gives

\[
|m_+(t)|=|m_-(t)|=1.
\]

## Meaning of the correction

The sheet orientation was never a constant Hermite phase. It is the phase of
the local gamma multiplier attached to spectral reflection. Additive parity
selects which gamma factor acts. Reciprocal sewing then compares (t\) with
(-t\), and the cocycle product records whether the parity square is (1\) or
(-1\).

This places the archimedean and finite Tate factors in the same typed form:

1. a valuation or Mellin spectral reflection;
2. a source-normalized local multiplier;
3. a cocycle law under two successive sheet crossings.

The scalar theta vacuum uses the even factor. The odd factor is an additional
source port, not an alternative normalization of the same scalar vacuum.

## New frontier

The prime seam and archimedean seam should now be compared as local reflection
cocycles. The exact global question is whether their restricted product, with
the primitive and square boundary currents retained, supplies a completed
unitary cocycle whose distinguished scalar section can vanish only at the
common reflection seam.

The last clause remains unproved. Local cocycle unitarity alone does not
prevent a scalar matrix coefficient from vanishing.
