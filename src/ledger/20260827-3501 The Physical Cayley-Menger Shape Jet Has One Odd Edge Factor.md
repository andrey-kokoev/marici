---
author: marici.Benincasa
date: 2026-08-27
---

# 3501 — The Physical Cayley–Menger Shape Jet Has One Odd Edge Factor

## Hard-to-vary claim

The exact physical second-shape jet of the labelled three-site
Cayley--Menger determinant is polynomial and exchange-equivariant. Its first
jet contains the unique antisymmetric edge factor \(a^2-b^2\); its second jet
is a nonzero symmetric polynomial.

## Frozen determinant

Use the source-labelled Cayley--Menger matrix

\[
\begin{pmatrix}
0&1&1&1&1\\
1&0&c^2&a^2&b^2\\
1&c^2&0&P_2^2&P_1^2\\
1&a^2&P_2^2&0&P_3^2\\
1&b^2&P_1^2&P_3^2&0
\end{pmatrix}
\]

and \(K=-\det(\mathrm{CM})/2\). Substitute

\[
P_1=1+t,\qquad P_2=1-t,\qquad P_3=1.
\]

Exact differentiation gives

\[
K_1=
2(a^2-b^2)(a^2+b^2-2c^2+1),
\]

and

\[
K_2=
2(a^4-2a^2b^2+7a^2+b^4+7b^2-2c^2-2).
\]

Under the labelled site exchange \(a\leftrightarrow b\),

\[
K_0\mapsto K_0,
\qquad K_1\mapsto-K_1,
\qquad K_2\mapsto K_2.
\]

All six determinant, degree, parity, factor, and nonvanishing checks pass.

## Consequence

The formal coefficients in Entry 3495 are now source-derived:

\[
k_1=K_1/K_0,
\qquad
k_2=K_2/K_0.
\]

No unidentified geometric jet remains. The second-shape insertion can now be
expanded entirely in the labelled rational relative basis. Its only new
denominator is an additional power of the already frozen Cayley--Menger
branch; no new carrier support appears.

## Next attack

Substitute these expressions into the six occurrence jets, clear the common
\(K_0^{5/2}\) twist denominator, and export each occurrence as a polynomial
numerator over the retained marked-wall powers. Then construct the
proper-face residue matrix.

## Evidence

- `research/benincasa/compile_physical_cm_shape_jet.py`;
- `research/benincasa/results/physical-cm-shape-jet.json`.

Allocator claim: `seqclaim-77a5f50726ecef669d63d9e5`.

