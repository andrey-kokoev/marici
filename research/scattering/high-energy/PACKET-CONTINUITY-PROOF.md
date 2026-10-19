# H5: exact continuity identity and verified downstream source binding

## Algebra, including residuals

On mass-carrying downstream coordinates let M be the positive diagonal mass matrix, H the retained Hermitian stiffness/native/contact matrix, and b the entrance forcing. Output trace coordinates are retained in H psi but have zero independent stored mass. They must not be invented as local occupations. Work at hbar=1 and allow a real common rotating-frame energy E_ref. Define

    r = i M psi_dot - [(H-E_ref M) psi - b].

For a strain slice j, with four incoherently mixed incident columns alpha, define

    P_j = (1/4) sum_alpha psi_j,alpha* M_j psi_j,alpha.

Taking its derivative gives the exact identity

    Pdot_j = (2/4) Im sum_alpha psi_j,alpha* (H psi-b+r)_j,alpha.

The real reference energy drops out. Terms within a slice cancel by Hermiticity. Nearest-strain couplings -a M_local/(Delta lambda)^2 give signed increasing-strain current

    J_(j+1/2) = (2a/(4 Delta lambda^2)) Im sum_alpha psi_j,alpha* M_local psi_(j+1),alpha.

The actual hinge quadrature weights and unweighted finite graph records must be used, not a uniform substitute. Entrance contributes 2 Im(b_port* y_port)/4, with the source trace map and its sqrt(s_star) normalization. The endpoint contact contributes minus 2 g_exit Im(eta_111* zeta)/4. Thus

    Pdot_j = J_entry,j - J_exit,j - (J_(j+1/2)-J_(j-1/2)) + delta_j,
    delta_j = (2/4) Im sum_alpha psi_j,alpha* r_j,alpha.

In particular

    |delta_j| <= (2/4) sum_alpha ||psi_j,alpha||_2 ||r_j,alpha||_2.

This uses Euclidean norms on the retained row equation; the physical mass is already present in r and P. An additional independently bounded arithmetic/compression error must be added when evaluating approximate stored arrays. A small observed residual is not itself a rigorous response-error certificate.

For exact solutions r=0, the H5 identity follows at every time. Finite spectral synthesis preserves the equation by linearity when the stationary equations and entrance/output traces are satisfied at every sampled energy. Products are formed **after** complex energy summation, retaining all cross-energy interference. Averaging over the four prepared columns is only performed after those products. No claim about their spanning the complete scattering matrix is needed.

Summing slices telescopes the internal current. Conditional strain means are only defined when total occupation is nonzero; they are separate readouts, not substitutes for the unconditioned identity.

## Source and computation boundaries

`check_packet_continuity.py` freshly reconstructs fields and derivatives at five declared times from stored complex spectral factors for the primary and refined **time-resolved 2.30-centred pilot**. It independently computes occupation derivatives, entry, exit and inter-slice currents, and the interior equation residual using the stored sparse operator. It also checks that the observed continuity defect equals the residual contribution, up to a declared floating arithmetic tolerance. No saved time-series pass flags are used.

These are numerical source-consistency checks, not exact proofs about floating arrays, new stationary solves, or continuum error bounds. The differential identity above is exact algebra; its numerical audit has a different evidential role.

## Resolution of the response128 binding gap

The previous pilot-only attempt left H5 open because the location of the response truncation had not been traced. Fresh inspection of the pinned `source_scripts/response_feedback.py` now identifies it: the Galerkin response extension changes the **entrance** approximation. Its resulting forcing is `b=ent.g*ent.S.conj().T@d['u']`; the complete retained downstream field is independently obtained as `down.diagnostic_field[:,:down.nport]@b`. No 128-direction projection is applied to the downstream strain slices covered by H5.

The continuity argument above holds for any such entrance forcing and its exact downstream solution. Thus an error in the approximate entrance forcing changes the downstream solution but does not introduce an omitted-direction term into these downstream equations. It does not validate the full entrance equation or eliminate the response-error obligations in H7/H8.

`check_response128_continuity.py` freshly evaluates **all 17** stored stationary downstream equations, including both outgoing boundary kernels, and reconstructs the moment-matched 3.30-centred four-column packet at five fixed times. It recomputes signed currents, interior derivatives and the residual contribution to continuity without trusting saved pass flags. Dropping the exit term fails its numerical countercontrol. These floating consistency tests use a declared 1e-8 tolerance; that tolerance is not a certified approximation-error bound.

**H5 is established as an identity of the exact specified downstream finite equations for all finite coherent spectral superpositions and all times.** The proof is algebraic, not an inference from five time samples. Rounded saved arrays satisfy the measured residual ledger rather than literal zero-residual equalities. The source-binding audits cover both the original pilot and later response128 fixture; no new stationary solve, full-space norm audit of the original half-line, continuum result or source-dynamics derivation is claimed.
