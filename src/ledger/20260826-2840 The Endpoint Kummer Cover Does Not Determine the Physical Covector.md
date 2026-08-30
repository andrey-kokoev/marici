# 2840 — The Endpoint Kummer Cover Does Not Determine the Physical Covector

## Retraction

Entry 2838 incorrectly promoted the endpoint branch support to the separable coefficient form

\[
\frac{d\xi}{\sqrt{1-\xi^2}}
\]

and interpreted its toy period \(\pi\) as a source-normalized cosmological readout. That promotion is withdrawn.

## Frozen strict-transform measure

Entry 2363 derives the actual source measure

\[
\frac{da\wedge d\xi}{\sqrt{K_{\rm exc}(a,\kappa,\xi)}},
\]

where

\[
\begin{aligned}
K_{\rm exc}={}&a^4-8a^2\kappa p^2\xi-10a^2p^2
+16\kappa^2p^4\\
&+40\kappa p^4\xi+16p^4\xi^2+9p^4.
\end{aligned}
\]

The mixed derivative

\[
\partial_\xi\partial_a^2K_{\rm exc}=-16\kappa p^2
\]

is generically nonzero. Moreover, \(K_{\rm exc}|_{\xi=1}\) retains its \(a^4\) term, so \(1-\xi^2\) is not a factor of the source kernel.

## What is established

The discriminant of \(K_{\rm exc}\), treated as a quadratic in \(a^2\), is supported on the existing endpoint divisors

\[
\kappa=\pm1,
\qquad
\xi=\pm1.
\]

This establishes the endpoint Kummer cover and its deck action. It does not produce a rank-one endpoint covector after the \(a\)-fiber is forgotten.

## Correct frontier

The following remain unconstructed:

- a source-normalized covector on the two endpoint route occurrences;
- its transport under endpoint-chain maps;
- the contragredient identity requested by Nima;
- a physical scalar period derived from that covector.

The exact defect test \(VU-I\) is therefore not yet typed. Applying it to the toy arcsine covector would repeat the same error.

## Surviving results

Entries 2835 and 2836 remain valid at their stated chain-incidence scope:

- one marked endpoint is selected while a unit wall is rejected;
- the unweighted two-endpoint boundary packet is \((-1,+1)\) and its coarse sum vanishes.

Neither statement determines the full coefficient-valued period.

## Durable artifacts

- `research/benincasa/check_endpoint_kummer_readout_typing.py`
- `research/benincasa/endpoint-kummer-readout-typing.json`
