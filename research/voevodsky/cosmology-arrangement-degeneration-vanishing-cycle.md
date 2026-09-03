# Arrangement degeneration and vanishing class

## Question

Does the concurrent-fiber null class transport to the original triangle through the arrangement degeneration?

## Claim boundary

For the family `X=0`, `Y=0`, `X+Y+tZ=0`, the incidence determinant is `t`. Over `t!=0`, the coordinate change `Z'=tZ` trivializes the family, whose second cohomology is constantly rank one. At `t=0`, the new circuit relation `l3-l1-l2=0` appears and the special complement has second cohomology zero.

The specialization map is therefore `0 -> Q` in degree two. The generic generator maps to the rank-one vanishing quotient; no special-fiber nullhomotopy transports back to it.

Away from zero, the would-be circuit has residual `tZ`. Using the special relation to kill the generic class requires division by `t`, which is not regular at the degeneration and is not a source-natural family morphism over the base.

## Disposition

The degeneration identifies `Xi_log` as precisely the class lost at concurrency. The concurrent geometry supplies no regular horn on the original fiber. The next leaf tests whether a controlled `1/t` logarithmic object defines an admissible nearby-cycle boundary or only restates the vanishing-cycle connecting morphism.

## Verification

- `research/voevodsky/check_cosmology_arrangement_degeneration_vanishing_cycle.py`
- `research/voevodsky/results/cosmology_arrangement_degeneration_vanishing_cycle.json`
