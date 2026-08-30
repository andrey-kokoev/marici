# Completed theta truncations turn RH into zero flow

## Bounded question

After Hurwitz rules out stable completion of nowhere-zero finite Euler
sections, is there a source-derived finite approximation whose divisor is
allowed to converge to the completed theta divisor without inserting zero
data?

## Complete first, truncate second

Write the centered completed theta transform as

\[
X(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du,
\]

where the completed source \(\Phi\) is real, positive, even, and decays
faster than every exponential.  For \(L>0\), define

\[
X_L(z)=\int_{-L}^{L}\Phi(u)e^{izu}\,du
      =2\int_0^L\Phi(u)\cos(zu)\,du.
\]

This order is source-authorized: modular completion has already produced the
fixed real-contour carrier, and only then is its geometric support truncated.
No zero location enters the definition.

Every \(X_L\) is an even real entire function of exponential type \(L\).
For each compact set \(K\subset\mathbb C\),

\[
\sup_{z\in K}|X(z)-X_L(z)|
\le
\int_{|u|>L}\Phi(u)e^{M_K|u|}\,du
\longrightarrow0,
\]

where \(M_K=\sup_{z\in K}|\operatorname{Im}z|\).  Thus \(X_L\to X\)
locally uniformly on the entire plane.

Unlike the finite Euler products, the finite relative sections \(X_L\) are
not required to be nowhere zero.  Hurwitz and the argument principle now work
in the correct direction: every isolated zero of \(X\), counted with
multiplicity, is approached by zeros of \(X_L\).

## Exact moving-boundary law

Evenness of the source gives

\[
\partial_LX_L(z)=2\Phi(L)\cos(zL).
\]

If \(z(L)\) is a simple zero of \(X_L\), implicit differentiation yields

\[
z'(L)
=-
\frac{2\Phi(L)\cos(Lz(L))}
     {\partial_zX_L(z(L))},
\]

with

\[
\partial_zX_L(z)
=-2\int_0^L u\Phi(u)\sin(zu)\,du.
\]

This is an exact source-derived divisor dynamics.  It replaces the impossible
picture in which a zero suddenly appears only at Euler completion.

## What symmetry proves

For real \(z\), both the numerator and denominator in the velocity law are
real.  Consequently a simple real zero moves along the real axis for as long
as it remains simple.  Reality and evenness also force the complete divisor
symmetry

\[
z\longmapsto -z,
\qquad
z\longmapsto\overline z.
\]

Therefore a finite zero cannot leave the critical seam by an isolated smooth
motion.  A first finite departure must pass through a real multiple zero:

\[
\int_0^L\Phi(u)\cos(xu)\,du=0,
\qquad
\int_0^L u\Phi(u)\sin(xu)\,du=0.
\]

These two explicit source integrals are the collision equations.

## Small-window normal form

Set \(w=Lz\) and normalize

\[
Y_L(w)=\frac{X_L(w/L)}{2L\Phi(0)}
=\int_0^1\frac{\Phi(Lt)}{\Phi(0)}\cos(wt)\,dt.
\]

As \(L\downarrow0\),

\[
Y_L(w)\longrightarrow\frac{\sin w}{w}
\]

locally uniformly in \(w\).  Hence each fixed finite collection of the
rescaled initial zeros is a perturbation of simple real sinc zeros.  This
supplies a genuine initial real-zero regime on every bounded rescaled window.

It does not give a uniform statement over all zeros.  At every positive
\(L\), zeros with \(|w|\to\infty\) remain outside that perturbative control.

## The exact obstruction

The completed-theta truncation converts the zero-confinement problem into two
and only two possible failure mechanisms:

1. two real zeros collide at a solution of the collision equations and leave
   the seam as a conjugate pair;
2. a nonreal pair enters from spectral infinity, escaping every bounded
   rescaled window as \(L\downarrow0\).

Thus an all-real-zero theorem for the completed transform cannot follow from
symmetry or local continuation alone.  It requires either:

- a source inequality excluding every real double-zero collision and a
  separate no-entry estimate at infinity; or
- a global variation-diminishing theorem that controls both mechanisms at
  once.

This is a real obstacle, not a request for more numerical certification.
Compactly supported positive even sources do not generally have Fourier
transforms with only real zeros, so the missing law must use special completed
theta structure.

## Deutsch--Popper formulation

The counterfactual task is now finite and geometric:

> Starting from the sinc-like small-window divisor, construct an authorized
> completed-theta boundary motion that produces either a real collision or a
> nonreal zero entering from infinity.

The conjecture is that the completed theta source makes both constructions
impossible.  The first falsifier is an explicit pair \((L,x)\) satisfying the
two collision equations, or an explicit controlled nonreal branch arriving
from infinity.

## Result

Finite completed-theta truncations are the first admissible finite relative
sections in this programme: they preserve the completed carrier, converge
locally uniformly to \(X\), and already carry the approximating divisor.  Their
exact boundary law shows that RH has become a zero-flow confinement problem.

The newly exposed hard gate is global divisor bifurcation control: exclude
both finite real collisions and influx from spectral infinity using a
theta-specific source law.
