# Time-band concentration gives a nonnegative local Weil tail

## Question

Can one prove existence of a finite trial space whose orthogonal complement has nonnegative local Weil form, without assuming that Dirichlet modes sharply localize Fourier frequency?

## Claim boundary

Yes, for each fixed support window, assuming the established source-sector bounds. Use the spectral subspaces of the compact time--band concentration operator rather than Dirichlet modes. Eventual positivity of the gamma multiplier, compactness of low-frequency concentration, the absolute prime bound, and inclusion of endpoint representers produce a finite-codimensional nonnegative tail. This does not give an effective mode count or close the off-diagonal Schur gate.

## Source bounds

Fix \(L>0\). Write the local form as

\[
Q_L=\Gamma_L+P_L+E_L.
\]

Let \(m(u)\) be the real gamma multiplier, including its constant normalization. For a frequency threshold \(R\), define

\[
m_R=\inf_{|u|>R}m(u),
\qquad
C_{\rm low}(R)=\max\left(0,-\inf_{|u|\leq R}m(u)\right).
\]

The digamma asymptotic gives

\[
m_R\longrightarrow+\infty.
\]

The fixed-support prime form obeys

\[
|P_L(f,f)|
\leq
C_{\rm prime}(L)\lVert f\rVert_2^2.
\]

## Concentration operator

Let \(J_L\) extend a function on \((-L,L)\) by zero, and let \(\Pi_R\) be Fourier projection onto \([-R,R]\). Define

\[
T_{L,R}
=
J_L^*\mathcal F^{-1}\Pi_R\mathcal FJ_L.
\]

This positive compact operator measures low-frequency concentration. Let its eigenvalues be

\[
1>\lambda_1\geq\lambda_2\geq\cdots\longrightarrow0.
\]

If \(f\) is orthogonal to its first \(M\) eigenvectors, then

\[
\lVert\Pi_R\widehat f\rVert_2^2
\leq
\lambda_{M+1}(L,R)\lVert f\rVert_2^2.
\]

## Signed tail estimate

Split the gamma integral into low and high frequency. For such \(f\),

\[
\Gamma_L(f,f)
\geq
\left[
 m_R-(m_R+C_{\rm low}(R))\lambda_{M+1}(L,R)
\right]
\lVert f\rVert_2^2.
\]

Therefore

\[
(\Gamma_L+P_L)(f,f)
\geq
\left[
 m_R-(m_R+C_{\rm low}(R))\lambda_{M+1}(L,R)
 -C_{\rm prime}(L)
\right]
\lVert f\rVert_2^2.
\]

Choose \(R\) so that

\[
m_R>C_{\rm prime}(L),
\]

then choose \(M\) so that

\[
\lambda_{M+1}(L,R)
\leq
\frac{m_R-C_{\rm prime}(L)}{m_R+C_{\rm low}(R)}.
\]

Compactness of \(T_{L,R}\) guarantees that such a finite \(M\) exists.

## Endpoint removal from the tail

The endpoint form is finite rank. Adjoin all endpoint Riesz representers to the finite trial space. On its orthogonal complement,

\[
E_L(f,f)=0.
\]

Thus the full tail block satisfies

\[
C_M\geq0.
\]

## Why this repairs the Dirichlet obstruction

High Dirichlet index alone does not directly prove small low-frequency Fourier mass. The concentration eigenbasis measures exactly that mass, so no unsupported frequency-localization inference is needed.

## Remaining gates

The proof is existential until explicit upper bounds for \(\lambda_{M+1}(L,R)\), \(C_{\rm prime}(L)\), and the gamma constants are supplied. Tail nonnegativity also does not imply full positivity. The finite/tail coupling must satisfy

\[
B_M=D_MC_M^{1/2}
\]

and

\[
F_M-D_MD_M^*\geq0.
\]

## Disposition

For each fixed \(L\), existence of a finite-codimensional nonnegative local Weil tail follows from source-side bounds and time--band compactness. The RH-bearing residual is now the range-compatible Schur condition plus effective constants. No RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_time_band_tail_inequality.py`
- `research/voevodsky/results/time_band_tail_inequality.json`
