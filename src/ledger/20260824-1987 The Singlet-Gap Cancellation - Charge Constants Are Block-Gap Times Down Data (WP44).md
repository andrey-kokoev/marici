---
author: marici.Figueiredo
---

# 1987 - The Singlet-Gap Cancellation: Charge Constants Are Block-Gap Times Down Data (WP44)

WP43 reduced the three anchor constants to exact chart ratios
C = Du Dd (CKM monomial)/(scale^2 M) and left the closed form of the WP36
magnitude function M as the open item. WP44 derives M on a large exact family
and finds the up-singlet cancels out of the constants entirely.

## The M anatomy (exact)

On every sheet whose down sector, in the up-canonical frame (up singlet
permuted to index 0, block swap allowed), has Hd_01 = 0, the WP36 commutator
form collapses (G1, max 2.3e-11 over 394 sheets):

  M = |Hd_02|^2 |Hd_12| |chi_block(s)|,
  chi_block(s) = (s - lam_b1)(s - lam_b2) = c^2 - (s - a)(s - b),

the up-block characteristic polynomial evaluated at the singlet. Derivation:
with u = Hd_01 = 0, WP36's C1 = -cv, C2 = v(s-b) are real multiples of v and
det[Hu,Hd]/(2i c sin(phi)) = |v|^2 (Im w/sin phi) [c^2 - (s-a)(s-b)].

Family coverage: u 128/232, c 202/424, t 64/192 sheets.

## The cancellation (exact)

chi_block(s) carries precisely the two singlet-to-block eigenvalue gaps, so
Du/chi_block(s) = (block gap) identically. The constants lose all up-singlet
content (G2, max 2.4e-14):

  C_anchor = (block gap) * Dd * (CKM monomial) / (scale^2 |Hd_02|^2 |Hd_12|)

one universal law; the class enters only through (scale, CKM monomial, block
gap). Evaluated, it reproduces the WP40-42 values exactly:
C_u = 0.9993729706, C_c = 1.0008814042, C_t = 0.9920333163.
This answers Nima's WP40-41 question: the constants are images of ONE law,
not class-specific coefficients.

## Closed-form readout on the family

The down eigenvectors have exact profiles (G3, max 1.1e-11)
  v(lambda) ~ (Hd_02/(lambda - Hd_00), Hd_12/(lambda - Hd_11), 1),
so on this family the entire CKM readout is closed-form chart algebra given
the eigenvalues: the constants are explicit chart-algebraic numbers, no
fitting. For unique-matching down graphs det Hd is the squared matching
product (G4, n = 394, max 5.3e-14) - the WP5/WP14 matching-determinant link
holds on the family.

## Boundary (negative, certified)

The family boundary is real: on the 104 complement u-sheets (Hd_01 != 0),
no universal quadratic M/chiB = Q(|Hd_01|,|Hd_02|,|Hd_12|, Re cross terms)
exists - global 6-basis lstsq leaves a 6.2e-3 max residual (G5). The
complement's M is the general WP36 polynomial, per-texture chart algebra.
Combined with WP39's off-locus drift, the constants are thereby certified
POINT VALUES determined by the physical flavor point through exact chart
algebra, not universal numbers and not simple physical monomials. This
closes the evaluation question WP43 left open: the derivation is complete
(closed form + evaluation); the values carry no further unidentified factor.

Certificate: checkers/wp44_singlet_cancellation.py ->
results/wp44_singlet_cancellation.json (5/5 gates).
