# Master theorem for the source-derived completed parity engine

> Scope refinement: this theorem classifies finite labelled point packets and
> finite point jets. Functional weak-* and Sobolev completions are classified
> separately in `functional-completion-extension-master-theorem.md`. Those
> completions add a smooth `l=2,3,4` magnetic kernel without invalidating the
> finite-support injectivity proved here.

## Theorem

Fix a finite labelled puncture set `P`, a finite source-jet bound at each
puncture, and the invariant HMLS/PSZ Green representatives. Form the strict LF
union over finite jet bounds, retaining both sphere charts, both helicities,
the prescribed finite-part distributions, and the fixed Green backgrounds.
Then:

1. **Source category.** The admitted source is a strict LF union of
   finite-dimensional labelled jet packets. It is not a product of independent
   Laurent coefficients and contains no infinite-order point distributions.
2. **Constructor.** The displacement-memory generator is
   \[
   \widehat K^+_\xi=
   \frac{(\bar z-\bar\xi)(1+\bar z\xi)^2}
   {(z-\xi)(1+z\bar z)^3(1+\xi\bar\xi)}.
   \]
   It glues exactly as a spin-two section.
3. **Atlas.** Source jets transform by triangular unsigned-Lah matrices with
   nonzero diagonal on chart overlap. Two-chart transport is faithful at every
   finite stage and on the LF union.
4. **Parity/helicity.** Chart parity `P` and helicity conjugation `sigma`
   commute and square to one. With `Q=P sigma`, the electric and magnetic
   projectors are complementary. Their joint port is faithful.
5. **Grade three.** The magnetic density factors through `Pi_M`. On finite
   point-supported magnetic jets its principal symbol is `p^4-q^4`, so it is
   injective. Therefore its full prequotient kernel is exactly the electric
   `Q=+1` sector.
6. **Local target.** The target is the finite-order union of prescribed
   principal parts, point-supported delta jets, and smooth normalization
   backgrounds. Complete local ports are faithful for distinct supports.
7. **Contours.** Green normalization removes the constant mode; spin-two
   reconstruction removes `l=0,1`. Passage to ordinary periods quotients exact
   forms and higher local derivatives. The complete period family is faithful
   on `H1(S^2-P)`, of dimension `|P|-1`.
8. **Reductions.** Gauge is a target quotient, conservation is a source
   restriction, and antipodal matching is the graph of an invertible adapter.
   These operations must not be represented by an untyped sum or deletion.
9. **Distinct punctures.** No additional magnetic interior kernel exists for
   arbitrary finite jet order or finite puncture number.
10. **Collisions.** An exact cluster of `n` label-blind order-`J` packets has
    kernel dimension `(n-1)(J+1)(J+2)/2`. A resolved one-dimensional collision
    moment map through order `L` has rank `min(n,L+1)` for distinct tangent
    directions. Multivariate ranks are the corresponding evaluation ranks.
11. **Named engine classes.** Magnetic towers, `E1`, and `E2` have no source
    preimage. Their physical analogues are, respectively, complementary parity
    aliases, declared zero/exact quotients, and geometry-dependent collision
    circuits. The vector `(1,-3,2)` occurs for the collision stencil
    `(0,1,3/2)` but is not universal.
12. **Cutoffs.** The centered exterior coefficients obey
    `(n+1)c_(n+1)=-(n+3)c_n`, begin at depth four, and require a coherent
    remainder. A positive-coefficient sextic witness proves that every finite
    omitted tail has nonzero grade-three response.

## Stable kernel and observable quotient

For distinct punctures before target quotient,

\[
 \boxed{\ker\mathfrak M_3=\mathcal H_{Q=+1}.}
\]

After restricting to the magnetic sector, the local grade-three kernel is
zero. For a collision moment map `V` followed by an ordinary period instrument
`I`, every further loss is located at one of

\[
 \ker V,\qquad \mathcal G+\mathcal Y_{\rm higher\ jet},
 \qquad \ker(I|_{H^1}).
\]

The observable quotient is therefore not a single Laurent-kernel quotient.
It is the composite of typed source specialization, de Rham reduction, and
instrument selection.

## Central falsifier

Every sufficiently local finite magnetic source jet is detected by the full
local target because multiplication by `p^4-q^4` is injective on polynomials.
The first counterexamples occur only after leaving that category: collision
label erasure, period quotient, selected ports, or characteristic smooth
enlargement.

## Scope

The theorem covers finite labelled puncture configurations, arbitrary finite
source-jet order, their exact and resolved collision strata, the two-chart LF
completion, and finite-order puncture distributions. It does not authorize
arbitrary smooth characteristic solutions, infinite jets, fractional covers,
or free Laurent products.

## Evidence

The exact pipeline is in `completed-physical-engine-diagram.md`. The hostile
boundary is in `completed-physical-engine-hostile-falsifiers.md`. The manifest
`checkers/completed_physical_engine_master_checks.py` reruns every constituent
checker and writes the aggregate result packet.
