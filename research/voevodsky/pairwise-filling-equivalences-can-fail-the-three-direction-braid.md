# Pairwise filling equivalences can fail the three-direction braid

## Frozen structural fixture

Use a three-coordinate binary source with an independent binary witness tag at each cut. A path changes each coordinate to its specified target once. Adjacent interchange swaps the two coordinate operations and reconstructs their intermediate coordinate state from the same outer boundaries.

Define two independently specified witness transports:

- preserving transport leaves all cut tags unchanged;
- twisted transport replaces the intermediate tag t_(i+1) by t_(i+1) XOR t_i, leaving the two outer tags unchanged.

Both are valid bijections between the corresponding source-typed filling spaces. Applying the same swap twice restores the tags and coordinate path. This is a separate finite source fixture, not a claim about the actual observer's undeclared higher maps.

## Third-level obstruction

Let s0 and s1 interchange the first and second adjacent pairs. Both routes s0 s1 s0 and s1 s0 s1 reverse a three-direction ordering. Higher coherence requires their transports of witnesses to agree (or to have an admitted higher comparison).

For initial order (0,1,2), coordinate endpoints 000 and 111, and cut tags (0,1,0,0), the twisted routes give:

    s0 s1 s0: order (2,1,0), tags (0,1,1,0)
    s1 s0 s1: order (2,1,0), tags (0,1,0,0).

The outer boundaries agree and the internal witness differs. With discrete tag identity, there is no equality or supplied higher equivalence between these fillings.

The checker verifies 24,576 elementary boundary/involution instances and 6,144 three-direction paths. Twisted transport fails 4,608 braid comparisons. Distant swaps commute in 1,536 four-direction cases; that condition alone does not fix the braid defect.

## Positive control

Tag-preserving swaps satisfy all tested braid comparisons. More generally, their action is the ordinary permutation of independent coordinate operations with cut tags fixed. Involution, distant commutation and the braid relations give the symmetric-group presentation, so the resulting transport is independent of the chosen adjacent-swap factorization for any finite number of these independent directions.

This is a concrete coherent control, not permission to replace source-given transport by an arbitrary tag-preserving map. Whether the actual source admits such a choice remains an independent construction problem.

## Structural conclusion

Three obligations are now separated by exact examples:

1. endpoint relation equality;
2. equivalence of intermediate filling spaces;
3. coherence of those equivalences across compositions of diamonds.

Equal endpoint relations need not give equally sized witness fibers. Individually bijective, boundary-preserving transports need not satisfy the braid coherence. The missing datum at this third level is a comparison of comparisons, whose admission must come from the source's witness identity structure.

## Reproduction

    python research/voevodsky/checkers/check_repeated_diamond_coherence.py

Artifacts:

- `results/repeated-diamond-coherence-contract.json`
- `results/repeated-diamond-coherence.json`
