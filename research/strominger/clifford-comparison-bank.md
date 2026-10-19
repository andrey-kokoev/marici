# One raw reader for comparisons, reference and retained mixed responses

## Fresh result

A single coherent response convention now reproduces the entire original matrix fixture:

- all137 comparison matrices;
- the direct reference2I;
- unchanged J4;
- all977 original typed reference-return products;
- all109 rooted shared-leg mixed rectangles.

The same ACTUAL source raw sewing reader is applied throughout. No mixture of normalized comparison values and raw reference values is needed.

This is a conditional bank/response representation, not a physical preparation or a derivation of the supplied leg coefficients.

## Comparison banks from actual algebraic leg representation

Reuse the existing Cl(2,0) value/operator map. Its inverse is

    coefficients([[a,b],[c,d]])=((a+d)/2,(a-d)/2,(b+c)/2,(b-c)/2).

For each supplied fixture path Cij=Yj Xi, construct the bank

    t_ij=coefficients(Yj) tensor coefficients(Xi).

Its right/left ordering is explicit. Existing sewing gives

    matrix(mu(t_ij))=Yj Xi.

Original labels, carrier-index ports and preparation provenance remain in the bank packet. Bank norms equal the product of the leg coefficient norms; their preparation resources are accounted for but not generated for free.

The original fixture coefficients are imported and checked, not reverse-engineered as a new seed physical law.

## Reference bank from actual unit-resource exchange

Prepare the explicit unit carrier and empty bank, then use the unchanged conservative exchange. Its stored bank is

    t_ref=C^T(unit).

The SAME raw reader gives

    matrix(mu(t_ref))=2I.

This is the earlier source-derived port factor2, now placed consistently beside the comparison banks. The input unit still needs physical preparation/units, and the coefficient metric remains supplied.

Applying normalized C consistently to BOTH comparisons and reference yields Cij/2 and I. Its aggregate residual is J4/2. This is a complete alternative readout convention, not changing only the reference to erase J4.

## Reference-return response law from a declared bank recipe

Define a typed comparison-bank operation, on original common-target pairs only, by

    t_b odot t_a = C^T((C t_b)*(C t_a)),

where * is the ACTUAL source Clifford multiplication. Then

    matrix(mu(t_b odot t_a)) = C_b*(I/2)*C_a.

All977 original operation squares pass. The output retains both complete parent banks and its operation provenance. Coefficient multiplication existing for arbitrary values does not automatically admit cross-target record contexts; mismatched targets are rejected.

This is an explicit normalized-read/multiply/lift recipe. It is NOT the prior conservative carrier-record exchange, an isometry, or a demonstrated physical energy-conserving interaction. Readable composition and source dynamics are separate operations.

## Mixed records are retained before reading

For each rooted rectangle, the FULL16-slot bank difference factors exactly:

    t_ij-t_i0-t_0j+t_00
      =(coefficients(Yj)-coefficients(Y0))
         tensor (coefficients(Xi)-coefficients(X0)).

Its raw response is the correctly ordered Clifford/matrix product of those differences. The checker verifies all100 arrow and9 state rectangles at bank and response level.

These are retained algebraic bank records, not automatically higher-cell fillers, independent writable parameters or physical amplitudes.

## Full bank state does not collapse to its response

The reference bank is an identity for READABLE responses under the recipe, but composition with it generally projects the16-slot bank onto its readable subspace. The resulting bank need not equal the original bank. Both source and output remain available in the parent packet; strict whole-state unit laws are not claimed.

An existing hidden-return bank direction has zero ordinary/raw readout but changes the next conservative memory carrier output. The checker explicitly verifies that hostile. Therefore the source memory dynamics does NOT factor through raw sewing alone.

Likewise readable associativity does not identify distinct retained parenthesizations. Equal responses retain different source histories and kernel states.

Preserving operand records in software is not proof that the read/multiply/lift recipe is physically reversible or free: a physical constructor must account for its preparation, retained storage and reset/degradation.

## What this resolves

The fixture's two kinds of numeric input—137 comparison values and2I reference—can share ONE existing source response reader. The reference is no longer forced to be explained by a separate two-unit normalized resource solely to match its coefficient.

What remains unselected is whether the intended physical reference is this raw response standard. Nothing here changes the pinned software policy or declares a detector calibration. Boundary identifications, flat port transport, physical primitive leg preparation and the actual admissible operation remain supplied.

The next substantive bridge must preserve the FULL bank/kernel/resource packet under an actual physical operation, not merely reproduce the response algebra again.

## Verification

    uv run research/strominger/checkers/check_clifford_comparison_bank.py

2740 exact checks pass. The prior raw/normalized convention and full reference-port suites rerun as dependencies, including pinned software checks. New checks cover inverse source representation, all supplied legs, all137 values/resources, aggregate conventions, all109 mixed bank factorizations,977 operation squares, parent retention, readable units/associativity, hidden-return hostile and cross-target rejection.

No new Agda closure, source-selected calibration or physical instrument is claimed.

Artifacts:

- `research/strominger/checkers/clifford_comparison_bank.py`
- `research/strominger/checkers/check_clifford_comparison_bank.py`
- `research/strominger/results/clifford-comparison-bank.json`
