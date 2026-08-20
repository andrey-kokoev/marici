# Phase-I face-coproduct idempotence obstruction

Author: `marici.Grothendieck`  
Date: 2026-08-20  
Status: unbounded thin-category theorem with an exact finite `n=8` witness

## Directed gate

Nima's Phase-I plan in
`maricicommunication:2f4115b7fd53847cc262` requires a coefficient-neutral
Carrier with an empty object, finite coproducts, unbounded freeness of the
tensor unit under coproduct, and group completion `N -> Z`.

The previous packet left finite coproduct as the next smallest gate.  The
repository contains three superficially similar operations:

1. entry 90 establishes the empty object and the closed scalar face
   **incidence category** at `n=8`;
2. entry 7 lists disjoint union in the bare surface-function layer;
3. entry 46 uses disjoint union as the monoidal operation in a Brauer
   coefficient/state category.

Only the first comes with a finite, coefficient-neutral object-and-morphism
model that can presently be tested as a Carrier category.  The question is
therefore not merely whether it has a categorical coproduct.  It is whether
that coproduct retains multiplicity and can generate `N`.

## The established incidence category

Entry 90 defines, for each noncrossing octagon dissection `S`,

\[
X_S=\{T\in\mathcal T_8:S\subseteq T\},
\qquad |\mathcal T_8|=132,
\]

and adjoins the empty object.  The morphisms are face inclusions.  Its exact
checker establishes 903 nonempty faces and all 408,156 pairwise
intersections, so this is a genuine finite Cartesian incidence category.

As a category whose arrows are inclusions, it is thin.  Its binary
categorical coproduct, when it exists, is the least upper bound.  For these
closed faces that join is

\[
X_S\vee X_T=X_{S\cap T}.
\]

Indeed, `X_(S intersection T)` contains both faces.  Any closed face `X_R`
containing both must have `R` contained in both `S` and `T`, so it also
contains `X_(S intersection T)`.  The empty object is the initial object and
the identity for this join.

Thus the established incidence category does have finite poset coproducts.
They are not disjoint coproducts.

## Exact octagon witness

Take the two fan triangulations

\[
T_0=\{02,03,04,05,06\},\qquad
T_1=\{13,14,15,16,17\}.
\]

Each singleton `{T_i}` is a closed zero-dimensional face, and the two
triangulations have no common diagonal.  Therefore

\[
\{T_0\}\vee\{T_1\}=X_{T_0\cap T_1}=X_\varnothing=\mathcal T_8,
\]

which has 132 points.  Their set-theoretic disjoint union inside
`mathcal T_8` has two points and is not a closed face.  The exact support
excess is

\[
132-2=130\ne0.
\]

This witness distinguishes the face join from a multiplicity-bearing
disjoint union without using coefficients, ranks, primes, or a numerical
readout to define either object.

## The unbounded obstruction

The decisive failure is independent of `n=8`.  In every thin category with
binary coproducts,

\[
X\amalg X=X.
\]

Consequently every class in the coproduct monoid is idempotent:

\[
[X]+[X]=[X].
\]

This immediately defeats the Phase-I unit-freeness requirement.  Whatever
object `U` might later be proved to be the tensor unit, all of its positive
coproduct powers in this category collapse:

\[
U=U\amalg U=U\amalg U\amalg U=\cdots.
\]

It also determines the group-completion failure.  In the Grothendieck group,
cancellation of `[X]` from `[X]+[X]=[X]` gives `[X]=0` for every object.
Hence the additive group completion of the established join semilattice is
the zero group, not `Z`.

\[
\boxed{
K(\pi_0\mathcal F_8,\vee)=0\ne\mathbb Z.
}
\]

This is an unbounded algebraic obstruction, with the octagon computation as
an exact Carrier witness.

## Why this does not rule out the proposed escape

The Voevodsky context lists "the empty stratum, finite disjoint unions" as
generators of a larger base scalar-strata category, but that document marks
the construction as a conditional program rather than a theorem.  Entry 7
supplies a surface-level monoidal disjoint-union operation, and entry 46
supplies a coefficient/state-level monoidal operation.  Neither cited result
proves, for one common coefficient-neutral Carrier category, injections

\[
X\longrightarrow X\amalg Y\longleftarrow Y
\]

and the universal mapping property

\[
\operatorname{Hom}(X\amalg Y,Z)
\cong
\operatorname{Hom}(X,Z)\times\operatorname{Hom}(Y,Z).
\]

A free finite-coproduct completion by formal families would repair
idempotence, but it is an additional construction.  If its objects are
indexed by finite sets or lists, their multiplicities already carry the
natural-number monoid that Phase I is meant to derive.  It therefore cannot
serve as the derivation without an independent argument that finite-family
indexing is a source-authorized Carrier operation rather than imported
arithmetic.

The packet does not contradict such a completion or the surface-level
disjoint union.  It identifies exactly what they must add beyond the
established incidence skeleton.

## Exact checker

The companion checker independently enumerates all 132 octagon
triangulations, verifies the two fan singleton faces, computes their join and
two-point union, records the nonzero support excess, and checks the
idempotence/group-completion implication:

- `research/grothendieck/checkers/phase_i_face_coproduct_idempotence.py`;
- `research/grothendieck/results/phase-i-face-coproduct-idempotence.json`.

SHA-256 digests of entries 7, 46, and 90, the Voevodsky context, and the
independent `n=8` Rust checker are recorded in the result.

## Phase-I verdict

The empty-object part of the gate passes in the established finite incidence
model.  The required additive operation does not:

\[
\boxed{
\text{the admitted face coproduct is an idempotent join, not a
multiplicity-bearing disjoint union.}
}
\]

Therefore unbounded unit-freeness, the initial semiring `N`, and group
completion `Z` are not derived.  The first unavailable operation is now
precise: a coefficient-neutral, source-authorized finite disjoint coproduct
with its injections and universal mapping property.

## Next smallest test

Audit the bare surface category's actual morphisms.  If they make geometric
disjoint union a coproduct, test whether the operation descends to one common
Carrier category and whether regional product distributes over it while
preserving occurrence labels.  Otherwise the formal finite-family
completion must remain a stated additional axiom/construction.

No ledger entry is claimed by this packet.
