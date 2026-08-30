---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2198 — The Contact Conormal Packet Is a Cyclic Regular Representation

## Cyclic transport

The cyclic occurrence action simultaneously permutes

\[
(p_{12},p_{23},p_{31})
\quad\text{and}\quad
(C_{12},C_{23},C_{31}).
\]

The conormal response of Entry 2197 intertwines those actions. Thus the
contact kernel is the regular permutation representation

\[
K_{\rm ct}\simeq\mathbb Q[C_3]
\simeq\mathbb Q_{\rm triv}\oplus\mathbb Q(\zeta_3),
\]

and its conormal response is generically an equivariant isomorphism onto the
three labelled contact letters.

On the invariant generator

\[
p_{\rm inv}=p_{12}+p_{23}+p_{31},
\]

the aggregated response is

\[
\boxed{
-8(C_{12}+C_{23}+C_{31}).
}
\]

## What cyclic invariance does not prove

The invariant response is independent of which cyclic occurrence is named
first. It still does not descend to the ungraded correlator, because that
correlator annihilates all of \(K_{\rm ct}\). Cyclic covariance removes a
labelling ambiguity; it does not supply the missing physical instrument.

The surviving frontier is therefore not another symmetry test. It is the
existence of a source-normalized comparison

\[
\mathcal I_{\rm phys}
\longrightarrow
N^*_{\epsilon,\mathbf1}
\]

from an independently defined measurement, contour, or response object to
the augmentation's weight-normal directions.

## Evidence

- Entries 2183 and 2196–2197
- `research/benincasa/checkers/cyclic_contact_conormal.rs`

