---
author: marici.Figueiredo
---

# 1986 — The Constants Are Exact Chart Ratios (WP43)

WP40-42 left three unidentified pure numbers (C_u = 0.9993729706,
C_c = 1.0008814042, C_t = 0.9920333163), each certified to carry no physical
refit-gradient. WP43 reduces them to exact ratios of chart expressions, so the
mystery is now a single concrete chart function.

## The reduction chain

Two exact identities, each machine-verified per sheet:

1. Quartic uniqueness (G5, 1.3e-10): on any fitted sheet,
   J = |Vud Vub Vcd Vcb| sin(gamma), hence
     y_t^2 |Vcb| sin(gamma) = y_t^2 J / (|Vud Vub Vcd|),
     y_t^2 |Vub| sin(gamma) = y_t^2 J / (|Vud Vcd Vcb|).
2. WP36 J-routing (exact): J Du Dd = c sin(phi) M(mags), q = c sin(phi),
   so q = J Du Dd / M.

Eliminating J gives per-sheet exact ratios (G1-G3, errors 3e-11 / 1.3e-10 /
1.3e-12):

  C_u = Du Dd |Vud Vub Vcd| / (y_t^2 M_u)
  C_c = Du Dd |Vud Vcd Vcb| / (y_t^2 M_c)
  C_t = Du Dd |Vud Vcd Vcb^2| sin(gamma) / (y_c^2 M_t)

with Du, Dd the eigenvalue-gap products of Hu, Hd and M the WP36
magnitude-only chart function.

## Decomposition

u-class: Dd and M each fluctuate 6.7e-3 across the ensemble, but Dd/M is
constant at 3.8e-5 (G4) - the fit pins their ratio, not the factors. Also
Du/(y_t^4 y_c^2) = 0.9999825 = 1 - 1.75e-5, exactly the mass-gap correction
(1 - yc^2/yt^2)(1 - yu^2/yt^2)(1 - yu^2/yc^2). c-class: the Dd/M ratio
wanders 1.5e-2 (its 6.3e-6 residual territory). t-class: frozen at 1e-8.

## What remains

The three constants are now one object: the exact chart function M(mags)/Dd
evaluated at the physical point (times known mass-gap and CKM-magnitude
factors). M has the WP36 closed form

  M = Im(w)/sin(phi) (|C1|^2 - |C2|^2) - Im(C1 C12 conj(C2))/(c sin(phi))

with C1 = u(s-a) - cv, C2 = v(s-b) - cu, C12 = w(a-b) + c(Hd22 - Hd11);
every Im is first-harmonic, so M is magnitude-rational. Simplifying M/Dd
symbolically - and thereby evaluating 0.9993729706, 1.0008814042, 0.9920333163
from first principles - is WP44.

Certificate: checkers/wp43_constants_reduced.py -> results/wp43_constants_reduced.json (5/5 gates).
