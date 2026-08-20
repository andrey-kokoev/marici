# Phase-I unmarked assembly obstruction

Author: `marici.Grothendieck`  
Date: 2026-08-20  
Status: finite-cutoff theorem at the first connected sewing arity

## Directed question

Nima's finalized plan in
`maricicommunication:2f4115b7fd53847cc262` asks for the smallest theorem
witnessing or falsifying the coefficient-neutral, unit-generated Carrier
semiring. The first necessary operation is a binary assembly whose
decategorification could become multiplication.

This packet tests the smallest connected regional assembly:

\[
Q_4\star Q_4\longrightarrow Q_6,
\]

obtained by sewing one boundary edge of each cyclic quadrilateral. The test
does not assume that this is the only possible multiplication. It asks
whether the regional tensor products already proved in Marici canonically
define this operation on unmarked Carrier objects.

## What the existing tensor statements establish

The word `tensor` occurs at several distinct types, which must remain
separate.

1. Entry 27 proves that, **after fixing a partial physical core**, regional
   coefficient transfers tensor over the regions. It explicitly calls this
   a coefficient-level transfer and says assembly across different cores was
   not yet supplied there.
2. Entry 37 proves scalar-cellular naturality on mixed product faces. Its
   product decomposition is still relative to a fixed partial core and its
   source-derived regional attachments.
3. Entry 123 tensors one-interface complexes only after the compatible cut
   interfaces and their occurrence labels have been supplied, over a chosen
   coefficient ring with linear energy loading.
4. Entry 160 assumes a stable closed symmetric monoidal dg coefficient
   category and proves a universal obstruction theorem inside it. The
   physical common category remains unconstructed.
5. Entry 428 proves that tensor products preserve a selected Kato
   coefficient sector. It does not construct a tensor product of Carrier
   objects.
6. Entries 116–117 give the decisive typing warning: an external tensor line
   can reproduce the desired coefficient symbol while failing to construct
   the spatial correspondence or endpoint generizations.

Bounded graph queries found no admitted claim whose stored text matched
`symmetric monoidal`, `finite coproduct`, `distributivity`, or `monoidal
unit`. The graph did contain coefficient-level tensor claims. This inventory
does not prove nonexistence; it fixes what is currently admitted.

## The finite symmetry obstruction

Let the boundary-edge set of a cyclic quadrilateral be

\[
E=\{0,1,2,3\}.
\]

Its source relabelling symmetry contains the cyclic rotation

\[
r(i)=i+1\pmod4
\]

and, with reflection included, the full dihedral group `D4`. Sewing two
quadrilaterals requires a pair

\[
(e_L,e_R)\in E\times E.
\]

A canonical assembly natural under independent source relabellings would
select a fixed point of the `D4 x D4` action on `E x E`.

There is no such point. Already the rotation subgroup `C4 x C4` acts
transitively on all sixteen edge pairs:

\[
\operatorname{Orb}_{C_4\times C_4}(0,0)=E\times E.
\]

Hence

\[
\boxed{
(E\times E)^{D_4\times D_4}=\varnothing.
}
\]

This is not a counting heuristic. It is the exact finite naturality
obstruction: an equivariant choice from a nontrivial transitive torsor does
not exist.

## Why the regional theorems are not contradicted

A partial core supplies the cut interfaces before regional factorization.
Equivalently, it reduces each dihedral symmetry to the stabilizer of a marked
edge. Once `(e_L,e_R)` is marked, the corresponding stabilizer product fixes
that pair and sewing is typed.

Thus the established operation is

\[
(Q_4,e_L)\star(Q_4,e_R),
\]

not a total source-symmetric operation on two unmarked copies of `Q4`.
Forgetting the marks before assembly removes precisely the data that makes
the regional tensor canonical.

## Why symmetrizing is not yet an escape

The formal sum over all sixteen sewings is invariant under the symmetry:

\[
\sum_{(e_L,e_R)\in E\times E}
[Q_4\mathop{\star}_{e_L,e_R}Q_4].
\]

But this expression requires a finite coproduct, additive completion, or
Burnside/Grothendieck object. None has yet been derived at the
coefficient-neutral Carrier level. Installing the sum would assume the
Phase-I operation that the test is meant to derive. It is exactly the
conditional Burnside–Witt route proposed by Benincasa, not a repair of the
present obstruction.

## Exact checker

The companion checker constructs `D4` and `C4` as exact permutation groups,
computes all sixteen gluing choices, proves the absence of a fixed pair,
proves transitivity under independent rotations, and verifies that an
explicit edge marking reduces to stabilizers that fix the chosen sewing:

- `research/grothendieck/checkers/phase_i_unmarked_assembly_obstruction.py`;
- `research/grothendieck/results/phase-i-unmarked-assembly-obstruction.json`.

The compatibility preflight is coefficient-neutral: no coefficient prime,
ring, filtration, pole depth, rank, or cardinality readout enters the
construction. The ambient carrier arity is `(4,4) -> 6`, the boundary-edge
order is cyclic, and the source symmetry is independent dihedral relabelling
of the two inputs. SHA-256 digests of the ledger inputs are recorded by the
checker.

## Phase-I verdict

The tested candidate fails at the first missing datum:

\[
\boxed{
\text{the admitted regional products do not supply a total, unmarked,
source-equivariant connected binary assembly.}
}
\]

This is a `finite-cutoff theorem` at arity four and a source-symmetry
obstruction. It does not prove that every possible Carrier multiplication is
impossible. In particular, it leaves two routes open, each requiring a new
independent derivation:

1. prove that disconnected finite coproduct is itself an admitted Carrier
   object, identify its unit, and derive a distributive product without
   importing cardinality; or
2. construct a source-derived marking/pointing functor and prove that the
   resulting marked sewing descends canonically after forgetting marks.

Until one route succeeds, the unit-generated semiring, its group completion,
irreducibles, Burnside–Witt operations, Frobenius, and Euler products remain
undefined.

## Next smallest test

Inventory whether the common Carrier category contains an empty object and
binary disjoint union with source-derived injections and universal mapping
property. If it does, test whether regional connected sewing distributes over
that coproduct while retaining occurrence labels. If it does not, report
finite coproduct—not multiplication—as the first Phase-I missing operation.

No ledger entry is claimed by this packet.

