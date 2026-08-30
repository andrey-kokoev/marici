---
author: marici.Nima
---

# 1545 — Prime Cyclic Deck Traces Become Nilpotent Exactly at Their Deck Prime

## Status

All-prime cyclic generalization of Entry 1544, with exact matrix audits for
\(p=2,3,5,7\).

## Characteristic zero

Let \(\sigma\) be the cyclic shift on the regular \(p\)-dimensional
representation of \(C_p\). Over \(\mathbb Q\), the normalized trace

\[
\boxed{
e_{\rm tr}
=\frac1p\sum_{k=0}^{p-1}\sigma^k
}
\]

is a rank-one idempotent:

\[
e_{\rm tr}^2=e_{\rm tr}.
\]

It projects onto the invariant line and splits the regular representation
into the trace line and its complementary augmentation representation.

## Characteristic \(p\)

Over \(\mathbf F_p\), put

\[
U=\sigma-1,
\qquad
N=\sum_{k=0}^{p-1}\sigma^k.
\]

The cyclic relation gives

\[
\boxed{
U^p=0,
\qquad
N=U^{p-1}.
}
\]

Consequently

\[
\boxed{
\operatorname{rank}N=1,
\qquad
N^2=0.
}
\]

For the all-ones transfer column \(T\) and trace row
\(\operatorname{tr}\),

\[
\boxed{\operatorname{tr}T=p=0.}
\]

The normalized projector cannot be formed, and the trace line is embedded in
a non-semisimple unipotent extension.

## Arithmetic law

For a prime cyclic deck packet,

\[
\boxed{
\begin{array}{c|c}
\operatorname{char}K\ne p
&\text{normalized trace projector exists}\\
\operatorname{char}K=p
&\text{trace becomes a square-zero norm operator}
\end{array}
}
\]

The exact checker verifies the rational and modular matrices independently
for the first four primes. The identities above prove the pattern for every
prime.

## Meaning

The carrier does not manufacture prime numbers. It supplies finite deck and
stabilizer orders. Arithmetic coefficients detect the primes dividing those
orders because precisely those primes obstruct normalized trace descent.

Thus a source-derived route to distinguished primes is:

\[
\boxed{
\text{finite carrier symmetry order}
\longrightarrow
\text{failure prime of coefficient descent}.
}
\]

This is a bounded, falsifiable mechanism. A claimed intrinsic prime must be
traced to an independently derived finite symmetry or incidence order; a
numerical coincidence alone is insufficient.

## Durable evidence

- research/nima/check_supercritical_infinity_jet.sage;
- Entries 1543–1544;
- allocator claim seqclaim-286092c8c6a94e8cb5170fc3.
