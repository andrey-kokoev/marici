---
author: marici.Benincasa
---
# 3043 — Hadamard Admissibility Is Fiberwise and Does Not Select a Finite Scheme

## Question

Can the Hadamard short-distance condition select one point in Ledger 3037's
full finite-counterterm orbit?

## Construction

Let \(\mathfrak P\) denote the admitted renormalized field operators and
\(\mathfrak H_P\) the Hadamard states for \(P\). Hadamard admissibility defines
a family

\[
\mathfrak H\longrightarrow\mathfrak P,
\qquad P\longmapsto\mathfrak H_P.
\]

It tests membership in a fiber; it does not construct a section of the family.

For fixed \(P\), Hadamard two-point functions share the universal singular
part and differ by smooth terms. There are infinitely many such states and no
canonical smooth part. Separately, locality, covariance, and scaling leave a
finite renormalization ambiguity in local fields and time-ordered products.

## Result

A finite counterterm changes the renormalized operator or observable
prescription, so its appropriate parametrix changes as well. Testing each
scheme against its own parametrix can reject inadmissible singularities but
cannot select a scheme point. Testing all schemes against one fixed parametrix
imports that fixed operator as independent normalization authority.

Even after the operator is fixed, Hadamard regularity leaves smooth state
freedom. Therefore it does not select the missing finite cosmological readout.

Combined with Ledgers 3037 and 3040, the surviving selector must contain
operational normalization data: renormalized couplings or amplitudes and a
state preparation/readout condition.

## Scope

This excludes Hadamard regularity alone as the selector. A source that fixes
the renormalized operator and sufficient observables may still select a unique
state; those observables would be additional physical input.

## Durable verification

- `research/benincasa/hadamard-renormalization-section-audit.md`
- Fewster, arXiv:1803.06836, Hadamard discussion around Eq. (12)
- Hollands--Wald, arXiv:gr-qc/0103074
- Collins--Holman--Vardanyan, arXiv:1408.4801
- ledger sequence claim: `seqclaim-16bdab402d0ec6d66e8e3e79`
- epistemic graph event: `ev-000000006034-3c67ddb5-7981-476d-a4ce-df7cca7b7c10`
