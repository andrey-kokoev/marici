# A checked two-schema complete comparison basis for normalization maps

## Theorem

For the frozen `DependentResolutionAlgebra` interpretation, two explicit law
schemas together with the existing `Structural.Generated` closure constructors
are complete for **every actual semantic comparison witness**:

    (q : Complete) (d e : Resolve Seed q) (p : evaluate d = evaluate e)
      -> Σ(c : Generated d e). sound(c) = p.

`NormalizationComparisonBasis.agda` proves this exact existing
`Structural.Completeness` type, at every universe level. No all-source
completeness premise, postulate or semantic-path import constructor is used.

This is completeness for the chosen normalization-map interpretation. It is
not completeness for every possible observer of resolution histories, nor a
finite presentation of all internal identities of arbitrary atomic types.

## The two schemas

1. **Seed normalization.** A retained normalization route seed compares with
   the canonical normalization seed at its same complete endpoint.
2. **Rule normalization.** A rule applied to canonical child histories compares
   with the canonical seed at its output endpoint.

The second schema only handles canonical children. It does not take an
arbitrary tree or requested semantic witness as an argument. Neither schema
accepts a semantic path to be imported into Generated.

The unchanged closure constructors supply reflexivity, inversion,
concatenation and dependent congruence. This is a finite family of schemas,
not a finite set of instances or a finite-branching restriction. A congruence
premise can be indexed by an arbitrary type.

## Why it is complete

Structural induction constructs `reduce(d) : Generated d canonical(q)`.
At a seed, use seed normalization. At a rule, normalize all children using
dependent congruence and then apply rule normalization. Concatenating
`reduce(d)` with the inverse of `reduce(e)` gives a generated comparison.

The semantic carrier consists of maps

    Π(x : El Q). Σ(y : Normal(Q)). y = normalize(Q,x).

It is contractible as a dependent function of equivalence fibres. Therefore
the identity type between any two evaluated maps is contractible. This proves
that the generated comparison's interpreted witness equals the **requested**
p, not merely that some comparison exists. Path-space contractibility also
provides higher comparisons and can be iterated.

These facts concern normalization operations over fixed faithful coordinates.
They do not assert that El Q or its path spaces are contractible. Arbitrary
index and atomic loops remain in the normalized values and retained inputs.
The non-E/Pi rule semantics remains the previously explicit choice of
canonical normalization of the full output expression; it is not promoted
to a universal history-sensitive observer.

## Checked positive and hostile cases

`NormalizationComparisonBasisRegression.agda` checks:

* the previous explicit dependent reordering is now derived from these two
  schemas, without adding `dependent-reorder` as a new primitive law;
* its original comparison witness is reconstructed;
* the comparison under an infinitely indexed native Pi context is generated;
* distinct raw histories and distinct derivations remain distinguishable;
* the exact requested witness is retained in the output record;
* the entire resulting comparison package is a subsequent input at the next
  universe level, with that whole prior package recoverable by reflexivity;
* deleting rule normalization leaves an invariant separating rule roots from
  seed roots, so the required rule/seed comparison is not derivable;
* deleting seed normalization leaves an invariant separating the actual
  four-step and five-step route seeds, so their comparison is not derivable.

The deletion tests show both roles are needed in this presentation. They are
not a minimality theorem across all imaginable presentations.

## Retention and remaining programme

`Requested` retains the complete endpoint, both raw histories, the requested
witness, generated derivation and witness reconstruction. No quotient of raw
route or derivation records is introduced.

The finite-basis obligation is now solved for this frozen semantics. Still
open: native compilation of the primitive route steps currently embedded in
seeds, and the broader source-identity/interpretation coverage obligations.
The native compiler must preserve remembered endpoint provenance rather than
silently identifying retained and unwrapped packages.

## Verification

Fresh verification passed Agda 2.8.0-3d04bac / Cubical 0.9 with
`--safe --cubical --guardedness` and `--ignore-interfaces`:

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NormalizationComparisonBasisRegression -Fresh
```

* `research/nima/agda/NormalizationComparisonBasis.agda`
* `research/nima/agda/NormalizationComparisonBasisRegression.agda`
* `research/nima/results/agda-NormalizationComparisonBasisRegression.json`
* `research/nima/results/agda-NormalizationComparisonBasisRegression.log`

Tree: `issue-tree:ec9d8dc9a050db37f5f82cd0`.
