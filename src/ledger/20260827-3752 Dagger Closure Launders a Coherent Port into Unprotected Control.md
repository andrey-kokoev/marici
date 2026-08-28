---
author: marici.Strominger
date: 2026-08-27
---

# 3752 — Dagger Closure Launders a Coherent Port into Unprotected Control

## Round-trip obstruction

Let (i:E\to S) be the coherent selector port with column vector
(i=(1,1)^T). Its external round trip is the scalar (i^\dagger i=2), but
ordinary dagger closure also generates

\[
ii^\dagger=
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

This selector endomorphism does not commute with the protected projector.
Hence freely adjoining a coherent port and its dagger launders port authority
into unprotected internal-control authority.

A sector-pure port has a protected diagonal round trip, but contains no
relative coherence and cannot detect the metaplectic sign.

## Structural consequence

Object typing alone is insufficient. The instrument needs a source-authorized
partial composition law. Protected endomorphisms and coherent ports should be
different arrow kinds, as in a colored operad or double category; a companion,
conjoint, dagger, or internal round trip must not be inferred without a typed
cell.

Executable closure therefore means closure under authorized composites, not
under every formally type-correct composite.

## Evidence

- `research/strominger/dagger-closing-a-coherent-port-launders-it-into-an-unprotected-control.md`;
- `research/strominger/checkers/coherent_port_dagger_closure_no_go_checks.py`;
- `research/strominger/results/coherent_port_dagger_closure_no_go_checks.json`.

The exact checker passes 9 of 9 gates. Checker SHA-256:
`0998ff89f1a3bcf0c917c8a10a4bdb64ef9c756f9e806964fd7324ae006d5bbc`.

Allocator claim: `seqclaim-a19395a8fbd49fc3e90d4d17`.
