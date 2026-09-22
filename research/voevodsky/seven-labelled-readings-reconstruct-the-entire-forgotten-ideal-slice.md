# Seven labelled readings reconstruct the entire forgotten ideal slice

## Result

There is now a standalone exact decoder for the entire seven-dimensional ideal slice of the forgotten three-diamond cube. It uses seven source-derived readings, no source archive, and no producer lookup.

It reconstructs all eight path coefficients, their labels and the ideal filtration level within the declared slice. Seven scalar coordinates are dimension-minimal; the already acquired canonical vacuum contributes one, so six additional readings are required.

This is a conditional inverse on the stated source domain, not a method for proving that an unknown input belongs to that domain.

## 1. The source domain

Background is two. The ordered blocks are (2,3), (5,7), (11,13). In each block P means sorted order and Q means reversed order. All events are forgotten.

There are eight concatenated paths. Index a coefficient a_b by the integer mask b from 0 to 7; bit i indicates reversal of block i+1. For example mask 1 means QPP and mask 4 means PPQ.

The ideal constraint is

    a_0+a_1+...+a_7=0.

These eight labelled coefficients with one relation are the seven-dimensional source to be reconstructed. No other event order or retained-mark pattern is admitted by this decoder.

## 2. The seven readings

All rows have outer corner 2->60060, vacuum buffers and unscaled unit-vacuum normalization.

| Value | Input ID | Forgotten seams | Coefficient formula |
|---|---|---|---|
| y0 | vacuum_PPP | 2->4, 12->60, 420->4620 | a0 |
| y1 | vacuum_QQQ | 2->6, 12->84, 420->5460 | a7 |
| y2 | first_block_P | 2->4, 4->12 | a0+a2+a4+a6 |
| y3 | blocks_1P_2P | 2->4, 12->60 | a0+a4 |
| y4 | blocks_1P_3P | 2->4, 420->4620 | a0+a2 |
| y5 | blocks_1Q_2P | 2->6, 12->60 | a1+a5 |
| y6 | blocks_1Q_3P | 2->6, 420->4620 | a1+a3 |

The two-seam rows are new readings on the SIX-event outer corner. They are not assumed available from the old four-event stage-two observer.

## 3. Complete inverse

The reconstruction is explicit:

    a0 = y0
    a1 = y1+y2+y5+y6
    a2 = y4-y0
    a3 = -y1-y2-y5
    a4 = y3-y0
    a5 = -y1-y2-y6
    a6 = y0+y2-y3-y4
    a7 = y1.

These coefficients sum to zero identically. Substitution reproduces every supplied reading. The independent ordered-cut recorder verifies the seven source-basis and seven reading-basis roundtrips, proving the inverse on the whole rational slice by linearity.

The decoder also computes

    m_T=sum_(b contains T) a_b.

The least |T| with nonzero m_T gives the source's ideal order on this slice. All seven nonzero interaction modes are checked against the actual ordered Fox vanishing tests. The zero source belongs to every ideal power.

This recovers the filtration of the declared source element; it does not assert a canonical source-bimodule splitting outside the slice.

## 4. Examples, not assumed acquisitions

Synthetic mixed readings

    (y0,...,y6)=(-28,7,-16,-24,-26,6,4)

reconstruct

    (a0,...,a7)=(-28,1,2,3,4,5,6,7).

The pure cubic readings

    (1,-1,0,0,0,0,0)

reconstruct

    (1,-1,-1,1,-1,1,1,-1),

the actual product (P-Q)(P-Q)(P-Q), certified at ideal order three in this slice.

These are generated test fixtures. No measured user source has been supplied or physically reconstructed.

## 5. Standalone use

The decoder is standard-library-only and runs with just its Python file and a readings JSON file:

    python research/voevodsky/certificates/reconstruct_seven_dimensional_ideal_slice.py research/voevodsky/results/seven-dimensional-ideal-readings-example.json

To inspect the exact source and row contract:

    python research/voevodsky/certificates/reconstruct_seven_dimensional_ideal_slice.py --model

Input uses labelled rational strings and a digest binding the complete source/reading model. There are no unlabelled positional arrays to reinterpret silently. The optional independently supplied terminal check must be zero; nonzero contradicts the ideal assumption.

The decoder rejects missing/extra readings, numeric rather than rational-string values, invalid rationals, duplicate JSON keys, model mismatch and contradictory terminal checks. It does not accept an original-source archive field.

Artifacts include:

- `results/seven-dimensional-ideal-slice-model.json`
- `results/seven-dimensional-ideal-readings-example.json`
- `results/seven-dimensional-ideal-reconstruction-example.json`
- `results/seven-dimensional-ideal-cubic-readings.json`
- `results/seven-dimensional-ideal-cubic-reconstruction.json`
- `results/seven-dimensional-ideal-decoder-tests.json`

## 6. Stability and retention

For the eight reconstructed path coefficients and seven unscaled readings, the inverse matrix has operator norms exactly four in both l1 and l-infinity. Thus, conditional on a correct source model and an admitted reading-error budget,

    ||coefficient error|| <= 4 ||reading error||

in either of these respective norms. No tiny feature amplitude is divided out. This is not a physical acquisition-error certificate or a bound in a differently weighted source norm.

Retaining the seven readings WITH their source/row model is recoverably equivalent to retaining this ideal-slice element. There is no remaining source kernel inside this domain. Keeping only a further scalar summary would require a new residual audit.

## 7. The domain cannot certify itself

The tests deliberately exhibit two limits:

1. A cube source outside I can have all seven readings zero. An independent terminal reading detects that example.
2. A nonzero ideal source OUTSIDE the eight-path cube can have all seven readings zero AND terminal reading zero. One example is the difference of forgotten paths

       (5,2,3,7,11,13) - (5,3,2,7,11,13).

   It is a genuine source ideal element, but every selected row requires an initial seam 2->4 or 2->6, which neither path has.

Therefore seven-reading consistency, even with a zero terminal check, cannot establish the support assumption. The decoder correctly returns the unique solution WITHIN its declared model; it cannot rule out an unobserved source outside that model.

Under the lossless-retention rule, applying this decoder to a broader source requires independent support evidence or retention of the complementary source information. The model restriction itself must not become another unmarked erasure.

## Verification

    python research/voevodsky/checkers/check_seven_dimensional_ideal_decoder.py

All checks pass, including isolated two-file execution, exact basis inverses, filtration recovery, invalid-input rejection and the explicit out-of-domain collisions.
