# A boundary anomaly has a canonical minimum-energy block lift

## Inverse problem

Let

\[
A:\mathbb R^n\to\mathbb R^2
\]

be the two-boundary moment map for block frustrations. Given a desired anomaly

\[
d=(d_R,d_L),
\]

solve

\[
A\omega=d.
\]

For \(n>2\), this has an \((n-2)\)-dimensional family of solutions.

## Minimum-energy representative

Using the Euclidean frustration energy

\[
E(\omega)=\|\omega\|^2,
\]

the unique minimizer is

\[
\omega_*
=A^T(AA^T)^{-1}d.
\]

This is the Moore--Penrose right inverse of the boundary map. It exists whenever the two boundary covectors are independent.

## Orthogonal decomposition

Every solution is uniquely

\[
\omega=\omega_*+h,
\qquad
h\in\ker A.
\]

Moreover,

\[
\langle\omega_*,h\rangle=0,
\]

and therefore

\[
\|\omega_*+h\|^2
=
\|\omega_*\|^2+
\|h\|^2.
\]

The anomaly-visible and boundary-invisible sectors split orthogonally once an energy metric is chosen.

## Interpretation

```text
boundary anomaly d
-> canonical visible frustration omega_*
+ arbitrary invisible interior block h
```

The boundary pair determines only the visible two-dimensional component. Minimum energy sets the invisible component to zero.

This is the inverse counterpart of endpoint rank reset:

- forward quotient forgets \(h\);
- minimum-energy lifting chooses \(h=0\);
- alternative lifts reintroduce an interior history.

## Metric dependence

For a positive state metric \(W\), the minimizer becomes

\[
\omega_*
=W^{-1}A^T(AW^{-1}A^T)^{-1}d.
\]

So the canonical lift is not determined by boundary data alone. It is canonical relative to the selected energy geometry.

Choosing the Green precision metric would produce a locally regularized block; choosing a diagonal metric produces the simplest amplitude penalty. Comparing these metrics is the next model-selection question.

## Verification

```text
python research/coherence/check_minimum_energy_boundary_anomaly_lift.py
```

The checker verifies exact constraints, kernel orthogonality, and energy minimality for 350 rational anomaly problems through fifteen events.

Artifacts:

- `check_minimum_energy_boundary_anomaly_lift.py`
- `minimum-energy-boundary-anomaly-lift.v1.json`
