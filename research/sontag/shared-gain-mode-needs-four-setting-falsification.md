# Shared Gain Mode Needs Four-Setting Falsification

## Question

What is the cheapest calibration packet that can validate the shared detector
mode used by the coupled robust determinant certificate?

## Frozen model

During one static calibration epoch, suppose

\[
k_i=s_i\theta,
\qquad
(s_{XX},s_{YY},s_{XY},s_{YX})=(1,-1,1,-1).
\]

A known zero-correlation input makes the normalized calibration record equal to
the imbalance product:

\[
y_i^{\mathrm{cal}}=k_i.
\]

After sign adjustment, the shared-mode hypothesis is simply

\[
s_i k_i=\theta
\]

for all four settings.

## Exact minimum

One zero-correlation calibration record at each setting is sufficient. Compute
the four sign-adjusted values and test whether they agree. Equivalently, apply
three independent contrast rows comparing the last three adjusted coordinates
with the first.

Four setting records are also necessary for worst-case validation. If any one
setting is omitted, construct a hostile gain vector that follows the shared
mode on every measured setting and adds a nonzero deviation only at the omitted
setting. The measured packet is identical to a valid shared mode, while the
full gain vector violates it.

Thus fewer than four records can falsify some deviations but cannot certify the
complete four-setting relation.

## Bounded calibration error

Suppose each calibration yields an interval

\[
k_i\in K_i.
\]

Sign-adjust each interval, reversing endpoints when necessary. The shared-mode
model remains compatible exactly when

\[
\bigcap_i s_iK_i\ne\varnothing.
\]

Every value in that intersection is a possible common \(\theta\). An empty
intersection rejects the shared-mode Carrier. A nonempty intersection does not
select one trajectory; it supplies the coupled reachable set to the robust
determinant calculation.

This test is stronger than four marginal bounds and weaker than assuming a
point gain. It retains precisely the compatibility relation supported by the
calibration data.

## Temporal gate

The four-record minimum assumes one static calibration epoch. Sequential
measurements under uncontrolled drift do not test the same \(\theta\). The
apparatus must additionally provide one of:

- simultaneous setting channels;
- a continuously observed common-mode state;
- a schedule and drift model transporting all records to one epoch;
- or repetitions sufficient to distinguish setting dependence from temporal
  evolution.

Without this gate, a failed equality may be temporal drift rather than failure
of the shared spatial mode, while compensating drift may falsely mimic equality.

## Control interpretation

The shared-mode relation is a one-dimensional nuisance realization embedded in
four sensor coordinates. Its validation requires observing the three transverse
contrast directions. The four direct setting records supply one common-mode
coordinate plus those three residual coordinates.

This is model discrimination before robust control. The tighter reachable set
is admissible only after the calibration experiment has exposed every direction
that the model claims absent.

## Marici consequence

A low-dimensional Carrier model cannot be justified by the dimension of its
parameterization alone. Its complement must be probed. The model-validation
packet therefore belongs to the capability witness alongside the estimator:

- excitation inputs;
- observed setting coordinates;
- contrast residuals;
- calibration epoch;
- accepted common-mode interval;
- and falsification threshold.

## Verification boundary

The dependency-free checker verifies the rank-three contrast test, constructs
an indistinguishable omitted-setting hostile for every three-setting subset,
shows all four exact records detect every single-setting deviation, and tests
the interval-intersection criterion.

The result is minimal only for direct scalar zero-correlation records with no
additional hardware relation. A separate simultaneous common-mode monitor can
change the experiment design, but its coupling to all four settings then needs
its own validation.

