# Individual spectral atom is nonclosable in the order topology

## Question

Can the endpoint-corrected remainder form be constructed by treating each spectral atom as a closable rank-one form on the order completion and summing afterward?

## Claim boundary

No. A single point spectral atom defines an unbounded, nonclosable evaluation functional in the cumulative-sum \(L^2\) topology. Therefore an atomwise sum of closed rank-one forms is unavailable. This does not prove that the jointly completed remainder form is nonclosable; cross-atom or source-level completion may alter the result.

## Gaussian analysis representation

Under the cumulative-sum realization, Gaussian analysis has the form

\[
(\mathcal Ag)(a)
=
C_a
\int_0^\infty
u g(u)e^{-a u^2}du,
\]

with a nonzero scalar \(C_a\). A spectral atom at squared label \(x>0\) would act algebraically on Gaussian generators by

\[
L_x(g_a)=e^{-ax}.
\]

If \(L_x\) extended continuously to the order Hilbert space, Riesz representation would supply \(v_x\in L^2(du)\) satisfying

\[
\int_0^\infty
u v_x(u)e^{-a u^2}du
=
e^{-ax}
\]

for all \(a>0\), after normalization.

Setting \(y=u^2\) would say that an absolutely continuous \(L^2\)-derived measure has Laplace transform equal to the Laplace transform of the point mass \(\delta_x\). Laplace uniqueness would force that measure to equal \(\delta_x\), which is impossible. Hence \(L_x\) is unbounded.

## Rank-one nonclosability

A densely defined scalar functional is closable only if its adjoint has dense domain in \(\mathbb C\). For a nonzero scalar codomain, this would provide a Riesz vector and therefore a bounded extension. Thus the unbounded algebraic functional \(L_x\) is not closable.

Consequently the rank-one quadratic form

\[
q_x(f)=|L_x(f)|^2
\]

is nonclosable. Equivalently, there exists a sequence \(f_n\) in the Gaussian span such that

\[
\lVert f_n\rVert_{\rm ord}
\longrightarrow0,
\qquad
L_x(f_n)=1.
\]

Then

\[
q_x(f_n-f_m)=0,
\qquad
q_x(f_n)=1.
\]

## Consequence

Even after removing the endpoint, a zero-side decomposition into separate point-evaluation forms cannot be imported term by term into the order completion. Each atom is individually nonclosable in this topology.

This does not imply that the complete source kernel

\[
K_{R,h}(a,b)
=
H_R(a+b)-H_R(a+b+h)
\]

is nonclosable. An infinite jointly regularized kernel can have cancellations or a stronger collective topology not present in its formal atomwise pieces. Establishing that requires one sequence controlling the full form, not one isolated component.

## Coherence interpretation

The source-completed kernel must precede spectral atom decomposition. Completion and decomposition do not commute:

\[
\operatorname{close}
\left(
\sum_x q_x
\right)
\]

cannot be replaced by

\[
\sum_x
\operatorname{close}(q_x),
\]

because the individual closures do not exist.

## Disposition

`atomwise_spectral_form_completion` fails. The only surviving route is joint source-kernel closability, tested directly on \(K_{R,h}\). No full-form nonclosability or RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_spectral_atom_order_nonclosability.py`
- `research/voevodsky/results/spectral_atom_order_nonclosability.json`
