# 583 — Two Kinematic Derivatives Preserve the Deletion Diagram

## Hard-to-vary claim

The functorial deletion diagram of Entry 581 is preserved by the sourced top twisted de Rham connection in two independent kinematic directions.

## Frozen calculation

Retain

\[
\gamma=5,qquad \mathbb F_{32003},qquad
\text{ambient degree }9,qquad
\text{pole depths }(2,2).
\]

For a labelled form

\[
\frac{P}{K^k\prod_iq_i^{e_i}},
\]

the parameter derivative used in the quotient presentation is

\[
\nabla_\lambda=
\partial_\lambda P+
(\gamma-k)K_\lambda\frac{P}{K}
-\sum_i e_i(q_i)_\lambda\frac{P}{q_i}.
\]

The Cayley--Menger derivatives are evaluated exactly by the five-point stencil, which is exact because \(K\) has parameter degree at most four. The two directions are \(\partial_x\) and \(\partial_y\).

## Essential typing correction

The localization representative for adjoining \(q_j\) is \(Pq_j/q_j\). Since \(q_j\) depends on kinematics, differentiating it requires the explicit numerator term

\[
\partial_\lambda(Pq_j)=
(\partial_\lambda P)q_j+P(q_j)_\lambda.
\]

Omitting the second term would test a frozen presentation rather than the rational class.

## Result

For every deletion edge \(S\subset S\cup\{j\}\), the exact normal forms satisfy

\[
\boxed{
\nabla_\lambda\circ L_{S,j}
=
L_{S,j}\circ\nabla_\lambda
}
\]

for both \(\lambda=x,y\).

There are twelve edges, hence twenty-four naturality tests per generic point. All pass at

\[
(x,y,z)=(2,3,4),\qquad(3,5,6).
\]

Thus the tested result is

\[
48/48
\]

commuting derivative--localization squares.

## Narrow conclusion

The deletion cube is not only an incidence-compatible diagram of quotient spaces. In two independent source directions it is a diagram of Gauss--Manin modules on the tested generic fibers.

This supports sector-specific coefficients over an unchanged energy/deletion carrier. No new carrier incidence is indicated.

## What remains open

Flatness is not inferred from pointwise naturality. It requires second parameter jets and a direct reduction of

\[
[\nabla_x,\nabla_y]
\]

including derivatives of the reduced coefficients. Nor is extension through the discriminant or compatibility with the physical integration chain established.

## Next falsifier

Construct the mixed second jet of the frozen product-pole presentation and test curvature on every mask, followed by compatibility of the resulting flat packet with the top relative/Gysin rank-one class.

## Artifacts

- `research/benincasa/marici-gm/src/bin/generic_q_pole_twisted_derham_rank.rs`
- `research/benincasa/deletion-connection-naturality-audit.json`
