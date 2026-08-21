# 1320 — The Full Kummer Deck Falsifies Bounded First-Order Polynomial IBP

## Correction

This entry retracts the positive closure claim in Entry 1315.

The earlier pilot had two coupled sampling defects:

1. it retained only three of the 32 Kummer sheets;
2. it counted sheet rows as independent base points.

Consequently the degree-four consistency was an interpolation artifact on an incomplete occurrence object.

## Frozen ansatz

\[
\partial_z\Omega+a(z)\Omega
=
\sum_{i=1}^3\partial_{u_i}(V_i\Omega),
\qquad
V_i\in\mathbf Q[u_1,u_2,u_3],
\qquad
\deg V_i\le d.
\]

The corrected checker evaluates the complete 180-term form on every deck character at each independently generated base point.

For each degree it uses

\[
N_{\rm base}=N_{\rm unknown}+24
\]

complete 32-sheet orbits. The tests are repeated over

\[
\mathbf F_{1009},\quad \mathbf F_{1013},
\qquad
z=7,\quad z=11.
\]

## Result

For every tested fiber and prime,

\[
\boxed{
d=0,1,2,3,4,5
\quad\Longrightarrow\quad
\text{the affine first-order polynomial-vector-field system is inconsistent}.
}
\]

The degree-five systems contain 169 unknowns and 6176 evaluated equations. Their coefficient ranks vary with the fiber, as expected on the specialized Kummer function space, but the augmented system is inconsistent in all four independent tests.

## Narrow theorem

Over characteristic zero, a rational identity of the frozen form would specialize to a consistent identity at every good finite-field fiber. The observed inconsistency at good fibers therefore falsifies the bounded ansatz through degree five:

\[
\boxed{
\nexists\,
a(z),V_1,V_2,V_3
\text{ of the declared polynomial type with }\deg V_i\le5.
}
\]

This does not exclude:

- higher differential order;
- rational or logarithmic vector fields with the frozen wall alphabet;
- a larger relative de Rham basis;
- supported boundary terms.

## Methodological consequence

All 32 labelled Kummer occurrences are required before an IBP relation is admissible. Sampling a few sheets can create false exactness, exactly as collapsing occurrence labels can create false carrier maps.

The next finite search should compare two predeclared extensions:

1. first-order logarithmic certificates with denominators restricted to the existing projective alphabet;
2. second-order polynomial certificates on the full deck cover.

Whichever has the smaller source-derived finite bound is tested first. No post hoc denominator may be added after inspecting consistency.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_first_order_ibp_pilot.rs`
- `research/benincasa/results/five-site-asymmetric-first-order-ibp-pilot.json`

Allocator claim: `seqclaim-db1d17b67fd0d1546722da7f`.
