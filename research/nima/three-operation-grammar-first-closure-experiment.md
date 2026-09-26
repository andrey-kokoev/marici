# Three-operation grammar: first closure experiment

## Declared interpretation

Take P(X)=Pi(i:Bool).X and S(X)=Sigma(i:Bool).X, with permitted constructors PP, SP, PS. A word records applications innermost first. Every full word is retained, together with reversible encoding/decoding between its nested values and a dependent container form.

This is a deliberately simple semantics for the proposed grammar. P and S here build new types; the *normalization* is the lossless change of presentation. Interpreting every grammar edge itself as a repackaging of the same source would require different, reindexed operation definitions.

## Closure

Each expression has a container presentation

Sigma(bits:Bool^a). Pi(position:Fin(2^b)). Q.

Its full constructor word remains attached to the presentation. S retains one choice bit; P retains two independently indexed copies of the prior choice/position structure. The closed signature rules are

PP: (a,b) -> (4a,b+2)
SP: (a,b) -> (2a+1,b+1)
PS: (a,b) -> (2a+2,b+1).

Structural induction supplies these formulas at every finite depth. There is thus a finite recursive description from the outset. No depth cutoff is needed for syntactic/type-family closure.

## First cross-branch recurrence

At depth four, two distinct complete words have the same container type:

Q --SP--> --PS--> --SP--> --PP-->
Q --PS--> --PP--> --SP--> --PS-->.

Both send an arbitrary signature (a,b) to (32a+36,b+5); from bare Q both give 36 binary choices and 32 Q-positions. Decode after encode constructs their actual equivalence. This relation is uniform in Q, since the codecs never inspect or change Q entries. Associativity of these canonical comparisons follows from cancellation of inverse codecs; the checker exercises two three-presentation triangles at depth six.

This does not establish that this one relation generates all equivalences between words. The finite relation-presentation problem remains open. Cardinal equality alone is insufficient; the code retains the actual bijections and original expression words.

## Growth and recurrence are distinct

The position exponent b increases strictly at every constructor, so the same formal container signature never returns along a branch. Special substitutions such as Q=Unit can erase some distinctions at the value-type level; the statement concerns the formal Q-indexed container. Cross-branch equivalences accumulate while branch complexity grows.

At depth 8, 6,561 words yield 5,229 container signatures, with up to five words in a signature class. Codec round trips cover all 1,093 words through depth six using explicit labeled values and retained choice bits. The census is finite evidence; arbitrary-depth closure and strict b growth follow from the displayed recurrences.

## Next target

Determine a complete presentation of the equivalences induced by these canonical codecs, and then decide whether this semantics matches the intended source-realization/observer grammar. Higher comparison data require a higher-valued interpretation beyond the present set model. Keep the full words, maps and source indices throughout.

Checker: `research/nima/checkers/check_three_operation_coherence_grammar.py`.
Result: `research/nima/results/three-operation-coherence-grammar.json`.
