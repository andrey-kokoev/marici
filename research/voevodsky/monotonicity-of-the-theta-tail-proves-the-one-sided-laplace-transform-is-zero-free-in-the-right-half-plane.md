# Monotonicity of the theta tail proves the one-sided Laplace transform is zero-free in the right half-plane

## One-sided transform

Let

\[
F(s)
=
\int_0^\infty
\Phi(u)e^{-su}
\,du,
\qquad
\operatorname{Re}s>0.
\]

Assume the established theta-tail properties

\[
\Phi(u)>0,
\qquad
\Phi'(u)<0
\]

for \(u>0\).

## Sine-transform lemma

If \(g\) is positive, decreasing, integrable, and nonconstant, then for every \(b>0\),

\[
\int_0^\infty
g(u)
\sin(bu)
\,du
>0.
\]

To see this, divide the integral into half-periods of length \(\pi/b\). Pair each positive half-period with the following negative half-period. After translating the second interval back by \(\pi/b\), the pair is

\[
\int_0^{\pi/b}
\left[
 g\left(u+
\frac{2k\pi}{b}
\right)
-
g\left(u+
\frac{(2k+1)
\pi}{b}
\right)
\right]
\sin(bu)
\,du,
\]

which is nonnegative by monotonicity and positive unless \(g\) is constant on every such pair. Summing the pairs proves the claim.

## Application to the theta tail

Write

\[
s=a+ib,
\qquad
a>0.
\]

The damped density

\[
g_a(u)
=
e^{-au}
\Phi(u)
\]

is positive and strictly decreasing. Therefore, for \(b>0\),

\[
\operatorname{Im}F(a+ib)
=
-
\int_0^\infty
 g_a(u)
\sin(bu)
\,du
<0.
\]

For \(b<0\), conjugation gives

\[
\operatorname{Im}F(a+ib)>0.
\]

For \(b=0\),

\[
F(a)>0.
\]

Consequently,

\[
F(s)\ne0
\]

throughout the open right half-plane.

## Consequences

The causal impedance

\[
m(s)
=-
\frac{F'(s)}{F(s)}
\]

is analytic on the complete right half-plane. No pole or branch choice obstructs the one-sided Hardy realization.

The causal Cayley transfer

\[
\theta_+(s)
=
\frac{1-m(s)}{1+m(s)}
\]

is therefore meromorphic only where \(1+m(s)=0\), not where the source Laplace transform vanishes.

## What this does not prove

Zero-freeness of \(F\) does not by itself imply

\[
\operatorname{Re}m(s)
\ge0.
\]

Since

\[
\operatorname{Re}m(s)
=
-
\partial_a
\log|F(a+ib)|,
\]

the remaining positive-real condition is equivalent to monotone decay of \(|F(a+ib)|\) as the damping parameter \(a\) increases.

That modulus monotonicity is stronger than pointwise monotonicity of \(\Phi\).

## Control interpretation

The one-sided causal plant has no unstable transmission zeros in its natural right half-plane. The unresolved issue is dissipativity of its logarithmic-derivative impedance, not well-posedness of the transfer denominator.

## Disposition

The theta-tail monotonicity supplies a direct, source-derived zero-free theorem for the one-sided Laplace transform. This cleanly separates the causal zero-free problem from the stronger positive-real and reciprocal-feedback gates.
