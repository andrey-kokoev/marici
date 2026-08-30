# Detector Gain Is a Nuisance-State Observability Problem

## Control question

Aspect's detector-gain audit derives the exact observation law

\[
y=\frac{C+k}{1+kC},
\]

where \(C\) is the true Stokes correlation and \(k=e_Ae_B\) is the product of
the two local detector imbalances. Exact efficiency correction works when
\(k\) is known at acquisition time. What can the determinant records identify
when \(k\) is not independently observed?

## Exact non-identifiability

For every admissible pair \((C,k)\), the same observed value \(y\) is produced
by the balanced-detector pair \((C',0)=(y,0)\). Thus the map

\[
(C,k)\longmapsto y
\]

is not injective.

Apply Aspect's setting-dependent hostile to the true-boundary packet. One
physical explanation has determinant residual zero and nonzero imbalance
products. A second explanation takes the biased correlations as the true
correlations and sets every imbalance product to zero. It has the same observed
packet and a strictly positive determinant residual.

Therefore the determinant sign is not identifiable from the four normalized
correlations and populations alone. This is structural aliasing between plant
state and sensor state, not merely a larger error bar.

## Active calibration makes the nuisance observable

The cheapest exact calibration input has known true correlation \(C=0\). Its
observed value is

\[
y_{\mathrm{cal}}=k.
\]

Once \(k\) is measured for the relevant setting and epoch, invert the observation
law:

\[
C=\frac{y-k}{1-ky}.
\]

The calibration input supplies persistent excitation in the nuisance direction.
It separates a detector imbalance from a physical correlation without relying
on the target state itself.

The calibration record must share:

- analyzer setting;
- detector channel assignment;
- acquisition epoch;
- gain regime and saturation state;
- and lineage to the corrected science record.

Otherwise terminal correction joins states from different sensor trajectories.

## Drift gate

A calibration performed at another time is not automatically a state estimate
for the measurement time. There are three admissible constructions:

1. simultaneous calibration or a continuously monitored gain port;
2. bracketing calibrations plus a source-derived drift model, such as affine
   drift over the bracket;
3. a robust set-membership certificate propagating a bounded gain trajectory.

Using a stale value without one of these constructors is an open-loop assumption.
In the exact hostile, a stale balanced calibration leaves the false-positive
determinant unchanged.

For affine drift, two calibration anchors determine the nuisance value at the
intermediate measurement exactly. For arbitrary drift they do not. The drift
model is therefore part of the Carrier dynamics, not a numerical interpolation
convention.

## Robust certificate

If calibration supplies only a set \(k\in K\), first map the entire set through

\[
C(k)=\frac{y-k}{1-ky}
\]

for every setting. Then minimize the determinant residual over the resulting
joint correlation set and population-error set. Componentwise radii are safe
only if they enclose this nonlinear image and its cross-setting covariance.

A strictly positive worst-case residual certifies NPT. A positive residual at
one fitted gain trajectory does not.

## Marici consequence

The instrument Carrier must include the sensor state and its estimator, not only
the corrected scalar record. The relevant capability witness joins:

- the science preparation;
- the analyzer Task;
- detector-gain dynamics;
- calibration excitation;
- gain estimate or uncertainty set;
- corrected correlation;
- and the determinant decision.

This is an example where control theory adds a missing Marici piece: a record
can be algebraically calibrated yet not dynamically identifiable. The missing
constructor is the nuisance-state observation channel with lineage and a drift
model.

## Verification boundary

The dependency-free exact checker reproduces Aspect's false-positive hostile,
constructs the balanced-detector observational alias, verifies exact recovery
from a zero-correlation calibration, shows stale calibration fails, and verifies
affine interpolation from two bracketing calibration anchors.

The result assumes Aspect's factorized imbalance law and zero transverse local
marginals. It does not cover dead time, accidentals, saturation, or
nonfactorizable detector coupling.

