# Prior-research clue audit for the based determinant assignment

## Question

What existing source constructions constrain the missing assignment

\[
\kappa_G:Q_a\longmapsto K_{G,a},
\qquad
K_{G,a+b}=K_{G,a}\star K_{S_aG,b},
\]

and do any of them already construct it?

## Bold conjecture tested

The most economical conjecture is that one existing operator family can simultaneously realize the moving endpoint cocycle, the primitive and square Euler currents, the connected third-determinant tail, reciprocal transport, and the signed ratio-window faces.

The audit rejects this conjecture in its single ordinary-operator form. Prior research instead points to a three-stratum relative determinant packet with a based groupoid action and a two-sided linking block.

## Source-derived clues

### Endpoint groupoid cocycle

The endpoint increment

\[
b_G(a)=G(a)-G(0)
\]

obeys

\[
b_G(a+b)=b_G(a)+b_{S_aG}(b).
\]

It is a cocycle on the translation action groupoid. It is not a cyclic trace on the coefficient-sensitive crossed product. This supplies the based primitive line and explains why an unbased operator assignment loses interval provenance.

Source: `endpoint-incidence-requires-a-groupoid-cocycle-beyond-a-bare-translation-trace.md`.

### Prime-loop Euler operator

In the Euler domain, the diagonal return

\[
L(s)e_p=p^{-s}e_p
\]

satisfies

\[
\operatorname{Tr}L(s)^k=\sum_pp^{-ks}
\]

and generates the primitive, square, and connected Euler coefficients from one operator. This is the correct common Euler operator there.

It does not extend as one ordinary trace-class operator to the critical strip: the primitive grade becomes distributional, while square and connected grades have different completion types.

Source: `the-common-euler-operator-is-the-prime-loop-return-not-the-positive-incidence-gram.md`.

### Valuation-chain Stein attachment

The source intertwiner `J_p`, weighted shift `A_p`, and moving-window observer `B_p` satisfy

\[
G_p-A_p^*G_pA_p=B_p^*B_p.
\]

This gives the exact based boundary attachment and transported-window composition law. The source Gram is noncoercive and cannot be substituted for the linear Euler return: its coefficients are squared and it forgets ordered phase.

Sources: `the-missing-sewing-object-is-a-local-recollement-and-a-global-stratified-boundary.md` and `the-valuation-chain-Stein-identity-is-the-source-derived-seam-attachment-before-determinant-sewing.md`.

### Normalized determinant character

For an already constructed relative operator assignment, the third-determinant anomaly is an exact trace-class two-cocycle. Low-grade normalization strictifies it to a one-dimensional character. Hence determinant coherence after assignment is solved; it does not produce the assignment.

Sources: `determinant-line-is-a-normalized-hopf-module.md` and `the-third-determinant-multiplicative-anomaly-is-a-trace-class-coherence-cell.md`.

### Mellin--Poisson dual section

The theta Mellin--Poisson functional sews primitive, square, connected, seam, endpoint, and archimedean lines to the scalar Xi section. It establishes scalar provenance. Because the section vanishes, it is divisor-bearing dual data, not an invertible trivialization or a reverse construction of the operator packet.

Source: `the-theta-mellin-poisson-functional-is-the-source-trivialization-of-the-three-stratum-determinant-line.md`, with its recorded correction.

### Two-sided linking requirement

A triangular incidence graph has determinant independent of its off-diagonal source map. A determinant sensitive to the analytic--arithmetic relation must use a reciprocal block

\[
T_X=
\begin{pmatrix}
A_{+,X}&M_X\\
N_X&A_{-,X}
\end{pmatrix}
\]

with source-derived forward and reverse links. Their pairing ideals must be Morita-full with a noncollapsing margin. Neither link may be fitted after scalarization.

Source: `the-complete-finite-rh-operator-must-be-a-two-sided-linking-block.md`.

### Ambient connection without source compression

The labelled Mellin connection is flat and source-derived. The source-selected Riesz projection needed to compress it to a defect bundle is absent. Pointwise equalizer matrices and ambient parallel transport do not select that projection.

Source: `the-ambient-mellin-connection-exists-but-the-source-riesz-compression-does-not.md`.

## Named rivals and falsifiers

1. **Positive incidence Gram as common operator.** Fails because its trace has squared coefficients rather than linear Euler coefficients.
2. **Bare translation trace.** Fails cyclicity once endpoint coefficient multiplication is retained.
3. **Scalar analytic continuation of the Euler determinant.** Continues a readout, not an operator or trace-ideal packet.
4. **Triangular incidence block.** Its determinant erases the off-diagonal source map.
5. **One-way linking block.** Its determinant still factorizes; reciprocal interaction is absent.
6. **Low-moment reconstruction.** Exact equal-trace/equal-square hostiles have unequal connected determinants.
7. **Universal Fourier interval operator.** It is source-blind and fails cutoff-uniform Douglas domination for the moving-window row.
8. **Riesz compression chosen from zeros.** It derives source geometry backward from the desired divisor.

## Analytic form of the obstruction

The obstruction is not a missing scalar formula. It is the incompatibility of three source requirements on one ordinary operator carrier:

- endpoint incidence is a noncyclic, state-based translation-groupoid cocycle;
- Euler multiplicities are powers of a linear ordered return;
- critical-strip completion separates primitive distributional, square Hilbert, and connected determinant-class grades.

A single Schatten operator cannot carry all three with the required provenance. The smallest surviving target is therefore a based three-stratum relative determinant object whose connected grade admits `det_3`, together with a reciprocal two-sided linking block and the retained endpoint groupoid cocycle.

## First missing typed object

Prior work does not construct the forward and reciprocal links

\[
M_X:E_{-,X}\to E_{+,X},
\qquad
N_X:E_{+,X}\to E_{-,X}
\]

on the full tail--seam--primitive--square--connected carrier. Equivalently, the relative-trace/determinant comparison morphism

\[
\Theta_{\rm tr}:\mathcal A_{\rm trans}\to\mathcal S_3
\]

remains absent.

Acceptance requires, before determinant evaluation:

1. the based translation composition law;
2. primitive and square trace identities;
3. the connected third-determinant coordinate of the same packet;
4. reciprocal exchange of the two links;
5. signed ratio-face anomaly compatibility;
6. finite Morita fullness and a declared completion margin.

## Disposition

The search finds strong constraints and rejects the single-operator conjecture. It does not find a hidden construction of `kappa_G`, `Theta_tr`, or the reciprocal linking pair. The branch remains blocked at that source morphism. The surviving clue is a retyping: seek a based three-stratum relative linking object, not an ordinary common Schatten operator.