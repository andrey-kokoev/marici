# 1945 — The Five (D_4) Occurrences Assemble to a Nonzero Invariant Logarithm

## Question

Entry 1944 places the physical (D_4) singularity in the open stratum of the
frozen cyclic slice.  What is its local monodromy after retaining all five
occurrence labels, and does the cyclic scalar sum cancel the logarithm?

## Local labelled blocks

Entries 1878, 1881, and 1882 establish for every cyclic occurrence:

- an ordinary interior (A_1) fold;
- a nonzero source residue;
- Picard--Lefschetz intersection of absolute value one;
- a strict source-regulator pairing.

Hence each labelled local period has the form

\[
I_i(\tau)=c_i\log\tau+\text{holomorphic},
\qquad c_i\neq0,
\]

for a source-normalized transverse equation (	au=0) of (D_4).

Let (r_i) denote a regular lift and (v_i) its vanishing line.  The
nilpotent logarithm of monodromy is

\[
N(r_i)=v_i,qquad N(v_i)=0.
\]

In the ordered basis

\[
(r_0,\ldots,r_4,v_0,\ldots,v_4),
\]

the exact matrix is

\[
N=
\begin{pmatrix}
0&0\\
I_5&0
\end{pmatrix}.
\]

Therefore

\[
\boxed{\operatorname{rank}N=5,\qquad N^2=0.}
\]

## Cyclic assembly

Entry 1883 identifies the occurrence object as the regular representation

\[
\mathbb Q[C_5],
\]

with character ((5,0,0,0,0)).  Over (mathbb Q),

\[
\mathbb Q[C_5]
\simeq
\mathbb Q_{\rm triv}\oplus\mathbb Q(\zeta_5).
\]

The invariant regular lift obeys

\[
N\left(\sum_{i=0}^4r_i\right)
=
\sum_{i=0}^4v_i
\neq0.
\]

Cyclic transport preserves the common source-residue and regulator-pairing
orientation.  Consequently the five invariant coefficients add; they do not
cancel.

## Result

\[
\boxed{
\text{The cyclic scalar period retains a nonzero rank-one logarithmic
extension at }D_4=0.
}
\]

Before invariant projection the labelled monodromy has rank five.  The
selected scalar channel sees its one-dimensional trivial-character part.

This is local monodromy at the activated open root.  It does not construct a
global Picard--Fuchs operator or assert that every algebraic root of (D_4)
is physical.

## Architectural consequence

The full mechanism is now source-derived:

\[
\text{existing triple-wall incidence}
+\text{five labelled }A_1\text{ coefficient folds}
+\text{physical current}
\longrightarrow
\text{nonzero invariant logarithm}.
\]

No new carrier generator is required.

## Next falsifier

Compute the local scalar connection residue in the invariant channel and
verify that its unipotent monodromy agrees with the above integral
Picard--Lefschetz normalization.  Then test whether the four-dimensional
nontrivial (C_5)-character sector is visible in any occurrence-sensitive
observable or is killed by the scalar readout.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_d4_cyclic_monodromy.rs`
- `research/benincasa/results/five-site-d4-cyclic-monodromy.json`
- Entries 1878 and 1881--1883
- allocator claim: `seqclaim-8c1f1292a65f72b284a3ec5b`

