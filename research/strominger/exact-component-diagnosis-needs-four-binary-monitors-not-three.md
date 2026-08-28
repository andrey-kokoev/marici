# Exact Component Diagnosis Needs Four Binary Monitors, Not Three

## Linear rank versus global diagnosis

Aspect's falsifier compiler exposed a rank-one terminal observation on a
four-dimensional linearized failure carrier. Three independent rows restore
linear rank four. That statement is correct infinitesimally and for signed
single-coordinate mutations.

It does not solve the global binary problem.

Let the four component-health bits be

\[
(l,p,c,r)\in\{0,1\}^4.
\]

The terminal sign contrast is present exactly when all four capabilities work:

\[
T(l,p,c,r)=l p c r.
\]

Only the ideal state maps to one. The other fifteen states all map to zero.

## Counting lower bound

Three additional binary monitors have at most

\[
2^3=8
\]

distinct codes inside the terminally blind fiber. They cannot separate fifteen
failure configurations. Four binary monitors have sixteen codes and are
sufficient; direct health monitors for all four components give an injective
signature.

Thus the diagnostic requirements are:

```text
linearized primitive-failure diagnosis
  terminal contrast plus three independent scalar directions

exact arbitrary binary-subset diagnosis
  four additional binary component monitors
  or fewer nonbinary ports with at least fifteen distinguishable blind outputs
```

The terminal bit becomes redundant once all four direct health bits are
available, although it remains the scientific sign readout rather than a health
monitor.

## Aspect interpretation

This is exactly the transition from the falsifier compiler to its ontology and
composition hostiles. Rank closure over a declared tangent carrier does not
imply injectivity on nonlinear or correlated mutations. The first correlated
failure class forces enlargement of the diagnostic contract.

The corrected claim is therefore:

> Three monitors repair tangent diagnostic rank; four binary monitors repair
> exact component-subset diagnosis.

Neither statement grants physical implementation authority.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/exact_component_diagnosis_lower_bound_checks.py
```

The checker exhausts all sixteen component-health states and proves the coding
lower bound.
