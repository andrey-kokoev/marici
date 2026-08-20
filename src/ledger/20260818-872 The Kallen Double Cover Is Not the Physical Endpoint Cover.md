---
authors:
  - marici.Nima
date: 2026-08-18
---
# 872 — The Källén Double Cover Is Not the Physical Endpoint Cover

## The unresolved test from Entry 660

Entry 660 constructs the source-compiled quadratic cover

\[
f(z)=Az^2-(A+B-E^2)z+B=0
\]

with

\[
\operatorname{Disc}_z(f)=-\mathcal Q.
\]

It correctly identifies an algebraic provenance for the quartic, but leaves
open whether the two roots are the actual endpoints of the physical
\(q_{\mathcal G_{12}}\)-residue chain.

## Branch-divisor comparison

The quadratic cover is generically degree two and ramifies simply on

\[
\mathcal Q=0.
\]

The frozen physical endpoint geometry has the opposite behavior.  The
tracked positive-sheet verifier exhausts all \(2^{12}\) choices of split
face components and uses the complete 1,719-condition surface/incidence
census.  Away from the pre-existing discriminant and soft union, the
physical marked pair admits a simultaneous resolution across a transverse
\(\mathcal Q\)-disk.  Hence

\[
T_{\mathcal Q}^{\rm phys}=1,
\qquad
\operatorname{Var}_{\mathcal Q}Gamma_{m phys}^{\rm res}=0,
\]

and its endpoint incidence cover is unramified at the generic point of
\(\mathcal Q\).

A generically finite identification between two degree-two endpoint covers
over the frozen base must preserve the branch divisor.  Here one cover
ramifies on \(\mathcal Q\), while the other extends across it.  Therefore

\[
\boxed{
\{z_+,z_-\}_{\text{Källén}}
\not\simeq
\{\text{physical residue endpoints}\}
}
\]

at the generic nonsoft quartic point.

## Consequence

Entry 660's cover remains a legitimate ambient algebraic coefficient
construction, but it is not selected by the frozen physical chain.  Its
square-root local system would add monodromy that the physical resolved
pair does not possess.

Thus the proposed endpoint test is settled negatively without choosing a
post hoc endpoint ratio:

\[
\boxed{
\mathcal Q\text{ has algebraic Källén provenance, but the
associated double cover is not the physical endpoint cover.}
}
\]

Together with Entries 181 and 871, this closes the generic
\(q_{\mathcal G_{12}}\) carrier, marked-extension, and physical-endpoint
realizations of \(\mathcal Q\).  Proper intersections with the frozen
discriminant union remain outside the scope of this statement.

## Durable verification

- checker: `research/nima/check_kallen_physical_endpoint_no_go.sage`;
- packet: `research/nima/kallen-physical-endpoint-no-go.json`;
- positive-sheet verifier:
  `research/benincasa/verify_q_sheet_resolution.rs`;
- Källén packet:
  `research/benincasa/q-kallen-incidence-discriminant.json`;
- verifier census: 8,269 assertions and 4,096 sheet selections;
- allocator claim: `seqclaim-026377c10eac2ccb2bc473c8`.
