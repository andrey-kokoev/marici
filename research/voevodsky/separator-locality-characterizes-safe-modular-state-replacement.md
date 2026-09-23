# Separator locality characterizes safe modular state replacement

## Typed setting

A retired block has internal coordinates H and retained interface coordinates S. Its complete source-relative relation is R subset H x S. The surrounding state has coordinates S x X and arbitrary relation E subset S x X. All shared coordinates and all shared constraints must occur in this factorization; hidden cross-block constraints are not permitted to disappear.

Define the exact interface relation

    Q(s) iff there exists h with R(h,s).

The original composite is C={(h,s,x): R(h,s) and E(s,x)}. Replacing the block gives Cbar={(s,x): Q(s) and E(s,x)}.

## Separator-locality theorem

For every surrounding E,

    projection_(S,X)(C)=Cbar.

This is the elementary existential distributivity identity

    exists h [R(h,s) and E(s,x)]
      iff [exists h R(h,s)] and E(s,x).

It establishes equality of public possibilities, not equality of fine carriers. Every query determined by the retained (s,x) relation therefore agrees. In particular membership, extrema, emptiness and possible/forced predicates agree whenever their semantics are defined.

Every later constraint f(s,x) can be conjoined with E without altering this proof. Inductively, arbitrary finite retained-interface-only refinements preserve the replacement. Adaptive continuations based solely on those public answers follow the same branches. This is a semantic theorem, not an algorithmic completeness claim for arbitrary predicates.

## Necessity for unrestricted interface contexts

If Q' is proposed as a universal replacement and exact interface-point contexts E_s are permitted, then equivalence in every surrounding context implies Q'=projection_S(R): a context pinning the interface to any point in the symmetric difference detects an emptiness disagreement.

Thus exact projection is both sufficient and necessary for universal retained-interface-context equivalence, assuming the context language can test every relevant point. For restricted or rational-only languages, necessity must be stated relative to their separating power and admitted state class. It is not automatically equality of arbitrary real subsets.

Separator locality is a sufficient syntactic restriction on future contexts, not a necessary property of every individually harmless constraint. A constraint mentioning h may happen to be redundant. The theorem characterizes exact summaries for all interface-only contexts; it does not assert that every nonlocal constraint breaks equivalence.

## What nonlocal continuations expose

Take S={s}, H={0,1}. Relations R0={(0,s)} and R1={(1,s)} have the same interface image {s}. A new constraint h=0 leaves R0 feasible and R1 empty. No representation identifying these fine relations solely by their interface image can answer both continuations correctly.

This is a semantic impossibility, not a missing optimizer. If the interface promises later fine-audit access, it must retain an adequate finer state, restrict the continuation, or explicitly weaken its meaning. The owning parallel-tail-segment example already establishes this phenomenon inside the analytical source.

## Multiple blocks and gluing

Let blocks R_i(H_i,S_i) have pairwise disjoint interiors H_i; all intersections and cross-block constraints are represented in the retained variables S and surrounding E. Then

    exists (h_1,...,h_k) [E(s,x) and all_i R_i(h_i,s_i)]
      iff E(s,x) and all_i Q_i(s_i).

For a finite number of blocks, choose a filling of each nonempty fiber at the common interface assignment. Because interiors are disjoint and all overlaps are fixed in S, the fillings glue. This requires no canonical choice or equivalence of different fillings. A runtime constructor needs effective lifting procedures, which are an extra deliverable beyond existential semantics.

For recursive decompositions, every variable shared by parts must be present at their joining separator. Small separator cardinality alone does not bound the representation complexity of Q_i. Difference constraints and globally balanced gain systems supply a closed relation language with controlled interface rows; arbitrary polyhedral projections can have quadratic or larger growth.

## Two independent capability contracts

### Answer-preserving replacement

Retain a verified exact Q. Public queries and permitted interface-local continuations depend only on Q and E. The old internal variables are not needed at runtime for those semantics.

### Fine-witness reconstruction

Additionally retain an effective lift taking each admitted s to some h with R(h,s), or sufficient source/evidence data from which to compute one. This may require much more information than Q. Returning a representative from an unrelated saturated source fiber is not enough.

Neither capability authenticates observations or supports reconstructing the actual source. Fine witness outputs may reveal information outside the public mathematical query language, so confidentiality and observable transcript equivalence require separate contracts.

## Verification and retention policy

A migration proof must establish both inclusions Q=projection(R), bound to independently expected source/schema/evidence. Forward cuts alone are insufficient. A verified transition can authorize using Q as the live state. Whether the original rows and proof can be discarded depends on the trust/provenance policy: future independent replay requires its validation context or another trusted commitment/admission mechanism. This theorem is not permission to delete an external archive.

The cost ledger therefore has separate entries for live public state, migration proof, provenance archive, optional lifting data and future query work. A short interface relation does not imply that all five accounts shrink.

## Executable finite context test

The attached checker exhausts all 16 block relations on two internal and two interface values and all 16 surrounding relations on two interface and two external values. It verifies the identity for all 256 pairs, then for all 16 possible local refinements of each context (4096 controls). It checks multiple-block gluing, necessity via point contexts, and a nonlocal distinguishing constraint.

These are implementation controls for the semantic equations, not the proof of an infinite-domain theorem. The general proof is the quantifier identity above. No new analytical-source admission or optimizer claim is made.

## Binding to the lane

- Exact projection with lifting: owning Fourier--Motzkin compiler and lazy envelope oracle.
- Controlled summary class: difference constraints and balanced gains.
- Actual gluing: certified gain-block composition.
- Failed nonlocal replacement: continuation-relative parallel tail histories.
- Checked implementation change: pinned bidirectional certificate translators.

This consolidates those results into one replacement criterion rather than adding another elimination algorithm. The next implementation gate is a state API that distinguishes answer-only migration from migration retaining a fine-lift capability, and declares which continuation language each migrated state supports.

## Reproduction

    python research/voevodsky/checkers/check_separator_locality.py

Artifact: `results/separator-locality.json`.
