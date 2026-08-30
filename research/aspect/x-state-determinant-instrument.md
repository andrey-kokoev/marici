# Optical determinant instrument for labelled X states

## Question

Can an optical instrument reach the invariant partial-transpose boundary for
an asymmetric labelled X state, where the simpler linear witness can fail?

## Measurement map

Write `b` and `c` for the `01` and `10` populations and `z` for the corner
coherence between `00` and `11`. A joint computational-basis measurement gives
`b` and `c`. Four joint Stokes settings isolate both quadratures of `z` even
when the other X-state coherence `w` is present:

```text
Re(z) = (XX - YY)/4
Im(z) = -(XY + YX)/4.
```

The sums and differences cancel `w`; no assumption that the nuisance
coherence vanishes is required.

## Invariant decision

The relevant partial-transpose block has determinant `bc - |z|^2`. Define
the signed NPT residual

```text
Delta = Re(z)^2 + Im(z)^2 - bc.
```

Positive `Delta` is exactly the NPT side of this labelled X-state boundary.
This test is phase invariant once both quadratures have been measured.

## Decisive hostile

Freeze `b=1/100`, `c=9/100`, and `z=(3+4i)/100`, with a nonzero nuisance
coherence. The determinant residual is `1/625`, so the state is on the NPT
side. The phase-aligned linear witness using only `Re(z)` is nevertheless
`1/50`, hence nonnegative and inconclusive.

The failure is structural. Asymmetric leakage replaces the arithmetic mean in
the linear witness by the geometric boundary `sqrt(bc)`, while complex phase
makes a single quadrature insufficient. The five-setting determinant
instrument repairs both losses.

## Optical requirements

The instrument needs independently adjustable polarization analyzers on both
ports, coincidence-resolved `Z` populations, and the four correlation
settings `XX`, `YY`, `XY`, and `YX`. The analyzer phase frame must be calibrated
across those settings. Without that shared frame, the reconstructed
quadratures do not define one complex coherence.

## Verification

Run:

```text
python research/aspect/checkers/check_x_state_determinant_instrument.py
```

The dependency-free exact checker reconstructs `z` in the presence of
nuisance `w`, verifies the hostile, rejects a PPT control, and recovers the
known symmetric-leakage branch.

## One-sided robust certificate

The nonlinear residual must not be evaluated by simply inserting noisy point
estimates. Let each of the four correlation records have absolute error at
most `eta`, so each reconstructed quadrature has radius `r_z = eta/2`. Let
the population estimates have radius `r_p`. A safe lower bound is

```text
max(|Re(z_hat)|-r_z,0)^2
+ max(|Im(z_hat)|-r_z,0)^2
- (b_hat+r_p)(c_hat+r_p).
```

Only a strictly positive lower bound certifies NPT. At correlation radius
`1/100` and population radius `1/1000`, the asymmetric hostile retains lower
bound `849/1000000`.

The checker also freezes a true boundary state and pushes every estimate in
the adverse direction. Naive point substitution reports the false positive
`449/1000000`; the interval certificate correctly returns zero and withholds
the claim.

A common exact phase rotation preserves the determinant because it preserves
the quadrature norm. Differential frame drift, unequal quadrature gain, and
cross-setting covariance are outside this componentwise error box and require
separate calibration.

Run:

```text
python research/aspect/checkers/check_robust_x_state_determinant_instrument.py
```

## Separate finite-count contract

The three-correlation sewing contract does not automatically apply here. The
determinant instrument has six scalar estimates: four correlations and the
two populations extracted from one joint `Z` record. Give each correlation
statistical and systematic radius `17/2000`, and give each population
statistical and systematic radius `1/400`.

Acquire `276817` binary products in each correlation setting and `800000`
joint population trials. The correlation and population Hoeffding exponents
are each at least ten. A union bound over all six two-sided deviations is at
most `12 exp(-10)`. A rational Taylor lower bound for `exp(10)` proves this is
strictly below `1/100` without floating-point evaluation.

The resulting total radii are `17/1000` per correlation, `1/200` per
population, and `17/2000` per reconstructed quadrature. The asymmetric hostile
retains determinant lower bound `59/2000000` at confidence greater than
`99/100`.

The acquisition uses `1907268` events. This is deliberately a measurement
certificate, not a claim that the source follows a noise trajectory through a
predicted crossing.

Run:

```text
python research/aspect/checkers/check_finite_count_x_state_determinant.py
```
