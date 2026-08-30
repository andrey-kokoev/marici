# Nontrivial associator residue can be structure, not defect

## Question

What should be done with an associator that satisfies the pentagon but has a
nontrivial source-preserving cohomology class?

## Claim boundary

It should not automatically be repaired away. A normalized three-cocycle
defines the associator of a skeletal categorical group. When source-derived,
its nontrivial class is constitutive higher structure. Without source
derivation it remains an unresolved candidate, not an authorized constructor.

## Skeletal categorical group

Let \(G\) be a group of objects and let \(A\) be an abelian group of
automorphisms. In the simplest trivial-action model:

- objects are elements \(g\in G\);
- each object has automorphism group \(A\);
- tensor product on objects is multiplication in \(G\);
- tensor product on automorphisms is multiplication in \(A\);
- the associator at \((g,h,k)\) is
  \(\omega(g,h,k)\in A\).

Normalization supplies strict unit constraints. The pentagon is exactly the
three-cocycle identity for \(\omega\).

Therefore a coherent nontrivial associator is not a failed category. It is the
data that turns an ordinary group shadow into a categorical group.

## Residue promotion

The scalar associator residual occupies three possible types:

1. pentagon failure: a defect requiring repair;
2. cocycle and coboundary: presentation-dependent behavior removable by an
   authorized frame change;
3. cocycle and non-coboundary: a higher structural class, provided the source
   derives it.

This is the exact sense in which a coherencer residue can become the next-rung
object. It is not appended to hide failure. It is promoted only after passing
the higher coherence law and failing the admissible trivialization test.

## The \(C_2\) model

Take objects \(C_2\), automorphisms \(\{\pm1\}\), and

\[
\omega(a,b,c)=(-1)^{abc}.
\]

All associators are invertible, the unit-normalization equations hold, and the
pentagon holds. The class is nontrivial on the fixed skeletal carrier. This
defines a coherent categorical group with the same object-level multiplication
as \(C_2\) but additional higher composition data.

Forgetting automorphisms returns the ordinary group \(C_2\). Taking absolute
values also returns a strict-looking shadow. Both forgetful views erase the
distinction between the trivial and nontrivial categorical groups.

## Source-authority gate

Cohomological consistency alone does not prove physical or operational
relevance. Promotion requires:

1. a source-derived associator;
2. the exact coefficient group and its action;
3. pentagon verification;
4. a frozen class of admissible frame changes;
5. proof that the class is nontrivial under those changes;
6. a readout or constructor consequence sensitive to the class.

Without the sixth item, the higher class may be mathematically real but
operationally unobserved. Without the first, it is merely a fitted model.

## Cross-sector interpretation

- In topological phases, nontrivial associators can be genuine fusion data.
- In software authority, a residual comparison cell becomes a constructor
  only when its authority root and operational effect are declared.
- In flavor or optics, a calibrated phase cocycle may represent real transport
  structure, while an arbitrary fitted phase does not.
- In boundary completion, a source-derived anomaly class could be the missing
  higher object; a scalar determinant residual alone cannot authorize that
  interpretation.

## DPC

When a coherent residual survives:

1. test the relevant higher coherence equation;
2. test all admissible trivializations;
3. classify the surviving residue as source-derived or fitted;
4. construct the categorical extension only in the source-derived case;
5. identify an operational probe of the class;
6. otherwise retain it as an unresolved observation.

## Disposition

The coherence tower need not terminate by forcing every residual to zero.
It can terminate by recognizing a nontrivial coherent residual as the
associator of the correct higher object. The decisive gates are source
derivation, nontriviality, and observability.

## Verification

The checker check_c2_categorical_group.py verifies normalization, invertibility,
all pentagon instances, nontriviality against normalized source-local
rephasings, and the equality of the strict object shadow for the trivial and
nontrivial associators.
