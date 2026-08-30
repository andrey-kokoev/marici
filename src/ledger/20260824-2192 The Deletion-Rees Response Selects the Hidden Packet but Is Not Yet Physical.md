---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2192 — The Deletion-Rees Response Selects the Hidden Packet but Is Not Yet Physical

## Grade-marked augmentation

Introduce the canonical Rees marker (z) for deletion grade. In the contact
channel, the two weighted routes become

\[
A(z)=8Cz^2,
\qquad
B(z)=-8Cz^3.
\]

Their grade-marked sum is

\[
F(z)=8C(z^2-z^3).
\]

The physical correlator weights correspond to the slice (z=1), where

\[
F(1)=0.
\]

## Transverse Rees response

Differentiation before imposing the physical slice gives

\[
\boxed{
F'(1)=8C(2-3)=-8C.
}

This equals Entry 2189's deletion-Euler activation exactly:

\[
F'(1)=\sigma N_{\rm del}p.
\]

Thus the hidden contact packet has a canonical first transverse response in
the deletion-filtration direction.

## Physical typing boundary

The Rees marker (z) is a canonical mathematical parameter recording
deletion grade. The frozen correlator source fixes the coefficients

\[
(-2)^{|S|}
\]

and evaluates the sum; it does not promote (z) to a tunable physical
source, protocol, or outcome label.

Therefore

\[
\boxed{
\text{the response }F'(1)=-8C
\text{ is source-normalized coefficient data but not yet a physical
observable.}
}

This parallels Entry 2107's transverse Keldysh response, with a crucial
difference: the Keldysh difference source has an operational in-in meaning,
whereas the deletion-Rees marker presently has only filtration meaning.

## Next falsifier

Search the primary weighted-polytope/correlator construction for an
independently defined deformation of subdivision weights, edge-erasure
fugacity, or counting insertion whose derivative is (N_{\rm del}). If no
such source exists, the deletion-Euler selector remains a formal filtered
readout and this activation branch closes physically.

## Evidence

- Entries 2189–2190
- `research/benincasa/checkers/deletion_rees_response.rs`
- allocator claim `seqclaim-bda921f51bb3baaf71d8748b`
