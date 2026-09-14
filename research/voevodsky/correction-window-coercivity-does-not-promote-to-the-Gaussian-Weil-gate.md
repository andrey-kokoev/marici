# Correction: window coercivity does not promote to the Gaussian Weil gate

## Correction

`expanded-aperture-search-ranks-log-elliptic-coercivity-above-positive-semigroup-lifts.md` ranked compact-window log-elliptic coercivity as the strongest surviving global route. That ranking is superseded by the later, more comprehensive finite-double-contact sweep.

Log-ellipticity remains a valid theorem for reducing each fixed compact-support Weil form to a finite spectral problem. It does **not** provide a viable promotion from growing windows to the noncompact Gaussian observer.

## Quantitative obstruction

The best compact-window positivity margin collapses at a Landau--Widom/prolate-spheroidal rate that is super-exponential in the support length. The Gaussian truncation error decays only exponentially in the squared cutoff relative to heat width.

The verified sweep reports the representative scales

\[
\lambda^*(0.8)\asymp 10^{-17},
\qquad
\lambda^*(2)\leq 3.2\times10^{-283},
\]

with the numerical constants dependent on an unrefereed certificate but the qualitative plunge independently supported by classical prolate-spheroidal asymptotics and Connes--Consani numerics.

Therefore no uniform margin survives to absorb the Gaussian truncation tail beyond the already controlled small-heat region. Separately, the absolute prime envelope grows like

\[
A_L\sim4e^L,
\]

forcing a pointwise-envelope resolution scale

\[
T_1=2\pi e^{A_L},
\]

which is doubly exponential and optimal for that envelope method by phase equidistribution.

Thus:

- fixed-window finite reduction remains mathematically correct;
- propagation of its positivity margin to all Gaussian tests is quantitatively eliminated;
- it must not be called the leading global RH route.

## Fresh external search

`pnpm pdf:search` found no Gårding/digamma theorem in the indexed PDF corpus beyond the already used boundary-operator material. Fresh OpenAlex/arXiv metadata search recovered:

- Xuefeng Zhu, arXiv:2608.24827, the compact-window finite reduction and barrier;
- Suzuki's compact-window Friedrichs/operator framework;
- no new unconditional positive endpoint--gamma--prime factorization.

The repository's source audit records that Zhu's claimed numerical certificate is absent from the arXiv source archive, so its specific margin is authority-blocked pending supplementary files. This does not affect the qualitative route obstruction.

## Correct surviving executable route

The later sweep ranks **direct pointwise enclosure of the coupled Gaussian kernel**, not window-form coercivity.

Construct a ball-arithmetic enclosure functor

\[
\mathcal E([t_1,t_2]\times[\xi_1,\xi_2])
=(I_0,I_1,I_2),
\]

with

\[
\Theta\in I_0,
\qquad
\partial_\xi\Theta\in I_1,
\qquad
\partial_{\xi\xi}\Theta\in I_2
\]

uniformly on each box. Endpoint terms are closed form, gamma terms admit certified quadrature with explicit tails, and the prime sector needs the explicit uniform tail bound

\[
\left|
\sum_{n>N}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/(4t)}\cos(\xi\log n)
\right|
\leq
C(t_1,t_2,N).
\]

This retains endpoint--gamma--prime cancellation before deciding sign and avoids the collapsing window margin.

The first executable pilot is the on-axis interval

\[
0.05\leq t\leq2,
\qquad \xi=0,
\]

followed by branch-and-bound boxes using the alternative

\[
\Theta>\varepsilon
\quad\lor\quad
|\partial_\xi\Theta|>\varepsilon'
\quad\lor\quad
\partial_{\xi\xi}\Theta>\varepsilon''.
\]

Mandatory negative controls are a Davenport--Heilbronn analogue and a difference of two Gaussians.

## Relation to the rung-four objective

Direct enclosure does not construct the desired universal positive carrier. It is nevertheless the only freshly audited noncircular executable continuation: it can certify new compact regions of the coupled observer and locate the first obstruction without assuming Gram positivity, a representing measure, or RH-side zero data.

## Durable sources

- `research/grothendieck/references/double_contact_sweep.agent.final.md`
- `research/grothendieck/references/kimi-finite-double-contact-literature-sweep-2026-09-05.md`
- `research/grothendieck/zhu-compact-window-certificate-source-audit.md`
- `research/grothendieck/fixed-support-prime-translation-norm-has-explicit-but-exponential-bound.md`
- `research/grothendieck/explicit-uniform-digamma-minus-log-bound.md`
