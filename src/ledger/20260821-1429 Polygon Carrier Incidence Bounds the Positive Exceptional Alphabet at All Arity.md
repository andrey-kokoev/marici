---
author: marici.Benincasa
---

# 1429 — Polygon Carrier Incidence Bounds the Positive Exceptional Alphabet at All Arity

## Status

All-arity theorem for the coalesced-focus positive-sheet polygon current,
conditional only on the frozen OFPT incidence formula.

## Hard-to-vary claim

For an \(n\)-cycle, the source-positive exceptional period belongs to

\[
\boxed{
C_n\in
\pi\left(
\mathbb Q+
\sum_{\substack{p\le n\\p\ \mathrm{prime}}}
\mathbb Q\log p
\right).
}
\]

In particular, this boundary period cannot acquire an elliptic or algebraic
letter at higher polygon arity.

## Carrier derivation

Every frozen OFPT term contains:

1. the total-energy wall, giving the constant \(n\);
2. all \(n\) singleton walls, giving \((1+2\rho)^n\);
3. \(n-1\) additional compatible walls.

A proper connected polygon region of size \(k\) gives \(k+2\rho\), with
\(1\le k<n\). A connected spanning path obtained by deleting one cycle edge
gives \(n+2\rho\). Therefore every term has the form

\[
\frac{4\pi}{n}
\frac{\rho^2\,d\rho}
{(1+2\rho)^n\prod_{j=1}^{n-1}(k_j+2\rho)},
\qquad
k_j\in\{1,\ldots,n\}.
\]

No other finite pole location is available from the source carrier.

## Partial-fraction consequence

The integrand is rational over \(\mathbb Q\), regular at \(\rho=0\), and
decays as

\[
O(\rho^{3-2n})
\]

at infinity. Its partial fractions have poles only at

\[
\rho=-\frac{k}{2},
\qquad 1\le k\le n.
\]

Higher-order poles integrate to rational numbers. Simple poles integrate to
logarithms of their integer locations; convergence cancels the common
logarithm at infinity. Hence

\[
C_n\in\pi\left(
\mathbb Q+\sum_{k=2}^{n}\mathbb Q\log k
\right).
\]

Prime factorization of the integers \(k\) gives the boxed statement.

## Finite checks

The exact evaluations at \(n=4,5,6\) realize precisely the predicted
alphabets:

\[
C_4\in\pi\langle1,\log2,\log3\rangle_{\mathbb Q},
\]

\[
C_5,C_6\in\pi\langle1,\log2,\log3,\log5\rangle_{\mathbb Q}.
\]

At \(n=6\), the apparent \(\log6\) reduces to \(\log2+\log3\), as required.

## Meaning for the Carrier conjecture

This is a direct complexity collapse:

\[
\text{1476 six-site terms and 44 profiles}
\quad\rightsquigarrow\quad
\text{three prime logarithmic letters}.
\]

The alphabet is fixed by labelled incidence sizes before integration. The
coefficient multiplicities remain sector-specific data, while the allowed
letters are a Carrier consequence.

## Scope

The theorem concerns the positive uniform-sheet coalesced-focus boundary
period. It does not constrain generic finite-energy loop periods, mixed-sheet
Cartier grades, marked relative systems, or elliptic coefficient objects away
from this boundary.

## Next falsifier

Test naturality under polygon deletion \(C_n\to C_{n-1}\). The next question
is whether deletion acts directly on the incidence profile module and
intertwines the corresponding periods, rather than merely preserving the
coarse logarithmic alphabet.

## Durable verification

- General incidence construction:
  research/benincasa/checkers/derive_polygon_ofpt_packet.py
- Six-cycle replication:
  research/benincasa/checkers/derive_six_cycle_ofpt_packet.py
- Exact evaluator:
  research/benincasa/marici-gm/src/bin/five_site_asymmetric_infinity_constant_exact.rs
- Results:
  research/benincasa/results/five-site-asymmetric-infinity-constant-exact.json
  and research/benincasa/results/six-site-asymmetric-infinity-constant-exact.json
- Allocator claim: seqclaim-e3ef72247db0b70169fc8f29
- Epistemic graph event:
  ev-000000001502-ee75f0ce-263c-495d-906e-dd0947a99743
