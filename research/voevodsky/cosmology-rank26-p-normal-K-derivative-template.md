# Uniform K-multiplication derivative template

## Issue-tree position

The target-activation envelope was falsified, exhausting that leaf. Tree rescoring selected the independent \(K\)-multiplication absorption branch. Its first leaf asks whether the 4,224 derivative rows have a uniform source construction.

## Result

For a source relation

\[
e-Ke_+=0,
\]

the directional derivative is

\[
D_v(e-Ke_+)=-(D_vK)e_+.
\]

Every degree-14 \(K\)-family derivative row is exactly a retained monomial shift of this one directional polynomial, copied across the pole and marked-level blocks.

The checker verified all 4,224 rows for each of `nx`, `ny`, and the p-tangent direction, with zero failures. The directional polynomials have respectively 5, 5, and 6 monomial terms. It also verified

\[
D_{n_x}K-D_{n_y}K=D_{n_x-n_y}K.
\]

## Disposition

The \(K\)-derivative source-generation problem collapses from 4,224 unrelated rows to one polynomial template per direction. This is an algebraic mechanism for generation, not yet for absorption into `S+T`.

The next depth-first leaf is to determine whether multiplication by \(D_vK\) factors through the retained special \(K\)-relation and tangent complex, thereby constructing a uniform absorption homotopy rather than rowwise pivot certificates.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_derivative_template.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_derivative_template.json`
