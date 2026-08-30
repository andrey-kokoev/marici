# Set-Valued Gain Observation Yields a Robust Determinant Margin

## Question

When detector calibration and drift determine only an interval of possible gain
imbalance, what exact NPT statement survives every compatible sensor trajectory?

## Exact interval transport

Under the factorized detector model, invert the observed correlation \(y\) at
imbalance product \(k\):

\[
C(y,k)=\frac{y-k}{1-ky}.
\]

For \(|y|<1\) and \(|k|<1\), the map is increasing in \(y\) and decreasing in
\(k\). Hence

\[
y\in[y_-,y_+],
\qquad
k\in[k_-,k_+]
\]

gives the exact interval hull

\[
C\in
\left[
C(y_-,k_+),
C(y_+,k_-)
\right].
\]

This is a set-valued nuisance observer. It propagates every calibration and
drift trajectory compatible with the declared bounds instead of selecting one
nominal gain.

## Determinant set transport

Transport the four setting intervals through

\[
\operatorname{Re}z=\frac{C_{XX}-C_{YY}}{4},
\qquad
\operatorname{Im}z=-\frac{C_{XY}+C_{YX}}{4}.
\]

For an interval \(I=[a,b]\), define its distance from zero by

\[
d(I,0)=
\begin{cases}
0,&0\in I,\\
\min(|a|,|b|),&0\notin I.
\end{cases}
\]

If population intervals are \(b\in B\) and \(c\in C\), a safe determinant
lower margin is

\[
d(I_{\operatorname{Re}z},0)^2
+d(I_{\operatorname{Im}z},0)^2
-\max_{b\in B,c\in C}bc.
\]

A strictly positive value certifies NPT for every compatible gain and
population state. Otherwise the instrument withholds the claim.

## Two exact dispositions

For Aspect's true-boundary gain hostile, gain intervals containing the actual
imbalances produce a nonpositive worst-case margin. The positive naive point
residual is correctly rejected.

For a separated NPT fixture with both coherence quadratures equal to one tenth
and population product one two-hundredth, narrow gain intervals around the
actual setting gains retain a strictly positive worst-case margin. Thus the
set observer does not merely become conservative everywhere; it certifies when
the physical separation exceeds the reachable nuisance effect.

## Dynamic origin of the gain set

The interval \([k_-,k_+]\) must be the reachable set of a declared calibration
and drift model. Examples include:

- simultaneous calibration with a finite measurement interval;
- affine bracketing with bounded anchor error;
- bounded-rate drift propagated between calibration epochs;
- a monitored gain state with bounded process and observation disturbance.

An arbitrary analyst-chosen interval is not a Carrier state estimate. Its
lineage must identify the calibration records, propagation law, setting, and
science epoch from which it was constructed.

## Control interpretation

The robust NPT margin is an output-separation margin between two reachable
sets: the set of physical correlations compatible with the calibrated sensor
dynamics and the PPT boundary. It is the detector analogue of a robust safety
certificate.

This suggests a general Marici rule: a nonlinear decision built from corrected
records should be evaluated over the full reachable estimator set. A decision
at one nominal reconstructed state is not robust evidence when an unobserved
nuisance direction can cross the decision boundary.

## Verification boundary

The dependency-free checker proves the exact monotone corner rule by rational
derivatives, transports the four intervals, rejects the boundary false
positive, and certifies the separated NPT fixture. It assumes independent
rectangular gain sets and exact populations. Coupled gain covariance can yield
tighter bounds and should be retained when a calibration model supplies it.

