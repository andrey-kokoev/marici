# Corrected oscillator test: two retained-family promotions

## Correction

The preceding two-step test used reversible endpoint re-presentation. That was not the requested generative iteration. This test uses the existing `incoming_promotion` from `research/nima/checkers/check_rung_transport_diagram.py`: group by incoming endpoint, create fresh family labels and next-level endpoints, retain every member, and apply the same constructor to the resulting family records.

Only the named pure definitions are loaded from the owner checker by AST, avoiding its unrelated fixture execution and output. Its existing mean/add/scale operations are specialized to exact scalar coefficients. The promotion definition itself is unchanged. No new adjacency or reverse physical edge is added.

## Actual input and successor records

Input is the same four oscillator coefficient records: u->a, b->a, a->y, u->y. The first incoming promotion creates two actual records:

- the oscillator-target family retains u->a and b->a;
- the output-target family retains a->y and u->y.

Each has a fresh label, generated endpoint fields, member mass and the original member records. Feeding those actual outputs into the second promotion gives:

| Existing endpoint policy | Original records | First promotion | Second promotion |
| --- | ---: | ---: | ---: |
| Inherited incoming key | 4 | 2 | 2 |
| Common promoted target | 4 | 2 | 1 |

Both are already declared policies in the owner implementation. The common-target policy is not selected merely because it produces one enclosing record. Counts do not select a physical interpretation.

## The three presentations are not three physical ports

At each level construct the architecture's actual three presentations:

    labelled records -> from-indexed records -> to-indexed records,
    labelled records ------------------------> to-indexed records.

The indirect map unindexes the from-view and indexes by target. Both routes produce exactly the same target view. The inverse indexing maps recover the same complete records. This is a concrete presentation triangle at each generated level; the oscillator and bath need not be squeezed into three primitive ports.

The readout walks retained members recursively and composes the original coefficient routes. It does not consult a separately saved source table or treat a family mean as a replacement transfer coefficient. The mean is an aggregate annotation, not a new oscillator law.

For both endpoint policies, all three presentations at all three levels recover r=3/5 and q=-4/5 at resonance. The symbolic response/noise identity is preserved. The second-level objects recover both the actual intermediate family records and all original coefficient records.

## Hostile and disposition

Zeroing the bath coefficient deep inside the final retained record, while leaving aggregate annotations untouched, changes the recovered commutator to 9/25. The readout detects the corruption. This distinguishes real retention from a result reconstructed from a hidden source copy.

The generative test now succeeds at its stated scope: **two actual family promotions preserve the oscillator domain and its presentation triangles**. The previous literal-three-port rejection remains only a rejection of that mistaken interpretation; it is not evidence against triangles of structured presentations.

This does not yet identify the presentation triangle with every intended formed-triangle construction or establish its FCC/tetrahedral realization. No relabelling of the two/one family counts is offered as that geometric identification. The corrected result removes the erroneous re-presentation-only test without promoting it to universal physical-law coverage.

## Verification

`uv run --with sympy python research/strominger/checkers/check_oscillator_family_promotion.py` exited zero through structured-command, execution `structured_command_execution:e_42200_1792520307534046800_29`. Receipt: `research/strominger/results/oscillator-family-promotion/verification.json`. It pins the owner constructor, source report and both test implementations. Owner artifacts were not modified; no formal proof-assistant compilation or experiment was run.
