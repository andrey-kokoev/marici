# Coherence ideal versus evaluation kernel

## Question

How can the formal Laurent presentation distinguish lawful overpresentation from underdetermination introduced by an inadequate evaluation?

## Claim boundary

This packet specifies the missing theorem interface and a finite counterexample to unrestricted fidelity. It does not construct a physical amplitude or prove joint faithfulness of any physical probe family.

The existing channel Laurent algebra `P` is already downstream of triangulation sums, relabeling equivalences, and gluing equalities. Those coherence theorems are literal equalities in `P`; their differences generate only the zero ideal there. Therefore `P` cannot itself retain the overpresentation needed to define a nontrivial coherence ideal.

Introduce a pre-presentation algebra `A` whose generators retain presentation witnesses—triangulations, regional decompositions, relabelings, and composite gluing routes—and a canonical quotient `q : A -> P`. Define the coherence ideal as `ker(q)`. For each source-authorized probe `s`, let `phi_s : P -> K_s` be its evaluation. The correctly typed detection theorem is

\[
\bigcap_s \ker(\phi_s\circ q)=\ker(q).
\]

Equivalently, the induced probe family on `P` is jointly faithful. Strict containment above `ker(q)` measures residual underdetermination; quotienting `P` by the full kernel of one probe must not be described as coherence.

## Finite collision

At any polygon size with distinct diagonals `d` and `e`, take a trivial additive momentum group, the zero momentum configuration, and the admissible constant even readout with value one. Assign every channel unit to `1`. Then `channelVariable d` and `channelVariable e` both evaluate to `1`, while their exponent-basis monomials are distinct in the free Laurent algebra. Their difference is a nonzero kernel element.

This refutes unrestricted injectivity of `planarChannelReadoutEvaluation`. It does not establish that the difference lies outside `I_coh`, because `I_coh` has not yet been constructed.

## Required formal objects

1. A pre-presentation algebra `A` retaining route and decomposition witnesses.
2. The canonical forgetting map `q : A -> P` and the coherence ideal `ker(q)`.
3. A proof that each admissible composite probe `phi_s ∘ q` annihilates `ker(q)`.
4. A source-derived probe index and product evaluation on `P`.
5. A joint-faithfulness theorem or an explicit residual class in the intersection quotient.
6. Separate normalization and physical-record maps after detection.

## Finite pre-presentation construction

At a bounded polygon stage, let `A_0` be the finite type of retained presentation routes. A route records its constructor family and witnesses: a global triangulation term, a regional decomposition with local triangulations and embedding order, or a nested gluing route. Define `q_0 : A_0 -> P` by the existing Laurent expressions.

The primitive coherence object is the kernel pair

\[
K(q_0)=A_0\times_P A_0,
\]

not an ideal. Its inhabitants are pairs of routes whose equality in `P` is supplied by existing relabeling, factorization, associativity, or overlap theorems. Only after applying a free linear or algebraic presentation functor does this kernel pair generate an ideal.

For a probe `phi`, the observational kernel pair of `phi ∘ q_0` contains `K(q_0)`. A pair in the difference is an explicit underdetermination witness: the routes denote distinct Laurent objects but the probe identifies them. Thus the finite acceptance test is equality of two kernel pairs, with exact residual pairs when equality fails.

## Disposition

The single-evaluation quotient is observational. Coherence has already been collapsed on entry to `P`, so it cannot be reconstructed inside `P`. At finite stage the correct comparison is `K(q_0)` against `K(phi ∘ q_0)`; ideal language is admitted only after a declared linearization functor.
