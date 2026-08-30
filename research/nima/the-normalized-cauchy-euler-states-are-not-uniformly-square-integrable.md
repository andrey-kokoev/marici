# The normalized Cauchy Euler states are not uniformly square integrable

The max-kernel ratio can be decided for the natural exhaustion
\(X_P=\{p:p\le P\}\).

Define a probability measure on the \(P\)-smooth semigroup by

\[
\mu_P(n)
=
\frac{1}{A_P n},
\qquad
A_P=\prod_{p\le P}(1-p^{-1})^{-1}.
\]

If \(N,M\) are independent with law \(\mu_P\), then

\[
\mathbb E|Z_{X_P}|^2
=
\sum_{n,m}\mu_P(n)\mu_P(m)\min(n,m)
=
\mathbb E\min(N,M).
\]

Under \(\mu_P\), the prime valuations are independent geometric variables:

\[
\Pr(v_p(N)=k)
=
(1-p^{-1})p^{-k}.
\]

Hence, for \(S_P=\log N\),

\[
m_P:=\mathbb E S_P
=
\sum_{p\le P}\frac{\log p}{p-1},
\]

and

\[
v_P:=\operatorname{Var}(S_P)
=
\sum_{p\le P}
\frac{p(\log p)^2}{(p-1)^2}.
\]

Standard prime-sum asymptotics give

\[
m_P\sim\log P,
\qquad
v_P\sim\frac12(\log P)^2.
\]

Apply Paley--Zygmund to the nonnegative random variable \(S_P\). For any fixed
\(0<\theta<1\),

\[
\Pr(S_P\ge\theta m_P)
\ge
(1-\theta)^2
\frac{m_P^2}{m_P^2+v_P}.
\]

With \(\theta=1/2\), the right side stays bounded below by a positive constant.
For two independent copies,

\[
\Pr\!\left(
N\ge e^{m_P/2},
\ M\ge e^{m_P/2}
\right)
\ge c^2
\]

for all sufficiently large \(P\). Therefore

\[
\mathbb E|Z_{X_P}|^2
=
\mathbb E\min(N,M)
\ge
c^2e^{m_P/2}
=
P^{1/2+o(1)}.
\]

In particular,

\[
\sup_P\mathbb E|Z_{X_P}|^2=\infty.
\]

Thus the finite mean-one normalization does not produce an \(L^2\)-bounded
Euler family in the Cauchy carrier. The failure is not a delicate possible
obstruction; it is forced by the independent geometric valuation law.

This closes one proposed route. The nonlinear Euler exponential cannot itself
be the completion-stable Green state. Any completed positive Gram must first
remove, quotient, or Schur-route the growing valuation cloud through the
theta/archimedean boundary system.

The scale of failure is also informative. The Cauchy normalization fixes the
first moment exactly, while the second moment grows at least like a positive
power of the prime cutoff. Therefore no logarithmic wall subtraction alone can
repair this quadratic escape.

The next theorem must identify a source-derived compensating channel before
the \(L^2\) norm is formed. Candidate operations are:

- relative theta sewing at the full adelic level;
- a Schur complement against the external constant--delta carrier;
- or a change from absolute Euler state norm to a mixed source-observer form.

A scalar renormalization applied after the max-kernel Gram is too late.

The sharp falsifier for any proposed repair is preservation of the lower-bound
event: if the repaired state still carries the sector
\(S_P\ge m_P/2\) with uniformly positive mass and unchanged amplitude, its
quadratic norm must diverge.
