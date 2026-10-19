# Y1267: positive facet nonoverlap, actual shared positive corner

Iteration 7, 2026-10-13. Freshly read the mutable work net's history-8/history-9 alpha6=0 continuation.

## Same target, regular inverse, wrong positive facet interior

At both fixed positive moment-curve external Z, forward-map each history's positive alpha6=0 boundary fixture and invert the identical Y into the other source chart.

All four receiving inverse branches are regular and reconstruct the same normalized target. They have alpha6=0 and seven other nonzero parameters. Nevertheless history 8 -> 9 gives negative receiving alpha2, and history 9 -> 8 gives negative receiving alpha1. Explicit negative ordered source minors certify nonpositivity, not just inconvenient coordinates.

The common Y1267 normal and identical seven target tangent entries give eight exact local residue-square equalities, with fixed ordered-dlog normalization and alpha6 deletion sign -1. Orientation reversals fail. The four algebraic density sums and differences are nonzero and retained. No fitted coefficients or weighted cancellation claim is introduced.

## Symbolic transition and sign proof

Use the external six-row basis (1,2,3,5,6,7). At both fixed Z, its relation for row 4 is

    Z4 = Z1/20 - 3 Z2/10 + 3 Z3/4 + 3 Z5/4 - 3 Z6/10 + Z7/20.

On history 8's alpha6=0 boundary, lifting Y directly on that basis gives a source matrix with zero columns 4,8 and parallel columns 3,5: the history-9 boundary cell. Its canonical extraction gives

    H alpha2 = -A alpha1*(6*A alpha5+1)
               / [5*A alpha5*(3*A alpha1+4)].

Conversely use the corresponding seven-label kernel row with k4=1. Starting from history 9's zero columns 4,8, add (q,0)^T k, where

    q = -20*H alpha2*H alpha5/(6*H alpha5+1).

This leaves CZ unchanged and produces the A parallel constraints (3,4,5) and (6,7). Extraction gives

    A alpha1 = -20*H alpha2*H alpha5
               / [15*H alpha2*H alpha5+6*H alpha5+1].

Both negative-sign identities are symbolic in all surviving source parameters; the positive numerator and denominator polynomials have strictly positive coefficients. Thus positive facet interiors do not overlap within these inverse localizations at the two fixed Z. Other full transition formulas are retained in the receipt.

## A nonredundant successor: the actual shared corner

The obstruction vanishes at A alpha1=0 or H alpha2=0. Here the two positive source boundary closures genuinely coincide:

    History 8 (A): alpha1=alpha6=0.
    History 9 (H): alpha2=alpha6=0.

The six surviving parameters are related by

    H alpha1=A alpha2;
    alpha3,alpha4,alpha5,alpha7,alpha8 unchanged.

After this relabeling, the signed embedded source matrices are symbolically identical, not merely their divisor labels or numerical target points. Positivity holds at both selected corner fixtures. The target tangent rank is six and the ordinary full differential rank is eight at both fixtures. This supplies an actual shared codimension-two source/target germ for a paired residue test.

Paired iterated residues have not been computed in this receipt. In particular, the common corner is not yet a weighted nine-form cancellation certificate.

## Next executable action and scope

Compute alpha6 residue first in both charts, then alpha1 for history 8 and alpha2 for history 9. Use the explicit six-parameter corner transition, common target tangent coordinates and ordered-source deletion parity. Test the paired density sum and an orientation-reversal hostile.

Keep any unweighted local result distinct from the missing weighted component/sector map, source-chain orientation anchors, global covering and full facet provenance. The scientific gates remain open; missing historical replay inputs remain missing. The sign and corner controls concern these source charts and the two pinned external Z, not an arbitrary-Z/global atlas theorem.

## Reproduction

    python research/benincasa/checkers/check_shared_y1267_composite_facet.py

Receipt: `research/benincasa/results/shared_y1267_composite_facet.json`.

Seven grouped checks pass. Predecessor source/checker hashes are verified. Evidence is symbolic rational transition/source identities and exact local target differential algebra.
