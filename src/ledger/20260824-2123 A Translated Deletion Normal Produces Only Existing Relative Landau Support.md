# 2123 — A Translated Deletion Normal Produces Only Existing Relative Landau Support

## Hard-to-vary claim

The relative Landau tangency between one source-translated deletion normal and the three-site Cayley--Menger boundary produces only existing total-energy, soft, and external-triangle support. It produces no quartic factor.

## Frozen system

Take the labelled deleted edge `12` and set

\[
E_T+2y_{12}=0,
\qquad
A=y_{12}^2=\frac{E_T^2}{4}.
\]

Write

\[
B=y_{23}^2,
\qquad
C=y_{31}^2,
\qquad
p_i=P_i^2.
\]

Let `K(A,B,C;p_1,p_2,p_3)` be the frozen five-by-five Cayley--Menger determinant. Away from the coordinate-soft endpoints `B C=0`, generic tangency to the fixed-`A` hyperplane is governed by

\[
K=0,
\qquad
\partial_BK=0,
\qquad
\partial_CK=0.
\]

## Exact elimination

Symbolica elimination of `B,C` gives

\[
\boxed{
\operatorname{Elim}_{B,C}
(K,K_B,K_C)
=
-128E_T^2p_1^2
\Lambda(p_1,p_2,p_3)^3,
}
\]

where

\[
\Lambda(p_1,p_2,p_3)
=p_1^2+p_2^2+p_3^2
-2p_1p_2-2p_2p_3-2p_3p_1.
\]

Thus the support is

\[
E_T=0,
\qquad
P_1=0,
\qquad
\Lambda(P_1^2,P_2^2,P_3^2)=0.
\]

The cyclic images give the corresponding labelled soft factors for deletion of `23` and `31`.

## Verification

The exact Rust/Symbolica checker is

`research/benincasa/marici-gm/src/bin/three_site_deletion_landau.rs`.

It constructs the Cayley--Menger determinant from the frozen distance matrix, differentiates before elimination, and computes the two-stage Sylvester resultants exactly.

## Classification

\[
\boxed{
\text{translated deletion normal}
+
\text{Cayley--Menger tangency}
\longrightarrow
\text{existing energy/soft/triangle carrier only}.
}
\]

No new carrier divisor and no \(\mathcal Q\)-like coefficient support occurs in this one-deletion relative Landau sector.

## Scope

This closes the generic tangency for one deleted edge and its cyclic images. It does not yet close:

- simultaneous tangency involving two or three translated normals;
- coordinate-soft endpoint components excluded by the generic `BC nonzero` typing;
- marked denominator collisions beyond the Cayley--Menger boundary;
- physical relative-cycle activation after analytic continuation.

## Next falsifier

Test the first genuinely multi-port locus using two translated normals, for example

\[
E_T+2y_{12}=0,
\qquad
E_T+2y_{23}=0,
\]

together with the Cayley--Menger boundary and the correctly reduced tangency equations. Saturate coordinate-soft components before interpreting the elimination. A surviving factor must be classified against existing support before comparison with any successor quartic.

