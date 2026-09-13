# A block frustration needs an allocation rule before it propagates

## Frustrated consistency

Replace exact local agreement by

\[
P_n-\rho P_{n-1}
-
F_n+\rho F_{n+1}
=\omega_n.
\]

The defect \(\omega_n\) measures the difference between the event reconstructed from the past and future presentations.

## Allocation freedom

Write those two reconstructed events as

\[
u_n^{P}=u_n+a_n,
\qquad
u_n^{F}=u_n+b_n,
\]

with

\[
a_n-b_n=\omega_n.
\]

The frustration fixes only the difference. It does not determine how much belongs to either orientation.

A one-parameter split is

\[
a_n=\theta\omega_n,
\qquad
b_n=-(1-\theta)\omega_n.
\]

The induced boundary shifts are

\[
\delta P_{N}
=
\theta\sum_n\rho^{N-n}\omega_n,
\]

\[
\delta F_0
=
-(1-\theta)\sum_n\rho^n\omega_n.
\]

Thus the same local defect can propagate entirely left, entirely right, or be split between both boundaries.

## Exact single-defect example

For \(\rho=3/5\), a defect of magnitude two at the middle of a nine-event block gives:

| allocation \(\theta\) | right past boundary | left future boundary |
|---:|---:|---:|
| 0 | 0 | \(-162/625\) |
| \(1/2\) | \(81/625\) | \(-81/625\) |
| 1 | \(162/625\) | 0 |

The local cocycle is identical in all three cases. Boundary propagation is not defined until an allocation rule is supplied.

## Gauge interpretation

Changing \((a,b)\) by

\[
(a,b)\mapsto(a+h,b+h)
\]

preserves \(a-b=\omega\). This common shift is an allocation gauge. Boundary readouts are gauge dependent unless the permitted \(h\) is restricted or quotiented.

Possible gauge-fixing rules include:

- past-causal allocation \(\theta=1\);
- future-causal allocation \(\theta=0\);
- time-symmetric allocation \(\theta=1/2\), requiring two invertible;
- minimum-energy allocation relative to a chosen metric.

None follows from the consistency defect alone.

## Boundary-invisible frustrations

If \(\omega\) lies in the two-moment kernel,

\[
\sum_n\rho^{N-n}\omega_n=0,
\qquad
\sum_n\rho^n\omega_n=0,
\]

then both boundary shifts vanish for every scalar allocation \(\theta\). Such a frustration is an intrinsically interior residual.

Three sites already suffice to construct a nonzero example.

## Consequence

The proposed obstruction theory has two stages:

```text
local frustration class omega
-> allocation/gauge choice
-> boundary anomaly pair
```

Only the two weighted moments of the allocated defect reach infinity. The remaining component stays inside the block kernel.

This mirrors the earlier realization theorem: local labelled data are high-dimensional, while the endpoint anomaly is rank two.

## Verification

```text
python research/coherence/check_frustrated_block_defect_allocation.py
```

The checker verifies exact allocation dependence for one local defect and constructs a three-site frustration invisible at both boundaries for every allocation.

Artifacts:

- `check_frustrated_block_defect_allocation.py`
- `frustrated-block-defect-allocation.v1.json`
