# Convex filling pencils have continuous center-based coherence

## Owning restriction and identity convention

Use the independently verified three-bin moment carrier restricted to Grothendieck's certified interior rectangle in (S,F). The observation is the fixed stepwise lower-functional pair, not the exact prime kernel. Equip source fibers with their ordinary Euclidean topology. This is an explicit choice of witness equivalence, distinct from the discrete tags of the braid-defect fixture.

## Continuous section

The four rectangle corners have certified source lifts x00,x01,x10,x11. For normalized coordinates u,v in [0,1], define

    s(u,v)=(1-u)(1-v)x00+(1-u)v x01+u(1-v)x10+uv x11.

The weights are nonnegative and sum to one. Convexity places s in the admitted source. Linearity of observation gives exactly the requested (S,F), continuously in u,v.

Every fiber contracts by

    H(x,t)=(1-t)x+t s(S(x),F(x)).

Both endpoints have the same observation, so the entire contraction lies in that fiber and in the admitted source. The section is fixed by H.

## Parameterized diamond equivalence

For outer points a,b, the two middle fibers lie over (S(a),F(b)) and (S(b),F(a)). The rectangle supplies both throughout the parameter domain. Map each fiber constantly to the other's section point. The composites are their center maps, and H supplies the two homotopy-inverse laws. All formulas vary continuously with the outer observations.

These maps are homotopy equivalences, not inverse bijections of exact source points. They intentionally use the declared topological identity rather than preserve all pointwise source information.

## Coherence mechanism

Comparisons among nonempty fibers factor through their centers. Every positive-length composite is the same final-center map. Identity comparisons carry the explicit center contraction. More generally, two parameterized witnesses in a fixed convex fiber can be joined by pointwise convex interpolation; where they agree on a prescribed boundary, this interpolation keeps that boundary fixed. A continuous sphere-valued family in such a fiber extends over its cone by contraction to the continuously chosen center.

This provides explicit constructions for compatible higher fillers. It is not a machine formalization of a complete infinity-category or a claim that arbitrary independently chosen comparison maps already satisfy all coherence laws.

## Exact checks and observation boundary

Fresh independent replay confirms the owning rectangle and corner lifts. Exact rational controls check 81 fiber-contraction instances, 486 parameterized diamond cases, and 81 two-parameter filler cases. The continuum statements follow from the displayed affine/convex identities, not the finite samples.

An independently checked kernel-direction perturbation keeps S,F fixed while changing x1 along a contraction. Thus bin-level audits do not automatically descend through this witness equivalence. Functions of S,F remain invariant. A richer observation contract would require reevaluating the admissible contractions.

## Disposition

The proposed parameterized convex coherence has an explicit continuous construction on the owning rectangle. Reversal exchanges the two fiber roles and their center maps. The discrete braid obstruction and this positive convex result are compatible: the source's identity structure and retained observations determine whether a higher comparison is admissible.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/check_convex_filling_coherence.py

Artifacts:

- `results/convex-filling-coherence-contract.json`
- `results/convex-filling-coherence.json`
