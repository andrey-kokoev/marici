---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 819 — The Generic Kato Root Is Not Horizontal in the A3 Lattice

## Gate

Entry 818 asks whether the generic rank-one Kato image is preserved by the
intrinsic \(A_3\) monodromy. If it is not, the rank-two vector-space quotient
cannot be promoted to a quotient local system.

Use the ordered \(A_3\) root basis with Cartan form

\[
C=
\begin{pmatrix}
2&-1&0\\
-1&2&-1\\
0&-1&2
\end{pmatrix}
\]

and Coxeter monodromy

\[
T=
\begin{pmatrix}
0&0&-1\\
1&0&-1\\
0&1&-1
\end{pmatrix}.
\]

## Norm obstruction

The only rational eigenvalue is \(-1\). Its eigenline is

\[
\ker(T+1)=\mathbb Q(1,0,1)^T.
\]

But

\[
(1,0,1)C(1,0,1)^T=4.
\]

A generic \(A_1\) vanishing cycle inside an \(A_3\) singularity is a root,
and every root has Cartan norm two. Exhausting the twelve \(A_3\) roots
shows that none lies in \(\ker(T+1)\). Therefore

\[
\boxed{\text{the generic Kato line is not horizontal}.}
\]

This conclusion does not depend on choosing which labelled root represents
the generic \(A_1\) cycle.

## Explicit defect

For the representative labelled root \(\alpha_1=(1,0,0)^T\),

\[
T\alpha_1=\alpha_2.
\]

The source \(A_1\) line has local monodromy \(-1\), so the intertwining
defect is

\[
\boxed{
T\,i(\alpha_1)-i(-\alpha_1)
=\alpha_1+\alpha_2.
}
\]

It is nonzero in vanishing cohomology. Consequently no strict rank-two
quotient local system exists. A chosen \((T^2+1)\)-plane would be an
unmotivated projector rather than the physical quotient.

## Required object

The correctly typed object is

\[
\operatorname{Cone}\!\left(
K_{\rm generic}\xrightarrow{i}V_{A_3}
\right),
\]

together with a source-derived monodromy homotopy whose boundary is the
displayed defect. Entry 817 supplies the correct associated-grade ranks but
not this homotopy. Because the defect is nonzero in the cohomology model, it
can only become a boundary in an enhanced thimble/perverse specialization
complex.

Thus the present outcome is:

\[
\boxed{
\text{strict horizontality: refuted;}
\qquad
\text{homotopy-coherent cone: required but unconstructed.}
}
\]

## Corrected global size

Entry 816 is authoritative:

\[
N_{A_3}=66,\qquad
\dim V_{A_3}=198,\qquad
\dim\operatorname{Cone}_{\rm red}=132,
\]

with cyclic character

\[
\chi_{C_3}=(132,0,0).
\]

The corrected checker and packet for Entry 817 now use this census.

## Meaning for H2

The existing carrier and associated-grade coefficient symbols still have
the right ranks. What fails is the stronger claim that the generic Kato
line admits a strict horizontal quotient. H2 now depends on whether the
predeclared nearby-cycle calculus supplies the required chain homotopy.
No new carrier stratum is indicated.

## Verification

- checker:
  research/benincasa/marici-gm/src/bin/a3_kato_horizontality_gate.rs;
- packet:
  research/benincasa/a3-kato-horizontality-gate.json;
- allocator claim seqclaim-1ada45d1d62361e94a28dcf1.

## Next falsifier

Construct the source-normalized \(A_3\) thimble complex from the original
\(i\epsilon\) prescription. Test whether \(\alpha_1+\alpha_2\) is the
boundary of its canonical mixed soft--signed coherence cell. If not, the
current nearby-cycle coefficient calculus fails at this corner.
