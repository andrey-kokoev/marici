# Deutsch--Popperian conjecture: robust full abstraction needs a criticism margin

## Status

This packet strengthens exact full abstraction to completion-stable full
abstraction. It isolates the failure mode in which every finite interface is
injective but inequivalent realizations become asymptotically indistinguishable.

## 1. Exact versus robust separation

Let \(\mathcal E\) be a space of typed realizations, let \(G\) be the authorized
gauge action, and let

\[
N:\mathcal E/G\longrightarrow\mathcal Y
\]

be the experimental nerve. Exact full abstraction says that \(N\) is injective.

Choose a source-relevant quotient metric \(d_{\mathrm{src}}\) and an observation
metric \(d_{\mathrm{obs}}\). Robust full abstraction requires a lower control

\[
d_{\mathrm{obs}}(N(R),N(R'))
\ge
\omega\bigl(d_{\mathrm{src}}([R],[R'])\bigr),
\]

where \(\omega(t)>0\) for \(t>0\). A linear lower bound has the form

\[
d_{\mathrm{obs}}(N(R),N(R'))
\ge
c\,d_{\mathrm{src}}([R],[R'])
\]

with \(c>0\).

Injectivity says distinct source classes differ somewhere. A positive criticism
margin says the difference cannot disappear under completion, noise, or finite
precision.

## 2. Linear quotient theorem

Let \(L:S\to Y\) be a bounded linear observation and let \(K\subseteq S\) be the
authorized gauge subspace. Assume

\[
\ker L=K.
\]

Then \(L\) induces an injective map

\[
\overline L:S/K\longrightarrow Y.
\]

The observation is robustly fully abstract precisely when \(\overline L\) is
bounded below:

\[
\|Lx\|
\ge
c\,\operatorname{dist}(x,K)
\]

for some \(c>0\). Equivalently, \(\overline L^{-1}\) is bounded on its range.

Thus exact full abstraction requires the correct kernel. Robust full abstraction
additionally requires a closed, bounded-below quotient image.

## 3. Finite-stage collapse

For cutoff realizations \(S_N\) with gauges \(K_N\) and observations \(L_N\),
define

\[
c_N
=
\inf_{x\notin K_N}
\frac{\|L_Nx\|}{\operatorname{dist}(x,K_N)}.
\]

Every finite stage is fully abstract when \(c_N>0\). Completion-stable full
abstraction requires

\[
\inf_N c_N>0.
\]

If \(c_N\to0\), choose normalized representatives \(x_N\) satisfying

\[
\operatorname{dist}(x_N,K_N)=1,
\qquad
\|L_Nx_N\|\to0.
\]

This sequence is an approximate explanatory kernel. It is the canonical hostile
witness: every finite critic succeeds exactly, yet criticism loses all uniform
power.

## 4. Statistical meaning

Suppose observational error is at most \(\varepsilon\). Under a linear criticism
margin \(c\), source classes separated by more than

\[
\frac{2\varepsilon}{c}
\]

cannot be confused. When \(c_N\to0\), the required precision or sample budget
diverges.

Therefore an explanatory distinction can be mathematically identifiable but
operationally uncriticizable at available resources. Exact injectivity must not
be reported as robust understanding.

## 5. Dynamic version

For a linear evolution \(A\) and observation \(J\), the finite-horizon Gramian is

\[
W(L)=\sum_{k=0}^{L-1}(A^*)^kJ^*JA^k.
\]

After quotienting authorized gauge, exact dynamic full abstraction requires

\[
\ker W(L)=K.
\]

Robust dynamic full abstraction requires

\[
\langle x,W(L)x\rangle
\ge
c^2\operatorname{dist}(x,K)^2.
\]

The square root of the smallest positive quotient eigenvalue is the finite
criticism margin.

## 6. Quantum version

For quantum channels, the observation metric must include the contexts actually
authorized. If arbitrary entangled ancillas are admitted, channel
distinguishability is naturally measured by a completely bounded or diamond-type
norm. If they are not physically or source-authorized, using that norm silently
enlarges the critic.

A central readout may have a large exact kernel even though the endpoint algebra
is faithful. Conversely an informationally complete finite readout can have a
smallest singular value tending to zero as the endpoint family grows. Algebraic
tomography and stable tomography are different achievements.

## 7. Toric-code witness

On the fixed smallest torus, adding two independent loop probes separates the
four logical sectors by discrete bits. With noiseless binary readout, the finite
margin is exact and nonzero.

Across growing lattices, however, the physical implementation of a
noncontractible probe may acquire a noise-dependent cost. The algebraic loop bit
remains faithful while the executable criticism margin can decay with loop
length. This separates:

- algebraic full abstraction of logical sectors;
- robust measurement of those sectors;
- fault-tolerant implementation of the measurement.

No result at the first layer supplies either later layer.

## 8. Three-lens consequence

Scalarization can fail in two ways.

1. It has a genuine kernel: phase or order is erased exactly.
2. It is injective on a restricted family but increasingly ill-conditioned:
   phase or order survives only in a vanishing residual.

The second failure is subtler. Symbolic calculations can certify every finite
instance while the completed scalar interface loses a bounded inverse.

Thus the compiler from ordered plant to scalar diagnostic needs both:

\[
\ker L=K
\]

and a uniform lower bound on the induced quotient map.

## 9. Minimal finite hostile family

Let

\[
L_N=
\begin{pmatrix}
1&0\\
0&N^{-1}
\end{pmatrix},
\qquad
K_N=0.
\]

Each \(L_N\) is injective, so every finite stage is fully abstract. But

\[
c_N=N^{-1}\longrightarrow0.
\]

The unit source difference

\[
x_N=(0,1)
\]

has observation norm \(N^{-1}\). This is the smallest matrix witness separating
finite faithfulness from completion-stable criticism.

Adding a reference row

\[
R_N=(0,1)
\]

produces a uniformly bounded-below combined observation. The reference repairs
the margin only if that row is independently source-authorized.

## 10. Condition number of understanding

Define the local criticism condition number by

\[
\kappa_N=c_N^{-1}.
\]

It measures how much observational error can be amplified when reconstructing a
source distinction modulo gauge. Infinite \(\kappa\) means either a true kernel
or loss of closed range. Large finite \(\kappa\) means fragile criticism.

An explanatory report should therefore state:

- the claimed source quotient;
- the exact contextual kernel;
- the criticism margin or modulus;
- its cutoff dependence;
- the authority and cost of contexts achieving it.

## 11. Strengthened DPC

Understanding is not merely a fully abstract representation of a problem. It is
a representation whose non-gauge distinctions remain criticizable with a
nonvanishing margin under the completions and perturbations admitted by the
problem.

This does not require one universal numerical constant. It requires an explicit
modulus connecting source difference to observable difference over the declared
regime.

## 12. Critic

A uniform global margin may be impossible even for excellent explanations.
Continuous parameter models naturally contain arbitrarily close alternatives.
Demanding one constant over the entire model class would reject ordinary
well-posed local inference.

The repair is stratification. Require a local or compact-regime modulus after
quotienting gauge, and identify singular strata where the margin vanishes. Those
strata are not automatically failures; they are boundaries at which the
explanatory interface changes rank and must be retyped.

## 13. Bottom line

Full abstraction removes hidden exact kernels. A criticism margin removes hidden
approximate kernels. Completion can create the second without creating the
first at any finite stage.

The next question for every sector is therefore:

> What is the smallest source-authorized context family whose quotient
> observation map remains bounded below over the declared completion regime?
