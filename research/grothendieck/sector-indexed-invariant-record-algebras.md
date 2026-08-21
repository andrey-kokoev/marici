# Sector-indexed invariant-record algebras: two composition squares

## Scope

This packet formalizes the category requested by Nima and verifies the first
two nontrivial composition squares, in radiative memory and cosmology. It does not
postulate a cross-sector bridge, a Carrier multiplication, or a Phase-II
object.

## Typed objects

An object is a tuple

\[
X=(s,V,G,R_X,p_X,\mathcal R_X),
\]

where `s` is the sector, `V` its substrate/readout space, `G` its sourced
symmetry, `R_X` either `A[V]^G` or a declared physical-observable subalgebra,
`p_X` the physical constructor/selection provenance, and `mathcal R_X` the
support, chain, framing, and coherence resources.

The current four-sector objects remain heterogeneous:

\[
R_{\rm mem}=\mathbb Q[q_2,q_3],\quad
R_{{\rm str},n}=\mathbb Q[x^2]\text{ or }\mathbb Q[x],\quad
R_{\rm cos}=\mathbb Q^{32},
\]

while flavor supplies only a typed observable subalgebra, not a presentation
of its complete weak-basis invariant ring.

## Constructor-induced morphisms

Let `X=(V,G,R_X,...)` and `Y=(W,H,R_Y,...)`. A sourced constructor

\[
F:V\longrightarrow W
\]

with a declared homomorphism `phi:G -> H` induces the contravariant map

\[
F^*:R_Y\longrightarrow R_X,\qquad f\longmapsto f\circ F,
\]

exactly when all of the following typed conditions hold:

1. `F` and `phi` are source-derived, with `F(gv)=phi(g)F(v)`;
2. pullback closes on the declared algebras, `F^*(R_Y) subset R_X`;
3. `F` intertwines the physical selections/readouts;
4. the required support, chain, framing, and coherence resources transport.

For complete invariant rings, equivariance proves invariant closure. For a
proper observable subalgebra, closure is an additional condition. Conversely,
an algebra homomorphism without a sourced `F` and these resources is not a
morphism in this category. These conditions are necessary and sufficient by
definition of the typed constructor category; they do not claim that every
abstract invariant-ring homomorphism comes from a substrate constructor.

Composition is contravariant:

\[
(E\circ F)^*=F^*\circ E^*.
\]

## First closed fiberwise diagram: radiative memory

The three direction-labelled memory samples form the permutation module
`P=Q^3`. Its constant line and directional plane

\[
V=\{(x,y,z):x+y+z=0\}
\]

are source-established by the radiative-memory audit. The first physical
constructor is the constant-mode quotient

\[
F:P\to V,\qquad
F(x,y,z)=(x-\bar x,y-\bar x,z-\bar x),
\quad \bar x=(x+y+z)/3.
\]

The second constructor is the `D3`-invariant scalarization

\[
E:V\longrightarrow\operatorname{Spec}\mathbb Q[q_2,q_3].
\]

Write `e1,e2,e3` for the elementary symmetric generators of `Q[P]^D3`.
The induced pullbacks are

\[
F^*(q_2)=\frac{e_1^2}{3}-e_2,
\qquad
F^*(q_3)=e_3-\frac{e_1e_2}{3}+\frac{2e_1^3}{27}.
\]

The sourced composition closes:

\[
(E\circ F)^*=F^*\circ E^*.
\]

Exact controls verify 2,197 compositions, 13,182 direction permutations, and
10,985 constant-mode shifts. This is limited to the finite constant-sample
line; it does not model the full sphere `l<=1` kernel.

The zero-mean inclusion `i:V->P` still gives the exact algebraic identities
`i^*(e1,e2,e3)=(0,-q2,q3)` and `i^*F^*=id`, but it is not needed for the
physical composition and remains untyped as a physical constructor.

## Second closed fiberwise diagram: cosmology

For `G=(C2)^5`, Entry 1225 supplies coefficient and Betti labels `(g,h)`,
simultaneous deck transport, and the physical pairing. The sourced quotient
and selection are

\[
F(g,h)=g\oplus h,
\qquad E=\delta_0\in\operatorname{Fun}(G,\mathbb Q).
\]

Their composite is exactly

\[
(E\circ F)(g,h)=\delta_0(g\oplus h)=\delta_{g,h}.
\]

The checker derives all 1,024 compositions and orbit fibers and all 32,768
simultaneous deck-transport identities. The two sectors therefore realize
the same diagram shape:

\[
\text{quotient a covariant redundancy}
\longrightarrow
\text{apply an invariant physical selection}.
\]

This is shared calculus, not a cross-sector algebra homomorphism.

## Cross-sector and arithmetic obstruction

The census supplies no sourced constructor between distinct sector fibers.
Thus the current cross-sector category has four objects and no admitted
cross-sector arrows. This is absence of a bridge, not algebraic
incompatibility.

The first formal repetition family can nevertheless be tested. On memory,
linear scaling gives

\[
[n]^*q_2=n^2q_2,\qquad [n]^*q_3=n^3q_3,
\]

so every index acts on the graded invariant algebra. On a finite abelian deck
group `G`, the pullback of the physical identity idempotent is

\[
[n]^*\delta_0(d)=\delta_0(nd).
\]

This preserves `delta_0` exactly when multiplication by `n` has trivial
kernel, equivalently

\[
\gcd(n,\exp G)=1.
\]

For five-site cosmology, `G=(C2)^5`, so precisely the positive odd indices
survive. Every even index collapses all differences to zero and changes 992
of the 1,024 physical pairing values. The maximal common operation indices
for memory and this cosmology fiber therefore form the positive odd
multiplicative monoid. They are not closed under addition and hence do not
form the conditional semiring.

Thus automatic common `pi_0`-semiring naturality is exactly obstructed, not
merely untyped. The surviving prime-to-exponent system is only a
multiplicative indexing theorem. No Adams, Frobenius, or lambda structure is
claimed. Extending it still requires independently sourced sectorwise
physical repetition constructors and selection-coherence cells.

## Variance under changing deck groups

For a homomorphism of finite deck groups `phi:G->H`, ordinary pullback gives

\[
\phi^*\delta_{0,H}=\mathbf 1_{\ker\phi}.
\]

It preserves the frozen identity selection exactly when `phi` is injective.
This adds a variance clause to the typed category: group-level repetition is
natural for every homomorphism, but physical-selection pullback is natural
only along deck monomorphisms.

For a quotient or forgetting map, the algebraically canonical repair is the
covariant fiber sum

\[
(\phi_!f)(h)=\sum_{g:\phi(g)=h}f(g).
\]

It satisfies

\[
\phi_!\delta_{0,G}=\delta_{0,H},\qquad
(\psi\phi)_!=\psi_!\phi_!,\qquad
\phi_!(f\,\phi^*g)=\phi_!(f)g.
\]

The unnormalized sum is forced: averaging rescales the identity selection by
`1/|ker phi|`. This transfer is a canonical algebraic resource candidate,
not yet a physical cosmological constructor. Admission requires a
source-derived deck trace/Gysin map with orientations, support, multiplicity,
and chain normalization.

## Verdict

The minimal typed organization is a sector-indexed category with two verified
nonidentity composition chains. Radiative memory and five-site cosmology
instantiate the same quotient-then-selection diagram independently.
Cross-sector morphisms remain untyped. The full common semiring action is
falsified by the cosmological selection, while the prime-to-exponent
multiplicative subsystem survives. Across changing deck groups, pullback is
selection-compatible only for monomorphisms; fiber-sum transfer is the exact
algebraic repair candidate for noninjective maps. The next admissible
experiment is to derive such a trace/Gysin constructor from source geometry,
not to promote the finite-group formula by analogy.

## Artifacts

- `research/grothendieck/checkers/sector_indexed_invariant_record_algebras.py`;
- `research/grothendieck/results/sector-indexed-invariant-record-algebras.json`;
- `research/nima/radiative-memory-readout-composition.md`;
- `research/nima/cosmology-readout-composition.md`;
- `research/nima/readout-arithmetic-naturality-obstruction.md`;
- `research/nima/prime-to-exponent-readout-operations.md`;
- `research/nima/deck-selection-variance.md`;
- `research/nima/finite-deck-transfer.md`.
