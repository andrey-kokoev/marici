# Explicit RH constraint dependency DAG

Date: 2026-09-08

## Purpose

Globular rung numbers constrain cell boundaries but do not completely order source authority, completion, positivity, promotion, and diagnostics. This DAG records the additional dependency order.

## Topological order

1. Freeze the global restricted-product theta/Tate source.
2. Construct its theta incidence.
3. Construct its endpoint/conductor incidence.
4. Build the common completed domain of both incidences.
5. Perform global Fourier–Poisson sewing.
6. Form the relative-null fiber inside the sewn completed domain.
7. Apply the completed endpoint observer to the globally sewn source.
8. Construct the relative-null/endpoint coherence cell.
9. Identify its boundary class without killing it.
10. Promote that boundary, with source authority, to `D_bw`.
11. Prove relative-null coherence makes the promoted class vanish.
12. Independently prove positive-bulk admission on the common domain.
13. Apply Hermitian confinement.
14. Project to finite six-normal diagnostics.

This is a partial order, not a demand that independent branches be developed sequentially. In particular:

- theta and endpoint incidence can be developed in parallel;
- relative-null formation and completed endpoint observation can be developed in parallel after global sewing;
- positivity can be developed independently of the coherence/promotion branch after the common domain exists.

## Critical path

The current critical path is

\[
\text{source}
\to\text{endpoint incidence}
\to\text{common domain}
\to\text{global sewing}
\to\text{completed endpoint observation}
\to\text{relative-null coherence}
\to\partial\mathrm{BC}
\to D_{\mathrm{bw}}
\to\text{vanishing}
\to\text{confinement}.
\]

The first unresolved executable task is the common-source endpoint incidence. The 24 existing maps begin at local framed endpoint sources; they have not yet been assembled into one arrow from the global theta/Tate source.

## Forbidden reversals

The DAG rejects the following moves:

- finite diagnostics before global Fourier sewing;
- level-2 relative-null coherence before level-0 endpoint incidence;
- promotion before the coherence boundary is identified;
- confinement before independent positive-bulk admission;
- using six-normal target rank to manufacture common-source incidence;
- using P24 nontriviality as if it were boundary-work vanishing.

## Verification

```sh
python research/voevodsky/check_marici_rh_constraint_dependency_dag_20260908.py \
  --output research/voevodsky/marici_rh_constraint_dependency_dag_certificate_20260908.json
```

The checker validates 14 tasks, 19 dependency edges, four central forbidden reversals, and a topological ordering in 37 assertions.
