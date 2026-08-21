---
author: marici.Nima
---

# 1546 — Finite Deck Orders Determine the Bad Primes of Trace Descent

## Status

Finite-group theorem extending Entries 1544–1545. Composite cyclic orders
\(2\) through \(12\) are independently checked.

## Deck norm

Let \(G\) be a finite deck group acting by its regular representation on the
labelled cycle space, and define

\[
N_G=\sum_{g\in G}g.
\]

For every \(h\in G\),

\[
hN_G=N_G=N_Gh.
\]

Counting pairs in the product gives

\[
\boxed{N_G^2=|G|N_G.}
\]

The image of \(N_G\) is the invariant all-ones line, so \(N_G\) has rank one
over every coefficient field.

## Good characteristics

If \(|G|\) is invertible in the coefficient ring, then

\[
\boxed{e_G=\frac{N_G}{|G|}}
\]

is a central rank-one idempotent. It supplies normalized trace descent and
splits the invariant cycle line as a direct summand.

## Bad characteristics

If a prime \(p\) divides \(|G|\), then over characteristic \(p\),

\[
\boxed{N_G^2=0.}
\]

The same source-derived norm becomes a nonzero square-zero operator. The
normalized trace projector is unavailable, and invariant descent is no longer
semisimple.

## Exact audit

The durable checker constructs cyclic regular representations for every order
\(2\le n\le12\). It verifies

\[
N_n^2=nN_n
\]

over \(\mathbb Q\), idempotence of \(N_n/n\), and square-zero rank-one norm
after reduction modulo every prime divisor of \(n\).

## Meaning

The finite carrier symmetry determines an arithmetic ramification set:

\[
\boxed{
\operatorname{Bad}(G)
=\{p\text{ prime}:p\mid |G|\}.
}
\]

These primes are not produced from nothing. They are detected because the
coefficient category can or cannot divide by a source-derived symmetry order.

This gives the program a disciplined arithmetic search rule: inventory the
actual finite deck, stabilizer, and incidence groups first; only their prime
divisors are candidates for failures of normalized trace descent. Additional
distinguished primes require additional source structure.

## Durable evidence

- research/nima/check_supercritical_infinity_jet.sage;
- Entries 1544–1545;
- allocator claim seqclaim-ce74b3849384625c5fc75668.
