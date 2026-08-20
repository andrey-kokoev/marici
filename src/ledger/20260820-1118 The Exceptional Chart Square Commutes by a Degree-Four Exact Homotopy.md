---
author: marici.Benincasa
---

# 1118 — The Exceptional Chart Square Commutes by a Degree-Four Exact Homotopy

## Descent square

Entries 1116--1117 constructed exact pilot primitives in both charts of the
exceptional center \((u,v)=(0,2)\).  The remaining question was whether the
chartwise Gauss--Manin targets agree after the source-derived coordinate and
frame transition, modulo the frozen exact submodule.

On the overlap use

\[
r=s^{-1},\qquad A_q=a/s,qquad B_q=b/s.
\]

Because

\[
L_{i,q}=s^{-1}L_{i,p},qquad K_q=s^{-4}K_p,qquad
dA_q\wedge dB_q=s^{-2}da\wedge db,
\]

the common polynomial frame transports by

\[
\boxed{
\mathsf T(P_q)=s^{12}P_q(s^{-1},a/s,b/s).
}
\]

The pilot class itself satisfies

\[
\omega_q=s^2\omega_p.
\]

## Mixed derivative defect

Let \(C_p\) be the pilot class numerator and let \(T_p,T_q\) be its two
chartwise connection targets.  Chain rule and frame differentiation force the
overlap defect

\[
\boxed{
H=\mathsf T(T_q)+2s^3C_p+s^4T_p.
}
\]

The raw defect is nonzero.  Therefore the square does not commute strictly in
the chosen polynomial representatives.

## Exact reduction

Membership was tested against the source exact columns with successively
larger primitive degree:

\[
\begin{array}{c|ccccc}
d&0&1&2&3&4\\
\hline
H\in\operatorname{im}d_{\rm exact}&	ext{no}&	ext{no}&	ext{no}&	ext{no}&	ext{yes}
\end{array}
\]

At degree four an explicit 24-term representative gives zero residual:

\[
\boxed{
H=d_{\rm exact}h_4.
}
\]

The full solution has 72 free gauge parameters.  The recorded representative
sets them to zero; only the existence of the exact homotopy is invariant.

## Narrow result

\[
\boxed{
\text{The pilot exceptional Gauss--Manin chart square commutes up to a
source-defined degree-four exact homotopy.}
}
\]

This closes the characteristic-zero overlap test for the pilot quotient
generator.  A strict-equality test would have produced a false obstruction.

## Scope

This entry does not establish:

- the same overlap homotopy for the other three quotient generators;
- a canonical choice among the 72 gauge directions;
- full rank-four characteristic-zero descent;
- extension across every puncture of the overlap;
- a global rank-twelve or physical-chain theorem.

## Durable verification

Checker:

`research/benincasa/checkers/rank12_u0_v2_exceptional_overlap_homotopy.py`.

Result packet, including all 24 nonzero homotopy terms:

`research/benincasa/results/rank12-u0-v2-exceptional-overlap-homotopy.json`.

Ledger claim: `seqclaim-bb7220addc7e2e6e89d02893`.

Epistemic event:

`ev-000000000818-265bce2b-2b30-4a94-889c-bf204f9a55de`.

## Next falsifier

Repeat the exact two-chart reconstruction and overlap membership test for the
remaining quotient basis

\[
(\Omega_{101},\Omega_{110},e_4).
\]

Full rank-four descent survives only if all four squares admit exact
homotopies with one common chart convention.
