# The five-wall comparison requires a Sobolev--exponential rigging

## Correction to the radial carrier

The projective space defined only by weighted `L2` seminorms is sufficient for
Laplace pairings and the integral order current. It is not sufficient for the
five-wall comparison: point evaluation and derivative traces are not
continuous on an `L2` space.

The radial carrier must therefore be strengthened to

\[
\mathcal S_{\exp}^{\infty}(\mathbb R)
=
\bigcap_{a>0}\bigcap_{k\ge0}
\{f:e^{a|q|}\partial_q^j f\in L^2,
\ 0\le j\le k\},
\]

with seminorms

\[
p_{a,k}(f)^2
=
\sum_{j=0}^k
\|e^{a|q|}\partial_q^j f\|_2^2.
\]

The completed theta source and its parameter derivatives lie in this carrier
by superexponential decay.

## Trace continuity

The one-dimensional Sobolev estimate on a bounded neighborhood of `q_0`
gives

\[
|f(q_0)|
\le C_{q_0,a}p_{a,1}(f).
\]

Applying the same estimate to derivatives gives

\[
|f^{(j)}(q_0)|
\le C_{q_0,a,j}p_{a,j+1}(f).
\]

Hence every finite endpoint jet used by the constant, delta, and
archimedean wall rows is continuous. Integration, Laplace pairing, and all
parameter jets remain continuous by the earlier weighted Cauchy--Schwarz
bounds.

## Stability of the existing constructions

Translation satisfies, for each `a,k`,

\[
p_{a,k}(\tau_Lf)\le e^{a|L|}p_{a,k}(f).
\]

At `L=log n`, rapid label decay again absorbs the factor `n^a`. Therefore all
polynomial-logarithmic Euler syntheses remain continuous on

\[
\mathcal S_{\mathrm{lab}}
\widehat\otimes_\pi
\mathcal S_{\exp}^{\infty}.
\]

The order operator satisfies

\[
(Sf)'=-2f,
\qquad
(Sf)^{(j+1)}=-2f^{(j)},
\]

and its endpoint constants are bounded by `||f||_1`. Thus it maps continuously
to the augmented ordered carrier consisting of two endpoint constants plus a
Sobolev--exponential derivative coordinate.

Reflection and compact positive dilation families act continuously on this
stronger carrier, so reciprocal oddness, degree minus one, and cutoff
independence are unchanged.

## Consequence for the five-wall audit

After this refinement, all individual finite wall rows are legitimate
continuous traces on one common core:

- constant and delta rows use finite Sobolev traces;
- primitive and square rows use rapid-label Euler dual sections;
- the archimedean row uses Laplace and endpoint jets;
- the ordered relative row uses the continuous bilinear Green pairing.

Continuity now makes each separately defined row cutoff-independent. What is
not automatic is equality of cross-polarized rows produced by different
source-authorized routes. That remaining comparison is algebraic incidence
plus Green polarization, not a missing trace topology.
