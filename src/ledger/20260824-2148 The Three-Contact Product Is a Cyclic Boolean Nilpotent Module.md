---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2148 — The Three-Contact Product Is a Cyclic Boolean Nilpotent Module

## Hard-to-vary claim

The all-deleted three-contact coefficient object has an intrinsic rank-eight
nilpotent module whose graded dimensions are

\[
\boxed{1,3,3,1.}
\]

This reproduces the Boolean deletion cube's dimension vector inside one
source-defined coefficient object, without supplying morphisms between the
eight deletion sectors.

## Tensor logarithmic system

Let

\[
\tau_i=(2\pi i)^{-1}\log\nu_i.
\]

The product of three contact systems has basis

\[
\tau_S=\prod_{i\in S}\tau_i,
\qquad
S\subseteq\{1,2,3\}.
\]

The labelled variation \(N_i=T_i-I\) acts by

\[
N_i\tau_S=
\begin{cases}
\tau_{S\setminus\{i\}},&i\in S,\\
0,&i\notin S.
\end{cases}
\]

Therefore

\[
N_i^2=0,
\qquad
[N_i,N_j]=0.
\]

By monomial degree, the module has Hilbert vector

\[
\binom30,\binom31,\binom32,\binom33
=(1,3,3,1).
\]

Moreover, the top class \(\tau_1\tau_2\tau_3\) is cyclic: applying every
labelled subset of the \(N_i\) produces each of the eight basis vectors once.

## Relation to the deletion carrier

The same vector

\[
1\to3\to3\to1
\]

labels the edge-deletion cube of Entry 2112. The match is source-derived on
both sides:

- deletion subsets label Carrier sectors;
- logarithmic monomials label coefficient grades;
- variation removes one labelled logarithm just as deletion removes one
  labelled occurrence.

But Entry 2113 remains in force. Equal Boolean indexing and dimensions do not
construct coefficient arrows between distinct deletion sectors. The present
module lives at the all-deleted contact-product vertex.

## Narrow conclusion

\[
\boxed{
\text{the correlator Carrier cube and contact coefficient module share one
labelled Boolean algebra, but at different categorical levels.}
}
\]

This is stronger than a rank coincidence and weaker than a totalized
Gauss--Manin deletion complex. It identifies a canonical local model for the
coefficient algebra that any future deletion comparison must preserve.

## Evidence

- Entries 2112--2113 and 2143--2147;
- `research/benincasa/checkers/three_contact_boolean_nilpotent.rs`;
- allocator claim `seqclaim-240ecc5a79be473915a6d14c`.

## Next falsifier

Test one actual adjacent deletion map against this Boolean module. A valid
map must preserve the occurrence label and intertwine deletion with the
corresponding variation \(N_i\). If no source-derived map exists, retain the
Boolean match as a local coefficient model only.
