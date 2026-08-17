---
id: 393
date: 2026-08-17
title: The Beck-Chevalley Coefficient Square Closes Strictly
---

# The Beck-Chevalley Coefficient Square Closes Strictly

Entry 392 reduced the one-road realization to the Beck--Chevalley comparison
between the generic first-Rees map and the closed logarithmic residue. On the
minimal normal--Čech coefficient enhancement, that comparison has no
obstruction.

The already forced coefficients are
\[
 k=x_3,\qquad a=-\frac{X_{D03}}{u_{D03}}.
\]
The normal--Čech incidence equation is
\[
 x_3a+\frac{X_{D03}}{u_{D03}}k=0.
\]
Substitution gives the strict identity
\[
 -\frac{x_3X_{D03}}{u_{D03}}
 +\frac{x_3X_{D03}}{u_{D03}}=0.
\]
Both terms have the same fine multidegree, and the sign is the fixed
cohomological localization-triangle sign. No integer, occurrence variable,
normal parameter, or Rees parameter is inverted to obtain the cancellation.

Independently, the log-expanded geometric path has the unique primitive
occurrence syzygy
\[
 C_{\log}=X_1E_{13}+X_{D03}E_{D3},
\]
with its middle boundary cancelled and endpoint boundary
\[
 dC_{\log}=X_{D03}X_0c-X_1X_5v_+.
\]
Thus the carrier coefficient and orientation are also fixed rather than
fitted.

## What this proves

There is no coefficient-level Beck--Chevalley obstruction. If the expanded
path is tensored with the standard \(x_3\) normal--Čech interval and mapped
using the already proved generic and lower coefficients, its critical square
commutes strictly.

This does not yet construct the geometric two-cell. The expanded-path audit
constructs a relative log carrier inside the marked pentagon, whereas the
generic \(q_{03}^{Q}\) state belongs to the absolute quotient \(F_2/F_1\).
No checked-in morphism attaches the \(x_3\) normal--Čech factor of that
relative carrier to the absolute \(Q\)-generator and simultaneously to the
target localization triangle.

Therefore the remaining datum is exactly one support attachment:
\[
 (C_{\log}\otimes K_{\check C}(x_3))_{\rm top}
 \longrightarrow q_{03}^{Q},
\]
with its closed face equal to the logarithmic Cartier unit. Once this
attachment is constructed, the strict identity above supplies its
Beck--Chevalley compatibility automatically; Entry 388 then supplies
uniqueness and reflection compatibility.

Connector existence remains open, but it is no longer obstructed at the
coefficient, sign, degree, endpoint, or parity levels.

The executable audit is
research/voevodsky/check_d03_beck_chevalley_coefficient_gate.py.
