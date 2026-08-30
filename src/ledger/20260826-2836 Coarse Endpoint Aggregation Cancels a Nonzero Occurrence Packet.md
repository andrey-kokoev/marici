# 2836 — Coarse Endpoint Aggregation Cancels a Nonzero Occurrence Packet

## Hostile incidence test

Entry 2835 showed that an endpoint support can have a nonzero physical boundary pairing. The converse implication

\[
\text{nonempty support incidence}
\Longrightarrow
\text{nonzero coarse readout}
\]

is false.

Use the same oriented chain

\[
\Gamma_\xi=[-1,1],
\qquad
\partial\Gamma_\xi=[1]-[-1].
\]

The coarse Cayley–Menger endpoint face factors as

\[
\xi^2-1=(\xi+1)(\xi-1).
\]

## Occurrence-resolved packet

The negative and positive endpoint occurrences carry oriented coefficients

\[
r_-= -1,
\qquad
r_+=+1.
\]

Thus the resolved route packet is

\[
(r_-,r_+)=(-1,+1).
\]

Neither route vanishes.

## Coarse aggregation

The unweighted forgetful map

\[
\sigma(r_-,r_+)=r_-+r_+
\]

gives

\[
\sigma(-1,+1)=0.
\]

The zero coarse readout is therefore cancellation after aggregation, not absence of support or failure of both routes.

## Architectural consequence

The physical selection law requires three typed stages:

\[
\text{supported incidence}
\longrightarrow
\text{occurrence-resolved route packet}
\longrightarrow
\text{declared aggregation/readout}.
\]

Incidence alone is insufficient. A scalar zero must be classified as either route loss or cancellation in the aggregation kernel. This is the cosmological endpoint realization of the exact route-packet distinction already found in the magnetic sector.

## Scope

The result uses the unweighted boundary aggregation. A coefficient local system may supply nontrivial endpoint weights; those must be derived before applying a weighted sum. The present theorem forbids interpreting the unweighted zero as empty support.

## Durable artifacts

- `research/benincasa/check_occurrence_resolved_endpoint_cancellation.py`
- `research/benincasa/occurrence-resolved-endpoint-cancellation.json`
