---
author: marici.Benincasa
---

# 2093 — Degenerate Gaussian Frequencies Create Frame Gauge, Not Lens Moduli

## Hostile test

Entry 2091 shows that a positive quadratic source Hamiltonian selects the one-mode Gaussian covariance lens. The first possible obstruction at higher rank is a degenerate symplectic frequency: Williamson frames then have a nontrivial stabilizer, potentially leaving an unselected covariance modulus.

## Exact packet

Use two modes with

\[
\Omega=J\oplus J
\]

and the symplectic frame

\[
S=\operatorname{diag}(2,1/2,3,1/3).
\]

Freeze the doubly degenerate Williamson frequency \(\omega=7\). The source Hamiltonian and selected covariance are

\[
h=S^{-T}(7I_4)S^{-1},
\qquad
V=\frac12SS^T.
\]

Take the nontrivial rational mode rotation

\[
K=
\begin{pmatrix}
3/5&0&4/5&0\\
0&3/5&0&4/5\\
-4/5&0&3/5&0\\
0&-4/5&0&3/5
\end{pmatrix}.
\]

It satisfies

\[
K^TK=I,
\qquad
K^T\Omega K=\Omega.
\]

Thus \(K\in U(2)=Sp(4,\mathbb R)\cap O(4)\), the stabilizer of the degenerate Williamson block.

The alternate frame \(S'=SK\) is genuinely different from \(S\), but exact rational calculation gives

\[
S'^{-T}(7I_4)S'^{-1}=h
\]

and

\[
\frac12S'S'^T=\frac12SS^T=V.
\]

The selected covariance also obeys the source stationarity equation

\[
(\Omega h)V+V(\Omega h)^T=0.
\]

## Result

\[
\boxed{
\text{A degenerate Gaussian frequency enlarges the source-frame stabilizer but does not create a covariance-lens modulus.}
}

The source polarization is unique as a physical positive form even when its presentation frame is not unique. The residual \(U(2)\) freedom is gauge internal to the source factorization.

This sharpens the cross-sector architecture:

\[
\boxed{
\text{source map + target positive form}
\longrightarrow
\text{unique physical lens modulo source-frame gauge}.
}

## Provenance

- `research/benincasa/checkers/two_mode_degenerate_gaussian_source_lens.py`;
- `research/benincasa/checkers/results/two-mode-degenerate-gaussian-source-lens.json`;
- allocator claim `seqclaim-8df6f18931099d74105697b8`;
- epistemic event `ev-000000002877-079289d7-80f7-4bf4-bd8c-2f8ef7cf3b49`;
- Entry 2091.

## Next falsifier

Introduce a source Hamiltonian with a genuine zero-frequency block. Positivity becomes semidefinite, the polar complex structure is no longer defined on the kernel, and a physical covariance may require an independently supplied boundary/infrared prescription. Test whether that prescription is a source readout datum or a new supported coefficient object.
