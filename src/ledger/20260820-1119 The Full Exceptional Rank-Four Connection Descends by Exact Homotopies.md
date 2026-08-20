---
author: marici.Benincasa
---

# 1119 — The Full Exceptional Rank-Four Connection Descends by Exact Homotopies

## Extension of Entry 1118

Entry 1118 established overlap coherence for the pilot generator
\(\Omega_{111}\).  The same source-derived transport has now been applied to
the complete exceptional quotient basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_4).
\]

No chartwise primitive or transition was refitted per generator.

## Forced frame weights

The source forms determine the overlap weights

\[
\boxed{
(w_{111},w_{101},w_{110},w_{e_4})=(2,1,1,-1).
}
\]

For a generator of weight \(w\), the common-frame defect is

\[
H_w=mathsf T(T_q)+w s^{w+1}C_p+s^{w+2}T_p,
\]

where

\[
\mathsf T(P_q)=s^{12}P_q(s^{-1},a/s,b/s).
\]

Every \(H_w\) is nonzero before exact reduction.

## Degree-filtered exact closure

The first exact homotopy degree and one sparse representative size are

\[
\boxed{
\begin{array}{c|c|c|c}
\text{generator}&w&d_{\min}&\#\operatorname{supp}h\\
\hline
\Omega_{111}&2&4&24\\
\Omega_{101}&1&5&25\\
\Omega_{110}&1&4&28\\
e_4&-1&6&32
\end{array}}
\]

For every row,

\[
H_w=d_{\rm exact}h_w
\]

with exact zero residual over \(\mathbb Q(s)[a,b]\).

## Hard-to-vary conclusion

\[
\boxed{
\text{The complete exceptional rank-four Gauss--Manin target descends across
the two Rees charts in the frozen exact complex.}
}
\]

The descent is derived rather than strict.  The varying minimal degrees are
coefficient data; they do not require additional carrier cells.

This supplies the characteristic-zero overlap mechanism missing from Entry
1098.  It also confirms the H2 pattern at this exceptional center:

\[
\boxed{
\text{unchanged weighted carrier and exact calculus}
+\text{ nonuniform rank-four coefficient homotopies}.}
\]

## Scope

This entry establishes connection-target overlap coherence.  It does not yet
establish:

- a canonical primitive representative for each homotopy;
- integral-lattice normalization;
- extension through all four denominator punctures;
- compatibility with the physical relative integration chain;
- global rank-twelve characteristic-zero descent away from this center.

## Durable verification

Checker:

`research/benincasa/checkers/rank12_u0_v2_exceptional_overlap_homotopy.py`.

Result packet containing every exact homotopy coefficient:

`research/benincasa/results/rank12-u0-v2-exceptional-overlap-homotopy.json`.

Ledger claim: `seqclaim-434a70ca4a65cfd894642937`.

Epistemic event:

`ev-000000000820-661be8a0-b853-42be-8646-7c6312f2c60a`.

## Next falsifier

Audit extension across the denominator divisor

\[
s(s-1)(s^2+6s+1)=0.
\]

Compute the local residues and specialization of all four descended
homotopies at each component.  A residual supported cone there would be
coefficient support on an existing divisor; failure requiring an undeclared
incidence would reopen the carrier question.
