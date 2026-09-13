# Constrained Green lifts place anomalies on the admissible boundary

## Support-constrained inverse problem

Suppose a two-boundary anomaly must be explained by coefficients supported on an allowed interior set

\[
S\subset\{1,\ldots,n-2\}.
\]

Minimize the Green energy

\[
u_S^TK_{SS}u_S
\]

subject to the two terminal moment constraints.

Let

\[
a=\min S,
\qquad
b=\max S.
\]

## Extreme-support theorem

The unique Green-minimum lift is supported only at \(a\) and \(b\):

\[
\operatorname{supp}u_*
\subseteq\{a,b\}.
\]

All allowed sites strictly between them receive zero coefficient.

## Why

On the allowed set, the left endpoint covector is proportional to the Green Gram row based at \(a\):

\[
K(0,j)=\rho^aK(a,j)
\qquad(j\in S).
\]

Similarly, the right endpoint covector is proportional to the row based at \(b\):

\[
K(n-1,j)=\rho^{n-1-b}K(b,j).
\]

Applying \(K_{SS}^{-1}\) sends these two covectors to coordinate vectors at \(a\) and \(b\). The Riesz representers of boundary observation therefore live on the extreme allowed sites.

## Nested admissible regions

If endpoint support is forbidden, the anomaly moves to the nearest allowed interior layer. If that layer is also forbidden, it moves to the next admissible boundary. It does not spread through the permitted bulk under the Green norm.

```text
allowed region S
-> identify min(S), max(S)
-> place minimum-energy anomaly there
```

## Interpretation

The previous endpoint-supported result was not an accident of permitting physical endpoints. It is a Markov property of Green energy:

> Boundary data are represented on the boundary of the admissible support region.

This is mathematically reminiscent of boundary localization, but it is not by itself a holographic or physical spacetime claim. It follows from the one-dimensional exponential Green kernel and the chosen quadratic metric.

## When bulk support can appear

A delocalized minimum requires changing at least one ingredient:

- use a non-Markov or longer-range state metric;
- impose local amplitude or sparsity constraints at the extreme sites;
- penalize boundary layers more strongly;
- require smooth source profiles rather than point coefficients;
- add interior observations or equations.

## Verification

```text
python research/coherence/check_constrained_green_anomaly_lift.py
```

The checker verifies the extreme-support theorem for 100 exact rational problems with arbitrary nonempty interior support sets containing at least two sites.

Artifacts:

- `check_constrained_green_anomaly_lift.py`
- `constrained-green-anomaly-lift.v1.json`
