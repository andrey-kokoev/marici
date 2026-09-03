# Abel summation controls modulated bad-interval trains

## Question

How can the periodic Dirichlet cancellation survive slowly varying interval widths and centers without returning to an endpointwise triangle bound?

## Claim boundary

Abel summation replaces component count by the discrete total variation of interval amplitudes. For a periodic train with slowly modulated endpoints, the Fourier endpoint sum is controlled by a geometric partial-sum factor times amplitude variation. This is the correct perturbation mechanism. The required source bound on endpoint variation and the resulting transition integral remain open.

## Modulated train

Write the bad intervals as

\[
I_j=[jp+\alpha_j,jp+\beta_j],
\qquad j=0,\ldots,N-1.
\]

Their Fourier endpoint sum is

\[
E(t)
=
\sum_{j=0}^{N-1}
 e^{ijpt}A_j(t),
\]

where

\[
A_j(t)
=
e^{i\beta_jt}-e^{i\alpha_jt}.
\]

The bad-set Fourier kernel is

\[
k_\Omega(t)
=
\frac{E(t)}{2\pi it}.
\]

## Abel identity

Let

\[
P_j(z)=\sum_{k=0}^jz^k.
\]

Then

\[
\sum_{j=0}^{N-1}A_jz^j
=
A_{N-1}P_{N-1}(z)
+
\sum_{j=0}^{N-2}
(A_j-A_{j+1})P_j(z).
\]

For \(|z|=1\),

\[
|P_j(z)|
\leq
\min\left(j+1,\frac2{|1-z|}\right).
\]

Consequently,

\[
|E(t)|
\leq
\min\left(N,\frac2{|1-e^{ipt}|}\right)
\left(
|A_{N-1}(t)|+
\operatorname{TV}_j A(t)
\right),
\]

where

\[
\operatorname{TV}_j A(t)
=
\sum_{j=0}^{N-2}|A_{j+1}(t)-A_j(t)|.
\]

This replaces the previous factor \(N\) outside every frequency by a resonant geometric factor and a modulation budget.

## Endpoint variation reduction

The elementary inequality

\[
|e^{ix}-e^{iy}|
\leq|x-y|
\]

gives

\[
\operatorname{TV}_j A(t)
\leq
|t|
\left[
\operatorname{TV}(\alpha)
+
\operatorname{TV}(\beta)
\right].
\]

Thus a total-variation bound on the endpoint offsets produces a pointwise kernel estimate without quadratic component loss.

## Source geometry needed

In the one-prime case, endpoints solve

\[
m_\Gamma(u)-c_2\cos(u\log2)=\delta.
\]

Within successive positive cosine lobes, monotonicity of \(m_\Gamma\) should move left endpoints inward and right endpoints inward. The needed theorem must prove this monotonic ordering and bound

\[
\operatorname{TV}(\alpha)+
\operatorname{TV}(\beta)
\]

from the first and last root offsets. A derivative comparison must exclude extra turning points within a lobe.

## Resonances

The factor \(|1-e^{ipt}|^{-1}\) is large near dual resonances. These neighborhoods must be integrated using the trivial bound \(|E(t)|\leq2N\); away from them, use the Abel bound. This reproduces linear Dirichlet energy only if the resonance widths and variation term are balanced explicitly.

## Disposition

The variable-width correction is reduced to a source endpoint-variation theorem plus a resonance integral. No transition-trace certificate or RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_abel_modulated_interval_train.py`
- `research/voevodsky/results/abel_modulated_interval_train.json`
