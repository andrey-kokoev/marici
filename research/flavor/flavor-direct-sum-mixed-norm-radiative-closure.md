# Direct-sum mixed-norm radiative closure: WP731

## Question

Is the off-diagonal portal-block coefficient in WP730 optional, or is a mixed
singlet–triplet scalar channel generated whenever both representation-labelled
Higgs portals are present?

## Symmetry closure

Let

\[
R_h=H^\dagger H,
\qquad
R_A=\operatorname{Tr}(S_A^\dagger S_A),
\qquad
R_B=\operatorname{Tr}(S_B^\dagger S_B).
\]

If a source symmetry admits both (R_hR_A) and (R_hR_B), then (R_A) and
(R_B) are individually neutral scalar invariants. Their product (R_AR_B)
is therefore also neutral. Independent phases, signs, or representation labels
cannot forbid this mixed norm quartic while retaining both portals.

The norm-sector potential must contain

\[
V=
\frac{\lambda_h}{4}R_h^2+
\frac{\lambda_A}{4}R_A^2+
\frac{\lambda_B}{4}R_B^2+
\frac{\delta_A}{2}R_hR_A+
\frac{\delta_B}{2}R_hR_B+
\frac{w}{2}R_AR_B.
\]

## Exact Hessian-square coefficients

For three real vector sectors with component counts (N_h,N_A,N_B), the
one-loop scalar divergence is proportional to the Hessian-square polynomial
(operatorname{Tr}[(\nabla^2V)^2]). The coefficients of the three mixed norm
monomials are

\[
\begin{aligned}
C_{hA}={}&2(N_h+2)\lambda_h\delta_A
+2(N_A+2)\lambda_A\delta_A
+2N_B\delta_Bw+8\delta_A^2,\\
C_{hB}={}&2(N_h+2)\lambda_h\delta_B
+2(N_B+2)\lambda_B\delta_B
+2N_A\delta_Aw+8\delta_B^2,\\
C_{AB}={}&2(N_A+2)\lambda_Aw
+2(N_B+2)\lambda_Bw
+2N_h\delta_A\delta_B+8w^2.
\end{aligned}
\]

The checker independently constructs the full Hessian for component counts
((2,3,4)) and recovers these general formulas exactly.

## Flavor-model multiplicities

The Higgs doublet has four real components. Each complex three-by-three matrix
scalar has eighteen. Thus

\[
(N_h,N_A,N_B)=(4,18,18),
\]

and

\[
\begin{aligned}
C_{hA}={}&12\lambda_h\delta_A+40\lambda_A\delta_A
+36\delta_Bw+8\delta_A^2,\\
C_{hB}={}&12\lambda_h\delta_B+40\lambda_B\delta_B
+36\delta_Aw+8\delta_B^2,\\
C_{AB}={}&40(\lambda_A+\lambda_B)w
+8\delta_A\delta_B+8w^2.
\end{aligned}
\]

At (w=0), both nonzero portals generate

\[
C_{AB}=8\delta_A\delta_B.
\]

Therefore the uncoupled surface (w=0) is not radiatively closed when both
portals are active. At nonzero (w), the portal equations acquire the mutual
feedback terms (36\delta_Bw) and (36\delta_Aw). This supplies an explicit
source for WP730's off-diagonal stability entry.

## Claim boundary

The calculation is exact for the radial norm sector. The complex matrix
scalars also admit single-trace quartics and, in the simultaneous theory,
additional mixed tensor contractions depending on the declared flavor
symmetry. Those operators can enlarge the beta system and change numerical
fixed-point coordinates. They cannot remove the fact that the norm cross term
is symmetry allowed and sourced by the product of the two Higgs portals at the
all-cross-couplings-zero locus.

WP731 therefore proves radiative coupling of the two portal channels, not a
complete fixed point. The next grammar gate is to enumerate all independent
mixed matrix-scalar quartics and determine whether a source grading can reduce
them without also removing either additive Yukawa portal source.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp731_direct_sum_mixed_norm_radiative_closure.py`

Generated result:
`results/wp731_direct_sum_mixed_norm_radiative_closure.json`.
