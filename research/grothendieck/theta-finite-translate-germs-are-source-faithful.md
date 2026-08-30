# Theta finite translate germs are source-faithful

## Statement

Let `q_1<...<q_N` be distinct nonnegative shifts of the completed theta
kernel.  Then

\[
 \boxed{
 \sum_{j=1}^Nc_j\Phi(t+q_j)\equiv0
 \quad\Longrightarrow\quad
 c_1=\cdots=c_N=0.}
\]

Thus the complete seam germ separates every finite labelled coefficient
packet.  This is the finite detector theorem left open by packet 180.

## Source asymptotic

For `u>=0`, the completed theta kernel has the positive labelled expansion

\[
 \Phi(u)=\sum_{n\ge1}T_n(u),
\]

where

\[
 T_n(u)=
 \left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)
 e^{-\pi n^2e^{2u}}.
\]

The `n=1` term dominates super-exponentially:

\[
 \Phi(u)=T_1(u)(1+o(1))
 \qquad(u\to+\infty).
\]

Indeed every `n>=2` ratio to `T_1` is a polynomial/exponential prefactor
times

\[
 e^{-\pi(n^2-1)e^{2u}},
\]

and the resulting positive tail is dominated by a convergent geometric
majorant for sufficiently large `u`.

For every fixed `d>0`, it follows that

\[
 \frac{\Phi(u+d)}{\Phi(u)}
 \sim
 e^{9d/2}
 \exp\left[-\pi(e^{2d}-1)e^{2u}\right]
 \longrightarrow0.
\]

## Triangular dominance proof

Assume

\[
 F(t)=\sum_{j=1}^Nc_j\Phi(t+q_j)=0
\]

for all sufficiently large real `t`. Divide by the least-shift translate
`Phi(t+q_1)`.  Every ratio with `j>1` tends to zero, hence

\[
 c_1=0.
\]

Remove that term and repeat. Induction gives every `c_j=0`.

Because `Phi` is real analytic, vanishing of the full germ at the seam implies
vanishing on an interval and therefore on the positive ray. The same
triangular argument applies.  No zero data or RH-equivalent positivity enters.

## Jet formulation

Define the infinite Cauchy-jet detector

\[
 \mathcal J_Q(c)
 =\left(
 \sum_{j=1}^Nc_j\Phi^{(k)}(q_j)
 \right)_{k\ge0}.
\]

If every component vanishes, the seam germ has a zero of infinite order and
is identically zero. Therefore

\[
 \boxed{\ker\mathcal J_Q=0.}
\]

Since the coefficient space is finite-dimensional, some finite jet
truncation is already injective.  More precisely, the descending kernels

\[
 K_M=\bigcap_{k=0}^M
 \ker\left(c\mapsto\sum_jc_j\Phi^{(k)}(q_j)\right)
\]

must stabilize at zero after finitely many strict dimension drops.  The
minimal sufficient jet order depends on the labelled packet and is not
asserted to be `N-1`.

## Meaning for the detector hierarchy

The source hierarchy is now exact:

\[
 \begin{array}{c|c}
 \text{detector}&\text{finite labelled faithfulness}\\
 \hline
 \text{endpoint value }\tau&\text{fails for two labels}\\
 \text{complete seam germ / full jet}&\text{faithful}
 \end{array}
\]

Hence scalar cancellation is loss in a grade-zero projection, not loss of the
full source relationship. The higher seam jets retain the missing relative
information.

## Completion obstruction

Finite faithfulness is not uniform faithfulness.  As labels become close in
the analytic geometry, normalized coefficient packets may have germs whose
norm tends to zero even though no finite packet is exactly annihilated.  The
next theorem must therefore choose the source-authorized germ topology and
test a lower frame bound or strict inductive-limit exactness.

The hostile family is a sequence of finite packets `c_X` such that

\[
 \|c_X\|_{\rm source}=1,
 \qquad
 \left\|\sum_qc_{X,q}\Phi(\,cdot+q)\right\|_{\rm germ}
 \longrightarrow0.
\]

Adjacent logarithmic labels remain the first mandatory test.

## Scope

This packet proves linear independence and finite germ/jet faithfulness for
distinct nonnegative shifts. It does not prove a cutoff-independent jet order,
a uniform lower bound, or continuity of every arithmetic constructor in the
germ topology.
