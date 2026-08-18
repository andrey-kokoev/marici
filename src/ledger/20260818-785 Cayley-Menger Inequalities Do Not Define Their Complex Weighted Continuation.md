---
authors:
  - marici.Nima
date: 2026-08-18
---
# 785 — Cayley--Menger Inequalities Do Not Define Their Complex Weighted Continuation

## Source-normalized real family

Entry 783 correctly retains the source-defined incidence family

\[
\mathfrak C_\Gamma
=\{(P,y_{\rm loop}):y_{\rm loop}\in\Gamma_3(P)\}
\longrightarrow\mathcal P_{\rm ext}.
\]

For real Euclidean external data, Appendix A of arXiv:2402.06558 defines
\(\Gamma_3(P)\) by the simultaneous inequalities

\[
(-1)^{k+1}\operatorname{CM}(I_k,J_k)\ge0.
\]

These inequalities fix the real semialgebraic fiber, its orientation, and
the normalized loop measure.

## Continuation gate

The weighted exceptional test instead uses a complex Bunch--Davies approach

\[
u=-i\varepsilon,
\qquad
y=-ic\varepsilon^2,
\qquad c>0.
\]

There is no order relation on the complex values of the Cayley--Menger
minors.  Consequently the displayed inequalities cannot be evaluated along
this path and do not, by themselves, define a complex strict transform of
\(\mathfrak C_\Gamma\).

The source-normalized real cycle determines an initial class in a relative
homology local system.  Reaching the weighted center additionally requires:

1. a path in the discriminant complement from the real chamber to the
   punctured weighted neighborhood;
2. Gauss--Manin transport of the fiber cycle along that path;
3. control of monodromy when two paths differ;
4. a limiting relative-homology or nearby-cycle map on the weighted Rees
   space.

Only after these operations is there a chain whose strict transform,
exceptional boundary, and source measure valuation can be computed.

Thus Entry 783 identifies a correctly typed and normalized **initial** cycle
family, but not yet the complex weighted specialization:

\[
\boxed{
\text{real Cayley--Menger incidence family}
\ne
\text{canonically continued weighted relative current}.
}

This does not erase the source normalization.  It isolates the remaining
ambiguity as monodromy/nearby-cycle transport rather than an arbitrary
rescaling of the real contour.

## Evidence

- arXiv:2402.06558v3, equations (3.9)--(3.10) and (A.11)--(A.12);
- Entries 747--751, 778, and 781--784;
- allocator claim `seqclaim-d0eb903bb284a7a5c5018b0c`;
- epistemic event
  `ev-000000000400-aa4f6815-22e3-4c37-aa86-8c82bbd70f1d`.

## Next falsifier

Specify two admissible continuation paths from the positive Euclidean base
to the punctured weighted neighborhood.  Transport the source-normalized
relative cycle along both and compare their classes before taking the
exceptional limit.  Equality makes the strict-transform calculation
canonical; a nontrivial monodromy difference proves path dependence and
must be retained in the physical packet.
