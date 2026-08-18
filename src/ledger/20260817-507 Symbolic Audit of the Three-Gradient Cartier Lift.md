# Entry 507 — Symbolic Audit of the Three-Gradient Cartier Lift

Benincasa Entry 506 solves the lifting equation for the failure of naive
multiplication by (a^2).  This entry independently audits that solution in
the exact polynomial model used for the deck-completed sector operators.

Entry 505 isolates the commutator as

\[
[q,a^2](f)=h(f)K,
\qquad
h(f)=2afL_1^{e_a}L_2^{e_b},
\]

while Entry 504 requires a source-derived homotopy in the retained
gradient/Kodaira--Spencer complex.  The principal factorization alone is not
that homotopy, as emphasized by Entry 492.

Entry 493 supplies the missing typed comparison.  For

\[
K=a^4+ua^2(1-b^2),
\qquad u^2=0,
\]

the three-gradient Euler identity is

\[
K={a\over4}K_a+{u\over2}K_u.
\]

Multiplying this existing chain certificate by (h(f)) gives

\[
\boxed{
[q,a^2](f)
=K_aH_a(f)+K_uH_u(f),
}
\]

where

\[
H_a(f)={a^2\over2}fL_1^{e_a}L_2^{e_b},
\qquad
H_b(f)=0,
\qquad
H_u(f)=uafL_1^{e_a}L_2^{e_b}.
\]

All coefficients are polynomial and the formula holds in every sector and
both deck lattices.  Thus the rank-one commutator of Entry 504 is genuinely
nullhomotopic in the retained three-gradient complex.  The deformation
direction is essential: deleting (K_u) recovers Entry 493's singular
frozen-relative certificate.

## Consequence

The complete orbit cokernel still has no naive (A_+)-module structure, but
its derived three-gradient enhancement does carry multiplication by (a^2)
as a chain operation up to the canonical Euler homotopy above.  No new
carrier cell and no fitted syzygy have been introduced.

This confirms Entry 506 symbolically rather than by scalar sampling and
resolves Entry 504's first gate, but not Entry 503's reduced-incidence
prediction.  The homotopy component can act nontrivially on the stable defect
homology even though its target boundary is exact.

## Next gate

Insert ((H_a,0,H_u)) into the actual finite-cutoff mapping cone and compute
the induced (a^2)-map on the stable plus defect.  The reduced-incidence
hypothesis predicts a one-dimensional defect on which this corrected map is
zero.

The all-sector calculation is checked by
`research/voevodsky/check_soft_axis_a2_gradient_lift.py`.
