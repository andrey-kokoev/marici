# Krylov magnitude has fibers; moments repair readout, not selection

Work package: WP613  
Owner: marici.Figueiredo

## Positive quotient coordinate

After WP612, the normalized physical content of one Krylov seed is

\[
\kappa=27p_1p_2p_3,
\qquad
p_i=\operatorname{Tr}(P_i^AP_x),
\qquad
\sum_i p_i=1.
\]

The normalization gives (0\le\kappa\le1). Zero means the seed misses an
eigendirection; one is attained only by democratic support.

## Exact nonfaithful fiber

The two normalized distributions

\[
p={1\over13}(1,6,6),
\qquad
q={1\over13}(2,2,9)
\]

are not permutations of one another, yet

\[
\prod_i p_i=\prod_i q_i={36\over2197}.
\]

Thus the descended Krylov magnitude does not identify the physical seed
distribution. This is an exact positive-coordinate instance of finite data
not implying a singleton fiber.

## Source-generated moment completion

For distinct eigenvalues (a_i), the seed moments are

\[
\mu_k=\langle x,A^kx\rangle=\sum_i a_i^kp_i.
\]

The record ((\mu_0,\mu_1,\mu_2)) is the three-by-three Vandermonde transform
of (p) and therefore reconstructs every weight exactly. At
((a_1,a_2,a_3)=(1,2,3)), its determinant is two. For the hostile pair,

\[
(\mu_1,\mu_2)_p=(31/13,79/13),
\qquad
(\mu_1,\mu_2)_q=(33/13,91/13).
\]

The moment tower is jointly faithful on the admitted probability simplex.
This parallels the finite contextual inversion results in other sectors.

## Why faithfulness is not selection

The moment tower reports which seed distribution was supplied. It does not
choose one. Likewise, extremizing only (kappa) selects an endpoint:

- maximization selects democratic support;
- minimization selects a missing eigendirection.

The central CKM columns are positive, strongly hierarchical and strictly
interior. Their normalized products are all below (0.01), far from the
democratic maximum, while none is zero. A monotone coefficient-free action of
the Krylov magnitude therefore misses observed flavor.

An interior source law must predict at least two independent moments or an
equivalent full weight vector. Inserting their measured values into a positive
potential would encode the target rather than explain it.

## Instrument typing

For (A=H_u) and a down spectral seed, the probabilities are one CKM column:

\[
p_i=|V_{ij}|^2.
\]

Charged-current branching fractions measure these weights, and the moments
are executable summaries once the spectral eigenvalues are calibrated. They
are not additional source interventions. A proposed architecture is refuted
if its independently predicted moments disagree with those records.

The remaining constructor problem is therefore sharper: derive the moments
from a microscopic evolution and seed-preparation process while preserving
the observed charged-current matrix. Merely measuring or reconstructing them
does not supply that process.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp613_krylov_magnitude_moment_completion.py

The generated result is
research/flavor/results/wp613_krylov_magnitude_moment_completion.json.
