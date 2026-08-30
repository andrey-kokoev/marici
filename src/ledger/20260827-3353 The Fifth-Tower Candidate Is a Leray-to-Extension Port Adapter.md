---
author: marici.Benincasa
date: 2026-08-27
---

# 3353 — The Fifth-Tower Candidate Is a Leray-to-Extension Port Adapter

> **Type correction (Entry 3357).** The fifth tower identifies the allowed
> Leray/extension composition and its rank-one relational residue. A pointed
> map from that residue to a preparation--instrument system is a separate
> instrument constructor. Thus the adapter described below is not itself the
> fifth tower; it is the next realization relation connected to its output.

## Question

Entry 3349 proves that an unpointed linear admissibility tower cannot select
the nonzero rank-twelve coherence amplitude. Does the frozen source already
contain a more specific operation that could point the torsor?

## The two existing constructions

Entries 304 and 3323 derive the cyclic Leray transition

\[
g_{31,12}=\frac{X_3}{X_2}.
\]

Its logarithmic class is

\[
\ell=d\log\frac{X_3}{X_2},
\]

with primitive residue vector \((1,-1)\) on the ordered soft divisors.

Independently, Entries 3328 and 3341 identify the boundary-regular extension
line

\[
\mathcal E=
\operatorname{Ext}_{\partial}(q_0,e_6)
=\mathbb Q\langle\omega\rangle,
\qquad
\omega=d\log\frac{v}{v-2}.
\]

On the homogeneous chart, \(\ell\) and \(\omega\) have the same primitive
residue vector.

## Type distinction

The operation \(d\log\) sends a transition function to a logarithmic
connection class. It does not automatically turn that class into an
off-diagonal extension of \(q_0\) by \(e_6\).

The missing operation has type

\[
\alpha:
\mathbb Q\langle\ell\rangle
\longrightarrow
\mathcal E.
\]

Both source and target are one-dimensional difference-character lines.
Consequently

\[
\operatorname{Hom}_{\mathbb Q}
(\mathbb Q\langle\ell\rangle,\mathcal E)
\simeq\mathbb Q.
\]

Every scalar map respects the support, orientation reversal, and occurrence
character. These constraints identify the adapter line but do not point it.

The reconstructed candidate corresponds to

\[
\alpha(\ell)=C_2\omega,
\qquad
C_2=-\frac18.
\]

The zero adapter and every other rational multiple satisfy the same formal
covariance tests.

## Result

The first concrete fifth-tower object is a port adapter between two already
existing constructions:

\[
\text{cyclic Leray descent}
\longrightarrow
\text{rank-twelve relative extension}.
\]

Neither Carrier incidence, logarithmic support, primitive residues, nor
occurrence equivariance selects this adapter. The adapter must be derived as a
pointed natural transformation from the source, not introduced because its
value reproduces \(C_2\).

This clarifies why the existing evidence is unusually strong but still
insufficient: it identifies the source line, target line, support, character,
and candidate scalar. Only the arrow connecting the two functors is missing.

## Finite falsifier

Construct the source-normalized weighted Leray specialization as a functor on
the complete four-stratum relative object. Apply it to the labelled \(q_0\)
quotient generator and retain the \(e_6\) first-Rees costalk.

The fifth-tower proposal survives only if this construction produces a
lift-independent natural transformation \(\alpha\). Its value must be computed
before comparison with \(C_2\).

- If \(\alpha=C_2\), the source points the torsor at the published candidate.
- If \(\alpha=0\), the candidate extension is unauthorized.
- If \(\alpha\) depends on a weighted lift or splitting, the fifth tower has
  not been constructed.

## Scope

This entry identifies the missing operation and its exact one-dimensional
ambiguity. It does not assert that the operation exists in the frozen source.

## Verification

The checker is
`research/benincasa/checkers/audit_leray_extension_port_adapter.py`; its packet
is `research/benincasa/results/leray_extension_port_adapter.json`.

Allocator claim: `seqclaim-ff2051a8af7f41f513f23013`.

Epistemic graph event:
`ev-000000007187-0b3b4de5-8ba0-4bf8-ac6b-60e1cac01d8f`.
