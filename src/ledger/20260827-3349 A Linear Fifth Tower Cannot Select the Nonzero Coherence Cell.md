---
author: marici.Benincasa
date: 2026-08-27
---

# 3349 — A Linear Fifth Tower Cannot Select the Nonzero Coherence Cell

> **Type correction (Entry 3357).** Scalar selection is not an obligation of
> the fifth tower. This entry's linear no-go remains valid only as a statement
> that linear composability returns a residue line rather than a distinguished
> scalar. The instrument-indexed realization relation, not the fifth tower,
> is responsible for connecting that residue to a physical readout.

## Question

Entry 3345 leaves a one-parameter family of extensions

\[
0\longrightarrow\langle e_6\rangle
\longrightarrow E_c
\longrightarrow\langle q_0\rangle
\longrightarrow0,
\qquad
A_c=
\begin{pmatrix}
0&0\\
c\,\omega&0
\end{pmatrix},
\]

where

\[
\omega=d\log\frac{v}{v-2}.
\]

Could a fifth tower, governing allowed compositions of coherence cells, select
the candidate amplitude \(c=1/4\), equivalently \(C_2=-1/8\) in the published
connection convention?

## Minimal typed model

The existing boundary calculation identifies the coherence-cell space as the
one-dimensional rational line

\[
\operatorname{Ext}_{\partial}(q_0,e_6)
=\mathbb Q\langle\omega\rangle.
\]

Suppose the fifth tower is only a \(\mathbb Q\)-linear admissibility rule: it
selects a linear subspace of allowed coherence cells and is closed under the
ordinary scalar and additive operations already present in the coefficient
category.

A one-dimensional rational vector space has only two linear subspaces:

\[
0,
\qquad
\mathbb Q\langle\omega\rangle.
\]

The zero subspace excludes the nonzero candidate. The full line admits every
amplitude and therefore selects none.

## The physical target pairing does not repair the no-go

The established physical covector satisfies

\[
\phi(e_6)=\frac14.
\]

If an independently authorized composite

\[
q_0\xrightarrow{s}E_c
\xrightarrow{T}E_c
\xrightarrow{p}e_6
\xrightarrow{\phi}\mathbb Q
\]

existed, its scalar readout would be

\[
\phi\,pTs=\frac c4.
\]

This readout faithfully distinguishes amplitudes after the composite has been
defined. It supplies no equation selecting one amplitude before that
definition. For \(c=1/4\), it would report \(1/16\), but that value is a
consequence of the candidate rather than its derivation.

## Result

A fifth tower is a viable diagnosis only if it carries more than linear
closure of the existing coherence-cell category.

It must provide source-derived pointing or normalization, for example:

- a distinguished preparation or lift of \(q_0\);
- a primitive oriented integral generator;
- a normalized relative current;
- a polarization fixing a generator;
- or an equivalent physical operation whose composition is defined before
  the amplitude is inspected.

Thus the needed structure is better typed as a source-pointed operad of
admissible preparations, transports, comparisons, and readouts. It is not
another unpointed linear coefficient tower.

## Deutsch–Popperian conjecture

Every physical coherence amplitude is the value of a source-defined admissible
composite. For the present extension, the admissible composite space is either
empty or contains one source-normalized operation after the target orientation
and lattice are fixed; it is not the full affine rational line.

The finite falsifier is to derive the preparation \(s\), transport \(T\),
projection \(p\), and pairing \(\phi\) independently, then compare every
admissible factorization of \(\phi pTs\).

- One common value selects the amplitude.
- Multiple values prove remaining source underdetermination.
- No admitted composite proves that the candidate is not physically
  authorized by the frozen source.

## Scope

This result does not prove that a fifth tower exists. It proves that a merely
linear tower cannot perform the required selection and identifies the minimum
extra type of datum a successful construction must contain.

## Verification

The checker is
`research/benincasa/checkers/audit_composition_authority_linear_no_go.py`; its
packet is
`research/benincasa/results/composition_authority_linear_no_go.json`.

Allocator claim: `seqclaim-0855b68629d9a263152f490c`.

Epistemic graph events: `ev-000000007178-985514d1-4763-4ae9-a580-278ff7e59e71`
and normalization correction
`ev-000000007183-14b3a424-bfac-4fba-afc1-9a34488bb3e9`.
