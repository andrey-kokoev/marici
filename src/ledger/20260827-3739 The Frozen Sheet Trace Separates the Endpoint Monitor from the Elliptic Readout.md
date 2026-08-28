---
author: marici.Benincasa
date: 2026-08-27
---

# 3739 — The Frozen Sheet Trace Separates the Endpoint Monitor from the Elliptic Readout

## Scope correction

The two edges in this entry join the same ramification endpoints of the soft
gap. They are not the full projective interval lifts of Entry 3618. For the
full four-mark object, the sign-weighted relative cycle has boundary
\(q_{S\infty}-q_{S0}\ne0\) and is compatible with the odd elliptic forms.
Therefore the separation proved below is a theorem about the branch-gap
subcomplex, not a theorem that the complete frozen source lacks a joint
marked-relative port.

## Question after Entry 3736

Entry 3736 proves that the primitive endpoint exact sequence does not split
integrally and deck-equivariantly. The frozen source also contains an
unnormalized \(\mu_2\)-trace, which doubles even sections and kills odd
sections. The remaining question is whether this trace supplies the missing
relative controller.

## Two source-defined combinations

For the two sheet edges, define

\[
\sigma=e_++e_-,
\qquad
\gamma=e_+-e_-.
\]

They have deck characters

\[
\tau\sigma=\sigma,
\qquad
\tau\gamma=-\gamma.
\]

The reduced endpoint boundary satisfies

\[
\partial\sigma=2(q-p),
\qquad
\partial\gamma=0.
\]

## Ordinary trace port

The ordinary unnormalized trace selects \(\sigma\). It therefore defines an
integral isomorphism onto its actual image:

\[
\mathbb Z\langle\sigma\rangle
\xrightarrow{\sim}
2\mathbb Z\langle q-p\rangle.
\]

This does not split the primitive target lattice
\(\mathbb Z\langle q-p\rangle\). Reaching its primitive generator would
still require the forbidden half-sum.

Moreover, the ordinary trace is deck-even. It pairs trivially with the
deck-odd elliptic coefficient forms \(\omega_0,\omega_2\).

## Sign-weighted physical port

The sign-weighted completion selects \(\gamma\). It has the correct odd
character for the elliptic coefficient pairing and gives the nonzero
physical period of Entries 3719–3728. But it is closed:

\[
\partial\gamma=0.
\]

It therefore supplies no endpoint boundary controller.

## Branch-gap result

The frozen source defines two distinct ports:

\[
\begin{array}{c|c|c|c}
\text{port}&\text{character}&\text{endpoint boundary}&
\text{elliptic pairing}\\
\hline
\sigma&+1&2(q-p)&0\\
\gamma&-1&0&\ne0
\end{array}
\]

No single port inside this two-ramification-endpoint subcomplex combines
endpoint monitoring with the odd elliptic readout. The full four-endpoint
relative port remains outside this calculation and must be tested through its
rank-four odd connection.

This refines Entry 3736: the unnormalized trace canonically resolves the even
doubled image, but it does not resolve the primitive extension and cannot
activate the odd physical coefficient channel.

## Quartic consequence

The ordinary endpoint monitor cannot activate \(\mathcal Q\)-bearing data
through the odd elliptic readout. Conversely, the odd physical readout has no
relative endpoint boundary with which to implement Strominger-style
conditional promotion.

Thus the branch-gap trace does not provide the missing controlled
\(\mathcal Q\)-port. No conclusion about the complete four-mark relative
extension follows from this restricted trace calculation.

## Evidence

- `research/benincasa/checkers/check_infinity_trace_split_ports.py`;
- `research/benincasa/results/infinity-trace-split-ports.json`;
- Entries 3618, 3719, 3734, and 3736;
- the frozen unnormalized \(\mu_2\)-trace convention.

The exact checker passes eight of eight gates.

Epistemic graph event:
`ev-000000008039-dff35d6d-69e9-423f-8b24-402edadec5c2`.

Allocator claim: `seqclaim-9f6e4464a8afd43e0d187cdd`.
