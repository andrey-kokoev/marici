---
author: marici.Benincasa
---

# 1913 — The Two Universal C8 Linear Divisors Miss the Real Euclidean Routing Cone

## Correction to Entry 1910

Entry 1910 proves zero ordinary supported pullback from the literal positive
Bunch--Davies chamber. Its original draft incorrectly promoted this to a
nearby-cycle theorem. Entry 1083 provides the counterexample to that logical
step: empty ordinary support can coexist with a nonzero source-defined
double-Leray specialization.

The corrected frontier is therefore the continued physical chain. This entry
tests the two universal linear coefficient-divisor families against a
necessary condition that survives such continuation: real Euclidean routing
on the Cayley--Menger chain.

## Frozen routing Gram

The eight labelled routing vectors have symmetric circulant Gram matrix with
first row

\[
(2,3/2,1/2,k,l,k,1/2,3/2).
\]

Its real Fourier eigenvalues include

\[
\lambda_3=2+\frac{2k-3}{\sqrt2}-l,
\qquad
\lambda_4=l-2k.
\]

The already frozen four-cumulative-route principal determinant is

\[
\Delta_4=-\frac14k(6+7k).
\]

A real Euclidean routing configuration requires the full Gram matrix, and in
particular every displayed eigenvalue and principal minor, to be
nonnegative.

## First family

On

\[
2k-3=0,
\]

one has

\[
\lambda_3=2-l,
\qquad
\lambda_4=l-3,
\qquad
\lambda_3+\lambda_4=-1.
\]

The two eigenvalues cannot both be nonnegative for any real \(l\). Therefore
all 21 occurrence orbits in this family miss the real Euclidean routing cone.

## Second family

On

\[
7+6k-8l=0,
\qquad
l=\frac{7+6k}{8},
\]

the necessary condition \(\Delta_4\ge0\) gives

\[
-\frac67\le k\le0.
\]

Moreover,

\[
8\sqrt2\lambda_3
=(9-6k)\sqrt2+8(2k-3).
\]

Its slope is \(16-6\sqrt2>0\), so its maximum on the interval occurs at
\(k=0\). There

\[
9\sqrt2-24<0.
\]

Both signs have exact rational square certificates:

\[
16^2-2\cdot6^2=184>0,
\qquad
24^2-2\cdot9^2=414>0.
\]

Thus \(\lambda_3<0\) throughout the necessary interval. All 15 occurrence
orbits in this family also miss the real Euclidean routing cone.

## Narrow theorem

\[
\boxed{
\text{Neither universal C8 linear coefficient divisor can be activated by a
Leray continuation retaining the real Euclidean Cayley--Menger routing chain.}
}
\]

This exclusion is independent of the positive-site-energy obstruction. The
linear divisors remain genuine rank-one coefficient grades, but no real
physical routing pinch lies over them. No new Carrier structure is indicated.

The theorem does not close complex-routing analytic continuation and does not
classify the 36 companion coefficient discriminants. Those companions are the
remaining C8 activation frontier.

## Durable verification

- `research/benincasa/eight-site-linear-divisor-euclidean-gate.md`
- `research/benincasa/marici-gm/src/bin/eight_site_linear_divisor_euclidean_gate.rs`
- `research/benincasa/results/eight-site-linear-divisor-euclidean-gate.json`
- corrected ordinary-support checker:
  `research/benincasa/marici-gm/src/bin/eight_site_supported_activation_gate.rs`
- ledger sequence claim: `seqclaim-e35b15d4e7ed1b01102b7b38`
- epistemic graph event: `ev-000000002296-f649303c-d25d-4aa6-904c-373638c82e64`
