# Theta cubic primitive-scale susceptibility

Author: `marici.Grothendieck`

## Purpose

The additive Poisson--Hermite programme fails because two individually
self-dual scale sectors can interfere negatively. This packet computes that
instability at first order and turns "primitive single scale" into a sharp
quantitative condition.

## 1. Atomic scale model

In the far-separated limit, a reciprocal theta scale pair at logarithmic
distance `L` contributes a radial atom at

\[
y=L^2.
\]

Normalize the primitive orbit to `y=1` and add a second orbit at squared
scale ratio `r>0` with infinitesimal weight `lambda`:

\[
z_t(\lambda)=1+\lambda r^t.
\]

Define

\[
k(\lambda)=9z_4(\lambda)^2-7z_3(\lambda)z_5(\lambda),
\]

\[
e(\lambda)
=35z_2(\lambda)z_5(\lambda)^2
+162z_4(\lambda)^3
-189z_3(\lambda)z_4(\lambda)z_5(\lambda),
\]

and

\[
R(\lambda)=36k(\lambda)^3-e(\lambda)^2.
\]

At the primitive ray,

\[
k(0)=2,
\qquad e(0)=8,
\qquad R(0)=224>0.
\]

## 2. Exact transverse susceptibility

The first variations are

\[
k'(0)=r^3(18r-7-7r^2),
\]

and

\[
e'(0)=35r^2-189r^3+297r^4-119r^5.
\]

Therefore

\[
\begin{aligned}
R'(0)
&=108k(0)^2k'(0)-2e(0)e'(0)\\
&=432k'(0)-16e'(0),
\end{aligned}
\]

which simplifies completely to

\[
\boxed{
R'(0)=-112r^2(10r^3-27r^2+5).
}
\]

This polynomial is the exact transverse susceptibility of the cubic cone to
an added Poisson scale sector.

At `r=1`,

\[
R'(0)=1344=6R(0),
\]

as required: adding the same scale merely rescales the source, and the
degree-six residual changes by the corresponding homogeneous factor.

At `r=3`,

\[
R'(0)=-32256<0,
\]

which is the first mixed coefficient of the explicit two-orbit falsifier.

## 3. Scale-separation transition

Put

\[
P(r)=10r^3-27r^2+5.
\]

Since

\[
P(1)=-12,
\qquad P(5/2)=-15/2,
\qquad P(3)=32,
\]

there is a large positive transition `r_*` in `(5/2,3)`. For every
`r>r_*`, an infinitesimal sufficiently remote scale orbit points toward the
outside of the cubic cone:

\[
\boxed{r>r_*\quad\Longrightarrow\quad R'(0)<0.}
\]

There is also a small positive root because `P(0)=5`; the susceptibility is
not invariant under exchanging the two atoms after fixing the first orbit's
weight and scale. The full finite-weight residual restores the appropriate
homogeneous exchange covariance.

The relevant conclusion is robust: Poisson-completed scale mixing has a
finite separation threshold beyond which its first-order effect is
destabilizing.

## 4. Meaning of primitivity

The standard theta source occupies the fixed scale `L=0`. A positive direct
sum of self-dual scale pairs moves it into a convex cone of Poisson-completed
sources. The susceptibility calculation shows that the cubic-positive region
is not preserved by that cone operation.

Thus "primitive" cannot merely mean that the source admits a preferred
decomposition. It must mean that independent reciprocal scale weights are
not admissible physical deformations. In categorical language, the target
property is not additive under direct sum:

\[
\boxed{
\text{Poisson closure is linear, but cubic coherence is sector-coupled.}
}
\]

Any proof functor assigning a positive Hermite energy separately to each
self-dual scale orbit and summing the results is impossible. It misses the
mixed susceptibility above.

## 5. Next theorem-shaped target

The standard lattice must supply a nonlinear constraint tying all apparent
scale sectors to one primitive generator. A faithful candidate should have
the form

\[
\text{primitive scale relation}
\quad\Longrightarrow\quad
\text{control of mixed Hermite susceptibility}.
\]

The next attack is to determine whether the theta heat equation supplies
that relation. Unlike Poisson summation alone, the heat equation connects
scale differentiation to the lattice Laplacian and therefore does not allow
independent weights at different reciprocal scales.

The sharp falsifier is now local: if a positive self-dual heat-flow orbit
through the standard theta source has negative cubic susceptibility, then
even primitive heat coherence is insufficient. If the heat tangent is
nonnegative while arbitrary scale-mixture tangents can be negative, the heat
equation is the first discriminator that survives the hostile source.

## 6. Scope correction: scale heat flow is universal translation

The proposed heat discriminator must be typed before its sign is tested. For
any even source `Phi`, not just theta,

\[
\frac{\Phi(u-L)+\Phi(u+L)}2
=\cosh(L\partial_u)\Phi(u).
\]

Its half-line even moments obey the exact binomial transport

\[
\boxed{
Z_t(L)=\sum_{j=0}^t
\binom{2t}{2j}L^{2t-2j}Z_j.
}
\]

In particular, with `tau=L^2`,

\[
\left.\partial_\tau Z_t(L)\right|_{L=0}
=\binom{2t}{2}Z_{t-1}
=t(2t-1)Z_{t-1}.
\]

This relation follows solely from translation and evenness. After moment
projection it contains no information about the square lattice, Poisson
coefficients, or arithmetic labels. Every hostile even analytic source has
the same scale-flow law.

Therefore the logarithmic heat/scale generator by itself is not the missing
discriminator. Calling it "theta heat flow" after discarding its discrete
initial spectrum would be a type error:

\[
\boxed{
\text{heat translation of the completed readout}
\ne
\text{arithmetic coherence of its lattice coefficients}.
}
\]

The scale-mixture counterexample is built precisely from such translated
orbits, so no positive theorem stable under this flow can exclude it.

## 7. Surviving arithmetic discriminator

What the hostile source lacks is not Poisson symmetry or heat evolution, but
one coherent square-spectrum coefficient packet. The standard theta series
has coefficients supported on one integral-square lattice and constrained
simultaneously by its modular/Hecke relations. Independent reciprocal scale
orbits destroy that eigenpacket structure while preserving Poisson closure.

The next theorem-shaped target is therefore narrower:

\[
\boxed{
\text{primitive square-spectrum eigenpacket}
\quad\Longrightarrow\quad
S_{34}\ge0.
}
\]

This target is allowed to be nonlinear after moment projection, but its
input condition must be checked on coefficients before summation. A mere
functional equation of the completed scalar is no longer sufficient.

The immediate attack should:

1. write the prime-square coefficient recursion satisfied by the standard
   theta packet;
2. determine whether it is a genuine Hecke eigenrelation or only a restated
   scaling identity;
3. propagate that relation into the pointed Hermite moment packet;
4. reject it if independent scale-pair sums satisfy the same relation.

## 8. All-prime coefficient rigidity

Consider a positive weighted square-spectrum packet

\[
\Phi_w(u)=\sum_{n\ge1}w_n\phi_n(u),
\qquad w_n>0.
\]

The label scaling law is

\[
\phi_{pm}(u)=p^{-1/2}\phi_m(u+\log p).
\]

Hence the `p`-divisible sector is

\[
\sum_{p\mid n}w_n\phi_n(u)
=p^{-1/2}\sum_{m\ge1}w_{pm}\phi_m(u+\log p).
\]

It equals the standard translated full packet

\[
p^{-1/2}\Phi_w(u+\log p)
\]

if and only if

\[
\boxed{w_{pm}=w_m\qquad(m\ge1).}
\]

Here equality of the coefficient packets follows from uniqueness of the
Laplace series with distinct rates `pi m^2`, under the same absolute
convergence that defines the theta source on the positive chamber.

Now impose this recursion for every prime `p`. If

\[
n=p_1p_2\cdots p_k
\]

with primes repeated according to multiplicity, successive application gives

\[
w_n=w_{p_2\cdots p_k}=\cdots=w_1.
\]

Therefore:

\[
\boxed{
\textbf{All-prime rigidity theorem.}\quad
\text{A positive weighted integral-square packet satisfying every standard
prime recursion has constant weights.}
}
\]

Up to overall normalization, the ordinary theta coefficient packet is the
unique member of this class.

## 9. Infinitesimal rigidity

Let

\[
w_n(\epsilon)=1+\epsilon\xi_n+O(\epsilon^2)
\]

be a coefficient deformation preserving all prime recursions. Linearization
gives

\[
\xi_{pm}=\xi_m
\]

for every prime and every `m`, hence

\[
\boxed{\xi_n=\xi_1\quad(n\ge1).}
\]

The only admissible tangent is common rescaling. Since `mathscr R_34` is
homogeneous of degree six in the source,

\[
\mathscr R_{34}[c\Phi]=c^6\mathscr R_{34}[\Phi],
\]

so common rescaling cannot change its sign.

This explains exactly why the negative scale-mixture susceptibility is not
an admissible tangent inside the primitive arithmetic stratum. It changes
the relative weights of coefficient sectors and necessarily violates at
least one prime recursion.

## 10. What the rigidity theorem does and does not prove

All-prime rigidity distinguishes the standard theta packet from both hostile
families already constructed:

- generic positive even sources have no integral-square coefficient packet;
- independent reciprocal scale sums do not obey one common recursion on the
  integer labels.

It is therefore the first discriminator to survive every preceding
falsifier. But rigidity is not positivity: it removes hostile deformation
directions without determining the sign at the remaining isolated source.

The live theorem is now pointwise rather than stable-family based:

\[
\boxed{
\text{derive }S_{34}\ge0\text{ from the simultaneous all-prime recursion
at the unique constant-weight packet.}
}
\]

Any successful argument must combine at least two prime recursions or their
global Euler coherence. A proof using only one prime leaves arbitrary weights
on the `p`-primitive residue classes and is too weak.

## 11. Canonical Euler primitive projector

Define commuting scale operators

\[
S_nf(u)=n^{-1/2}f(u+\log n).
\]

They satisfy

\[
S_mS_n=S_{mn},
\qquad
\phi_n=S_n\phi_1.
\]

Therefore, in the absolutely convergent positive chamber,

\[
\Phi=\sum_{n\ge1}S_n\phi_1
=\prod_p(I-S_p)^{-1}\phi_1.
\]

Möbius inversion gives the source-derived primitive projector

\[
\boxed{
\phi_1=\prod_p(I-S_p)\Phi.
}
\]

Finite products have an exact operational meaning: for a finite prime set
`P`,

\[
\prod_{p\in P}(I-S_p)\Phi
\]

retains precisely the labels not divisible by any prime in `P`. Letting `P`
exhaust the primes leaves only label one.

This projector is nonlinear in neither the source nor its coefficients, but
it is non-additive with respect to independently rescaled lattice sectors
because those sectors do not share the same integral-label action `S_p`.
It therefore distinguishes the standard theta packet before scalar moment
projection.

## 12. Euler-cluster formulation of the remaining sign

The exceptional residual is homogeneous of source degree six. Substituting

\[
\Phi=\prod_p(I-S_p)^{-1}\phi_1
\]

expands it into six arithmetic label channels with one common multiplicative
origin. The next faithful positivity target is not termwise label positivity,
which has already failed, but a connected Euler-cluster statement:

\[
\boxed{
\text{the completed six-copy Hermite cluster generated from one primitive
Euler packet has nonnegative total orientation.}
}
\]

This formulation excludes the two-scale Poisson counterexample by typing,
not by fitting the desired sign afterward. It also makes the next falsifier
finite in principle: find the smallest finite prime set `P` whose exactly
sewn Euler cluster has negative residual orientation.

The known scope boundary remains. The open-chamber scale operators are bulk
translations, and their radial-score cocycle is a coboundary. All possible
new orientation must arise from the common multiplicative incidence of the
six labels after completed modular sewing—not from an individual prime
translation or a resurrected seam scalar.

## 13. Finite-prime quotient remains infinite-dimensional

Fix a finite prime set `P` and impose

\[
w_{pn}=w_n
\qquad(p\in P,n\ge1).
\]

Every integer has a unique factorization

\[
n=d_P(n)c_P(n),
\]

where all prime factors of `d_P(n)` lie in `P` and `c_P(n)` is coprime to
their product. The recursion removes `d_P(n)` but leaves the core:

\[
\boxed{w_n=W(c_P(n))}
\]

for an arbitrary positive function `W` on the infinitely many `P`-free
integers.

Thus a finite family of prime recursions does not select a finite-dimensional
coefficient packet. Its quotient is still indexed by infinitely many
primitive cores.

The finite Euler projector

\[
\Pi_P=\prod_{p\in P}(I-S_p)
\]

acts exactly by

\[
\Pi_P\Phi
=\sum_{(n,\prod_{p\in P}p)=1}\phi_n.
\]

It removes every label divisible by a prime in `P`, but it is not the
rank-one primitive projector. Only the directed inverse limit

\[
P\nearrow\{\text{all primes}\}
\]

collapses the surviving cores to `n=1`.

## 14. No bounded Euler-census explanation

This has an immediate methodological consequence. A certificate proved by
enumerating the six-copy clusters for any fixed finite prime set controls
only one finite localization chart. It does not control the infinitely many
unseen primitive cores, and inspecting more primes one at a time never turns
that census into a uniform theorem.

The required statement must commute with the inverse limit. Concretely, one
needs either:

1. a prime-uniform cone preserved when a new valuation direction is added;
2. a monotone residual under `Pi_P -> Pi_(P union {q})`; or
3. an absolutely convergent connected-cluster identity whose tail has a
   source-derived sign.

Without one of these, a finite Euler computation is scouting rather than an
explanation.

The structure is the multiplicative analogue of the earlier modular warning:

\[
\boxed{
\text{finite prime closure is not all-prime coherence.}
}
\]

## 15. Exact refinement correspondence

If `P subset P union {q}`, the finer core set maps to the coarser one by
forgetting the `q`-free valuation distinction. Pullback duplicates a coarse
coefficient across its finer fibers and pushforward sums those fibers. Their
composite is the fiber norm

\[
q_!q^*=|q^{-1}(c)|
\]

on a finite capped chart, or its valuation-weighted analogue before capping.
This is the same Mackey norm already found for Boolean and prime-power route
refinement.

The physical all-label contraction is invariant under this correspondence,
but individual Euler clusters are not. Hence any proposed cluster
orientation must be covariant under prime-set refinement before it can
descend to the completed scalar.

This supplies the next sharp falsifier: one refinement square whose oriented
cluster sign is not preserved rules out that finite-cluster proof mechanism,
even if both endpoint scalar sums happen to be positive.

## 16. Frechet influence polynomial of the residual

Let

\[
K=9Z_4^2-7Z_3Z_5,
\]

\[
E=35Z_2Z_5^2+162Z_4^3-189Z_3Z_4Z_5,
\]

and `R=36K^3-E^2`. Under an infinitesimal source perturbation with moment
increments `delta Z_t`,

\[
\delta R=\sum_{t=2}^5A_t\,\delta Z_t,
\]

where

\[
\begin{aligned}
A_2={}&-70EZ_5^2,\\
A_3={}&-756K^2Z_5+378EZ_4Z_5,\\
A_4={}&1944K^2Z_4
-2E(486Z_4^2-189Z_3Z_5),\\
A_5={}&-756K^2Z_3
-2E(70Z_2Z_5-189Z_3Z_4).
\end{aligned}
\]

If the perturbing source is `Psi(u)`, then

\[
\boxed{
\delta R=\int_0^\infty\mathcal I(u)\Psi(u)\,du,
\qquad
\mathcal I(u)=\sum_{t=2}^5A_tu^{2t}.
}
\]

Thus the entire first-order response is controlled by one cubic polynomial
after factoring `u^4`:

\[
\mathcal I(u)=u^4(A_2+A_3u^2+A_4u^4+A_5u^6).
\]

This is the smallest tangent object compatible with the pointed Hermite
residual. It is source-derived and contains no fitted pairing.

## 17. Exact prime-tail response

The `p`-divisible sector is

\[
S_p\Phi(u)=p^{-1/2}\Phi(u+\log p).
\]

Put `ell_p=log p`. Its moment increments are

\[
\delta_pZ_t
=p^{-1/2}\int_{\ell_p}^\infty
(v-\ell_p)^{2t}\Phi(v)\,dv.
\]

Consequently the response to activating the complete `p`-divisible sector is
the single scalar tail integral

\[
\boxed{
\delta_pR
=p^{-1/2}\int_{\ell_p}^\infty
\mathcal I(v-\ell_p)\Phi(v)\,dv.
}
\]

Every prime probes the same influence kernel; arithmetic enters only through
the translated lower limit and the common completed source. This converts
the proposed prime-uniform cone into a concrete theorem:

\[
\text{orient all prime refinements by controlling the theta tail averages
of }\mathcal I.
\]

Pointwise positivity of `mathcal I` would be sufficient but is not required.
If it changes sign, the exact alternative is a variation-diminishing theorem
for its translated averages against `Phi`.

The smallest falsifier is equally explicit: one prime `p` for which the tail
integral has the forbidden sign relative to the proposed refinement
orientation. No label census is needed.

## Scope

The susceptibility formula and its sign transition are exact. They explain
the two-orbit counterexample but do not prove the standard theta residual
positive and do not prove RH.
