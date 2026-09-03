# Monomial probes detect the low-frequency prime divergence

## Question

Does restriction to the analytic heat-polynomial core prevent vectors from detecting the increasingly negative prime multiplier near frequency zero?

## Claim boundary

No, if all polynomial degrees are admitted. The monomials \(p_d(z)=z^d\) form an approximate identity at frequency zero after heat evaluation, so their normalized prime-form Rayleigh quotients converge to the cutoff multiplier value \(W_{P,N}(0)\). Consequently no conductor-uniform lower bound exists on the unrestricted polynomial core. A degree-restricted cofinal system or source-regularized joint form is not excluded.

## Monomial concentration

For

\[
p_d(z)=z^d,
\]

the heat evaluation is

\[
(V_hp_d)(u)
=
e^{-dhu^2}.
\]

Its squared modulus changes the observer measure to a multiple of

\[
e^{-(t+2dh)u^2}(1-e^{-hu^2})du.
\]

After normalization, these measures concentrate at \(u=0\) as \(d\) tends to infinity. The factor \(1-e^{-hu^2}\) vanishes quadratically, but rescaling \(u\) by \((t+2dh)^{-1/2}\) still gives a fixed integrable profile. Hence for every bounded continuous multiplier \(W\),

\[
\frac{
\langle V_hp_d,M_WV_hp_d\rangle
}{
\lVert V_hp_d\rVert^2
}
\longrightarrow
W(0).
\]

## Prime cutoff

For each fixed \(N\), \(W_{P,N}\) is bounded and continuous. Therefore

\[
\lim_{d\to\infty}
\frac{Q_{P,N}(p_d)}
{\lVert V_hp_d\rVert^2}
=
W_{P,N}(0)
=-
\sum_{n\leq N}
\frac{\Lambda(n)}{\sqrt n}.
\]

Taking the conductor cutoff onward gives

\[
\inf_{N,d}
\frac{Q_{P,N}(p_d)}
{\lVert V_hp_d\rVert^2}
=-\infty.
\]

Adding any fixed multiplier continuous at zero, including the unrenormalized gamma multiplier, shifts the limit by only its finite value at zero. It cannot restore a uniform lower bound.

## Parameter relation

The multiplier remains close to its zero value when

\[
|u|\log N
\ll1.
\]

The monomial observer concentrates on scale

\[
|u|
\asymp
(dh)^{-1/2}.
\]

It therefore resolves the negative well once

\[
dh
\gg
(\log N)^2.
\]

This identifies the relevant cofinal competition among degree, mesh, and conductor cutoff.

## Coherence consequence

The analytic core does not by itself remove the residual; its unbounded-degree observer family is jointly strong enough to see it. Any proposed higher coherencer must do more than declare analyticity. It must either:

1. derive a source-authorized coupled regime preventing \(dh\) from outgrowing \((\log N)^2\) before joint completion;
2. combine gamma and prime as a distribution before the multiplier cutoff is formed;
3. supply a graph norm in which the concentrating monomials do not have bounded norm;
4. produce an exact counterterm from the completed source identity.

A degree restriction alone cannot establish the full Hankel criterion unless a later dense-limit theorem restores all polynomial probes.

## Disposition

`joint_analytic_core_semiboundedness` fails for the unrestricted polynomial core under naive prime cutoff. The first surviving constructor is a source-regularized joint gamma--prime form or a stronger graph topology with proved density of the required Gaussian jets.

## Verification

- `research/voevodsky/checkers/check_monomial_probe_prime_divergence.py`
- `research/voevodsky/results/monomial_probe_prime_divergence.json`
