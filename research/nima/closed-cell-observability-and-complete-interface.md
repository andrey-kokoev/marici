# Closed-cell observability and a complete retained interface

## Exact ranks of the existing view

The two-factor closed rectangle-cell state space has dimension1039: two harmonic
orientation coordinates plus1037 zero-class closed modes. Restrict the existing
product-anchor rectangle-to-triangle map T2 to that space.

| Source sector | Dimension | Visible rank | Hidden dimension |
|---|---:|---:|---:|
| Internal boundary modes | 1037 | 277 | 760 |
| Full closed state | 1039 | 279 | 760 |

The two class directions survive independently. The triangle view also detects
277 internal directions, while760 closed internal directions lie in its kernel.
These ranks are computed exactly from an independent source basis extracted
from the2496 local3-boundaries and the two harmonic columns.

## A budget does not complete the readout

Among the local3-boundaries,1328 individually map to zero in the chosen triangle
view. Choose one nonzero b. The retained states b and -b have:

- the same zero orientation coordinates;
- the same zero triangle view;
- the same total weighted cost252;
- different labelled rectangle-cell values.

Therefore adding total cost to the class/view interface still leaves distinct
fixed-context states indistinguishable. The statement concerns labelled records;
no additional quotient identifying these states is imposed.

## A minimal linear completion

A linear interface that separates the full closed state must gain760 independent
readouts beyond the triangle view. The checker greedily selects individual
source-cell coordinates, keeping a coordinate only when it increases observation
rank. Exactly760 suffice, bringing the total rank to1039.

The selection depends on the explicit cell labelling and ordering. It is a
constructive implementation choice, not a canonical physical observable.
Keeping the entire source residual is another complete representation and
avoids choosing a coordinate subset, at the cost of redundancy.

An exact decoder carries observed values through rational row elimination and
back substitution. A test state using all1039 basis coordinates reconstructs
from its triangle view and the760 selected source readings. The augmented
observation matrix has full column rank, proving uniqueness for every closed
state in this linear model.

## Structural result

The current promoted interface has a measured information deficit:760 independent
closed modes. Preserving member identities and total cost does not make a smaller
readout injective. The architecture can retain those modes as complementary
records or choose an explicit complete readout interface.

The next return contract should distinguish the two interfaces:

1. A request on the partial triangle view has a family of admissible source
   responses, requiring a minimum-cost or other residual policy under closure.
2. A compatible request on the complete interface determines one source change.

The induced metric must accompany whichever interface is used. Observability
alone fixes reconstruction, not the response to incomplete requests.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_closed_cell_observability.py

Exact closed-basis and image ranks,1328 zero-image boundary controls, the equal-
budget sign pair, a minimal760-coordinate augmentation, and an explicit rational
decoder. The preceding two-factor transport certificates are rerun as part of
model loading. Reported ranks concern the concrete product-anchor map; other
presentation maps may have different visible/internal rank splits.
