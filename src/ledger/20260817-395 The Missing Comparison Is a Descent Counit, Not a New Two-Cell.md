---
id: 395
date: 2026-08-17
title: The Missing Comparison Is a Descent Counit, Not a New Two-Cell
---

# The Missing Comparison Is a Descent Counit, Not a New Two-Cell

Entry 394 separated the correct first absolute incidence from its zero literal
second transgression. Comparing that incidence with the weighted expanded path
now fixes the only integral scaling under which a chain comparison can exist.

The \(E_{D3}\) component of the literal absolute boundary has coefficient
\(X_3\), while the same component of
\[
 C_{\log}=X_1E_{13}+X_{D03}E_{D3}
\]
has coefficient \(X_{D03}\). Thus coefficients \(s,t\) on the generic and
expanded sides must satisfy
\[
 sX_3=tX_{D03}.
\]
Over the polynomial occurrence ring, without inversion, its unique primitive
monomial solution is
\[
 s=X_{D03},\qquad t=X_3.
\]
All other monomial solutions are common multiples of this one.

This is precisely the scaling already discovered independently in the
blown-up barycentric Morse carrier. There the corrected generic lift
\(q_J^{\rm abs}\), the lcm-weighted special carrier
\(\widetilde\xi^{\rm abs}\), and the seven-triangle thimble satisfy
\[
 dH_{\rm Morse}^{\rm abs}
   =q_J^{\rm abs}-x_3\widetilde\xi^{\rm abs}.
\]
The lcm construction of \(\widetilde\xi\) contains the forced
\(X_{D03}\)-weighted \(E_{D3}\) sector and the complementary
\(X_1\)-weighted sector that reaches the marked endpoint. Therefore
\(H_{\rm Morse}\) is already the required comparison homotopy on the
log-blown-up barycentric carrier. No further coefficient and no further
upstairs two-cell are missing.

## What remains

The identity above lives after pulling the absolute cellular cosheaf to the
blown-up barycentric face poset. The checked blowdown construction supplies
that pullback functor, but it does not supply a counit or proper pushforward
which:

1. sends the corrected generic lift \(q_J\) to the ambient
   \(q_{03}^{Q}\) derived class;
2. sends the expanded carrier to the nonzero \(F_0\) endpoint class;
3. carries the Morse homotopy to the ambient support-filtration Hom complex.

This explains both previous observations without contradiction. Upstairs,
the exceptional/logarithmic gallery permits the cross-support homotopy.
Downstairs, the literal \(D03\)-supported inclusion has zero second
transgression. The missing operation is exactly the descent counit that
remembers the exceptional contribution when contracting the log expansion.

The next test is therefore categorical but finite: construct the cellular
left Kan extension (proper pushforward) along the blowdown poset map on the
marked carrier, compute its counit on \(q_J\), \(\widetilde\xi\), and
\(H_{\rm Morse}\), and test whether the resulting ambient class is the
canonical support-filtration Yoneda class. A failure would be a genuine
descent obstruction; success would establish connector existence.

The executable coefficient audit is
research/voevodsky/check_d03_lcm_comparison_descent_gate.py.
