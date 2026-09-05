# Six-point NMHV worldsheet integrand construction

## Question

What explicit worldsheet object can be tested against the established six-point NMHV momentum-twistor components?

## General Yang–Mills half-integrand

For marked points `z_i`, define

\[
E_i=\sum_{j\ne i}\frac{s_{ij}}{z_i-z_j}.
\]

For gluon momenta `k_i` and polarizations `epsilon_i`, define

\[
\Psi=\begin{pmatrix}A&-C^{\mathsf T}\\ C&B\end{pmatrix},
\]

with off-diagonal entries

\[
A_{ij}=\frac{k_i\!\cdot k_j}{z_i-z_j},
\quad
B_{ij}=\frac{\epsilon_i\!\cdot\epsilon_j}{z_i-z_j},
\quad
C_{ij}=\frac{\epsilon_i\!\cdot k_j}{z_i-z_j},
\]

and `A_ii=B_ii=0`, `C_ii=-sum_{j != i} C_ij`. Fix

\[
\operatorname{Pf}'\Psi=
2\frac{(-1)^{p+q}}{z_p-z_q}
\operatorname{Pf}\!\left(\Psi^{pq}_{pq}\right).
\]

The ordered component candidate is

\[
A_6(\alpha)=\int d\mu_6\,\operatorname{PT}(\alpha)\operatorname{Pf}'\Psi.
\]

## Four-dimensional supersymmetric refinement

For a three-element negative-helicity set `L` and complement `R`, define

\[
\mathcal I_{6,L}(\alpha)=
\frac{1}{\operatorname{vol}GL(2)}
\prod_{a=1}^{6}\frac{d^2\sigma_a}{(a\,a{+}1)_\alpha}
\prod_{I\in L}
\delta^2\!\left(\tilde\lambda_I-
\sum_{i\in R}\frac{\tilde\lambda_i}{(I i)}\right)
\delta^{0|4}\!\left(\eta_I-
\sum_{i\in R}\frac{\eta_i}{(I i)}\right)
\prod_{i\in R}
\delta^2\!\left(\lambda_i-
\sum_{I\in L}\frac{\lambda_I}{(i I)}\right).
\]

The cyclic factor follows the ordering `alpha`. This supplies the helicity-sector localization absent from the ordinary reduced-Pfaffian statement.

## Convention map

For every ordering, momentum twistors give the common on-shell variables by

\[
\tilde\lambda_i=
\frac{\langle i\,i{+}1\rangle\mu_{i-1}
+\langle i{+}1\,i{-}1\rangle\mu_i
+\langle i{-}1\,i\rangle\mu_{i+1}}
{\langle i{-}1\,i\rangle\langle i\,i{+}1\rangle},
\]

with the identical linear map from `chi` to `eta`. The target is the coefficient of

\[
\prod_{I\in L}\prod_{A=1}^{4}\eta_I^A.
\]

## Normalization contract

Compare after removing the common momentum- and supermomentum-conservation delta functions, omitting the same coupling and factor of `i`, retaining the declared Parke–Taylor denominator, using `s_ij=<ij>[ji]`, and fixing the reduced-Pfaffian sign by the displayed formula. No multiplicative fit is permitted after evaluation.

## Exact localization algebra

Fixing `z1=0`, `z2=1`, and `z6=-1` leaves three scattering equations. Clearing their denominators introduces collision components, so the checker saturates the numerator ideal by every forbidden marked-point collision divisor. The saturated ideal is zero-dimensional and has a square-free degree-six elimination polynomial. Hence the exact fixture has six simple CHY solutions over the algebraic closure, matching `(6-3)!`.

Evidence:

- `research/nima/checkers/check_six_point_chy_localization_algebra.py`
- `research/nima/results/six-point-chy-localization-algebra.json`

## Global-residue control

The optimized companion-matrix trace evaluates the diagonal biadjoint CHY pairing exactly and matches the sum of all 14 planar cubic hexagon diagrams. The raw signs differ by `(-1)^(6-3)`, the predicted orientation factor between the ordered three-variable residue and the unsigned propagator sum. This fixes the global residue convention before polarization data enter.

Evidence:

- `research/nima/checkers/check_six_point_chy_biadjoint_global_residue.py`
- `research/nima/results/six-point-chy-biadjoint-global-residue.json`

## Yang–Mills reduced-Pfaffian test

The exact quotient-algebra trace now includes the reduced Pfaffian. An initial evaluation produced MHV and NMHV ratios `-1/16` and `+1/16`; the helicity-dependent sign identified a missing minus sign in the negative-helicity polarization convention. After that repair both ratios were `-1/16`. This common factor decomposes without fitting: five Pfaffian pairings require the CHY twice-dot-product matrix convention, contributing `2^5`, while the selected reduced-Pfaffian definition removes the provisional factor `2`; the ordered three-variable residue contributes `(-1)^3`. Applying those declared conventions gives ratio one for both the MHV control and the `(1-,2-,3-)` NMHV component.

Evidence:

- `research/nima/checkers/check_six_point_chy_yang_mills_pfaffian.py`
- `research/nima/results/six-point-chy-yang-mills-pfaffian.json`

## All-gluon component theorem

The exact reduced-Pfaffian residue agrees with the momentum-twistor construction for all 20 choices of three negative-helicity gluons in the ordering `(1,2,3,4,5,6)`. Every component is nonzero and every residual vanishes exactly.

Evidence:

- `research/nima/checkers/check_six_point_chy_all_nmvh_gluon_components.py`
- `research/nima/results/six-point-chy-all-nmhv-gluon-components.json`

## Cross-order and full-color theorem

All 480 pairs formed from 20 pure-gluon NMHV helicity assignments and 24 DDM orderings agree exactly between the CHY and momentum-twistor constructions. Direct contraction of the CHY residues with free-Lie half-ladder tensors is endpoint-basis independent for all 20 helicity assignments, retains 120 nonzero cyclic color words per generic component, and detects a hostile color sign mutation.

Evidence:

- `research/nima/checkers/check_six_point_chy_all_ddm_gluon_components.py`
- `research/nima/results/six-point-chy-all-ddm-gluon-components.json`
- `research/nima/checkers/check_six_point_chy_full_color_dressing.py`
- `research/nima/results/six-point-chy-full-color-dressing.json`

## Disposition

The worldsheet-plus-free-Lie construction independently derives the full color-dressed pure-gluon sector. The complete N=4 NMHV superamplitude is separately constructed by coupling the full momentum-twistor Grassmann tensor to the same free-Lie DDM module; its two endpoint bases agree in all 8,855 Grassmann tensor coordinates and 120 cyclic color words. A direct refined-worldsheet derivation of the non-gluon coefficients remains unperformed, but it is no longer required to establish the color-dressed superamplitude itself.
