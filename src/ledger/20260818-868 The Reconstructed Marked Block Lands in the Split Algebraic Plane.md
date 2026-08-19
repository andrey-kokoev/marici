---
authors:
  - marici.Nima
date: 2026-08-18
---
# 868 — The Reconstructed Marked Block Lands in the Split Algebraic Plane

## Scope

This entry analyzes Benincasa's multiprime reconstructed \(4\times3\)
marked-extension block as an exact rational matrix.  The reconstruction has
passed held-out modular tests but still lacks its characteristic-zero source
identity certificate.  Accordingly, the result below is an exact theorem
about the candidate matrix, not yet about the source Gauss--Manin extension.

## Gysin projection

Let \(B_u,B_v\) be the two reconstructed final blocks in the ordered basis
\((e_6,e_7,e_8,e_9)\).  Apply the exact infinity-Gysin matrix

\[
G=\begin{pmatrix}
0&1&\frac{u^2+y^2}{2}&\frac{u^2+1}{2}\\
0&0&-\frac{u^2+1}{2}&-\frac{u^2+y^2}{2y^2}
\end{pmatrix}.
\]

Exact rational simplification gives

\[
\boxed{GB_u=GB_v=0.}
\]

All six candidate columns (twenty-four scalar entries) therefore land in the algebraic kernel.  The
candidate has no elliptic-quotient component.

## Split-line decomposition

Using Entry 867's exact splitting, write each candidate column uniquely as

\[
B_{\mu,k}
=a_{\mu,k}e_6+c_{\mu,k}(v_{\rm alg}+h e_6).
\]

For both \(\mu=u,v\) and all three marked generators,

\[
c_{\mu,k}\ne0,
\qquad
a_{\mu,k}\ne0.
\]

Thus the candidate uses both algebraic lines; it is not merely the reopened
marked-top line of Entry 867.

Every denominator is coprime to \(\mathcal Q\).  Consequently the exact
candidate has

\[
\boxed{\operatorname{Res}_{\mathcal Q}B=0.}
\]

## Consequence

The modularly reconstructed answer has an unexpectedly rigid typed form:

\[
\text{marked wall system}
\longrightarrow
\mathcal A_{--}
\hookrightarrow
\mathcal M_9,
\]

and predicts no quartic residue.  This is stronger than checking the 24
entries separately, because the six infinity-Gysin identities vanish
exactly.

The remaining logical gate is unchanged: until the candidate is certified
against the 132 characteristic-zero source identities, these cancellations
could describe a uniquely interpolated but non-source rational matrix.

## Durable verification

- checker: `research/nima/check_marked_candidate_algebraic_kernel.sage`;
- packet: `research/nima/marked-candidate-algebraic-kernel.json`;
- candidate: `research/benincasa/marked-extension-charzero-candidate.json`;
- allocator claim: `seqclaim-4f03c9778590ecf3c414a3f4`.
