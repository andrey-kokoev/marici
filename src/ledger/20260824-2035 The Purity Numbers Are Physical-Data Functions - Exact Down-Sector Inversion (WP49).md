---
author: marici.Figueiredo
---

# 2035 - The Purity Numbers Are Physical-Data Functions: Exact Down-Sector Inversion (WP49)

## Question

WP48 closed the M-theorem M = Du.Dd.V3/(C_class.scale^2) but left the
three purity numbers C_u = 0.9993729702, C_c = 1.0008809,
C_t = 0.9920333163 as unidentified ensemble constants (WP48 open item
3). Nima's WP40-41 instruction was explicit: cherish the unidentified
constants until they are derived. WP49 derives them.

## The inversion: down sector from physical inputs only

On the WP44 family (Hd_01 = 0), the down Hermitian sector inverts
EXACTLY and RATIONALLY from physical data alone - the down masses
lam_j and the singlet CKM row moduli u_j = |V_ckm[k,j]|^2 at the
eigen-sorted singlet position k (u -> 0, c -> 1, t -> 2):

  d0   = sum_j u_j lam_j                        (spectral diagonal)
  beta = e3 . sum_j u_j / lam_j                 ((0,0) minor / resolvent)
  d1   = (beta.d0 - e3)/(e1'.d0 - e2 + beta)    (linear in d1: the cubic
                                                  terms cancel exactly)
  d2   = e1' - d1
  v^2  = p(d0)/(d1 - d0),   w^2 = p(d1)/(d0 - d1),
  p(x) = prod_j (x - lam_j),  e1' = e1 - d0

where (d0, d1, d2, v^2, w^2) are the chart entries Hd = [[d0, 0, *],
[0, d1, *], [*, *, d2]], v^2 = |Hd_02|^2, w^2 = |Hd_12|^2 of the family
presentation. The formulas are rational: no square roots, no fitting,
no chart data beyond the physical invariants on the right-hand side.

## Consequence: C_class is an explicit function of physical data

Substituting into the WP48 purity definition,

  C_class = blockgap . Dd . V3 / (scale^2 . v^2 . sqrt(w^2)),

every factor is now physical: blockgap and scale^2 are up-sector mass
data, Dd and the v^2, w^2 above are down masses plus CKM row moduli,
V3 is a CKM modulus product. The purities are no longer unidentified
numbers - they are evaluations of an explicit algebraic function F of
the physical flavor point.

Certification (all 394 family sheets, machine precision):

| class | max rel err (d0,d1,d2,v2,w2) | max rel err C |
|---|---|---|
| u | 7.3e-13 | 1.4e-14 |
| c | 1.2e-11 | 1.7e-13 |
| t | 4.9e-13 | 2.3e-13 |

Cross-frame consistency: the exact-frame singlet row (first basis
vector e_0) and the eigh eigen-sorted singlet row give identical d0 to
2.4e-13. The one implementation trap is the row index: the singlet CKM
row sits at the eigen-SORTED position k, not at its flavor index; a
flavor-index lookup silently reads the wrong row on permuted sheets.

## Measured-point evaluation

F evaluated at the measured flavor point (OBS17 central values)
reproduces the WP48 fitted constants within fit slack:

| class | C (measured point) | C (WP48 fitted) | deviation |
|---|---|---|---|
| u | 0.9993900742 | 0.9993729702 | 1.7e-5 |
| c | 1.0008845110 | 1.0008809 | 3.3e-6 |
| t | 0.9914853279 | 0.9920333163 | 5.5e-4 |

The deviations track the chi^2 slack of the physical inputs (the
t-class monomial |Vub|/|Vcb| is the slack-sensitive one). The c-class
deviation 3.3e-6 sits at the scale of the WP48 c-purity residual
(1.4e-6), indicating that residual is fit offset, not structure -
this tentatively settles WP48 open item 1.

## Boundary and open items

1. The linear d1 formula assumes the family (Hd_01 = 0). The
   complement-family inversion retains the loop-product term; deriving
   it is the natural continuation and would close WP48 open item 2.
2. The purities are NOT simple CKM monomials - the WP44 negative
   control stands. F is an honest algebraic function (spectral sums
   and resolvent minors), not a monomial.
3. Why F evaluates within 1e-2 of 1 for all three anchors is NOT
   explained by this derivation. That near-unity question is the new
   residue, stated openly.
4. The measured-point evaluation computes the FAMILY-presentation value
   of F at the measured point; family presentations of the physical
   point exist (the fitted sheets), so this is legitimate, but a
   complement-only point would need item 1 first.

## Verification

`./.venv/Scripts/python checkers/wp49_purity_derivation.py` reproduces
`results/wp49_purity_derivation.json` (10/10 gates, exit 0).
