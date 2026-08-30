# Exact visibility and arithmetic stabilization cutoffs

Fix `g>=2`, a nonempty finite admitted even-depth set `A`, a Laurent window
`I=[m_min,m_max] cap Z`, and the full target.

## Complete kernel-support visibility

The tower at depth `a` is visible exactly when

\[
m_{min}\le-(g+a-1)\le m_{max}.
\]

Let `S_g(A)` be the union of the Laurent exponents in every named kernel class
whose depth support is admitted:

\[
S_g(A)=
\{-(g+a-1):a\in A\}
\]

together with

\[
\{-2,0\}
\quad\text{if }g=2\text{ and }0\in A,
\]

and

\[
\{-8,0,2\}
\quad\text{if }g=2\text{ and }\{0,4,6\}\subseteq A.
\]

Define

\[
m_{low}^*(g,A)=\min S_g(A),
\qquad
m_{high}^*(g,A)=\max S_g(A).
\]

Then the exact necessary-and-sufficient window for displaying every predicted
kernel class is

\[
\boxed{
m_{min}\le m_{low}^*(g,A),
\qquad
m_{max}\ge m_{high}^*(g,A).
}
\]

The familiar tower-only lower bound

\[
m_{min}\le-(g+a_{max}-1)
\]

is one part of this statement.  At grade two the exceptional supports can
force the lower endpoint to `-8` and the upper endpoint to `2`.

## Rational-cohomology stabilization

The ordinary rational quotient has rank one as soon as any positive tower is
visible.  Thus its exact activation condition is

\[
\boxed{
\exists a\in A,\ a>0:
m_{min}\le-(g+a-1)\le m_{max}.
}
\]

Adding further visible positive depths changes the exact subspace and integral
index, but not the rational quotient rank.

## Integral arithmetic stabilization

Let

\[
\delta_{g-1}=\gcd_{j\ge1}(2j)^{\overline{g-1}}.
\]

For the prefix of positive even depths `{2,4,...,2s}`, define

\[
q_{g,j}=\frac{(2j)^{\overline{g-1}}}{\delta_{g-1}}.
\]

The exact minimal arithmetic stabilization length is

\[
\boxed{
s_g=\min\{s\ge1:\gcd(q_{g,1},\ldots,q_{g,s})=1\}.
}
\]

Equivalently, `2s_g` is the smallest prefix depth whose residue Smith divisor
equals the infinite-depth divisor.

This exact cutoff is finite with the uniform bound

\[
\boxed{s_g\le g.}
\]

Indeed `Q_g(x)=(2x)^(rising(g-1))` is an integer polynomial of degree `g-1`.
The fixed divisor of an integer polynomial of degree `n` is the gcd of any
`n+1` consecutive values together with their finite-difference lattice; in
particular the first `g` positive values determine it.  The bound is uniform,
not always minimal.

To make the minimal stabilizing prefix visible in the source window, it is
necessary and sufficient that

\[
\boxed{
m_{min}\le-(g+2s_g-1),
\qquad
m_{max}\ge-(g+1).
}
\]

The grade-uniform sufficient version obtained from `s_g<=g` is

\[
m_{min}\le-(3g-1),
\qquad
m_{max}\ge-(g+1).
\]

These are source visibility bounds.  They make no assertion about a truncated
target, which defines a different readout map.
