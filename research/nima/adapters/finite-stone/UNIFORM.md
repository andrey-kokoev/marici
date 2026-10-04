# Uniform finite Stone reconstruction

## Question and contract

Can reconstruction be derived from finite Boolean operations rather than received
as an equivalence? This is steps 1–4 of the approved Stone → Yoneda → Tannaka
roadmap. The pilot remains unchanged.

Input: a nonempty, explicitly enumerated carrier with decidable equality, bottom,
top, complement, meet and join tables satisfying the Boolean axioms. Enumeration
is supplied finiteness evidence, not inferred from a cutoff. No atoms, powerset
coordinates, inverse, or reconstruction equivalence are supplied. The one-element
Boolean algebra is admitted and corresponds to the empty point space.

Output: actual minimal nonzero elements; incidence representation into their
powerset; inverse given by finite join; certificates of both inverse laws and
Boolean-operation preservation. For each operation-preserving map B → C,
construct its opposite-direction map Atom(C) → Atom(B), with identity,
composition and naturality certificates. Recovery is up to Boolean isomorphism,
not equality of presentations or of enumeration orders.

SCC obligation: forward realization followed by route/coherencer compatibility.
No topological completion, infinite Stone theorem, or arbitrary-vocabulary claim.

## Governing test

- Problem: the pilot receives a domain-specific inverse instead of deriving one.
- Conjecture: the supplied finite Boolean tables suffice to compute atoms,
  reconstruction, and cross-object contravariant maps without changing the core.
- Rivals: hidden powerset coordinates; a carrier-size lookup; restriction to
  automorphisms; accidental dependence on labels; an invalid distributive-lattice
  input accepted as Boolean.
- Risky consequences: relabelled inputs reconstruct; noninvertible cross-size
  maps compose contravariantly; the zero-atom boundary works; missing Boolean
  laws and deliberately corrupted inverses/maps are rejected.
- Strongest test: exhaustive raw-map enumeration for carriers of sizes 1, 2, 4,
  combined with larger table and relabelling tests. These are bounded tests,
  not the universally quantified theorem.
- Disposition: implementation and verification status are recorded in
  `research/nima/results/uniform-finite-stone.json`. General Agda proof and native
  integration of that general proof remain open until separately checked.

## Mathematical derivation to formalize

For x ≠ 0, the nonempty finite set of nonzero elements below x has a minimal
member, hence an atom. Distinct atoms have meet zero: a nonzero meet would force
both atoms equal by minimality.

Let s be the join of all atoms below x. Then s ≤ x. If s ≠ x, Boolean
complementation gives x ∧ ¬s ≠ 0. An atom below this difference is both included
in s and disjoint from s, a contradiction. Thus x is that join.

An atom p is join-prime: if p ≤ u ∨ v, distribute p ∧ (u ∨ v); minimality
forces at least one of p ∧ u and p ∧ v to equal p. Induction extends this to
finite joins. Consequently an atom lies below the join of a subset of atoms
exactly when it belongs to that subset. These two results prove both inverse
laws; meet and complement become intersection and subset complement.

For h:B → C and q an atom of C, apply h to the decomposition of 1 in B.
Join-primality yields an atom p of B with q ≤ h(p). It is unique because h
preserves disjointness. Define h*(q)=p. Decomposing any x then proves
q ≤ h(x) iff h*(q) ≤ x. This identity gives naturality and determines h*
uniquely, yielding id*=id and (k∘h)*=h*∘k*. These are proof obligations,
not currently new Agda theorems.

## Evidence discipline

The executable accepts arbitrary labelled tables and checks their axioms;
bit-mask powersets are test fixtures only. Returning an object-specific checked
certificate is distinct from proving termination and correctness universally in
Agda. Keep the existing kernel-checked pilot separate from this algorithm's
bounded test evidence. A later Yoneda development must similarly distinguish
full faithfulness from an effective sufficient-probe reconstruction procedure.
