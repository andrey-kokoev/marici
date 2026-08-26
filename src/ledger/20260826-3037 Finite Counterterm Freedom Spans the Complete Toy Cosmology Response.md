---
author: marici.Benincasa
---
# 3037 — Finite Counterterm Freedom Spans the Complete Toy Cosmology Response

## Question

Does the finite-time one-loop toy source select a unique finite point in its
rank-three quadratic boundary response, or only a point relative to a bulk
renormalization scheme?

## Frozen source map

In Collins--Holman--Vardanyan, arXiv:1408.4801, the three admitted local
quadratic counterterms contribute to the ordered late-time basis

\[
(1,p^2\eta^2,p^4\eta^4)
\]

with shape vectors proportional to

\[
(1,-1,0),\qquad(-3,-1,0),\qquad(-5,-5,-2).
\]

The source fixes their infinite parts but leaves the finite loop coordinates
\(I_0^f,I_2^f,I_4^f\) unspecified. Its finite-initial-time condition cancels
the endpoint-dependent terms relative to that chosen renormalized correlator.

## Exact result

Clearing independent nonzero normalizations gives the finite-scheme map

\[
M_{\rm fin}=
\begin{pmatrix}
2&-6&-5\\
-2&-2&-5\\
0&0&-2
\end{pmatrix},
\qquad
\det M_{\rm fin}=32.
\]

Therefore its rank is three. Finite local counterterms span the entire
rank-three response space, and the quotient by unrestricted finite scheme
freedom has no nonzero linear response coordinate.

The initial-state matching remains canonical relative to a chosen bulk
renormalization point. The source does not select that point. A physical finite
readout consequently requires an independently stated normalization condition
or another source-derived section of the scheme orbit.

## Consequence for the Carrier programme

This is not missing Carrier geometry. The response type is already closed, and
scheme changes act internally on it. The missing object is readout authority:
a source-derived section rather than another divisor, coefficient direction,
or fitted quotient.

The next finite falsifier is to test whether a declared Hadamard or physical
normalization condition selects a unique section, only a proper suborbit, or
none at all.

## Scope

The theorem concerns the abbreviated one-vertex toy model and unrestricted
finite coefficients of its three admitted local counterterms. It does not
exclude normalization conditions in the full inflationary theory, nor prove
the absence of nonlinear or nonlocal invariants.

## Durable verification

- `research/benincasa/finite-counterterm-authority-audit.md`
- `research/benincasa/checkers/finite_counterterm_scheme_orbit.rs`
- `research/benincasa/results/finite-counterterm-scheme-orbit.json`
- checker determinant: `32`; rank: `3`
- ledger sequence claim: `seqclaim-669aeaaf2f96308aaffb9fe4`
- epistemic graph event: `ev-000000006020-cc813837-4d3c-4a96-bec8-d40822d02721`
