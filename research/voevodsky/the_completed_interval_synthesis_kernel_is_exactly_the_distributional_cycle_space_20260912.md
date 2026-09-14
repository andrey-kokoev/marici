# The completed interval-synthesis kernel is exactly the distributional cycle space

## Question

Does the finite identity between interval-synthesis kernel and graph cycles survive projective completion?

## Claim boundary

Yes for the interval-coverage map \(J\). This removes one part of the premise in completed augmented faithfulness. It does not by itself prove that the subsequent completed-theta transform is injective on the infinite interval-synthesis range.

## Completed maps

Let

\[
Jc=\sum_e c_e\mathbf1_{[A_e,B_e]},
\qquad
\partial c=\sum_e c_e(\delta_{B_e}-\delta_{A_e}).
\]

The projective source lies in unweighted \(\ell^1(E)\), because every exponential weight is at least one. Therefore the boundary series converges absolutely as a distribution against compactly supported smooth test functions.

The interval length estimate gives, for any \(\delta>0\),

\[
\|Jc\|_{L^1}
\leq
\sum_e|c_e|\ell_e
\leq
\delta^{-1}q_\delta(c).
\]

Thus \(J\) extends continuously into \(L^1(\mathbb R)\), and \(\partial\) extends continuously into distributions.

## Kernel identity

Termwise distributional differentiation is justified by absolute convergence and gives

\[
\frac{d}{dv}Jc=-\partial c.
\]

If \(Jc=0\), then \(\partial c=0\). Conversely, if \(\partial c=0\), then the distributional derivative of \(Jc\) vanishes. A locally integrable function with zero distributional derivative is almost everywhere constant. Since \(Jc\in L^1(\mathbb R)\), that constant must be zero. Hence

\[
\ker J=\ker\partial.
\]

This identity requires neither finite support nor compact support of the total interval packet.

## Consequence for completed history

Write completed common history as

\[
\widehat B_D=T_D\circ J,
\]

where

\[
T_Df(s)=\int f(v)\Phi_1(v)\Phi_1(v+s+D)\,dv.
\]

The proved identity gives

\[
\ker\partial=\ker J\subseteq\ker\widehat B_D.
\]

Equality with \(\ker\widehat B_D\) now reduces exactly to injectivity of \(T_D\) on the completed interval-synthesis range \(J(\mathcal C_{D,\exp})\). Finite leftmost-interval arguments do not establish this for packets with unbounded support.

## Disposition

The completed graph-cycle closure problem is solved at the interval-synthesis layer. Completed augmented faithfulness has one remaining analytic gate: prove that the completed-theta correlation transform \(T_D\) is injective on the specified \(L^1\) range, or exhibit a nonzero synthesized function in its kernel. The first missing source datum is an injectivity theorem for the recorded atom \(\Phi_1\), such as an applicable transform factorization with a nonvanishing multiplier and a justified half-line uniqueness argument.
