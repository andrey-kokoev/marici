# Phase-I surface disjoint-union typing obstruction

Author: `marici.Grothendieck`  
Date: 2026-08-20  
Status: unbounded mapping-class theorem with a source-typed finite audit

## Question left by the face-incidence obstruction

The `n=8` face category has an empty object and categorical coproducts, but
those coproducts are idempotent joins.  Its additive group completion is
therefore zero.  Entry 7 offers the apparent escape: the bare surface layer
has disjoint union, and a separating cut satisfies

\[
\Delta_C:\mathcal A_\Sigma\longrightarrow
\mathcal A_{\Sigma\setminus C},
\qquad
\mathcal A_{\Sigma\setminus C}
\simeq
\mathcal A_{\Sigma_L}\otimes\mathcal A_{\Sigma_R}.
\]

This packet checks whether the statement already supplies the finite
coproduct required by Nima's Phase-I plan.

## Three notions that must remain distinct

For two surfaces there are three different claims:

1. `Sigma_L sqcup Sigma_R` exists as a disconnected surface;
2. disjoint union is a symmetric monoidal operation;
3. disjoint union is a categorical coproduct, with component injections and
   a universal mapping property.

The first does not imply the second, and the second does not imply the third.
Entries 7 and 46 establish monoidality/factorization in their respective
surface-function and Brauer state layers.  Entry 10 lists a symmetric
monoidal state category as required structure.  None of these statements
defines component injections in one coefficient-neutral Carrier category.

## Exact source-typing failure

Write

\[
D=\Sigma_L\sqcup\Sigma_R.
\]

The separating-cut statement types the nonidentity operation as

\[
\Sigma\longrightarrow D
\]

on the surface-function assignment.  A coproduct diagram instead first
requires two legs

\[
\Sigma_L\xrightarrow{i_L}D
\xleftarrow{i_R}\Sigma_R.
\]

The cut has the correct target but the wrong source for either leg.  Mapping
classes supply only invertible arrows between surfaces of the same topological
type.  They cannot turn the connected parent `Sigma` into either cut
component, nor can they include a connected component into a disconnected
surface.

Thus the explicitly established coefficient-neutral operation graph contains
zero of the two required component-injection legs.  The exact typed deficit is

\[
\boxed{2-0=2\ne0.}
\]

Without the legs, the proposed bijection

\[
\operatorname{Hom}(D,Z)
\stackrel{?}{\cong}
\operatorname{Hom}(\Sigma_L,Z)
\times
\operatorname{Hom}(\Sigma_R,Z)
\]

cannot yet be stated, much less proved.

This is an insufficiency theorem for the admitted operation list, not a claim
that no larger surface category can contain such arrows.

## Positive control: multiplicity survives monoidally

Let `U` be one connected marked surface and retain only mapping-class
isomorphisms.  Diffeomorphisms preserve connected components.  Hence

\[
U^{\sqcup m}\cong U^{\sqcup n}
\quad\Longrightarrow\quad m=n.
\]

So the mapping-class groupoid generated from `U` under actual disjoint union
does retain unbounded multiplicity on isomorphism classes.  The checker
verifies every pair of powers through eight as a finite implementation
control.  This is the first positive trace of the desired additive monoid.

But the same invariant proves

\[
\operatorname{Hom}_{\mathrm{MCG}}(U,U\sqcup U)=\varnothing.
\]

The mapping-class groupoid therefore gives a symmetric monoidal sum whose
`pi_0` is a candidate free commutative monoid, not a categorical coproduct.
It passes multiplicity and fails the universal-property requirement.

## Why coefficient algebras do not close the neutral gate

There is a familiar conditional repair.  In the category of commutative
algebras over a fixed ring `R`,

\[
A\otimes_R B
\]

is a categorical coproduct.  Its legs use the algebra units:

\[
a\longmapsto a\otimes1,
\qquad
b\longmapsto1\otimes b.
\]

This explains why entry 7's factorization formula resembles a coproduct.  It
does not prove the Phase-I Carrier statement:

- the base ring `R` and its unit are coefficient data;
- the arrows are algebra homomorphisms in a realization target;
- no cited result proves that these target arrows lift to or reflect
  component injections in the common coefficient-neutral Carrier.

Using the coefficient-algebra coproduct would therefore cross the Carrier /
coefficient-lens boundary fixed in the conventions packet.

## Exact checker

The companion checker constructs the literal finite source/target graph,
computes the missing injection-leg deficit, and separately verifies the
mapping-class component-count control through eight disjoint-union powers:

- `research/grothendieck/checkers/phase_i_surface_disjoint_union_typing.py`;
- `research/grothendieck/results/phase-i-surface-disjoint-union-typing.json`.

It records SHA-256 digests of entries 7, 10, and 46.  The construction uses
no coefficient ring, prime, rank, pole order, or cardinality label as a
Carrier input.

## Phase-I verdict

The surface route improves on the face-incidence route but still does not
pass the gate:

\[
\boxed{
\text{surface disjoint union preserves multiplicity as a monoidal sum,
but no Carrier coproduct morphisms or universal property are derived.}
}
\]

The exact first unavailable datum is now a morphism class: source-authorized
noninvertible component injections.  After those are defined, their universal
mapping property must still be proved.

The result leaves a precise fork for the directed plan:

1. retain “finite coproduct” literally and construct the missing Carrier
   morphisms; or
2. weaken the additive requirement to a symmetric monoidal sum, in which
   case connected-component decomposition supplies a candidate free additive
   monoid and the next gate becomes a distributive regional product.

The second route changes the stated Phase-I hypothesis and is not adopted
here without direction.

No ledger entry is claimed by this packet.
