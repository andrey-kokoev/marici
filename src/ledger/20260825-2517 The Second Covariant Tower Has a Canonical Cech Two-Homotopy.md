---
author: marici.Benincasa
---

# 2517 — The Second Covariant Tower Has a Canonical Čech Two-Homotopy

## Claim

The six labelled second-normal covariant classes admit a canonical Čech total-cocycle packet. No choice of gradient-pivot chart survives in cohomology, and no new carrier divisor is required to glue the classes.

Let (p,q,r) be three localization charts. For each normal direction (i), let (D_i^p) be the first covariant lift on chart (p), and suppose

\[
D_i^p-D_i^q=[d,h_i^{pq}],
\qquad
h_i^{pq}=\iota_{V_i^p-V_i^q}.
\]

For the ordered second product (A_{ij}^p=D_i^pD_j^p), define

\[
H_{ij}^{pq}
=h_i^{pq}D_j^p+D_i^qh_j^{pq}.
\]

Then

\[
A_{ij}^p-A_{ij}^q=[d,H_{ij}^{pq}].
\]

On a triple overlap, (h_i^{pr}=h_i^{pq}+h_i^{qr}). The resulting Čech defect is itself exact:

\[
H_{ij}^{pq}+H_{ij}^{qr}-H_{ij}^{pr}
=[d,K_{ij}^{pqr}],
\qquad
K_{ij}^{pqr}=h_i^{qr}h_j^{pq}.
\]

Thus every labelled second class is represented by the total cocycle

\[
\boxed{(A_{ij}^p,H_{ij}^{pq},K_{ij}^{pqr})}.
\]

For three charts and the six symmetric labels

\[
(11),(22),(33),(12),(13),(23),
\]

the packet contains exactly (18) pairwise homotopies and (6) triple two-homotopies.

## Verification

`research/benincasa/checkers/check_second_covariant_cech_homotopy.py` verifies the finite cell census and the two formal graded-commutator identities. Its machine-readable packet is `research/benincasa/results/second-covariant-cech-homotopy.json`.

Epistemic graph admission: `ev-000000003490-2846ca6a-200f-4784-84e7-897ff5556bde`.

## Narrow consequence

Entries 2513 and 2515 established existing-support closure and pivot independence. This entry supplies the previously missing overlap coherence. The second-normal tower is therefore typed as a support-sensitive Čech/de Rham total object rather than as six single-chart rational fractions.

This does **not** yet identify its direct image in the generic lower rank-(34) module. The next finite falsifier is to construct a source-wall-only total-complex reducer for these cocycles. Feeding gradient-pivot denominators into the ordinary lower-sector reducer would confuse a computational chart with intrinsic source support and is prohibited.

## Classification

\[
\boxed{
\text{existing energy/marked carrier}
+\text{canonical higher coherence}
+\text{sector-specific coefficient transport}
}
\]

No new cosmological carrier datum is detected.

Allocator claim: `seqclaim-2ffc4ebf020e74f3fff74761`.
