# A positive metric fixes the frustration-allocation gauge

## Variational gauge fixing

Let

\[
a_i-b_i=\omega_i
\]

be the allocation of a block frustration between past and future event presentations. Choose positive costs \(w_i^P,w_i^F\) and minimize

\[
E(a,b)
=
\sum_iw_i^P a_i^2+
\sum_iw_i^F b_i^2
\]

subject to the defect constraint.

The unique minimizer is

\[
a_i=
\frac{w_i^F}{w_i^P+w_i^F}\omega_i,
\]

\[
b_i=
-\frac{w_i^P}{w_i^P+w_i^F}\omega_i.
\]

The orientation with lower assignment cost absorbs more of the defect.

## Equal-cost case

When

\[
w_i^P=w_i^F,
\]

the minimizer is the symmetric split

\[
a_i=\omega_i/2,
\qquad
b_i=-\omega_i/2.
\]

Thus half allocation is not implied by time symmetry alone over arbitrary coefficients. It is selected by an equal positive metric and requires two to be invertible.

## Exact optimality identity

Every other allocation has the form

\[
(a+h,b+h).
\]

At the minimizer, the linear cross term vanishes and

\[
E(a+h,b+h)-E(a,b)
=
\sum_i(w_i^P+w_i^F)h_i^2
\ge0.
\]

So the gauge-fixed representative is unique.

## Reflection covariance

Reflection exchanges past and future. If it also transports their costs by

\[
w^P_i\longleftrightarrow w^F_{-i},
\]

then the minimizing allocation transforms as

\[
a_i\longleftrightarrow-b_{-i}.
\]

The gauge fixing is therefore reversal covariant when the metric itself is treated as typed data.

## Boundary anomaly

After allocation, the boundary anomaly is no longer ambiguous:

\[
\delta P_N=
\sum_i\rho^{N-i}
\frac{w_i^F}{w_i^P+w_i^F}\omega_i,
\]

\[
\delta F_0=
-\sum_i\rho^i
\frac{w_i^P}{w_i^P+w_i^F}\omega_i.
\]

Here anomaly coordinates are the actual past- and future-tail boundary displacements, matching the allocation convention \(b_i<0\) for positive \(\omega_i\).

## Meaning

```text
frustration alone:
  gauge class of allocations

frustration plus positive allocation metric:
  unique representative
  definite boundary anomaly
```

A metric converts the underdetermined block obstruction into a deterministic propagation law. Different metrics define different effective causal biases.

## Verification

```text
python research/coherence/check_minimum_energy_frustration_allocation.py
```

The checker verifies exact optimality and reflection covariance in 600 rational cases.

Artifacts:

- `check_minimum_energy_frustration_allocation.py`
- `minimum-energy-frustration-allocation.v1.json`
