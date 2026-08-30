# Reducing-Subspace Threshold Survival Theorem

## Question

What exact source condition carries WP859's normalized dark state and complete
two-port instrument through a heavy threshold without attenuation?

## Full unitary dilation

Split the threshold Hilbert space into the declared two-port sector (L) and
heavy complement (H). Write the source-unitary matching map as

\[
W=
\begin{pmatrix}
A&B\\
C&D
\end{pmatrix}:
L\oplus H\longrightarrow L\oplus H.
\]

Unitarity gives

\[
A^*A+C^*C=I_L.
\]

Therefore the compressed light map (A) is an isometry exactly when

\[
C=0.
\]

Because (A) is square and then unitary, the remaining unitary identities
also force (B=0). Hence exact threshold survival is equivalent to (L)
being a reducing subspace of the full matching unitary:

\[
[W,P_L]=0.
\]

This is both necessary and sufficient. No small-mixing approximation can
replace it when the claim is exact numerical survival.

## Covariant transport of the complete packet

When the condition holds, the internal light block (A) may still be a
nontrivial unitary frame change. The selected state and both detector rows
must be transported together:

\[
d'=Ad,
\qquad
M'=MA^*,
\qquad
D'=DA^*.
\]

Then

\[
M'd'=Md=0,
\qquad
D'd'=Dd.
\]

The full two-port matrix remains unitary. This is simultaneous source/readout
parallelization, not an assertion that coordinates remain literally
unchanged.

## Smallest finite-mixing hostile

Mix only the first light port with one heavy state using the exact unitary
rotation

\[
W_*=
\begin{pmatrix}
3/4&0&-\sqrt7/4\\
0&1&0\\
\sqrt7/4&0&3/4
\end{pmatrix}.
\]

Its compressed light block is

\[
A_*=
\operatorname{diag}(3/4,1).
\]

Applied to the WP859 dark vector, it produces unequal component magnitudes
and norm (5/(4\sqrt2)). The projective ray, normalized magnitude, and
difference-port amplitude all change. The defect is exactly

\[
I-A_*^*A_*=C_*^*C_*
=\operatorname{diag}(7/16,0).
\]

Thus a full unitary ultraviolet threshold can still induce a non-isometric
low-energy compression. Ambient unitarity is not enough.

## Source symmetry required

The reducing property is source-authorized if (P_L) is a superselection
projector in the complete microscopic interaction algebra. Commutation with
one fitted mass matrix is too weak; every admitted threshold interaction must
preserve the projector. Heavy states carrying the same source quantum numbers
can reopen mixing even when a charge label appears compatible.

The minimal threshold theorem is therefore:

1. a source-derived projector (P_L) identifies the complete two-port packet;
2. (P_L) commutes with the full threshold interaction algebra;
3. matching transports the state and both readout rows functorially;
4. detector calibration is performed after this common-frame transport.

## Classification

Exact conditional threshold-survival theorem. It closes the algebraic
threshold gate for WP859 if the two-port sector is a source-protected reducing
subspace. No current flavor construction proves that superselection property.
The smallest falsifier is the single-heavy-mode rotation (W_*).

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp860_reducing_subspace_threshold_survival_theorem.py
```
