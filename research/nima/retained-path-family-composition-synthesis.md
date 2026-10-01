# Associative composition of retained weighted path families

## One composition contract across path lengths

`RetainedSuccessorLedger` now supports registered `WeightedPathFamily` records separately from its unchanged-copy `PathStage` records.

A weighted family retains:

- distinct complete path words and exact rational coefficients, including zero coefficients;
- a common positive word length;
- whether its payload was supplied or composed;
- both registered parent families for a composition;
- the exact parent-slot pair for every output word.

A supplied family can use a registered stage's entire carrier or a nonempty homogeneous subset of valid primitive words. The interface does not silently treat arbitrary supplied coefficients as values inherited from six primitive inputs. Mixed word lengths and zero-length units are outside this API.

## Operations

| Operation | Contract |
|---|---|
|`retain_payload(stage, values)`|Bind supplied coefficients to the ordered stage carrier. This does not assert they lie in the stage's origin-lift image.|
|`retain_path_payload(paths, values)`|Register an explicit homogeneous family of valid retained words.|
|`compose_payloads(left, right)`|Concatenate every endpoint-compatible pair and multiply its coefficients. Register both operands and all parent-slot bindings.|
|`deconstruct_payload(payload)`|Recover the stored operands and output-to-parent slot bindings.|
|`assembly_history(payload)`|Expose the retained binary assembly tree and supplied-leaf record IDs.|
|`composition_blocks(left, right, candidate)`|Describe endpoint-interface blocks and rank-one eligibility at this specific cut/domain.|

The earlier `compose_primitive_payloads` now delegates to this general contract and returns its coefficients in the registered first-successor carrier. Existing primitive callers retain their coefficient-vector API.

## Associative weighted words, distinct assembly histories

For homogeneous families x, y and z, both

    (x*y)*z and x*(y*z)

produce the same complete words and coefficients. Fixed operand lengths determine a unique split of each output word, so no extra parent-pair summation is needed at a fixed composition boundary. The coefficient of a three-part word is x_p y_q z_r in either bracketing.

The two registered results are NOT the same assembly record. One retains (x*y,z) as its immediate parents; the other retains (x,y*z). Deconstruction recovers both trees and the same ordered supplied leaves. Equality of flattened weighted words does not identify the assembly IDs or make them execution receipts.

Tests cover:

- all 216 primitive basis triples;
- mixed operand lengths (1,1,1), (2,1,1), (1,2,1), (1,1,2) and (2,2,2), through total length six;
- all five binary bracketings of four primitive inputs;
- arbitrary supplied intermediate coefficients, not just copied origin payloads.

## Factorization constraints belong to a cut

At a chosen m+n boundary, group left words by their target and right words by their source. At every matching vertex v, the block of a single product is

    W_v[p,q] = x_p y_q.

Thus every block has rank at most one. Conversely these conditions describe existence of some pair of factors on the specified operand word domains: each left word belongs to one target block and each right word to one source block. Nonparticipating input slots impose no output constraint.

The block audit checks the complete expected concatenation domain. Missing slots are not silently interpreted as zero coefficients. It reports eligibility, not equality with the particular supplied parent coefficients and not recovery of their preparation history.

### A decisive cut-dependent control

Supply a two-step payload with coefficients one on AB BA and DB BC and zero elsewhere. Its intermediate-B block has rank two, so it is not one product of primitive inputs at the 1+1 cut.

Nevertheless it is a valid supplied two-step family and can compose with an all-ones primitive family. The resulting three-step payload:

- is a single product at the 2+1 cut;
- is NOT a single product at the 1+2 cut.

This does not violate associativity: there was no primitive factorization of the supplied two-step operand to reassociate in the first place. A sum of two primitive products is not silently registered as a single primitive preparation.

## Compatibility with unchanged-copy extension

For any supplied coefficients on a registered path stage, composition with the all-ones primitive right family gives exactly the previous unchanged-copy successor. Tests verify the output carrier, coefficients, image decoder and coarse K-summary square.

General bilinear composition, however, is not claimed to be injective in both input coefficient vectors. Parent recovery uses the retained operand records, not an inverse of multiplication. This matters when coefficients vanish or no endpoints match.

## Empty composition and zero coefficients remain different

The product of an AB-only family and a CA-only family has no compatible words. It is registered as a structurally empty composition, with the intended total length and both operands retained. Further composition propagates that empty domain consistently under reassociation.

In contrast, AB composed with a zero-coefficient BA record has the nonempty word AB BA with coefficient zero. That word is not an identity and is not deleted.

The interface rejects empty supplied leaf families, but permits empty products generated by its endpoint rule. This policy preserves the difference between structural availability and a numerical zero without asserting that an unavailable physical experiment was executed.

Parallel primitive IDs sharing endpoints also survive. A duplicate-AB control produces fourteen distinct two-step words, including separate AB BA and AB:second BA coefficients and parent bindings.

## Verification

    python research/nima/checkers/check_retained_path_family_composition.py
    python research/nima/checkers/check_retained_path_successor.py
    python research/nima/checkers/check_retained_branch_comparisons.py
    python research/nima/checkers/check_bilinear_branch_preparation.py

All fresh runs pass. Hostile cases include foreign or copied weighted records, weighted records substituted for copy stages, invalid/duplicate/mixed-length/unsewn words, inexact or wrong-size payloads, and incomplete or incorrectly typed boundary domains.

Report: `results/retained-path-family-composition.json`.

## Structural synthesis

Repeated copying and primitive bilinear preparation now sit inside one associative retained-word composition interface. Complete payloads, single products, cut-dependent factorization and assembly provenance are separately represented.

The extension supplies neither a physical preparation schedule nor a spectrum on arbitrary weighted path families. Inherited spectral reads remain restricted to their earlier registered origin-image contract; a new weighted assembly record does not bypass that gate.
