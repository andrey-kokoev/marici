# Fixed-local-block prime semigroup is falsified by projection leakage

## Target

The corrected conjecture required complete normalized prime transfers `C_a` on one short-support Weil block to compose and admit a joint-coinvariant regular coextension.

## Canonical compression model

Let `K` be the ambient source form space, let `Y:H_0->K` be the isometric realization of one radical-reduced local positive block, and let `P=YY*` be its range projection. Let `U_a` be logarithmic translation by displacement `a`. The normalized cross transfer has the canonical compression form

`C_a=Y* U_a Y`.

Then

`C_a C_b-C_(a+b)`

`=Y*U_a P U_bY-Y*U_aU_bY`

`=-Y*U_a(I-P)U_bY`.

Thus composition holds exactly when every translated local vector has no component outside the chosen local block at the intermediate stage.

## Support falsifier

A short-support block is defined by functions supported in one bounded logarithmic cell. Nonzero translation moves that support to a different cell. Hence its ambient image is not invariant or coinvariant under all prime translations. Choose a nonzero vector supported near the boundary facing the inverse translation. Then

`(I-P)U_b*Yf != 0`.

This is exactly the coinvariance residual required to vanish by the corrected conjecture, so that conjecture fails on the intended fixed-cell realization. For forward composition one likewise has intermediate leakage `(I-P)U_bYf`; a later compression may accidentally annihilate it for one pair, but cannot supply the missing coinvariance law.

The obstruction is structural and precedes numerical evaluation of `C_2,C_3,C_6`: fixed-cell compression discards intermediate route data that an exact coextension must retain.

## Consequence

The joint-coinvariant coextension conjecture on a single fixed `H_0` is rejected for the intended short-support realization. Adding coinvariance does not repair the model; the actual local block does not satisfy it.

## Surviving replacement

Prime transport must act between distinct block fibers rather than as endomorphisms of one compressed block. Let `H_x` be the local Weil block over the cell at logarithmic location `x`. A prime gives a correspondence

`E_p(x):H_x -> H_(x+log p)`

that retains the leakage channel instead of projecting it away. Composition is then a typed map

`E_p(x+log q) tensor E_q(x) -> E_(pq)(x)`.

Mixed-prime coherence is a comparison between the two paths through different intermediate fibers. The global Weil space is the completion of the full fiber diagram, not the completion of repeated endomorphisms of one cell.

The three original problems are therefore retyped:

1. composition becomes associativity of fiber correspondences;
2. the `2 x 3` gate becomes a commuting tensor square with its full intermediate channels;
3. no-new-radical becomes faithfulness of the diagram's colimit form.

## Disposition

Both single-block dilation conjectures are falsified. The viable unified object is a prime-indexed product system of local Weil correspondences over the logarithmic cell groupoid. Its first test is whether the two complete paths from `H_x` to `H_(x+log 6)` agree before any projection back to `H_x`.
