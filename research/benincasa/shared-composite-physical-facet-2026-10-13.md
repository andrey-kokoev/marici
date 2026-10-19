# Common Y1234 divisor: regular algebraic overlap, positive nonoverlap

Iteration 6, 2026-10-13. Freshly read the mutable work net's recommended history-5/history-8 alpha2=0 comparison. This test uses the actual inverse circuits from iteration 5, not shared cell keys or tangent planes.

## Four same-target comparisons

At each of the two fixed positive moment-curve external Z, map the prior positive history-5 boundary fixture to Y, invert that same Y into history 8, then perform the reverse experiment from the history-8 fixture into history 5.

All four receiving inverses are regular: fiber and canonical-gauge denominators are nonzero, alpha2 is zero, the other seven parameters are nonzero, and forward reconstruction reproduces exactly the same normalized target Y. Thus these are genuine meromorphic/algebraic overlaps on Y1234=0.

They are not positive overlaps. Every receiving alpha5 is negative, and explicit ordered minors of the receiving signed embedded source matrix are negative. The donor boundary minors are nonnegative. The receipt retains all negative receiving minors and exact parameter values.

## Symbolic sign certificate, not just a sample rejection

For history 5's alpha2=0 chart, retain the other seven source parameters as symbols. Construct history 8's two five-space source lifts from the unnormalized Y=CZ. The common GL(2) row inverse cancels in the source minor ratios extracting receiving parameters. At both fixed external Z, exact identities give

    b1 = a1,
    b5 = -3*(4*a1+5) / ((30*a1+25)*a5+27*a1+30).

The numerator and denominator of -b5 have strictly positive polynomial coefficients in a1,a5. Therefore b5<0 for every positive donor a1,a5 on the selected boundary chart within the rational inverse localization. Its source minor Delta37 in canonical A gauge is b5, so this is also a source-positivity obstruction, not merely an inconvenient coordinate sign.

Solving this transition for the reverse alpha5 gives

    a5 = -((27*b1+30)*b5+12*b1+15) / ((30*b1+25)*b5),

also negative for positive b1,b5. The reverse rule is checked at the two reverse fixtures. The forward symbolic proof and inverse uniqueness explain the reciprocal obstruction on the same algebraic overlap; no global atlas or arbitrary-Z extension is asserted.

## Fixed oriented residue comparison

Choose seven target entries whose tangent Jacobians are nonzero in both charts. Use the identical normalized bracket Y1234 as target normal for both routes. The source alpha2 deletion sign is -1, with the original ordered eight-dlog orientation and no independent scale.

All eight source-residue/pushforward versus top-pushforward/bracket-residue squares agree exactly. All eight orientation-reversal controls have nonzero residuals.

At each of the four same-target comparisons, both the density difference and density sum are nonzero. The exact values and receiver/donor ratios are retained in the receipt. No scale was fitted to make them vanish. These residuals concern meromorphic continuations outside the receiving positive branch. They are not a failure of a positive weighted-descent cancellation gate: no admitted positive shared branch or weighted map has been supplied here.

## Scientific disposition

The same physical divisor label does not justify pairing these positive branch interiors. For this selected localized boundary chart at the two fixed external Z, the proposed positive overlap is rejected by an exact sign obstruction. The algebraic overlap and local differential computations are preserved, rather than discarded or promoted to global cancellation.

Remaining gates: source-chain orientation and complete facet provenance, positive covering, component/boundary extraction, the nine-to-sector weighted map and actual shared codimension-two cancellation. All verdicts remain open, and the 18 historical replay inputs remain missing.

Next executable test: histories 8 and 9, alpha6=0, share the physical divisor Y1267. Apply the same actual-inverse, localization, source-positivity and common-target-residue tests. If those branches also do not overlap, retain that disposition and seek actual shared codimension-two strata rather than pairing equal divisor labels.

## Reproduction and evidence

    python research/benincasa/checkers/check_shared_composite_physical_facet.py

Receipt: `research/benincasa/results/shared_composite_physical_facet.json`.

Six grouped controls pass: four regular algebraic overlaps, eight local squares, four rejected positive overlaps, two symbolic forward sign certificates, four retained nonzero sums/differences and eight orientation hostiles. Evidence is exact symbolic/rational algebra at the pinned external fixtures, not a kernel proof or complete weighted descent certificate.
