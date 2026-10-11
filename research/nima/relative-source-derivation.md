# Relative source-derivation criterion

Contract: `contracts/relative-source-derivation.v1.json`.
Typed algebraic fragment: `agda/TickRelativeSourceContract.agda`.

## Allowed premises

We explicitly permit the complex Cauchy completion, its standard coordinate inner product, the free module on the four native labels, a genuine external time interval, and one globally fixed exponential phase profile. These are mathematical interpretation premises, **not data recovered from Tick**. The phase, angular scale and time convention must be shared across both factors, all source states, and all Ticks.

The chosen return convention is positive continuation in reverse operation order. It is not literal time reversal of the forward curve; that would require inverse phases.

## Non-vacuous derivation criterion

Once that profile is fixed, a candidate must provide equalities to the prescribed construction:

1. Encode the source labels by the delta basis of their free module.
2. Extend the native factor flips linearly; no independent operator may be supplied.
3. Form `Q=(I-P)/2`, `H=pi Q` and `U(t)=I+(z(t)-1)Q`.
4. Traverse the resulting legs in the tag-specified order, reversing that order for the return from the double-flip target.
5. Derive the two-path observation from the two tags and prove its whole-record coherence.

This is stronger than the old coherence-only condition: a generic `Schedule → Path` function is not an admissible primitive. It must agree with the fixed traversal formula. It is still a **declared construction discipline**, not a theorem that bare Tick forces this analytic interpretation.

## What Agda checks now

`DerivedComponents` types the component equalities above for any fixed scalar ring, half, angular scale, time type and phase. `canonical` inhabits it by construction. `legs-agree` proves equality of the left legs of any two inhabitants for that same profile.

Fresh safe Agda dependency closure passed. Receipt: `results/relative-source-contract.json`.

This checks the algebraic provenance interface. It does not prove that arbitrary parameters satisfy analytic laws. In particular, half may not yet be verified as an inverse of two and phase may not yet be verified unitary; the concrete completion instantiation must discharge those separate requirements. The whole-path type and its analytic laws are not implemented here.

## Contract consequences and limits

- Mixed-factor generator freedom is excluded by the specified generator equality, not by claiming a new consequence of bare Tick.
- Relabeling covariance and factor locality remain required proof obligations for this construction; they cannot replace its derivation equalities.
- Equality is relative to one fixed analytic profile. Different branches, scales or phase profiles are not proved equivalent.
- The no-go for endpoint-separated Cubical-pointwise state selection is avoided by using external metric paths, not by weakening its endpoint hypotheses.
- The original source-derived conjecture is not closed or silently redefined. This is a separately named relative interpretation branch.

## Locality and covariance proved

`agda/TickRelativeLocality.agda` proves, for arbitrary vectors and phase parameters:

- Each generator and leg acts on one Bool fiber with the other coordinate fixed (exact slice locality).
- Independent identity/flip relabelings intertwine the represented flips, generators and legs, and relabel the delta basis correctly.
- Every injective Bool renaming equals either identity or flip, so the four factorwise relabelings exhaust the bijective cases.
- Exchanging factors interchanges left and right generators and legs, and exchanges the order labels of the composed two-leg operation.
- Derivation equalities transport slice locality and leg covariance to any admitted `DerivedComponents` candidate.

Fresh safe Agda dependency closure passed: `results/relative-locality.json`. The dependency `TypedGeneratorLayers.agda` emits an existing unused-import export warning (`isPropIsContr`); no proof error occurred.

These are algebraic slice and covariance laws, not yet a theorem about conjugation preserving completed operator algebras. Unitarity, inverses and the concrete analytic interface remain to be supplied. Nor is the two-leg composition result a proof of continuity on the glued metric path domain.

## Next bounded target

Instantiate the scalar parameters with the actual completion analytic interface, starting with the still-open scheduled unit-norm bound. Retain the metric-domain and whole-section obligations. The original one-shot planning portfolio remains stopped after its audit; its source-contract token must not be unlocked using this weaker relative criterion. Planning for this branch needs the explicitly relative target and its remaining obligations.
