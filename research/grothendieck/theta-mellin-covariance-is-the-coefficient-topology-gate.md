# Mellin covariance is the theta coefficient-topology gate

## Correction to the nonclosed-range obstruction

Packet 156 proves that full tail--seam synthesis is not bounded below relative
to unrestricted `L2(dp)` packet norm. This blocks a uniform closed-range
theorem, but RH only needs strict positive energy for the particular completed
state at each fixed spectral parameter. A lower bound uniform over all Mellin
heights is stronger than that requirement.

The next question is therefore not whether modulation exists, but how it acts
in the constructor-generated coefficient topology.

## Exact source-Gram covariance criterion

The source-Gram norm is

\[
 \lVert c\rVert_\Phi^2
 =C\int|\widehat c(\xi)|^2w(\xi)\,d\xi,
 \qquad
 w(\xi)=|\widehat\Phi(\xi)|^2.
\]

Mellin modulation in the logarithmic label coordinate is

\[
 (M_Nc)(p)=e^{iNp}c(p),
\]

so

\[
 \widehat{M_Nc}(\xi)=\widehat c(\xi-N).
\]

Consequently

\[
 \lVert M_Nc\rVert_\Phi^2
 =C\int|\widehat c(\eta)|^2w(\eta+N)\,d\eta.
\]

Therefore `M_N` extends boundedly to the source-Gram completion exactly when

\[
 \boxed{
 \operatorname*{ess\,sup}_\eta
 \frac{w(\eta+N)}{w(\eta)}<\infty,}
\]

with the ratio interpreted on the positive-weight set. Strong continuity of
the one-parameter modulation group requires the corresponding local bounds
and continuity in `N`.

This criterion is not automatic. Shifted real zeros or sufficiently
nonmoderate decay of `widehat(Phi)` can make the ratio unbounded. Thus the
Gram completion cannot be adopted merely because it makes synthesis
isometric; its Mellin covariance must be proved.

## Discrete arithmetic coefficient modules

On a weighted discrete label module

\[
 \ell^2(\mathbb N,\mu),
\]

the arithmetic Mellin character acts diagonally:

\[
 (M_Nc)_n=n^{iN}c_n.
\]

Because `|n^(iN)|=1`,

\[
 \boxed{\lVert M_Nc\rVert_{\ell^2(\mu)}=\lVert c\rVert_{\ell^2(\mu)}.}
\]

Hence any positive-Fock/source weight independent of `N` makes vertical
spectral translation a strongly continuous unitary group, provided the
logarithmic generator has its standard dense domain.

This is a strong reason to treat the labelled arithmetic module, rather than
unrestricted continuous `L2(dp)`, as the primary coefficient topology. But
the actual global weight and restricted-product completion must be derived;
the local prime Fock vacua alone do not automatically produce a global Hilbert
vector.

## Fixed-state completion versus uniform height

Suppose a source-derived coefficient Hilbert space `C_arith` is chosen, the
finite cutoffs converge

\[
 c_X(s)\to c(s)
\]

for each fixed `s`, and the full synthesis `U` is bounded and injective on
that space. Then

\[
 Uc_X(s)\to Uc(s),
\]

and

\[
 c(s)\ne0\implies\lVert Uc(s)\rVert>0.
\]

No uniform lower bound over all coefficient vectors or all imaginary heights
is required for this pointwise conclusion.

The remaining danger is a cutoff family that does not converge in the
constructor topology, or a completed spectral state lying outside its domain.
Those are source-completion questions, not closed-range questions.

## Three candidate topology tests

1. **Source-Gram completion:** prove the exact weight-ratio criterion for all
   authorized Mellin shifts and continuity of every boundary current.
2. **Discrete arithmetic completion:** derive the global positive weight,
   prove finite-cutoff convergence, and show full synthesis is bounded and
   injective.
3. **Added label energy:** identify an actual source generator whose graph
   norm supplies regularity; do not add a Sobolev term solely to improve the
   spectrum.

## Hostile modulation disposition

The family `e^(iNp)c` may not be excluded: on `p=log n` it is the authorized
character `n^(iN)`. Its vanishing synthesized energy at large `N` proves lack
of uniform-height stability, not failure of pointwise faithfulness.

The source topology is rejected only if an authorized fixed `N` modulation
does not extend continuously, or if a fixed completed state is lost under its
own cutoff limit.

## Honest frontier

The coefficient-topology question has an exact acceptance test:

\[
 \boxed{
 \text{derive }\mathcal C_{\rm arith},
 \text{ prove Mellin covariance, cutoff convergence, and injectivity of }U.}
\]

The source-Gram and arithmetic-label topologies are not interchangeable. A
comparison map between them must be constructed before transporting any
completion or closed-range conclusion.

