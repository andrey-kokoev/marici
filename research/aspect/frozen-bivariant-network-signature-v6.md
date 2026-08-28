# Frozen transport-enriched resolved network signature v6

## Status

Version 6 is a new frozen local candidate. Version 5 remains unchanged and falsified.

v6 adds the missing covariant half of resolved coherence: transport along the path groupoid of every resolved stratum.

## Repair of the v5 hostile

For a resolved metric route line over a circle, v5 could not distinguish flat holonomy (+1) from flat holonomy (-1). Both packets had identical metric, determinant, radical, valuation, crossing-form, and chart-transition data.

v6 declares a metric local system

\[
\rho:\Pi_1(S)\longrightarrow \operatorname{Iso}(R,G)
\]

on every resolved stratum (S). Global parallel records are the common fixed space of the loop holonomies:

\[
R^{\rho}=\bigcap_{\gamma}\ker(\rho(\gamma)-I).
\]

The retained boundary port is the quotient

\[
B_{\rho}=R/R^{\rho}.
\]

For holonomy (+1), the parallel-record dimension is one and the retained port is zero. For holonomy (-1), the parallel-record dimension is zero and the retained port has dimension one. The v5 hostile is therefore distinguished without adding a packet-specific cell.

## Functorial transport law

Transport is not an arbitrary list of isometries. It is a functor from the stratum path groupoid. It must preserve identities and composition, and the matrices assigned to a groupoid presentation must satisfy every defining relation exactly.

Changing charts or route frames conjugates the representation. Admission is invariant under that gauge change and under a change of groupoid presentation.

## Specialization law

If (J:R_{\mathrm{near}}\to R_{\mathrm{exc}}) specializes a nearby route system to an exceptional stratum, then corresponding loop transports must obey

\[
J\rho_{\mathrm{near}}(\gamma)=\rho_{\mathrm{exc}}(\operatorname{sp}\gamma)J.
\]

This prevents a locally valid holonomy from being silently erased at degeneration. Completed sewing still precedes finite projection.

## First unused hostile

Take a rank-two Euclidean route space over a torus. Assign its two loop generators the Pauli matrices

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Each generator is individually metric. But torus generators must commute, while

\[
XZX^{-1}Z^{-1}=-I.
\]

v6 rejects this packet. Individual metricity cannot be promoted to a path-groupoid representation.

## Frozen exclusions

v6 forbids:

- promoting bundle gluing to flat transport gluing;
- promoting local parallel sections to global parallel records;
- accepting generator isometries without groupoid relations;
- discarding a nonzero retained boundary port;
- erasing holonomy during exceptional specialization;
- adding packet-specific transport cells during replay.

## Next falsifier

The next attack should use a degenerating local system whose monodromy changes under exceptional specialization, or a completed system with an infinite-dimensional unit-modulus boundary spectrum. That tests whether finite path-groupoid data survive completion.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v6.py
```
