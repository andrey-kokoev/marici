# The minimal finite-context realization factorizes through labelled flux seams

## Three finite carriers

Fix distinct context positions

\[
S=\{x_1,\ldots,x_n\},
\qquad y_i=e^{x_i}.
\]

There are three relevant carriers:

1. the Green state space
   \[
   E_S=\operatorname{span}\{k_{x_i}\};
   \]
2. the labelled flux space
   \[
   F_S=\bigoplus_i\mathbb C_{x_i}^{\rm flux};
   \]
3. the endpoint double
   \[
   Q=L_-\oplus L_+.
   \]

## Green-to-flux isomorphism

For

\[
f=\sum_i u_i k_{x_i},
\]

the massive equation is

\[
(1-\partial^2)f=2\sum_i u_i\delta_{x_i}.
\]

Since the delta coefficient is minus the flux jump,

\[
J_i^1=-2u_i.
\]

Thus

\[
E_S\xrightarrow{\;1-\partial^2\;}F_S
\]

is an isomorphism after the fixed normalization by \(-2\). The labelled flux carrier retains the full finite realization rank \(n\).

Its induced metric is not the plain coordinate metric. In coefficient coordinates it is the Green Gram form

\[
\langle u,v\rangle=u^*K_Sv.
\]

## Flux-to-endpoint quotient

Endpoint observation is the two-moment map

\[
(J_i^1)_i
\longmapsto
\left(
-\frac12\sum_iJ_i^1/y_i,
-\frac12\sum_iJ_i^1y_i
\right).
\]

For distinct positions its rank is \(\min(2,n)\). Therefore, when \(n\ge2\),

\[
0\to K_S^{\rm moments}
\to F_S
\to Q
\to0,
\]

where

\[
K_S^{\rm moments}
=
\left\{J:
\sum_iJ_i^1/y_i=0,
\quad
\sum_iJ_i^1y_i=0
\right\}.
\]

Its dimension is \(n-2\).

## Commuting factorization

The direct asymptotic observation of a Green packet equals its observation through flux seams:

```text
E_S  --massive operator-->  F_S
 |                            |
 | direct asymptotics         | two weighted moments
 v                            v
             Q
```

The first arrow is rank preserving. All rank loss occurs in the second arrow.

## Minimality conclusion

This localizes the realization obstruction precisely:

```text
complete labelled protocol:
  retain E_S, equivalently labelled fluxes with Green metric

endpoint-only protocol:
  quotient F_S by the two-moment kernel

infinite labelled protocol:
  complete the directed Green system to H1(R)
```

The rank reset is therefore not produced by the differential law itself. The massive operator preserves all labelled state directions. It is produced by changing the observation protocol from seam-addressable to endpoint-only.

## Verification

```text
python research/coherence/check_finite_context_realization_factorization.py
```

The checker verifies the commuting factorization and ranks for one through eight contexts using exact rational arithmetic.

Artifacts:

- `check_finite_context_realization_factorization.py`
- `finite-context-realization-factorization.v1.json`
