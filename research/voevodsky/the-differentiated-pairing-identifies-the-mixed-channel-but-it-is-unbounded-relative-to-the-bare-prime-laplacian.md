# The differentiated pairing identifies the mixed channel, but it is unbounded relative to the bare prime Laplacian

## Source-derived mixed channel

The missing gamma--prime/endpoint coupling is not arbitrary. Let

\[
J_{loc,Q}(t)
=
J_\infty(t)
\prod_{q\in Q}J_q(t)
\]

be the completed dual/canonical pairing phase. Its metric connection is

\[
V_{loc,Q}(t)
=
\frac1{2i}
\partial_t
\log J_{loc,Q}(t).
\]

Differentiation of the preserved pairing gives

\[
B_{J_{loc,Q}}((D+V_{loc,Q})f,g)
+
B_{J_{loc,Q}}(f,(D+V_{loc,Q})g)
=0.
\]

After contour displacement, the Green boundary is the completed endpoint swap form. In the Clifford presentation, ordered composition of the local rotor and endpoint boost forces the mixed bivector

\[
B_{23}.
\]

Thus the signed mixed channel is already source-derived. It is the bounded augmented Green block

\[
\mathbb G_Q
=
\begin{pmatrix}
\mathcal A_Q&B_Q^*\\
B_Q&J_{end}
\end{pmatrix}
\]

on the phase-energy plus endpoint graph carrier.

## Question

Can this mixed channel serve as a bounded cross operator for the bare positive prime Laplacian feature

\[
\Phi_Qm
=
\bigoplus_{q\in Q}
\sqrt{a_q/2}
(I-U_{\ell_q})m?
\]

A bounded lift would require the connection row to be controlled by the Laplacian energy.

## Prime-Laplacian symbol

The Gram of \(\Phi_Q\) is multiplication by

\[
\lambda_Q(t)
=
\sum_{q\in Q}
a_q
(1-
\cos(t\ell_q)).
\]

At the aligned point \(t=0\),

\[
\lambda_Q(0)=0.
\]

Taylor expansion gives

\[
\lambda_Q(t)
=
\frac{t^2}{2}
\sum_{q\in Q}
a_q\ell_q^2
+O(t^4).
\]

Hence the bare edge energy loses two orders at the common prime resonance.

## Pairing-connection symbol

The finite-prime component of the differentiated pairing is

\[
V_Q(t)
=
\sum_{q\in Q}
a_q
\cos(t\ell_q)
\]

with the global sign fixed by orientation. At the aligned point,

\[
V_Q(0)=A_Q,
\qquad
A_Q=
\sum_{q\in Q}a_q>0.
\]

Thus the source-derived current does not vanish where the bare prime Laplacian vanishes.

## Bounded-lift obstruction

Suppose the connection form extended boundedly to the prime-edge completion. Then there would be a constant \(C_Q\) such that

\[
|\langle m,V_Qm\rangle|
\le
C_Q
\langle m,L_Qm\rangle
\]

on the source core. Localization makes the necessary pointwise estimate

\[
|V_Q(t)|
\le
C_Q\lambda_Q(t).
\]

Near \(t=0\), the left side tends to \(A_Q\) while the right side is \(O(t^2)\). No finite \(C_Q\) exists.

Equivalently,

\[
\lambda_Q(t)^{-1/2}V_Q(t)
\sim
\frac{A_Q}
{|t|}
\left(
\frac{2}
{\sum_q a_q\ell_q^2}
\right)^{1/2},
\]

which is unbounded.

Therefore the differentiated pairing channel does not define a bounded cross operator on the bare prime-Laplacian completion.

## Localized witness

Choose normalized real-boundary packets supported increasingly close to \(t=0\). Then

\[
\langle m_\varepsilon,
L_Qm_\varepsilon\rangle
\to0,
\]

while

\[
\langle m_\varepsilon,
V_Qm_\varepsilon\rangle
\to A_Q.
\]

Multiplication by \(z^2+1/4\) can additionally annihilate both endpoint evaluations without changing localization at zero. Hence endpoint graph augmentation alone does not repair the loss of control.

## Meaning of the existing bounded Green block

The augmented Green coupling is bounded on the phase-energy carrier because its norm includes

\[
e_Q(t)
=
1+
\kappa_{loc,Q}(t),
\]

and the phase-energy theorem gives

\[
|V_{loc,Q}(t)|
\le
C_Qe_Q(t).
\]

This positive baseline remains nonzero at aligned resonances. It is essential.

Thus the source-derived mixed channel is bounded only after replacing the bare prime edge norm by the completed phase-energy graph norm.

## Correct enlarged carrier

The minimal viable positive source carrier must retain both rows:

\[
\widetilde\Phi_Qm
=
\begin{pmatrix}
M_{e_Q^{1/2}}m\\
\Phi_Qm
\end{pmatrix}.
\]

Its Gram is

\[
\widetilde L_Q
=
M_{e_Q}
+
L_Q.
\]

On this carrier, the connection and endpoint Green rows are bounded. The signed completed form is a bounded readout of the enlarged positive feature.

However, boundedness is not contractivity. Positivity of the required Schur complement remains equivalent to the augmented horn gate.

## Tetrahedral interpretation

The bare \(H_{234}\) prime-edge feature does not contain enough metric at the aligned resonance to receive the \(H_{134}\) Green coupling.

The common tetrahedral bulk must include the phase-energy/reference row shared by both faces. This explains why common-bulk removal must occur only after the mixed Green channel is attached.

Orthogonally removing the baseline before coupling destroys boundedness of the positive comparison.

## Outcome

The cross-channel search has two answers:

1. the signed source-derived cross channel is the differentiated dual/canonical pairing, equivalently the forced Clifford \(B_{23}\) Green component;
2. it cannot be represented as a bounded cross operator over the bare prime translation Laplacian.

The next viable operator is the Schur complement on the enlarged phase-energy plus prime-edge plus endpoint graph carrier.

## Remaining gate

Let \(X_Q\) denote the bounded Green row on the enlarged carrier. The exact remaining test is

\[
\begin{pmatrix}
\widetilde L_Q&X_Q^*\\
X_Q&G_{end,Q}
\end{pmatrix}
\succeq0.
\]

Equivalently, after restricting to the positive support of \(\widetilde L_Q\),

\[
X_Q
\widetilde L_Q^{\dagger}
X_Q^*
\preceq
G_{end,Q}.
\]

This is the same augmented Schur--Douglas gate in its source-derived common-bulk coordinates. No additional unspecified cross operator remains.

## Disposition

The mixed channel has been identified, but the bare prime-Laplacian path is too small. The phase-energy baseline is forced by boundedness at aligned prime resonances.
