# Small theta windows have a globally real divisor

## Question

The rescaled completed-theta truncation converges to sinc on every compact
spectral window.  Can nonreal zeros nevertheless hide beyond every fixed
window as the support length tends to zero?

## Fixed-support rescaling

Define

\[
Y_L(w)
=
\frac{X_L(w/L)}{2L\Phi(0)}
=
\int_0^1 f_L(t)\cos(wt)\,dt,
\qquad
f_L(t)=\frac{\Phi(Lt)}{\Phi(0)}.
\]

The completed source is smooth and even, so \(\Phi'(0)=0\).  Taylor's theorem
therefore gives

\[
\lVert f_L-1\rVert_{C^2[0,1]}=O(L^2).
\]

At \(L=0\), the limiting transform is

\[
Y_0(w)=\int_0^1\cos(wt)\,dt=\frac{\sin w}{w},
\]

whose nonzero zeros are the simple real lattice points \(k\pi\).

## Uniform remote-zero control

Twice integrating by parts on the fixed interval gives

\[
Y_L(w)
=
\frac{f_L(1)\sin w}{w}
+
\frac{f_L'(1)\cos w}{w^2}
-
\frac1{w^2}\int_0^1f_L''(t)\cos(wt)\,dt.
\]

For sufficiently small \(L\),

\[
f_L(1)=1+O(L^2),
\qquad
\lVert f_L'\rVert_\infty+
\lVert f_L''\rVert_\infty=O(L^2).
\]

Choose disjoint conjugation-invariant disks of fixed radius around the remote
points \(k\pi\).  On their boundaries, and on the complementary remote
region, the sine term has the usual sine-type lower bound.  The remaining
terms are smaller by \(O(L^2/|w|)\).  Rouché's theorem consequently gives
exactly one zero in each remote lattice disk and no remote zeros elsewhere,
uniformly for all sufficiently small \(L\).

Because each disk is fixed by conjugation and \(Y_L\) is real entire, its
unique zero is real.  Counting multiplicity also makes it simple.

## Compact-zero control

After removing the remote region, only a fixed compact set remains.  Uniform
convergence

\[
Y_L\longrightarrow\frac{\sin w}{w}
\]

and disjoint Rouché circles around its finitely many zeros give one simple
zero near each \(k\pi\) and no others.  Conjugation again forces each unique
zero to be real.  The origin remains zero-free because \(Y_L(0)>0\).

Combining the compact and remote estimates proves that there exists
\(L_*>0\) such that every zero of \(Y_L\), and hence every zero of \(X_L\), is
real and simple whenever

\[
0<L<L_*.
\]

## Collision reduction

On every compact positive \(L\)-interval, remote zeros remain real and simple.
A simple real zero also has real velocity under the exact boundary flow.
Therefore the first possible creation of a nonreal pair must be a finite real
multiple zero satisfying

\[
\int_0^L\Phi(u)\cos(xu)\,du=0,
\qquad
\int_0^L u\Phi(u)\sin(xu)\,du=0.
\]

There is now no remaining boundary loophole:

- the complete small-window divisor is real and simple;
- infinity influx is impossible at finite \(L\);
- isolated finite zeros cannot be born only at \(L=\infty\) under locally
  uniform convergence.

Hence an off-real zero of the completed transform requires at least one finite
solution of the collision equations along the support flow.

Conversely, exclusion of every such collision keeps every finite-truncation
zero real.  Hurwitz then confines every zero of the completed transform to the
real centered axis.

Subject to the standard identification of real centered zeros with
\(\operatorname{Re}s=1/2\), RH is therefore reduced to one source inequality:
the two collision integrals never vanish simultaneously for \(L>0\) and real
\(x\).

## Hard obstacle

The reduction does not prove collision exclusion.  Generic smooth positive
even sources can pass through such double-zero bifurcations.  The missing
theorem must use special completed-theta structure to prove transversality of

\[
(L,x)
\longmapsto
\left(
\int_0^L\Phi(u)\cos(xu)\,du,
\int_0^L u\Phi(u)\sin(xu)\,du
\right)
\]

against the origin.

This is now the singular RH-bearing gate.  It is a two-variable, two-equation
source problem rather than an infinite hierarchy of positivity conditions.

## Falsifier

The smallest falsifier is explicit: one pair \((L,x)\) with \(L>0\) and real
\(x\) satisfying both collision equations.  A proof must exclude that pair
from theta source identities, not from prior knowledge of the zeta divisor.

## Result

The singular small-window boundary does not contain hidden nonreal zeros.
Together with finite sine-type control and Hurwitz stability, this reduces RH
to exclusion of finite real double-zero collisions in the canonical completed
theta support flow.
