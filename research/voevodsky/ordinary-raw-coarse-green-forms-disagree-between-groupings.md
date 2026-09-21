# Ordinary raw coarse Green forms disagree between groupings

## Scope and result

The raw single-seam derivative forms on the two coarse groupings do not have equal pullbacks to the ordinary common cell, when distinct coarse cut labels are orthogonal and vacuum/Omega have unit norm. An exact two-vector forgotten-sector witness suffices. This is not a claim about every possible prescribed coarse assembly.

This sharpens `ordinary-cut-observation-does-not-preserve-the-raw-coarse-green-form.md`: the issue is not only the choice of refined target. These two raw coarse forms themselves differ.

## Witness in the common ordinary cell

Use six distinct event indices 0,...,5. Let r(i,j) denote the forgotten local diamond relation and p(i,j) the forgotten path in that order. The two common-cell vectors belong to different retained partitions:

    u = r(0,1) tensor [p(2,3)] tensor r(4,5),
    v = r(0,2) tensor [p(1,3)] tensor r(4,5).

In the left grouping observe [aw] tensor c by D(aw) tensor D(c), retaining the coarse four-event cut label. Both vectors have the same four-event cut {0,1,2,3}. Their first derivative factors share exactly one edge with coefficient +1; their final factors coincide and have squared form four. Their diagonal squared forms are sixteen. Thus

    G_left = [[16,4],[4,16]].

In the right grouping observe a tensor [wc] by D(a) tensor D(wc), retaining the coarse two-event cut label. The labels {0,1} and {0,2} differ, so the cross pairing is zero. The diagonals remain sixteen:

    G_right = [[16,0],[0,16]].

In particular u+v has squared form 40 on the left and 32 on the right. Comparing only basis diagonals would miss the obstruction. Tensoring one common root state multiplies these entries by its squared form; nondegenerate root pairing also permits a nonzero paired root factor without requiring every root vector to have nonzero self-pairing.

All terms are forgotten: no theta forcing, spectral integration, memory feature weights, or conditioning affects this example. A global suspension unit phase on both arguments cannot repair the discrepancy.

## Consequence

No single form on the ordinary common cell can simultaneously be the pullback of both of these raw coarse forms along the fixed comparison maps. Equality of the source multiplication square and equality of the separately constructed cut observations do not imply that metric statement.

The shifted-product paired theorem is unaffected: it uses a specified common joint target and does not claim isometry of the ordinary coarse forms. The 2160 ordinary coordinates remain retained; this discrepancy does not make them radical.

## Productive next decision

Determine whether these raw derivative forms are the intended coarse forms. If so, the next artifact should be a source-derived cross-cut defect pairing, or an explicitly justified common assembly replacing the incompatible comparison target. Such an assembly must be identified as additional data, not inferred from source associativity. If a different coarse form is intended, give its exact carrier, cut identifications, and cross-cut entries and rerun this witness against it.

Do not try to repair the discrepancy by rescaling local theta features, choosing a positive relation metric, or dropping ordinary coordinates.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_ordinary_coarse_green_grouping_obstruction.py`

The checker uses the actual source derivative and relation routines from the existing six-prime comparison certificate. It computes both 2-by-2 matrices with retained coarse labels and verifies that every contributing coordinate is a vacuum/Omega coordinate. This is a finite exact obstruction, not a full 2160-dimensional form calculation or a proof of arbitrary coarse quotient descent.
