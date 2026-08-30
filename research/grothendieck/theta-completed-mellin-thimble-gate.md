# Completed Mellin thimble gate

## Exact completed coordinate

Put

\[
\vartheta_+(x)=\sum_{n\ge1}e^{-\pi n^2x},\qquad
G(x)=4x^{9/4}\vartheta_+''(x)+6x^{5/4}\vartheta_+'(x).
\]

With \(x=e^{2u}\), the completed theta source is \(G(x)=\Phi(u)\).
For \(w=1/2+z\), the bilateral transform is

\[
\boxed{
Z(z)=\frac12\int_0^\infty
x^{\,w/2-1/4}G(x)\,\frac{dx}{x}
=\xi(w).
}
\]

The normalization is audited at \(w=2\): both sides equal \(\pi/6\).
The half-line cosh transform used elsewhere is \(B(z)=Z(z)/2\); this fixed
positive factor disappears from every logarithmic derivative.

Termwise Mellin integration, initially in its honest convergence region,
gives

\[
\begin{aligned}
Z(z)
&=\pi^{-w/2}\zeta(w)
\left[2\Gamma\left(\frac w2+2\right)
-3\Gamma\left(\frac w2+1\right)\right]\\
&=\frac12w(w-1)\pi^{-w/2}\Gamma(w/2)\zeta(w).
\end{aligned}
\]

The first displayed line is to be read with the common gamma factor arranged
as in the second; its purpose is the source derivation, not a termwise-positive
decomposition.

Modular sewing gives \(G(1/x)=G(x)\). Substitution \(x\mapsto1/x\) then sends
\(w\mapsto1-w\), deriving the completed functional equation directly on the
same contour.

## Logarithmic moment form

Differentiating the completed integral before taking a quotient gives

\[
\frac{Z'(z)}{Z(z)}
=\frac12
\frac{\int_0^\infty(\log x)x^{z/2}G(x)\,dx/x}
     {\int_0^\infty x^{z/2}G(x)\,dx/x}.
\]

Thus the outer Pick target is exactly

\[
\boxed{
\beta\Re\mathcal M(z)+\alpha\Im\mathcal M(z)\ge0,
\qquad
\mathcal M(z)=
\frac{\int(\log x)x^{z/2}G(x)\,dx/x}
     {\int x^{z/2}G(x)\,dx/x}.
}
\]

The factor \(1/2\) in \(Z'/Z=\mathcal M/2\) does not affect the sign.
This is a completed, phase-preserving logarithmic barycenter. No labelled
boundary term remains.

## Source saddle equation

Using Haar coordinate \(dx/x\), define

\[
\mathcal S_z(x)=\log G(x)+\frac z2\log x.
\]

Every nondegenerate saddle satisfies

\[
\boxed{x\frac{G'(x)}{G(x)}=-\frac z2.}
\]

Modular inversion pairs the \(z\)-saddles with the \(-z\)-saddles. Complex
conjugation pairs the \(z\)-saddles with the \(\bar z\)-saddles. These are
source symmetries; they do not depend on the desired inequality.

## Conditional thimble theorem

Suppose, for a region \(\Omega\) in the outer quadrant, that the positive
Mellin contour admits a deformation into source-canonical thimbles
\(\Gamma_j(z)\) such that:

1. no zero of \(G\) or singularity is crossed;
2. the intersection numbers are constant on \(\Omega\);
3. modular and conjugation partners are retained together;
4. after one common phase is removed, every thimble denominator weight is
   nonnegative; and
5. every thimble logarithmic barycenter \(m_j(z)\) obeys
   \(\beta\Re m_j+\alpha\Im m_j\ge0\).

Then the completed barycenter \(\mathcal M(z)\) obeys the same cone inequality,
and hence the outer Pick target holds throughout \(\Omega\).

The proof is convexity: under conditions 2--4, \(\mathcal M\) is a positive
weighted barycenter of the \(m_j\), and a half-plane is convex.

This theorem is conditional. Establishing conditions 1--5 for the Riemann
source is the new analytic gate; they are not inferred from RH or from zero
locations of \(\xi\).

## Sharp local falsifier

The proposed mechanism fails at the first parameter \(z\) where any one of
the following occurs:

- a contributing saddle becomes degenerate;
- a Stokes crossing changes an intersection number;
- a required modular/conjugate partner ceases to share the common phase;
- the deformation crosses a zero of \(G\); or
- a canonical thimble barycenter crosses
  \(\beta\Re m+\alpha\Im m=0\).

The saddle discriminant

\[
\mathcal S_z''(x)=0
\quad\text{together with}\quad
xG'(x)/G(x)=-z/2
\]

is the first local object to compute. It detects a change of thimble topology
without inspecting the final Xi inequality.

## The physical saddle axis is nondegenerate

In logarithmic coordinate, write \(V(u)=-\log\Phi(u)\). The saddle map on the
real source axis is

\[
z(u)=V'(u),\qquad z'(u)=V''(u).
\]

The labelled-jet recurrence gives

\[
V''(0)\approx18.7269049295033211684>0.
\]

The existing directed source theorem proves \(V'''(u)>0\) for every \(u>0\).
Consequently \(V''(u)>0\) on the full real half-line, and \(u\mapsto V'(u)\)
is strictly increasing there. No saddle collision or degeneracy can originate
on the physical positive source axis.

The displayed base value is presently a 70-decimal truncated-theta audit, not
a directed interval in this artifact; its margin is enormous and the omitted
tail is superexponentially small. A formal reuse should import a directed
enclosure. The logical conclusion about the real saddle map is conditional on
that straightforward base enclosure together with the already certified
increasing-curvature theorem.

Thus the first genuine obstruction search is complex: zeros of
\((\log\Phi)''(u)\) off the real axis and their critical values under
\(z=-\Phi'/\Phi\).

## Status and next calculation

The Mellin identity, logarithmic-moment identity, saddle equation, symmetry
pairing, and conditional convexity theorem are exact. No global thimble
decomposition has yet been proved.

The next calculation is to locate the nearest complex zeros of
\((\log\Phi)''\), then map them to critical values of

\[
z(x)=-2xG'(x)/G(x),
\]

and test whether any enters the outer quadrant before the already certified
central region ends.

The first dense reconnaissance finds the boundary critical value
\(z\approx5.701318i\), followed by the first observed open-quadrant value
\(z\approx0.479911+9.624580i\). Its Pick image has
\(|t|=|z|^2\approx92.86285\), far beyond the certified radius \(8.5\). This is
not exhaustive: an argument-principle root count and a separate Stokes-phase
trace are the next gates. See
`theta-complex-saddle-critical-value-reconnaissance.md`.

The Stokes trace finds a genuine earlier candidate on \(z=1/2+ib\): at
\(b\approx5.98828529\), the physical saddle becomes phase-aligned with a
competitor, whose upward thimble changes from no real-contour intersection
below the event to one intersection above. This is stable under three flow
step sizes. It falsifies the globally single-thimble mechanism at
\(|t|\approx36.10956\). The canonical plus-paired saddle cone proxy remains
positive, so the live target is a two-thimble coupled positivity theorem. See
`theta-first-stokes-jump-and-coupled-saddle-gate.md`.

The post-jump relative-cycle geometry is now explicit: both zero-directed
branches share the simple amplitude zero `u=0.6388300536...i`, while the other
branches run to opposite real infinities. Their upward intersections have the
same oriented sign. Exact-path paired quadrature at `(a,b)=(0.5,6.03)` gives
cone `1.27968...>0` and reconstructs the independent real-contour transform to
relative error `4.67e-4`.

Exact component extraction shows principal cone `5.8083...` and competitor
cone `-3.7437...`; the coupled sum alone is positive. Their post-jump thimble
phases are unequal, so the earlier common-phase convexity hypothesis is not a
global theorem. It must be replaced after Stokes walls by an oriented complex
two-thimble inequality.

The next Stokes event confirms that the replacement must itself be stated at
the level of relative homology, rather than for a fixed number of saddles. At
\(b\approx9.6439257771\), a third saddle joins and the basis mutates through a
second simple zero of the analytically continued source. The incidence-forced
chain is

\[
-\infty\longrightarrow u_{\star,0}
\longrightarrow u_{\star,1}\longrightarrow+\infty.
\]

At \((a,b)=(1/2,9.66)\), this three-edge chain reconstructs the original real
contour to relative error \(5.16\times10^{-4}\) and has cone
\(2.96772133898>0\), against the direct value \(2.96858813246\). The live
global conjecture is therefore an oriented relative-cycle positivity theorem
covariant under Picard--Lefschetz basis mutation. Individual-thimble
positivity and any globally fixed two-thimble decomposition are both already
falsified. See `theta-first-three-thimble-chain.md`.

Artifacts:

- checkers/theta_modular_mellin_normalization.py
- results/theta-modular-mellin-normalization.json
- checkers/theta_completed_mellin_affine_audit.py
- results/theta-completed-mellin-affine-audit.json
