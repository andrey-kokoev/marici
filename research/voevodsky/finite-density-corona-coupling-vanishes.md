# Finite-density corona coupling vanishes

## Question

Can the bulk--corona cross block be obtained as the ordinary limit of the finite-conductor density embeddings?

## Claim boundary

No. Their canonical Hellinger coupling tends to zero as the conductor includes all primes. A surviving cross block would require renormalization or a separately derived nonlocal operator. No such operator is constructed here.

## Finite conductor density

For squarefree \(Q\), the normalized unit density relative to additive Haar measure is

\[
w_Q(x)
=
\frac{Q}{\varphi(Q)}
\mathbf 1_{x\bmod Q\in(\mathbb Z/Q\mathbb Z)^\times}.
\]

It satisfies

\[
\int w_Q\,d\mu_+=1.
\]

The canonical overlap between the additive constant vector and the square-root density vector is the Hellinger affinity

\[
\mathcal A_Q
=
\int\sqrt{w_Q}\,d\mu_+.
\]

Since the unit set has additive measure \(\varphi(Q)/Q\),

\[
\mathcal A_Q
=
\sqrt{\frac{Q}{\varphi(Q)}}
\frac{\varphi(Q)}Q
=
\sqrt{\frac{\varphi(Q)}Q}.
\]

For squarefree \(Q\),

\[
\mathcal A_Q
=
\prod_{p\mid Q}
\sqrt{1-\frac1p}.
\]

## Infinite-prime limit

Along conductors containing every prime up to a growing cutoff,

\[
\log\mathcal A_Q
=
\frac12
\sum_{p\mid Q}
\log\left(1-\frac1p\right).
\]

Using

\[
\log(1-u)
\leq-u
\]

and divergence of

\[
\sum_p\frac1p,
\]

one obtains

\[
\mathcal A_Q
\longrightarrow0.
\]

Thus the canonical finite-level coupling vectors become asymptotically orthogonal.

## Operator consequence

At every finite conductor, \(w_Qd\mu_+\) is absolutely continuous with respect to \(\mu_+\). In the limit, the multiplicative measure becomes singular and the ordinary density coupling disappears.

Therefore the block

\[
C:
L^2(\mu_+)
\longrightarrow
L^2(\mu_\times)
\]

cannot be defined as a nonzero strong limit of the unrenormalized square-root density identifications.

This agrees with the direct-sum decomposition

\[
L^2(\mu_++\mu_\times)
\cong
L^2(\mu_+)
\oplus
L^2(\mu_\times),
\]

where ordinary multiplication has zero cross block.

## Possible surviving constructions

A nonzero coupling could still arise from:

1. a renormalized limit
   \[
   \mathcal A_Q^{-1}C_Q;
   \]
2. a boundary trace retaining fluctuations rather than density mass;
3. an order--Mellin commutator;
4. a source-derived nonlocal correspondence between additive and multiplicative variables.

Each candidate must specify its domain, normalization, limiting topology, adjoint, and contribution to the completed form. The vanishing affinity supplies no authority for any one of them.

## Coherence interpretation

Finite conductor observers are mutually coupled, but their coupling coherencer has residue

\[
\mathcal A_Q
\longrightarrow0.
\]

The higher corona observer is therefore not obtained by ordinary continuous gluing of those finite observers. A renormalized higher coherencer is required if bulk--corona interaction is to survive.

## Disposition

The naive finite-density route to the cross block is closed. The next admissible test is whether a specifically normalized order--Mellin or fluctuation boundary map has a nonzero finite limit and a closed adjoint pair. Without that construction, the corona extension remains an orthogonal bookkeeping sector rather than a mechanism for prime cancellation.

## Verification

- `research/voevodsky/checkers/check_finite_density_corona_coupling.py`
- `research/voevodsky/results/finite_density_corona_coupling.json`
