# All-arity Catalan/QTDS transfer: preliminary novelty audit

## Candidate theorem already proved locally

For every even multiplicity `n=2m >= 6` and either alternating polarity, marked zero-physical-core scalar triangulations are canonically bijective with marked unique-sink quadrangulations. The construction has an explicit inverse. Its scalar flip distance is `(n-4)/2`; shortest routes are linear extensions of a disjoint union of chains; route averaging defines a canonical deck-odd contact homotopy. A separate vertex-local identity identifies the unique-sink slots with the polynomial contact sector of the complete QTDS period, with coefficient `-1` in the audited convention.

The durable proof is `src/ledger/20260813-26 Direct Catalan Bijection and QTDS Contact Theorem.md`, with exact checkers named there. Entry 27 reportedly extends occurrence/coefficient equality over arbitrary fixed physical cores, but not incidence-compatible assembly between different cores.

## Prior-art search

Searches were run against arXiv and OpenAlex for combinations of:

- associahedron, discrete Morse, and amplitudes;
- accordion complexes and amplitudes;
- quadrangulation chain maps and amplitudes;
- Stokes polytopes and discrete Morse theory;
- Catalan scalar-amplitude transfers;
- unique-sink quadrangulations and alternating associahedron orientations.

No direct match to the stated marked Catalan bijection, exact flip-distance theorem, disjoint-chain route poset, or QTDS contact identification was returned.

Closest prior families:

1. Manneville and Pilaud, *Geometric realizations of the accordion complex of a dissection* (arXiv:1703.09953): accordion complexes, fans, and polytopal realizations.
2. Pilaud and related work, *Stokes posets and serpent nests* (arXiv:1505.05990) and *The serpent nest conjecture for accordion complexes* (arXiv:1704.01534): quadrangulation flips, Stokes posets, and combinatorics.
3. Banerjee et al., arXiv:1811.05904: Stokes-polytopal positive geometry for quartic scalar amplitudes.
4. Arkani-Hamed and Figueiredo, *Tropical Amplitudes for Colored Lagrangians* (arXiv:2402.06719): tropical numerator functions and colored scalar interactions.

These sources make quadrangulations, flips, accordion complexes, and scalar amplitudes nonnovel individually. The search did not locate their combination with the exact marked zero-core/unique-sink bijection and QTDS coefficient theorem.

## Publishability assessment

This is a stronger candidate than the six-point BCJ mapping-cone result because it is all-arity, constructive, invertible, and connects a combinatorial theorem to an amplitude-sector identity. Novelty remains provisional until the four closest papers are read theorem-by-theorem rather than only searched by metadata/full-text keywords.

The most defensible paper claim is not “new quadrangulation geometry.” It is:

> the marked zero-core scalar sector admits a canonical all-arity discrete-Morse transfer to unique-sink quadrangulations, with an explicit inverse and route-poset formula, and this transfer computes the QTDS contact sector coefficientwise.

## Blocking novelty tests

1. Compare the direct bijection and inverse against every bijection or lattice map in arXiv:1505.05990, 1703.09953, and 1704.01534.
2. Check whether arXiv:1811.05904 already identifies unique-sink quadrangulations or the same contact coefficients.
3. Verify the claimed QTDS object and terminology against arXiv:2402.06719 and its successors.
4. Independently rerun the all-arity proof checkers and inspect whether “all arity” rests on proved symbolic lemmas rather than finite enumeration.

Until those pass, the status is “plausibly novel theorem candidate,” not “publishable theorem.”
