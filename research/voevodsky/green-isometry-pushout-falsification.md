# Falsification of unrestricted Green-isometry pushouts

## Question

Does the under-attachment sector of polarized Green spaces admit the pushouts required for covariant reindexing?

## Claim boundary

This packet tests finite-dimensional positive-definite spaces with form-preserving embeddings. Failure there blocks unrestricted Green pushouts but does not exclude certified amalgamations with additional cross-pairing data.

## Bold conjecture under test

Green-form-preserving embeddings form a category with pushouts, so an attachment \(X\to E\) can be transported covariantly along every structured map \(X\to Y\).

## Strongest falsification attempt

Take the initial span over the zero space

\[
0\longrightarrow \mathbb R,
\qquad
0\longrightarrow \mathbb R
\]

in the category of finite-dimensional real inner-product spaces and linear isometries. Suppose a pushout \(P\) exists with isometries \(i,j:\mathbb R\to P\).

There are two admissible cocones:

1. into \(D_1=\mathbb R\), with both legs the identity;
2. into \(D_2=\mathbb R^2\), with the legs the two orthogonal coordinate embeddings.

Universality for the second cocone requires an isometry \(P\to\mathbb R^2\) whose image contains two orthogonal unit vectors, so \(\dim P\ge2\). Universality for the first cocone requires an isometry \(P\to\mathbb R\), so \(\dim P\le1\). This is impossible.

Therefore even binary coproducts, hence general pushouts, fail in the isometry category.

## Exact residual

The obstruction is not positivity itself but undeclared cross pairing. A putative amalgam must decide the inner product between the two new complements. Different cocones demand incompatible values: one demands correlation one, another correlation zero.

The orthogonal direct sum chooses correlation zero and is useful, but it is not universal among all isometric cocones.

## Consequence for the Green bridge

The map

\[
\iota_p:\mathcal G_p^{\rm cyc}\to\mathcal G_p^{\rm full}
\]

cannot be reindexed by arbitrary pushout inside a category whose morphisms preserve the Green form exactly. The under sector is therefore not a global covariant displayed functor on that category.

## Revised architecture

Admit only cospans equipped with a source-derived amalgamation certificate specifying:

- the cross Green pairing between complements;
- positivity or controlled indefiniteness;
- radical compatibility;
- typed-port preservation;
- sewing compatibility.

Composition is then partial or lives in a double category/equipment of certified correspondences. Beck–Chevalley cells are obligations for composable certified squares, not automatic consequences of ordinary pushouts.

## Disposition

The unrestricted Green-isometry pushout conjecture is rejected. The surviving target is a category of certified amalgamations, or a double category whose horizontal arrows retain the cross-pairing witness.

## Verification

- `research/voevodsky/checkers/check_green_isometry_pushout.py`
- `research/voevodsky/results/green_isometry_pushout.json`
- `research/voevodsky/green-extension-variance-audit.md`
