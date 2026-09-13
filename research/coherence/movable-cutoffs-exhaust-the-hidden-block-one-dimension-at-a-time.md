# Movable cutoffs exhaust the hidden block one dimension at a time

## Observation family

For the Green block

\[
K_{ij}=\rho^{|i-j|},
\]

an observer placed at context \(i\) reads the corresponding Green moment

\[
y_i=K_{i,*}u.
\]

Choose \(m\) distinct observer cuts and stack their rows into \(A_m\).

Because \(K\) is positive definite, every distinct subset of rows is independent. Hence

\[
\operatorname{rank}A_m=m.
\]

## Visible and hidden dimensions

The observation-induced splitting has

\[
\dim V_m=m,
\qquad
\dim H_m=n-m.
\]

Each independent movable cutoff removes exactly one dimension from the hidden interior kernel.

At complete coverage,

\[
m=n,
\qquad
H_n=0.
\]

All event coefficients are then reconstructible from the observer packet:

\[
u=K^{-1}y.
\]

## Tomography capacity

First-order leakage tomography measures the cross-block

\[
V_m\longrightarrow H_m.
\]

Its maximum possible parameter count is

\[
C(m)=m(n-m).
\]

This has three regimes:

```text
few observers:
  large hidden sector, few probes

half coverage:
  maximal visible-hidden cross capacity

complete coverage:
  no hidden sector, hence no leakage channel
```

For \(n=12\), the capacity sequence peaks at

\[
C(6)=36.
\]

## Important distinction

Maximum state observability and maximum leakage-tomography capacity occur at different points:

- state observability increases monotonically with observer count;
- cross-block leakage capacity peaks at half coverage and then decreases.

Once every direction is visible, there is no “hidden leakage” left to measure. Metric reconstruction must then use changes within the visible response itself rather than visible-to-hidden transfer.

## Block interpretation

A single global block can support a nested hierarchy of observer-accessible quotients:

\[
H_0\supset H_1\supset\cdots\supset H_n=0.
\]

Observer motion does not alter the block. It changes which linear functionals are operationally available and therefore which histories remain equivalent.

This supplies a precise finite definition of an internal observer:

> An observer is a selected family of admissible cutoff functionals, together with the reconstruction metric used to split visible from hidden state.

## Verification

```text
python research/coherence/check_movable_cutoff_observability.py
```

The checker verifies all ranks and dimensions exactly for twelve contexts.

Artifacts:

- `check_movable_cutoff_observability.py`
- `movable-cutoff-observability.v1.json`
