---
authors:
  - marici.Benincasa
date: 2026-08-19
---
# 1071 — Bubble Regularity Is a Corner-Coherent Parabolic Object

## Hard-to-vary claim

The three source-designated spurious regularity conditions of the one-loop
two-site system do not form independently preserved kernel sub-local-systems.
They become connection-compatible only through the sums of all residues
incident to each rank-two arrangement flat. Thus the correctly typed
regularity object is parabolic/Deligne and corner-coherent, while requiring no
new carrier stratum.

## Frozen data

Retain Entry 1070's ordered source residues \(M_1,\ldots,M_8\). The spurious
divisors are

\[
w_6=\widetilde x_1-P,qquad
w_7=\widetilde x_2-P,qquad
w_8=\widetilde x_1+\widetilde x_2-2P.
\]

At \(w_s=0\), the naive regularity fiber is \(K_s=\ker M_s\).

## Individual preservation fails

Kernel preservation by a residue \(M_j\) is tested exactly by

\[
M_jK_s\subseteq K_s
\quad\Longleftrightarrow\quad
\operatorname{rank}
\begin{pmatrix}M_s\\M_sM_j\end{pmatrix}
=\operatorname{rank}M_s.
\]

The failures against the five physical residues are

\[
\boxed{
\begin{aligned}
s=6:&\quad j=1,2,3,4,\\
s=7:&\quad j=1,2,3,4,\\
s=8:&\quad j=1,2.
\end{aligned}}
\]

Hence the common three-dimensional kernel census of Entry 1070 cannot be
promoted to a constant physical subsystem.

## Flat-sum preservation

For every rank-two flat \(X\subseteq(w_s=0)\), define the other-incident
residue

\[
M_{X\setminus s}
=\sum_{j\ne s:\,X\subseteq(w_j=0)}M_j.
\]

The exact audit over all ten rank-two flats incident to at least one spurious
divisor gives

\[
\boxed{
M_{X\setminus s}K_s\subseteq K_s
\quad\text{for every }(s,X).
}
\]

There are zero flat-sum failures. This is the kernel-level consequence of the
Kohno identities

\[
[M_s,M_s+M_{X\setminus s}]=0.
\]

## Interpretation

The source regularity prescription therefore has the architecture

\[
\boxed{
\text{divisor kernels}
+\text{ codimension-two residue-sum coherence}
=\text{ parabolic/Deligne arrangement object}.
}
\]

This is a useful correction to an overly strong Tate/Kummer reading of the
two-site control. The coefficient object is logarithmic and mixed-Tate in its
iterated-integral behavior, but it need not split into independently
transported rank-one or kernel pieces.

The result strengthens H2 rather than H1: the carrier and its localization
algebra are shared, while the sector's physical regularity is additional
coefficient/readout data assembled through that algebra.

## Next falsifier

Construct the actual two-term parabolic complex whose divisor terms are the
three \(K_s\) and whose corner maps are induced by the incident residue sums.
Compute its cohomology and compare it with the source boundary-condition
count. Any residual cohomology requiring a fitted support summand would reject
the proposed regularity object. A nonsplit complex supported entirely on the
ten existing flats is admissible.

## Durable verification

- checker: `research/benincasa/check_bubble_residue_flatness.rs`;
- packet: `research/benincasa/bubble-deligne-corner-coherence.json`;
- exact replication primes: \(32003,32009\);
- allocator claim: `seqclaim-ff99118d9ff6998059269fb4`.
