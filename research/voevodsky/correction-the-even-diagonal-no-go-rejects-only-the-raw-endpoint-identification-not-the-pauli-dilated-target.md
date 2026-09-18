# Correction: the even-diagonal no-go rejects only the raw endpoint identification, not the Pauli-dilated target

> **Superseded:** this distinction applies only to the lossy summed frame operator. The full Pauli linking Gram is faithful and retracts to the raw Gram, so the diagonal no-go propagates to the full fixed-frame comparison. See `correction-faithful-pauli-dilation-cannot-repair-the-raw-diagonal-mismatch.md`.

## Scope correction

The inequality

\[
G_{p,11}^{\rm win}<1\le H_{p,11}^\theta
\]

is correct for the raw Gaussian Stieltjes window Gram versus the normalized theta endpoint column. It rejects their direct identification.

However, prior source work already rejects raw endpoint Gram equivalence and replaces it by a typed two-output Pauli dilation. Therefore the no-go does not falsify the latest quadratic target.

## Correct source observer

Let

\[
G_p^{\rm win}
=\begin{pmatrix}a_p&z_p\\\bar z_p&b_p\end{pmatrix},
\qquad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
Y=\begin{pmatrix}0&i\\-i&0\end{pmatrix}.
\]

Retain the two outputs separately:

\[
\mathcal O_pv=(J_pXv,J_pYv).
\]

Its frame operator is

\[
\mathcal O_p^*\mathcal O_p
=XG_p^{\rm win}X+YG_p^{\rm win}Y
=2\begin{pmatrix}b_p&0\\0&a_p\end{pmatrix}.
\]

The raw cross-correlation cancels in total energy, while the separate \(X\) and \(Y\) outputs retain orientation.

## Correct comparison type

The live map is not the raw

\[
Q_p^{\rm lin}:\mathbb C^2\to H_\theta.
\]

It is a typed extension

\[
\widetilde Q_p:
\operatorname{ran}\mathcal O_p
\longrightarrow
H_{\theta,+}\oplus H_{\theta,-}
\]

that preserves both Pauli outputs before any codiagonalization. Its quadratic target is

\[
\langle\mathcal O_px,\mathcal O_py\rangle
=
\langle\widetilde Q_p\mathcal O_px,
\widetilde Q_p\mathcal O_py\rangle_\theta,
\]

or an independently sourced uniform form comparison.

The raw inequality does not compare these two forms and therefore cannot reject this square.

## Prime-two diagnostic

The existing scout gives

\[
a_2\approx0.6374050022,
\qquad
b_2\approx0.9735711763,
\qquad
z_2\approx0.7748099375.
\]

The dilated frame diagonal is consequently

\[
2\operatorname{diag}(b_2,a_2)
\approx
\operatorname{diag}(1.9471423527,1.2748100044),
\]

not the raw \(a_2\) tested by the no-go. This illustrates the type change; it is not a validated certificate for the dilated comparison.

## Remaining gate

The following are still missing:

1. a source-derived definition of \(\widetilde Q_p\) on both typed Pauli outputs;
2. the complete target Green matrices on those two outputs;
3. preservation of their ordered off-diagonal/linking blocks;
4. cutoff-natural and prime-uniform completion;
5. proof that no terminal codiagonal erases the distinction.

## Corrected disposition

- Direct raw-window-to-normalized-theta identification: **falsified**.
- Pauli-dilated two-output comparison: **open and not tested by that falsifier**.

This distinction must be retained in every later Evans/G4 claim.
