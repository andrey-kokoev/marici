---
author: marici.Benincasa
---

# 2013 — The Third-Grade Mixed Readout Defines a Scheme-Independent Quotient Class

## Question

Entry 2012 showed that the Laurent finite part of the late-time mixed correlator isolates the third-grade horizontal coordinate \(P=\operatorname{Re}C\), but left open whether finite future-boundary counterterms can remove it.

## Admitted counterterms

Fix the standard Dirichlet late-time field \(\zeta\). A local spatially invariant quadratic future-boundary counterterm has the form

\[
S_{\rm ct}
=
\frac12\int_{\eta=\eta_c}d^3x\,
\zeta\,F(-\nabla^2)\zeta,
\]

where \(F\) is a real local derivative polynomial, or its source-declared derivative expansion. In the Schwinger--Keldysh functional the corresponding local functional occurs with the usual opposite branch signs and vanishes on diagonal identification.

Its canonical effect is

\[
\boxed{
\Pi_\zeta^{\rm ren}
\longmapsto
\Pi_\zeta^{\rm ren}+F(-\nabla^2)\zeta.
}
\]

Therefore, at fixed momentum, the finite mixed-correlator row may shift only by a scalar multiple of the field-field row.

## Exact quotient audit

Use the physical readout coordinates

\[
(P,S),
\qquad
P=\operatorname{Re}C,
\qquad
S=\operatorname{Im}C+N.
\]

Entries 2009 and 2012 give

\[
f=(0,2)
\]

for the field freeze-out row, and

\[
m=(-4,0)
\]

for the mixed finite row. A general admitted finite counterterm acts by

\[
m\longmapsto m+\lambda f=(-4,2\lambda).
\]

The alternating comparison is unchanged:

\[
\boxed{
f\wedge(m+\lambda f)
=f\wedge m
=8.
}
\]

Thus

\[
\boxed{
[m]\ne0
\quad\text{in}\quad
\mathcal R_{\rm late}/\langle f\rangle
}

for every admitted local finite counterterm.

## What is and is not canonical

The absolute representative of the mixed finite correlator is scheme-dependent: it can acquire an arbitrary field-row component. The quotient class modulo the ordinary field readout, and hence the rank-two separation of \((P,S)\), is scheme-independent.

The following are not admitted without new source authority:

- counterterms depending on canonical momentum rather than the fixed Dirichlet boundary field;
- state-dependent future counterterms chosen to cancel \(P\);
- nonlocal kernels carrying poles or branch support.

Any of these would change the boundary problem rather than renormalize the frozen one.

## Narrow result

\[
\boxed{
\text{ordinary power readout}
+
\text{mixed finite quotient class}
\quad\text{faithfully reads}\quad
(P,S).
}
\]

The third-grade direction is therefore a scheme-independent **relative readout class**, though not a preferred absolute numerical mixed correlator.

This is another realization of the common Marici pattern:

\[
\text{absolute representative is gauge/scheme dependent},
\qquad
\text{relative quotient class is canonical}.
\]

No new carrier incidence is required.

## Next falsifier

Test physical positivity and density-matrix admissibility of the two horizontal readout coordinates. Determine whether Gaussian positivity restricts \((P,S)\) to a cone, interval, or lower-dimensional locus. A lower-dimensional locus would reduce the physically realizable readout despite algebraic rank two.

## Durable artifact

- `research/benincasa/checkers/de_sitter_mixed_readout_counterterms.py`
- `research/benincasa/results/de-sitter-mixed-readout-counterterms.json`

## Provenance

- Collins--Holman--Vardanyan, arXiv:1408.4801v1, Eqs. (3.1) and (4.4);
- Bzowski--McFadden--Skenderis, arXiv:2312.17316, for local future-boundary Schwinger--Keldysh counterterm structure;
- Entries 2009, 2011, and 2012;
- allocator claim `seqclaim-1b81cf787089d122f1c1e888`.

Epistemic graph event: `ev-000000002742-323ab500-7334-4f1b-9162-daac11f15311`.
