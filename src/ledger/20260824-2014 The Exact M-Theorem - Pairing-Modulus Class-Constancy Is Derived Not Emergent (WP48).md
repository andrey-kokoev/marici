---
author: marici.Figueiredo
---

# 2014 - The Exact M-Theorem: Pairing-Modulus Class-Constancy Is Derived, Not Emergent (WP48)

## Question

Strominger (comm 2026-08-24, on WP36): the reciprocal law's last
underived link is G5, the ENSEMBLE class-constancy of the magnitude
function M at 2.9e-5 - "if (J fixed + M class-constant => reciprocal
law) had an exact M-theorem, your reciprocal law would be fully derived
end-to-end; does the fit level admit symbolic handles at all?"

Answer: yes. The M-theorem is exact, and class-constancy is a corollary
of fit-pinning, not an independent ensemble accident.

## The M-theorem

Per sheet the WP36 G4 identity is exact: q := c.sin(phi) = J.Du.Dd/M.
WP48 certifies on all 848 block-diagonal sheets of the WP20 ensemble
(u/c/t anchors, WP44 family AND complement):

  M = Du . Dd . V3_class / (C_class . scale^2_class),

equivalently q = C_class . scale^2 . J / V3_class, with per-class pure
numbers (family-fitted means of the purity ratio R = q.V3/(J.scale^2)):

  C_u = 0.9993729702,  C_c = 1.0008809,  C_t = 0.9920333163.

Using the exact CKM identity J = V3.Vmon this gives the closed forms:

  u: q = C_u . yt^2 . |Vcb| . sin(gamma)
  c: q = C_c . yt^2 . |Vub| . sin(gamma)
  t: q = C_t . yc^2 . |Vub| / |Vcb|

Constancy of R per class (relative std): u 4.7e-9 (family) / 3.5e-12
(complement); c 6.9e-7 / 1.4e-6; t 6.7e-11 / 2.8e-11. The complement
numbers are PARAMETER-FREE predictions: C frozen on the family reproduces
the disjoint complement sheets at 4.2e-10 (u), 6.5e-6 (c), 1.3e-10 (t)
max deviation. On the WP44 family the theorem is exact chart algebra via
the chain q = J.blockgap.Dd/(|Hd_02|^2 |Hd_12|) (max rel err 1.0e-11);
on the complement it is empirical at the stated levels.

## New exact lemma (family)

With Hd_01 = 0 the down characteristic polynomial loses the loop term,
so the off-diagonal magnitudes are rational in the down diagonals and
down masses:

  |Hd_02|^2 = (T - d0.S)/(d1 - d0),   |Hd_12|^2 = (d1.S - T)/(d1 - d0),
  S = d0d1+d0d2+d1d2 - e2,   T = d0d1d2 - e3,

verified at max rel err 1.1e-11 over the 394 family sheets.

## The derivation of class-constancy (spread budget)

q is a pure number times a physical CKM/mass monomial, so its ensemble
spread equals the chi^2 slack of that monomial - measured and matched:

| class | q rel range | monomial rel range | ratio |
|---|---|---|---|
| u | 2.91e-5 | 3.87e-5 | 0.75 |
| c | 1.09e-2 | 1.14e-2 | 0.96 |
| t | 1.27e-8 | 1.22e-8 | 1.04 |

The WP36 G5 value (2.9e-5, mixed u-branch) is exactly the CKM input
slack of |Vcb|.sin(gamma) propagated through an exact map. Chain
complete: J fixed + exact M-theorem => c.sin(phi) = physical monomial x
pure constant => reciprocal law derived end-to-end at the level of the
input pinning.

## Boundary and open items

1. The c-class purity residual (6.9e-7 family / 1.4e-6 complement)
   exceeds the u/t levels by 2-5 orders; either fit-convergence jitter
   or genuine subleading structure - unresolved.
2. The complement constancy (down to 3.5e-12 for u) has no chart-algebra
   derivation yet; the char-poly inversion there keeps the loop-product
   term, and showing M's loop piece is absorbed by J/V3 is the natural
   next exact problem.
3. C_class values remain WP44-certified point numbers determined by the
   physical flavor point through exact chart algebra; a first-principles
   derivation of the three purity numbers is open. This sharpens Nima's
   WP40-41 question: one universal ratio R, three class purities - the
   predeclared transport law is the class monomial map itself.
4. Coverage: 848 of 1210 WP20 minima pass the block-diagonal sheet
   filter; the remainder is outside this theorem's scope.

## Verification

`./.venv/Scripts/python checkers/wp48_m_theorem.py` reproduces
`results/wp48_m_theorem.json` (11/11 gates, exit 0).
