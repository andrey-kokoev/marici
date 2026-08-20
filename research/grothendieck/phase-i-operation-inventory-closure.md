# Phase-I operation-inventory closure

Author: `marici.Grothendieck`  
Date: 2026-08-20  
Status: typed closure over the currently admitted candidate inventory

## Purpose

Nima's finalized Phase-I plan asks for one coefficient-neutral Carrier with
finite coproduct, a second tensor, a tensor unit, distributivity, unbounded
unit-freeness, additive group completion, and an intrinsic multiplication
whose irreducibles could become primes.

The preceding packets tested each serious operation individually.  This
packet closes the inventory by placing every admitted meaning of “union,”
“product,” “tensor,” and “unit” at its actual type.  Closure here means
exhaustion of the named source candidates, not a theorem that no future
Carrier construction is possible.

## Additive candidates

| Candidate | Categorical coproduct | Retains multiplicity | Outcome |
|---|---:|---:|---|
| closed-face join | yes | no | idempotent; group completion is zero |
| geometric surface disjoint union | not proved | yes | free additive monoid only after explicit monoidal relaxation |

The two routes split the required properties.  The established categorical
coproduct forgets multiplicity; the multiplicity-sensitive operation lacks
component injections and the universal mapping property.

Under the declared monoidal relaxation, unique connected decomposition does
derive the free commutative monoid and its free abelian group completion,
hence additive `N` and `Z`.  This does not repair the literal coproduct gate
and does not provide multiplication.

## Multiplication candidates

A Phase-I product must satisfy all six conditions:

1. live at the Carrier level;
2. be coefficient-neutral;
3. be total on unmarked generated objects;
4. be source-equivariant;
5. possess an admitted object unit; and
6. distribute over the additive operation.

| Candidate | Carrier | Neutral | Total unmarked | Equivariant | Object unit | Distributive |
|---|---:|---:|---:|---:|---:|---:|
| connected edge sewing | yes | yes | no | no | no | unproved |
| fixed-core regional Cartesian product | no | no | no | typed after fixing core | no | unproved |
| framed physical-line external product | no | no | framed only | yes in scope | coefficient unit only | unproved |
| resolved Brauer-state tensor | no | no | yes in state category | yes in scope | no Carrier unit | unproved |
| formal finite-family pairwise tensor | not admitted | formally | formally | formally | not admitted | by construction |

No row satisfies all six conditions.

### Connected edge sewing

This is the only coefficient-neutral geometric multiplication candidate.  It
fails twice independently:

- unmarked quadrilateral sewing has no source-symmetry fixed interface pair;
- its arity law `n_L star n_R = n_L+n_R-2` requires an arity-two unit absent
  from the stable family.

The four-point primitive unit belongs to a framed coefficient line and has
Carrier arity residual `2`.

### Fixed-core and framed products

Entry 27 explicitly calls the regional result a coefficient-level transfer
after a partial physical core and its regions are fixed.  The all-even
framed theorem is stronger and genuinely coherent, but remains in the
cellular fs/Kato coefficient sector.  Neither gives a total unmarked Carrier
bifunctor or an object unit.

### Brauer tensor

Entries 46--47 construct a resolved state category over `Z[D]`, specialize
`D -> 1`, and then apply the derived modular envelope.  This is a powerful
state/coefficient tensor.  Treating it as the coefficient-neutral Carrier
product would reverse the established construction order and cross the
Carrier/coefficient-lens boundary.

### Formal finite families

The formal pairwise tensor of finite families would distribute by definition
and would recover the familiar multiplication of component multiplicities.
It is precisely the free-rig completion that the directed plan forbids us to
insert without source derivation.  Its finite index pairing is the target
multiplicity law, not evidence that Marici's Carrier forces it.

## Exact obstruction vector

The composed exact audits yield

\[
\boxed{(130,2,1,2)}
\]

with typed coordinates:

1. `130`: face-join support excess over a two-point disjoint union;
2. `2`: missing surface coproduct-injection legs;
3. `1`: missing fixed point for the first unmarked connected sewing;
4. `2`: four-point Carrier-unit arity residual.

These are different defects and cannot cancel one another.

## Realization-invariance gate

The framed fs/Kato product supplies one strong realization-specific control.
There is no independently derived common Carrier tensor whose string and
cosmology realizations can both be checked.  The first arithmetic-lens
falsifier also shows why a coefficient readout cannot replace that step:
occurrence-resolved, occurrence-forgotten, and quarter-enlarged lattices have
Smith orders `1`, `2`, and `4`.

Thus no invariant arithmetic readout has been obtained by descending from a
common multiplication.

## Exact checker

The companion checker imports and revalidates all six prior result packets,
constructs the typed candidate matrix, verifies that no multiplication row
passes every requirement, and records the exact obstruction vector:

- `research/grothendieck/checkers/phase_i_operation_inventory_closure.py`;
- `research/grothendieck/results/phase-i-operation-inventory-closure.json`.

Its deliberate failure requires at least one passing multiplication
candidate and observes zero, giving candidate deficit `1`.

## Final Phase-I verdict for the admitted inventory

\[
\boxed{
\begin{gathered}
\text{literal finite coproduct: not derived},\\
\text{conditional additive }\mathbb N\text{ and }\mathbb Z: derived,\\
\text{unital distributive Carrier multiplication: not derived},\\
\text{initial semiring and intrinsic primes: not derived}.
\end{gathered}
}
\]

Phase I therefore does not pass, and the conditional Phase-II
Burnside--Witt construction is not authorized by the finalized plan.

Further progress requires one of three explicit authority-bearing changes:

1. admit a new coefficient-neutral Carrier product and unit;
2. admit component-inclusion morphisms and prove geometric disjoint union is
   a coproduct; or
3. revise the finalized Phase-I requirements.

No ledger entry is claimed by this packet.
