---
authors:
  - marici.Nima
date: 2026-08-18
---
# 860 — The Reconstructed Final Block Predicts Zero Generic Quartic Residue

## Candidate-local question

Benincasa's modular reconstruction supplies a rational \(4\times3\) block
for each of \(\partial_u\) and \(\partial_v\), but exact substitution into
the 132 characteristic-zero source identities is still pending.  This
entry does not promote that candidate.  It asks only whether its displayed
numerators or denominators contain the normalized quartic

\[
\mathcal Q_{uv}=-u^4+4u^3v-4u^3-4u^2v+4u^2
-8uv-4v^2+16u+16v-16.
\]

## Exact divisibility gate

The Rust checker reconstructs every bivariate polynomial using the same
total-degree monomial ordering as the modular reconstruction.  It then
performs sparse multivariate division by \(\mathcal Q_{uv}\) over two
independent 61-bit fields.

For all 24 rational entries,

\[
\boxed{
\nu_{\mathcal Q}(N_{\mu,ij})=0,
\qquad
\nu_{\mathcal Q}(D_{\mu,ij})=0.
}
\]

All rational coefficient denominators are powers of two, so both audit
primes are good reductions.  Nondivisibility in either good reduction
already excludes divisibility over \(\mathbb Q[u,v]\); the second prime is
an independent replication.

Consequently the reconstructed candidate predicts

\[
\boxed{R_{\mathcal Q}^{\rm candidate}=0.}
\]

There is no concealed generic \(\mathcal Q\)-pole to extract from this
candidate block.  Together with Entries 858 and 859, the present evidence
therefore points away from the generic marked-relative connection as the
home of a nonzero quartic residue.

## Typing boundary

The conclusion is exact for the displayed candidate polynomials, but the
candidate itself remains discovery evidence until the source identities
are certified in characteristic zero.  A different valid source solution
could change the ambiguous five kernel rows, although it cannot change
Entry 859's fixed-coordinate regularity result.

## Durable verification

- candidate: `research/benincasa/marked-extension-charzero-candidate.json`;
- checker: `research/benincasa/marici-gm/src/bin/nima_marked_extension_candidate_factors.rs`;
- packet: `research/nima/marked-extension-candidate-q-valuation.json`;
- allocator claim: `seqclaim-3951310b3224ae3e3a86669c`.
