# Applying the existing operator theorem to the actual belt

## Procedure recovered

The applicable source is `research/nima/monomial-projector-support-theorem.md`, implemented by `operators(rotations, reference)` in `research/nima/checkers/check_octahedral_monomial_projectors.py`.

For g rotation placements and m full-support monomial coordinates, the three separately typed stages have supports

```text
L: g m²
G: g² m
N: g² m².
```

This is a theorem about specified rotations, their generated mode family and coefficient basis. It does not accept the number of geometric tetrahedra as its sole input.

## Actual belt inputs

The audit consumes `results/four_six_center_cones.json`, bound to the original `tetrahedron.html` geometry. Subdividing each of its six belt faces at that face's centroid gives eighteen small triangles, using precisely the proton's face-to-three-triangles rule.

It transforms the belt into the original proton's monomial Cartesian frame. It does not choose a new basis to manufacture zeros. Coordinates lie in Q(sqrt(2)); the cyclic modes lie in that field extended by i sqrt(3).

The belt has six proper rotations. This is not merely a restricted search result: its vertex covariance has a distinct axial eigenvalue, so every rotation preserves the rim axis. Preserving or exchanging the two equilateral rims allows at most three rotations of each kind. Six monomial rotations are explicitly found.

Those rotations partition the eighteen oriented triangles into **three orbits of six**, not one orbit of eighteen. Each orbit's modes are exactly generated from its reference vector. Every spatial coordinate is nonzero.

One orbit belongs to rim edges; two belong to the two oriented stitch-edge classes. Their source-mode squared norms are respectively 4198/675 and 2386/675 (the latter for both stitch classes). Thus calling all eighteen triangles copies of one rotated reference would change the source data.

## What the existing theorem gives without a new rule

For each orbit, g=6 and m=3:

```text
L = 54, G = 108, N = 324; total = 486.
```

Applying the existing constructor independently to the three orbits therefore gives

```text
3 × 486 = 1458,
combined stage supports: L=162, G=324, N=972,
collective-return rank: 3.
```

These are three independent normalized collective returns. This is an application of the theorem to verified inputs, not a newly compiled single-mode belt network. The hypothesis audit does not serialize all coefficient arrows.

## Why 4050 was only conditional

Substituting g=18,m=3 gives 162+972+2916=4050. But the belt does not supply that single eighteen-placement rotation family. Likewise, the previously suggested 6×135+15×216 imports equal within-sector and between-sector block supports before their geometric transport has been established.

The three-orbit construction cannot simply be called a one-mode neutron counterpart to the one-mode proton. Coupling its independent returns requires inter-orbit maps and a joint-selection rule; the existing `operators` function supplies neither automatically.

If one insists on a dense, full-support collective projector over all 54 spatial coordinates, that N alone would have 2916 transfers. Thus replacing the three independent returns by a single dense return is a significant architectural change, not a free identification of the three amplitudes.

## Verification

```text
python research/voevodsky/checkers/check_belt_operator_inputs.py
```

Twelve exact checks pass. Artifact: `results/belt_operator_inputs.json`, recording the rotations, source triangles, orbit norms and theorem-derived supports. No charge or physical mass is assigned.
