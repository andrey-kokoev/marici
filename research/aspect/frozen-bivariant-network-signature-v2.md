# Frozen bivariant network signature v2

## Status

Version 2 is a new frozen candidate. Version 1 remains unchanged and falsified.

The only new object type is a labelled factorization-route space. The only new cell type is a matrix route associator.

Cell creation during replay remains disabled. Maximum declared cell depth remains two.

## Matrix route associator

For two bracketings with labelled route spaces \(V_L\) and \(V_R\), the cell is

\[
F:V_L\longrightarrow V_R.
\]

It must declare both bracketings, both route-label lists, and its matrix. It is not a Gram pairing. Its type is compositional: it compares two factorizations of the same declared composite.

Under independent route-basis changes,

\[
F\longmapsto U_R F U_L^*.
\]

The following laws are mandatory:

1. route-space dimensions match the matrix;
2. dagger unitarity;
3. every pentagon available in the declared packet closes;
4. gauge covariance under independent route-basis changes;
5. naturality under declared restrictions and extensions;
6. every applicable hexagon closes when braided exchange data are claimed;
7. contextual exposure is declared separately.

Scalar associators are the one-dimensional special case. No separate packet-specific scalar or matrix subtype may be created during replay.

## Admission boundary

A local matrix cannot admit a packet. Full admission requires:

- the complete fusion or route-composition table for the packet;
- all associator matrices required by every tested pentagon;
- all exchange data required by every tested hexagon;
- exact checks or a preregistered uncertainty rule;
- a declared exposure map showing which cells are instrumentally comparable.

The contract explicitly forbids promoting local unitarity, one pentagon, or numerical matrix resemblance to global coherence.

## First unused local gate

The design witness was Fibonacci route mixing. The first unused local packet is the Ising associator

\[
F^{\sigma\sigma\sigma}_{\sigma}
=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

It is unitary, mixes both routes, and remains unitary under independent domain and codomain basis changes. Therefore it passes the new cell's local schema gate.

This is not global validation. The checker records only `candidate_v2_frozen_local_schema_pass`. The next decisive test requires a complete unused fusion packet and all applicable pentagon and hexagon identities with cell creation disabled.

## Files

- Contract: `research/aspect/contracts/frozen-bivariant-network-signature.v2.json`
- Checker: `research/aspect/checkers/check_frozen_bivariant_signature_v2.py`
- Result: `research/aspect/results/frozen_bivariant_signature_v2.json`

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v2.py
```
