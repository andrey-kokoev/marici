# Presentation-independent closed returns

## Nine explicit product-anchor maps

Combine three primitive anchor choices on each factor: a four-cycle, one
2-cycle with attached vertices, and two disjoint2-cycles. This gives nine maps
from the same rectangle-cell complex to the same Dowker triangle complex.
Every map passes its edge/2-cell chain square.

Their ranks on the1039-dimensional closed source space are

    279,207,247,
    207,138,187,
    247,187,215.

These differences concern internal cell information. Pulling the two target
periods back to the source gives identical class functionals for all nine maps.
The checker verifies their equality on a complete closed-source basis.

## Same class constraint, same return

For two different anchor maps, request the same two class increments. Combining
the two period constraints with source closure gives115 independent rows. Exact
minimum-cost solutions are the same harmonic source chain, with the same
retained rectangle cost.

Thus the class-level return genuinely descends across these presentation maps.
The equality follows from equality of the constraints on the admissible source
space and use of the same source metric.

## Complete retained presentations

For a full target-chain view y=T*x, retain the orthogonal complement
r=x-L*y, where L is the minimum-norm lift on image(T). Then x=L*y+r.

The checker transports a closed state containing both orientation and internal
components between the rank279 and rank215 views. Both target/residual packages
reconstruct the same x, restore source closure, and carry the same cost
84*||x||^2. Transport back recovers the original package exactly. The quotient
and residual budgets may redistribute while their sum remains fixed.

## Different partial constraints can require different returns

A local zero-class boundary mode is invisible in the rank215 map and visible
in the rank279 map. Asking each map to reproduce that mode's target change
yields a zero minimum update in one view and a nonzero update in the other.
Both requests have zero homology-class increment, but they impose different
cell-level constraints.

This negative control identifies the boundary of the coherence law: class
agreement does not imply equality of partially observed interventions.

## Invertible coordinate changes

Rescale every triangle coordinate by a specified nonzero rational factor,
transport the requested increments by the same factors, and retain the source
metric. The exact constrained minimum return is unchanged. This tests a genuine
coordinate change of the same source constraint, rather than a change in what
the interface observes.

## Structural law

A return is presentation-independent when the presentations express the same
admissible source constraint and transport the source cost. Complete retained
records implement this by reconstruction. Common class-level requests implement
it through equal period functionals. Partial views require an explicit relation
between their observation constraints.

The resulting model now separates representational changes from changes in
observability. To choose dynamics, specify which of the internal modes an
operation actually observes and constrains; class data and reconstruction
coherence alone leave that choice open.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_presentation_return_coherence.py

Nine exact view-rank/class-functional comparisons, two class-return solves,
complete metric-preserving roundtrip, a partial-view negative control and an
invertibly rescaled-return test. The solver uses exact rational normal equations
and verifies all source constraints. The checks apply to the fixed two-factor
complex and the declared cell metric.
