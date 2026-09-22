# Reciprocal history closure is stable under admitted development

## Frozen relation

Use the actual 638-state source/acquisition/delivery/issuance system and its original sixteen labels. Define compatibility by

    h R w iff every step of continuation word w is admitted from h.

A rejected step makes that word incompatible. Outputs are not part of this relation. Source/evidence coupling is freshly independently verified.

For a set A of histories, A' contains words admitted from every member of A. For a set B of words, B' contains histories admitting every word in B. These universal operators reverse inclusion and form a Galois correspondence. Set cl(A)=A''. The closed history sets and closed word sets are dually isomorphic. This part follows from the declared relation.

## Complete finite compatibility computation

Generate all distinct partial state transformations of finite words, using an undefined target after rejection. The resulting monoid has 1,267 elements. Their domains give 58 distinct compatibility columns, representing all finite words rather than a bounded word sample.

The 638 histories have 54 distinct singleton closures, equivalently 54 distinct admitted continuation languages. This is not a count of every closed subset in the concept lattice. The previous operational observer had 62 states because it also retained explicit outputs; this admission-only construction has a different contract.

## Composition certificate

For an event e, write f_e for its partial state transition. For every continuation word w,

    f_e^{-1}(dom(w)) = dom(ew),

with undefined inputs excluded. The checker verifies closure of the complete 58-column family under all sixteen preimages: 928 exact checks.

Let A be any history set contained in dom(e). Since dom(e) is a compatibility column, cl(A) remains in dom(e). Any column D containing f_e(A) has preimage containing A, hence also cl(A). Thus f_e(cl(A)) is contained in every such D. Extensivity supplies the reverse inclusion after closure, proving

    cl(f_e(cl(A))) = cl(f_e(A)).

This proves descent for every subset A satisfying the admission condition, without enumerating the power set of 638 states. Closed-image transitions compose coherently by the same identity, whenever their sequential admission conditions hold.

## DPC disposition and structural meaning

Reciprocal determination is stable under development for this complete admission language. A closed history description can be extended and reclosed without depending on which generating history set described it.

The structural reason is residual closure: the continuation question after e is already represented before e by the word ew. Including every finite admitted composition makes future compatibility tests available as present constraints.

This observation also limits the novelty of the result: with compatibility defined using all finite words, residual closure is an automata-theoretic consequence. The exact computation binds it to the actual coupled source. More restrictive continuation languages may fail to include the needed residual tests; richer output-sensitive or higher-cell compatibility requires its own definition and proof.

The result does not recover arbitrary source details or identify 54 classes with the full observer's states. It gives a precise reciprocal structure at the admission level and a compositional preservation theorem.

## Reproduction

    python research/voevodsky/checkers/check_reciprocal_history_closure.py

Artifact: `results/reciprocal-history-closure.json`.
