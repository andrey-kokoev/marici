---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2138 — The Correlator Deletion Adapter Stops at the Labelled First-Normal Module

> **RETRACTED by Entry 2143.** This entry incorrectly replaced the product of
> connected-component contact factors inside the all-deleted term by a direct
> sum. The source product has nonzero rank-one mixed variation.

## Hard-to-vary claim

The component-resolved edge-deletion adapter canonically detects the three
labelled homogeneous normal walls

\[
\nu_i=P_i^2-X_i^2=0,
\]

but its source-defined disconnected-sector readout is additive. Consequently
it does not generate the square-free second-normal module

\[
N_2=\langle\nu_1\nu_2,\nu_1\nu_3,\nu_2\nu_3\rangle.
\]

## Source calculation

For every isolated component incident to two deleted internal energies, the
component pole is

\[
q=L+y_a+y_b.
\]

Eliminating its two-distance Cayley--Menger critical equations gives, up to a
nonzero source-fixed unit,

\[
\operatorname{Landau}(q)
=p_f^2(p_f-L^2)^3\Lambda^3.
\]

At the three isolated-vertex contacts this specializes cyclically to

\[
P_i^2-X_i^2=\nu_i=0.
\]

The disconnected deleted graph contributes the direct sum of its connected
component readouts. Near the homogeneous locus its singular part therefore
has the form

\[
F_1(\nu_1)+F_2(\nu_2)+F_3(\nu_3),
\]

so every mixed normal derivative vanishes:

\[
\partial_{\nu_i}\partial_{\nu_j}F=0
\qquad(i\ne j).
\]

Multiplying component contributions would manufacture a coupling absent from
the frozen correlator adapter.

## Relation to the earlier lower-sector frontier

Entry 698 locates the generic lower algebraic letters in (N_2), and Entries
699--718 exhaust their intrinsic pair--triple Kummer/incidence mechanism. The
present calculation is independent: it shows that the later correlator
edge-deletion adapter reaches the labelled first-normal module but supplies no
new bridge to (N_2).

Thus it neither reopens the apparent-quartic verdict nor supplies a missing
derived pushforward comparison.

## Classification

- carrier: existing labelled edge-deletion and connected-component incidence;
- coefficient support: the existing normal, soft, and triangle walls;
- second-normal coupling: absent from this adapter;
- \(\mathcal Q\): not tested and not reopened;
- new carrier datum: none.

## Narrow conclusion

\[
\boxed{
\text{edge deletion explains where each }\nu_i\text{ enters the correlator,
but not how distinct }\nu_i\text{ couple.}
}
\]

Any mixed square-free normal class must come from a single connected
coefficient object, a derived pushforward, or a physical readout that is
independently present in the source. It cannot be obtained by multiplying
additive deleted sectors.

## Evidence

- Entries 698--718 and 2135--2137;
- `research/benincasa/marici-gm/src/bin/three_site_deletion_landau.rs`;
- `research/benincasa/marici-gm/src/bin/additive_contact_normal_grade.rs`;
- allocator claim `seqclaim-7293f3af061a9c183184246b`.

## Next falsifier

Do not continue inside the disconnected deletion cube. Instead freeze one
source-defined connected coefficient object in which two labelled normal
directions coexist before pushforward, and test whether its associated
second-normal comparison is nonzero. If no such object exists beyond the
already exhausted lower marked-relative system, the correlator-adapter route
is closed at second normal order.
