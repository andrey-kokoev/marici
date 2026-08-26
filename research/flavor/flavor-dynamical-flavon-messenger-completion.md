# Dynamical flavon messenger completion (WP435)

## Local-gauge consistency problem

WP434 promotes diagonal quark-generation (SU(3)_F) to a local gauge symmetry.
Fixed nonuniversal Yukawa matrices would explicitly violate that gauge
symmetry. They must therefore arise from dynamical fields or from spontaneous
breaking in a UV completion.

Introduce two Hermitian adjoint scalars (Phi_u,Phi_d) with covariant kinetic
terms

$$
\frac12\operatorname{Tr}(D_mu Phi_u D^mu Phi_u)
+\frac12\operatorname{Tr}(D_mu Phi_d D^mu Phi_d),
$$

where

$$
D_mu Phi=\partial_mu Phi-i g_F[F_mu,Phi].
$$

The WP128 two-adjoint potential is then a genuine dynamical scalar potential,
and its commutator term produces the WP433 gauge-mass shape after the adjoints
acquire vacuum expectation values.

## Direct Yukawa operator and its defect

The gauge-invariant adjoint-flavon Yukawa operator is

$$
\frac{c_u}{Lambda_u}\bar Q_L\widetilde H Phi_u u_R
+\frac{c_d}{Lambda_d}\bar Q_L H Phi_d d_R+\mathrm{h.c.}
$$

Each operator has canonical dimension five. It is a valid EFT portal but not a
renormalizable dynamical completion.

## Minimal vectorlike messenger repair

Add one up-type and one down-type vectorlike messenger pair
((U_L,U_R)) and ((D_L,D_R)). Each pair has the Standard Model quantum
numbers of the corresponding right-handed quark and transforms as a
fundamental of diagonal (SU(3)_F). The up-sector interactions are

$$
y_Q^u\bar Q_L\widetilde H U_R
+y_Phi^u\bar U_L Phi_u u_R
+M_U\bar U_LU_R+\mathrm{h.c.},
$$

with the analogous down-sector chain. All three vertices have dimension four.
Eliminating the heavy messenger at tree level gives

$$
-\frac{y_Q^u y_Phi^u}{M_U}
\bar Q_L\widetilde H Phi_u u_R,
$$

and similarly for (d). Thus

$$
\frac{c_u}{Lambda_u}=-\frac{y_Q^u y_Phi^u}{M_U},
\qquad
\frac{c_d}{Lambda_d}=-\frac{y_Q^d y_Phi^d}{M_D}.
$$

The vectorlike pairs contribute equal and opposite cubic flavor anomalies in a
left-handed basis, so WP434's spectatorless cancellation is preserved rather
than repaired by a chiral spectator sector.

## What is now dynamical

The gauge bosons, adjoint flavons, and messenger fermions all have kinetic
terms and renormalizable interactions. Nonuniversal Yukawa matrices arise from
flavon vacuum expectation values through an exact heavy-messenger matching map.
This supplies a genuine dynamical-flavon UV grammar.

It does not yet select the vacuum. WP128 proves bounded quartic coercivity and
degree-eight matching, but not the complete coupled global minimum after gauge,
messenger, Higgs, and radiative terms are included. Nor are the dimensionless
couplings, messenger masses, or (g_F f/v) derived.

## Falsifiers and next gate

The smallest exact falsifiers are a dimension other than four for any UV
vertex, a nonzero net messenger anomaly, or failure of tree-level elimination
to reproduce the dimension-five portal coefficient. These all pass in the
declared grammar.

The next gate is the full vacuum: determine whether a source-authorized
renormalizable two-adjoint potential has a stable noncommuting minimum that
retains the rank-eight gauge mass Gram and produces the admitted Yukawa span,
without choosing its eigenvalues from the measured flavor answer.

Run `uv run --with sympy python
research/flavor/checkers/wp435_dynamical_flavon_messenger_completion.py` to
regenerate the JSON result.
