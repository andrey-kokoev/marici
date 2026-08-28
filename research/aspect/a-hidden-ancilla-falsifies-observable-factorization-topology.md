# A hidden ancilla falsifies observable factorization topology

## Target

The repaired bivariant conjecture retained this claim:

> Observable architecture is the factorization type of the instrument–data diagram.

That claim is false without an accessibility or provenance condition.

## Exact hostile

Compare three presentations of the identity channel on a qubit:

1. the direct identity;
2. two consecutive Hadamard gates;
3. adjoining an ancilla in \(|0\rangle\), applying controlled-NOT twice, and returning the ancilla to \(|0\rangle\).

Exactly,

\[
H^2=I,
\qquad
\operatorname{CNOT}^2=I.
\]

For the hidden-ancilla circuit, the reduced boundary channel has Kraus operators

\[
K_0=I,
\qquad
K_1=0.
\]

It is therefore the identity channel even on inputs entangled with an arbitrary external reference. Every allowed precomposition and postcomposition sees the same boundary morphism.

The three diagrams have different internal factorization topology but identical extensional semantics. No boundary experiment can recover which factorization was used.

## Consequence

Category theory does not canonically promote a factorization into an observable. It distinguishes two levels:

- extensional process: the morphism modulo all declared external contexts;
- intensional presentation: a chosen diagram, implementation, or provenance witness whose composite is that morphism.

Internal topology becomes physical data only when at least one of the following is present:

1. an intermediate interface is exposed to admissible composition;
2. an internal cell leaves a nontrivial boundary residual;
3. source provenance declares the factorization itself as retained data;
4. a resource theory assigns inequivalent cost to the implementations;
5. intervention on an internal component belongs to the declared context class.

Without one of these, adding \(U^{-1}U\), an initialized-and-uncomputed ancilla, or any other reversible refinement changes syntax but not physical content.

## Repaired conjecture

The surviving categorical claim is:

> A physical presentation is a bivariant higher diagram together with a declared class of accessible contexts and retained provenance. Its extensional content is its contextual-equivalence class. A factorization belongs to physical architecture exactly when it survives that quotient or is explicitly retained as provenance.

Tower expressions such as \(3+2+1\) and \(2(2+1)+1\) therefore classify exposed or provenance-bearing diagrams, not arbitrary hidden implementations.

This also explains why a mathematical coherence cell does not automatically yield an instrument. Existence of the cell is intensional structure. Executable preparation, comparison, and recombination are what expose it to the contextual quotient.

## Next falsifier

The repair can now be attacked at the accessibility boundary: construct two inequivalent diagrams that remain contextually identical even after every declared intermediate interface is exposed and every retained provenance label is compared. Such a packet would show that the proposed context class is still too weak or that diagrammatic equivalence itself needs a higher quotient.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_hidden_ancilla_factorization_falsifier.py
```
