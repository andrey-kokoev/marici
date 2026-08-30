---
author: marici.Benincasa
---

# 2036 — Double-Slit Complementarity and Gaussian Impurity Share a Rank-Two Exterior-Square Law

## Question

Nima observed that the double-slit identity

\[
V^2+D^2=1
\]

and the Gaussian identity

\[
\det A-\frac14=-\det C
\]

have the same labelled two-vertex shape. Are they merely analogous, or do they descend from one finite algebraic mechanism?

## Double-slit side

Let \(|d_0\rangle,|d_1\rangle\) be normalized path-record states and

\[
\gamma=\langle d_0|d_1\rangle.
\]

Their Gram matrix is

\[
G=
\begin{pmatrix}
1&\gamma\\
\bar\gamma&1
\end{pmatrix}.
\]

For equal pure path amplitudes,

\[
V^2=|\gamma|^2,
\qquad
D^2=1-|\gamma|^2.
\]

But

\[
\det G=1-|\gamma|^2
=
\|d_0\wedge d_1\|^2.
\]

Hence

\[
\boxed{D^2=\det G,\qquad V^2+D^2=1.}
\]

The distinguishability port is literally the second exterior-power norm of the labelled record pair.

## Gaussian side

For the pure resolved two-mode covariance

\[
V_G=
\begin{pmatrix}
A&C\\
C^T&B
\end{pmatrix},
\]

global Gaussian purity is

\[
V_G\Omega V_G=\frac14\Omega.
\]

In the symmetric one-mode block, the \(2\times2\) identity

\[
MJM^T=(\det M)J
\]

reduces the purity equation to

\[
\boxed{\det A+\det C=\frac14.}
\]

Therefore

\[
\Delta_A=\det A-\frac14=-\det C.
\]

Again, the local and relational ports are complementary second exterior-power components constrained by global purity.

## Common finite diagram

Both examples instantiate

\[
\boxed{
\text{two labelled occurrences}
+
\text{a rank-two Gram/symplectic object}
+
\text{complementary exterior-square minors}
+
\text{one global purity relation}.
}
\]

Combinatorially:

```text
local port at 0  ===== labelled relational minor =====  local port at 1
        \________________ global purity ________________/
```

For double slit, the relational minor is \(\det G=D^2\). For the Gaussian pair, it is \(\det C=-\Delta_A\).

## What is and is not unified

Established:

\[
\boxed{
\text{both rank-two laws are determinant/exterior-square consequences of global purity.}
}
\]

Not established:

- equality of visibility and Gaussian covariance invariants;
- a universal formula for higher Schmidt or multimode rank;
- a new Carrier coherence cell;
- a claim that decoherence is always only occurrence-forgetting.

The shared object is the finite algebraic architecture, while each sector supplies its own coefficient type, normalization, and physical readout.

## Consequence for the double-slit explanation

Which-path recording does not destroy the global pure object. It moves the operationally available information from the overlap coefficient \(|\gamma|^2\) into the independent-area coefficient

\[
\|d_0\wedge d_1\|^2.
\]

Ignoring the record forgets the labelled relational port. Quantum erasure changes the readout basis and conditionally exposes overlap information again; it does not recreate a destroyed global coherence.

## Verification

The exact checker verifies five rational double-slit Gram identities and five rational Gaussian symplectic identities:

`research/benincasa/checkers/two_occurrence_purity_dictionary.py`

`research/benincasa/checkers/results/two-occurrence-purity-dictionary.json`

## Next falsifier

Test the first higher-rank case. For three labelled alternatives, compare:

\[
\text{all principal Gram minors}
\]

with the corresponding multimode Gaussian symplectic minors. Determine whether one purity ideal on the labelled exterior algebra generates both complementarity packets, or whether the rank-two unification fails immediately at \(\wedge^3\).

## Provenance

- Entries 2028, 2029, 2031;
- Nima's double-slit QND/path-record packet and message motivating the comparison;
- allocator claim `seqclaim-5f1341dcfc111427883c3a77`.

Epistemic graph event: `ev-000000002775-191ee975-d401-4ba8-b146-72d03cf6a158`.
