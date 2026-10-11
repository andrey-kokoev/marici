# Iteration 2: what the realized vertex must retain

Fresh input: `results/potential_complex_pullback_store.json`. Its complete source-bound verifier was rerun before this audit.

## A concrete loss, not just a dimension argument

The positive-depth fiber of the actual projection P -> T is a copy of the potential boundary sphere S2. A host point does not determine a potential direction. For example, the following two compatible pairs have depth 1/2 and exactly the same host readout:

```text
x  = (2/3, 1/6, 1/6)
y1 = (5/8, 1/8, 1/8, 1/8)
y2 = (1/8, 5/8, 1/8, 1/8).
```

They are distinct points in the constructed pullback. Therefore no decoder receiving x alone can reconstruct both. Adding a chosen direction would be additional input, not recovery from x.

The finite vertex inventory exhibits the same issue: each of the six host boundary vertices has fourteen pullback vertex preimages; each of the fourteen potential boundary vertices has six. Both projections together distinguish all 85 vertices.

## A lossless point interface

At positive depth retain `(host point x, potential boundary direction v)`. Recover

```text
h = 1 - 3 min(x_i)
y = (1-h)(1/4,1/4,1/4,1/4) + h v.
```

The codec rejects an interior potential point masquerading as a boundary direction. It round-trips an interior point of every one of the 432 four-dimensional cells. At depth zero the correct point encoding is simply the apex; no direction is determined there.

This gives a sufficient point interface. It is not a proof of globally minimal coding cost.

## Lossless storage of the entire folded object

A separate object-level recipe retains:

- the complete flagged T and C complexes;
- both interface maps and the source proton witness;
- the named ordered-product/cone reconstruction algorithm;
- the expected reconstructed root.

It omits the expanded pullback inventory. The decoder regenerates every product cell and its fold provenance, both projections, the conforming host refinement and the belt. The resulting packet is exactly equal to the original, including its root:

```text
c5e68edd89c4a126d08e4e46c0ed4fd3fc82dd2c78e2a2cdb933c79c21cfef97
```

Canonical JSON sizes:

| Stored content | Bytes |
| --- | ---: |
| Expanded contract | 64,833 |
| Factor contract without expanded P | 2,002 |
| Complete original packet, including proton witness | 1,280,351 |
| Complete recipe, including proton witness | 1,215,585 |

The 2,002 bytes are not the complete self-contained implementation cost: the decoder and source witness are necessary. These are serialized byte counts, not primitive coefficient-arrow counts or particle masses. No unrestricted minimality claim is made.

Removing one inward-fold chart, corrupting the center's interface image or substituting an unknown reconstruction algorithm causes rejection. Merely retaining a hash without the reconstructing payload is not this recipe.

## Important correction to the interpretation of realization

In the current ordinary PL pullback, the literal fiber over the realized host center is **one point**, not a tetrahedron or a collection of 24 folds. The fold information survives in the retained surrounding complex and its reconstruction recipe. The link of that point is S1 x S2.

Thus two readings must not be conflated:

1. A vertex **with a retained neighborhood/potential-complex witness**: the new recipe supports this interpretation.
2. A vertex whose **ordinary categorical point fiber itself contains the inward folds**: the depth-map pullback does not provide this.

Calling a decorated point a larger ordinary fiber would conceal the central obligation rather than solve it. The next executable step is to specify and construct the fold-bearing vertex interface explicitly—e.g. a retained germ or direction complex—and check its projection and universal-property obligations rather than silently changing categories.

## Belt and transport consequence

The six-panel belt remains exactly reconstructible from the flagged host complex. Its panel count comes from the full flag convention, not from an independently imposed neutron object. The reconstruction introduces no sheet permutation. The earlier flat-extension obstruction at the center remains in force.

## Checks and artifacts

All 19 checks passed, including complete source replay, explicit information-loss witnesses, all-cell point round trips, exact object reconstruction and negative controls.

```text
python research/voevodsky/checkers/check_pullback_retention.py
```

- `research/voevodsky/checkers/check_pullback_retention.py`
- `research/voevodsky/results/pullback_retention.json`
- `research/voevodsky/results/pullback_retention_recipe.json`

This is an audit and reconstruction of the actual iteration-1 pullback, not another unrelated glue model. Electron coefficient-port attachment and particle identification remain unconstructed.
