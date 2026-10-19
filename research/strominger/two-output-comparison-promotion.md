# Retained composition produces two photon-like comparison seeds

## Constructive successor

Start with the previously checked meeting at A,C:

- output 1: electron ABC and positron AEDC;
- output 2: electron CDEA and positron CBA.

For each output apply the same proposed compiler:

1. retain the two-edge path;
2. compose the first two edges of the three-edge path, retaining its middle vertex/history;
3. introduce the short path's composite and inverse-composite records as a shared seam;
4. record the short route and reversed compacted long route as two triangle boundary cycles.

This constructs compound arrows from paths. It does not equate paths merely because their endpoints match, nor assert that a comparison face is already supplied.

## Explicit outputs

| Output | Boundary cycles | Corner suppressed but retained in history |
|---|---|---|
| 1 | ABCA and ACDA | E, inside A -> E -> D |
| 2 | CBAC and CAEC | D, inside C -> D -> E |

Each has two triangular cycles sharing AC in opposite directions and six compound-arrow occurrences. The example uses four visible corner labels per output. All five primitive occurrences assigned to each output remain covered by the retained path records; all ten initial root occurrences survive overall.

Twelve emitted records are not twelve independent initial arrows: the seam records, their inverses and shortened arrows reference retained inputs. Physical execution/resource accounting is not supplied by this reference reuse.

The alternative uniform rule, composing the last two long-route arrows, is also tested. Five 2/3 cut pairs times two uniform rules give ten attempts and twenty output seeds. Neither uniform convention is selected by the present sources.

## Exact spectral result

After putting the shared seam first in the registry, each output is isomorphic to the prior photon six-occurrence incidence. Its characteristic polynomial is

    lambda^2 (lambda^2+lambda+1)(lambda^2-lambda-1).

The existing g_plus and g_minus vectors satisfy the exact omega and conjugate(omega) eigenvalue equations on every output. Thus the conjugate C3 mode pair, absent from the raw parallel-route reader, **does emerge after this explicit compound-arrow compiler**. No independent spin representation is attached.

An initial test used a different occurrence ordering for the fixed source vector. Reordering to the source shared-seam registry resolved that mismatch; the final exact run passes all seven checks.

## What this does and does not establish

This is a concrete mathematical candidate interaction compiler. It explains how two complete opposite five-cycle histories can yield two shared-edge comparison seeds without deleting their original histories.

It is not yet an operation derived from the unchanged source action library:

- the new output three-cycle permutations are not powers of the original five-cycle; the checker verifies this against all five inherited permutations;
- mathematical composite/inverse path records are not automatically executed source interactions;
- a closed boundary comparison does not itself supply its filling witness;
- the unchanged facet/cone assembler completes each four-corner source into a tetrahedron.

For the displayed choice these completed four-corner supports are ABCD and ABCE, two boundary-cell supports of the original electron four-simplex. Calling them two distinct final photon shapes would repeat the earlier seed/stage confusion. The positive result is the paired compound-arrow seeds and their recovered modes.

## Next source obligation

Identify one existing interaction/promotion rule that admits this path compiler, supplies the route-comparison witnesses, and selects the same photon output object in both branches. In particular, deriving those new three-cycle actions and the retained output rule is substantive; a relabelling or a particle-specific stop is insufficient.

## Verification

```sh
python research/strominger/checkers/check_two_output_comparison_promotion.py
```

Seven exact checks pass.
Result: `research/strominger/results/two_output_comparison_promotion.json`.
All twenty output occurrence manifests, primitive histories, generator permutations, spectral tests, completed geometries and source hashes are retained.
