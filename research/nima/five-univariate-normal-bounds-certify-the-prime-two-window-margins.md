# Five univariate normal bounds certify the prime-two window margins

## Parameters

Let

\[
u=\sqrt\pi\log2,
\qquad
\sigma=\frac{\sqrt3}{2},
\]

and let \(\Phi\) and \(Q=1-\Phi\) denote the standard normal distribution
and upper-tail functions.

The Stieltjes endpoint pair is represented by a standard bivariate normal
\((Z_1,Z_2)\) with correlation \(1/2\).

## Endpoint lower bound from Gaussian correlation

The event

\[
A_u=\{|Z_1|\le u,\ |Z_2|\le u\}
\]

is the intersection of two symmetric convex strips. The Gaussian correlation
inequality gives

\[
a_2
=
\mathbb P(A_u)
\ge
\mathbb P(|Z|\le u)^2
=
[2\Phi(u)-1]^2.
\]

Therefore the single univariate bound

\[
\Phi(u)>0.89
\]

implies

\[
a_2>0.78^2=0.6084>0.6.
\]

## Annular conditional split

Let

\[
I_1=[u,3u/2],
\qquad
I_2=[3u/2,2u].
\]

By sign symmetry,

\[
d_2^2
=
2P_{++}+2P_{+-}.
\]

Conditionally on \(Z_1=x\),

\[
Z_2
\sim
N\!\left(
\frac x2,
\frac34
\right).
\]

For \(x\in I_1\), the same-sign annulus probability is bounded by

\[
Q\!\left(
\frac{u-x/2}{\sigma}
\right)
\le
Q\!\left(
\frac{u}{2\sqrt3}
\right),
\]

while the opposite-sign annulus probability is bounded by

\[
Q(\sqrt3u).
\]

For \(x\in I_2\), use the coarser same-sign bound \(1/2\), with the same
opposite-sign bound.

Consequently,

\[
d_2^2
\le
2[\Phi(3u/2)-\Phi(u)]
\left[
Q\!\left(
\frac{u}{2\sqrt3}
\right)
+
Q(\sqrt3u)
\right]
\]

\[
\quad+
2[\Phi(2u)-\Phi(3u/2)]
\left[
\frac12+Q(\sqrt3u)
\right].
\]

## Rational certification packet

The following five outward bounds suffice:

\[
\Phi(u)>0.89,
\]

\[
\Phi(3u/2)<0.968,
\]

\[
\Phi(3u/2)>0.967,
\]

\[
Q\!\left(
\frac{u}{2\sqrt3}
\right)<0.362,
\]

\[
Q(\sqrt3u)<0.017.
\]

Using \(\Phi(2u)<1\), they give

\[
\Phi(3u/2)-\Phi(u)<0.078,
\]

and

\[
\Phi(2u)-\Phi(3u/2)<0.033.
\]

Therefore

\[
d_2^2
<
2(0.078)(0.362+0.017)
+
2(0.033)(0.5+0.017).
\]

The right side is

\[
0.093246<0.1.
\]

Thus the five scalar normal bounds imply both desired window estimates:

\[
a_2>0.6,
\qquad
d_2^2<0.1.
\]

## Completing the mass-bound margin

The source theta value satisfies

\[
M_\Phi
=
\xi\!\left(\frac12\right)
<0.5.
\]

Hence

\[
8(1-M_\Phi)^2a_2
>
8\left(\frac12\right)^2(0.6)
=
1.2.
\]

Combining with \(d_2^2<0.1\) yields

\[
d_2^2
<
8(1-M_\Phi)^2a_2
\]

with a rational margin greater than \(1.1\).

## Proof burden for the scalar bounds

Each of the five normal inequalities concerns an explicit algebraic multiple
of

\[
u=\sqrt\pi\log2.
\]

They can be certified independently using:

- rational enclosures for \(\pi\) and \(\log2\);
- alternating or interval Taylor bounds for the error function on a compact
  interval;
- Mills bounds for the largest argument.

No bivariate numerical library is needed.

The separate theta inequality \(M_\Phi<1/2\) must be certified from the
source completed-xi formula, not from a decimal literal.

## Consequence

Together with the monotone envelope for \(p\ge3\), these estimates close
the analytic theta-mass Schur certificate for every prime, conditional on the
constructor identifications already isolated.

The remaining first-edge gate is then source equality of the window and
completed-history incidences, not local coercivity.

## Verdict

The apparently numerical \(p=2\) obstruction reduces to five loose
one-dimensional normal-CDF inequalities. Their rational slack is large enough
for a short proof-producing checker or elementary analytic appendix.

Once those scalar enclosures and \(M_\Phi<1/2\) are formally recorded, the
primewise Wronskian Schur-loading margin is complete.
