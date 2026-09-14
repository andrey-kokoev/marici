# Smooth Q-manifold realization gate

Date: 2026-09-08

## Decision

A literal smooth Q-manifold in Bruce's category cannot retain the native Marici node near the conductor.

Work over any residue field of the spectator base. The native local model is

\[
B=k[x_0,x_2,x_4,x_1,x_3,x_5]/(x_ex_o:e\text{ even},\ o\text{ odd}).
\]

It is the union of two three-dimensional affine branches meeting at the origin. The defining ideal has nine independent quadratic minimal generators and height three. At the conductor all first derivatives of these quadrics vanish, so

\[
\operatorname{rank}J(0)=0,
\qquad \dim T_0\operatorname{Spec}B=6,
\qquad \dim_0\operatorname{Spec}B=3.
\]

Thus the reduced/native base is singular. It is also not a local complete intersection at the conductor: a height-three complete-intersection ideal would need three minimal generators, whereas this ideal needs nine.

A smooth supermanifold has a smooth reduced manifold. Therefore no smooth supermanifold can have this native node as its reduced local function ring. Adding odd coordinates or a homological vector field does not repair singularity of the reduced base.

## Consequence

There is no honest way to complete the remaining step while simultaneously requiring:

1. Bruce's smooth-supermanifold category;
2. the unchanged native node coefficient ring;
3. the strict `D35/D04` conductor behavior.

The GR formal moduli problem in `IndCoh` is not merely a provisional convenience; it is the natural realization category forced by the singularity. A smooth realization would have to resolve or replace the node and then prove descent back to it. Such a replacement would not be a literal realization over the same native base.

The non-lci calculation also rules out the most immediate finite quasi-smooth presentation with this classical truncation. More general derived, stratified, or infinite-cell resolutions remain possible but lie beyond Bruce's hypotheses.

## Analytic boundary

Even after replacing the singularity by a smooth presentation, Bruce's trace theorem would still require compactness, a nuclear Frechet smooth-function algebra, superorientation, and an invariant Berezin volume. None follows from the strict algebraic target.

## Verification

```sh
python research/voevodsky/check_marici_smooth_q_manifold_realization_gate_20260908.py \
  --output research/voevodsky/marici_smooth_q_manifold_realization_gate_certificate_20260908.json
```

The checker performs 19 exact dimension, generator and branch checks.
