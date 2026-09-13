# Boundary-leakage tomography sees only the visible-hidden cross-block

## Sector decomposition

The boundary map splits the state space, relative to the Green metric, into

\[
V=\operatorname{range}P,
\qquad
H=\ker A,
\]

where

\[
\dim V=2,
\qquad
\dim H=n-2.
\]

Here \(V\) contains minimum-energy boundary lifts and \(H\) contains boundary-invisible interior histories.

## What leakage measures

For a metric perturbation \(G\), first-order leakage from a boundary lift \(u_0\in V\) is

\[
\dot u=-(I-P)K^{-1}Gu_0.
\]

Consequently, experiments using arbitrary boundary targets probe only the operator

\[
V\longrightarrow H,
\qquad
u\longmapsto(I-P)K^{-1}Gu.
\]

This is the visible-hidden cross-block of the metric perturbation.

## Invisible perturbations

Two large sectors cannot be recovered by this protocol at first order:

1. perturbations acting entirely within \(V\), because \(I-P\) removes their response;
2. perturbations acting entirely within \(H\), because boundary-prepared states never enter that sector.

For a symmetric perturbation, the detectable cross-block has at most

\[
2(n-2)
\]

independent parameters, far fewer than the

\[
\frac{n(n+1)}2
\]

parameters of a general symmetric metric perturbation.

## Exact witnesses

Let \(v\in V\) and \(h\in H\). Symmetric metric perturbations of the forms

\[
G_{VV}=Kv v^TK,
\qquad
G_{HH}=Kh h^TK
\]

produce zero first-order leakage for every boundary target.

The cross perturbation

\[
G_{VH}=K(hv^T+vh^T)K
\]

is detected.

## Consequence

Bulk leakage is useful but incomplete tomography:

```text
boundary preparations + interior leakage measurement
-> recover visible/hidden coupling
-> cannot recover visible/visible metric
-> cannot recover hidden/hidden metric
```

Full metric identification requires interior preparations, interior forcing, or additional movable-cutoff observation maps that enlarge the visible sector.

This gives a precise operational role to movable observers: each new independent cutoff can expose previously hidden metric blocks.

## Verification

```text
python research/coherence/check_first_order_metric_tomography_limit.py
```

The checker constructs exact rational visible-visible and hidden-hidden perturbations with zero response, and a visible-hidden perturbation with nonzero response.

Artifacts:

- `check_first_order_metric_tomography_limit.py`
- `first-order-metric-tomography-limit.v1.json`
