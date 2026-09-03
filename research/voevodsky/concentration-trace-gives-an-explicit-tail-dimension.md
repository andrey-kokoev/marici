# The concentration trace gives an explicit tail dimension

## Question

Can the existential time--band cutoff be replaced by an explicit finite dimension without computing prolate concentration eigenvalues individually?

## Claim boundary

Yes. The trace of the time--band concentration operator bounds every ordered eigenvalue and yields an explicit sufficient trial dimension. The resulting bound is crude but source-independent and effective once the gamma and prime constants are enclosed. This does not compute those constants or prove the finite Schur form positive.

## Trace identity

With unitary Fourier normalization and low-frequency band \([-R,R]\), the concentration operator on \((-L,L)\) has integral kernel

\[
K_R(x,y)
=
\frac{\sin(R(x-y))}{\pi(x-y)}.
\]

Its diagonal value is \(R/\pi\). Therefore

\[
\operatorname{Tr}(T_{L,R})
=
\frac{2LR}{\pi}.
\]

Let

\[
\lambda_1\geq\lambda_2\geq\cdots\geq0
\]

be its eigenvalues. Since the first \(M+1\) eigenvalues are each at least \(\lambda_{M+1}\),

\[
(M+1)\lambda_{M+1}
\leq
\sum_j\lambda_j
=
\frac{2LR}{\pi}.
\]

Hence

\[
\lambda_{M+1}(L,R)
\leq
\frac{2LR}{\pi(M+1)}.
\]

## Explicit strict-tail condition

The time--band lower margin obeys

\[
\delta_{L,R,M}
\geq
m_R-C_{\rm prime}(L)
-
(m_R+C_{\rm low}(R))
\frac{2LR}{\pi(M+1)}.
\]

Assume

\[
m_R>C_{\rm prime}(L).
\]

Then the explicit sufficient condition

\[
M+1
>
\frac{2LR}{\pi}
\frac{m_R+C_{\rm low}(R)}{m_R-C_{\rm prime}(L)}
\]

implies

\[
\delta_{L,R,M}>0.
\]

No numerical concentration spectrum is required.

## Quantifier order

For every fixed support window \(L\), first choose \(R\) with \(m_R>C_{\rm prime}(L)\), then choose \(M\) from the displayed bound. This is

\[
\forall L\;\exists R\;\exists M.
\]

It does not provide one uniform \(R\) or \(M\) for all support windows.

## Cost of the crude trace estimate

The actual concentration spectrum has a sharper transition near the Shannon number \(2LR/\pi\). The trace bound ignores spectral decay beyond that transition and may greatly overestimate \(M\). It remains useful because it is rigorous and requires only elementary trace data.

## Remaining constants

An executable certificate now needs interval enclosures for

\[
m_R,
\qquad
C_{\rm low}(R),
\qquad
C_{\rm prime}(L).
\]

The prime constant is a finite explicit prime-power sum for fixed \(L\). The gamma constants come from real digamma bounds on compact and exterior frequency regions.

## Disposition

The concentration-eigenvalue blocker is removed. Effective strict tail positivity reduces to explicit gamma enclosures and a finite prime sum, followed by the finite Schur test. No RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_concentration_trace_tail_dimension.py`
- `research/voevodsky/results/concentration_trace_tail_dimension.json`
