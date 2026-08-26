# Distance to failure is the canonical relative margin

## Bounded question

Given a typed capability and a normalized compact realization space, can its
continuous completion margin be derived rather than guessed?

## Frozen failure geometry

Let \((X,d)\) be a compact metric space of normalized realizations. Let

\[
F\subseteq X
\]

be the closed failure set: the realizations in which the declared capability is
absent.

Define

\[
m_F(x)=d(x,F)=\inf_{y\in F}d(x,y).
\]

If \(F\) is empty, the capability cannot fail inside the declared model and no
finite failure distance is needed. Otherwise compactness makes the infimum
attained.

## Distance-margin theorem

For every \(x\in X\):

1. \(m_F(x)\geq0\);
2. \(m_F(x)=0\) exactly when \(x\in F\);
3. \(m_F\) is 1-Lipschitz:

   \[
   |m_F(x)-m_F(z)|\leq d(x,z);
   \]

4. every perturbation of size strictly less than \(m_F(x)\) remains outside
   \(F\);
5. a failure realization exists at distance exactly \(m_F(x)\).

Thus \(m_F(x)\) is the exact robustness radius against arbitrary perturbations
admitted by the frozen metric space.

The Lipschitz bound follows from the triangle inequality. Closedness gives the
zero-set statement, and compactness gives a nearest failure point.

## Canonical only relative to a metric

The failure stratum may be source-canonical while its numerical distance is
not. Replacing \(d\) by a rescaled or anisotropic metric changes the margin and
the nearest hostile perturbation.

A robustness claim must therefore freeze:

- the realization coordinates;
- the admissible perturbation directions;
- the norm or operational distance;
- normalization and gauge quotient;
- and whether perturbation cost is worst-case, average, or weighted.

Carrier geometry determines which changes are meaningful. The coefficient lens
and physical interface determine how their size is measured.

## Authorized perturbation distance

Not every ambient perturbation is physically admitted. Let
\(\mathcal R(x)\subseteq X\) be the realizations reachable from \(x\) by the
declared perturbation constructors. Define

\[
m_F^{\rm auth}(x)
=
\inf\{c(\pi):\pi\text{ is an authorized perturbation path from }x
\text{ to }F\},
\]

where \(c\) is the frozen path cost.

This can exceed the ambient distance or be infinite. It is the operational
robustness radius. Equality with ambient distance requires a constructor
realization theorem showing that nearest metric perturbations are executable.

The ambient margin diagnoses mathematical stability; the authorized margin
diagnoses control robustness.

## Matrix invertibility

Let \(X\) be a bounded finite-dimensional matrix set with operator-norm metric,
and let \(F\) be the singular matrices. For invertible \(A\),

\[
d(A,F)=\sigma_{\min}(A)=\frac1{\|A^{-1}\|}.
\]

The first equality is the exact nearest-singular-matrix theorem. The second
holds for the operator norm induced by the Hilbert norm.

Therefore determinant magnitude is not the canonical robustness margin. It
multiplies every singular value and can be tiny because many moderate
directions accumulate, or remain misleadingly large while one direction is
nearly singular after scale changes. The least singular value measures the
actual distance to failure.

## Positive effects and Gramians

For a positive semidefinite matrix \(Q\), let failure mean loss of strict
positivity. In operator norm,

\[
d(Q,F)=\lambda_{\min}(Q).
\]

This covers:

- observability Gramians;
- joint quantum target effects;
- feature Gram matrices;
- domination matrices on a frozen quotient;
- and positive Green-energy candidates at finite cutoff.

The nearest hostile perturbation subtracts the least eigenvalue along a least
eigenvector. Whether that perturbation is source-authorized is a separate
question.

## Kernel-faithfulness maps

Let \(L:V\to Y\) be a linear observation map on a frozen finite-dimensional
normalized source space. Failure is noninjectivity. With compatible Hilbert
norms,

\[
d(L,F)=\sigma_{\min}(L).
\]

For a reference augmented observation

\[
J=(L,R),
\]

the joint-faithfulness margin is \(\sigma_{\min}(J)\). If \(L\) is already
frozen and only \(R\) may vary, the relevant authorized distance is not the
ambient distance to all singular \(J\); it is the distance along the allowed
\(R\)-coordinates.

This distinction prevents an unauthorized repair row from being counted as a
nearby physical perturbation.

## Ordered-process tester frames

Let \(V\) be the real Hermitian space of admissible comb differences, and let a
finite tester family define

\[
\mathcal J:V\to\mathbb R^r,
\qquad
\mathcal J(\Delta W)_j=\operatorname{Tr}(T_j\Delta W).
\]

Failure of process faithfulness is singularity of \(\mathcal J\) on \(V\).
With frozen Hilbert-Schmidt and Euclidean metrics, the distance margin is

\[
\sigma_{\min}(\mathcal J).
\]

If testers have unequal experimental costs or variances, the correct metric is
weighted. Changing weights changes the nearest invisible process direction and
must be declared before optimization.

## Quotient and gauge typing

If physically equivalent realizations form gauge orbits, distance must be
defined on the quotient or minimized over the gauge group. Measuring raw
coordinate distance can assign positive separation to two descriptions of the
same realization.

For a compact isometric gauge group \(G\), one may define

\[
d_{X/G}([x],[y])=inf_{g\in G}d(x,gy).
\]

The failure set must be gauge invariant to descend. Noncompact gauge groups
require additional care because the infimum may fail to be attained and raw
factor gauges may escape.

## Distance-slack completion theorem

Apply the preceding compact margin-limit theorem with

\[
m=m_F.
\]

For nested feasible sets \(K_N\), define

\[
\delta_N=max_{x\in K_N}d(x,F).
\]

Then

\[
\delta_N\downarrow
\max_{x\in K_\infty}d(x,F).
\]

If every completed realization fails, the optimal finite distance to failure
collapses to zero. If the limit is positive, a completed realization has that
robustness radius.

This supplies a canonical continuous margin once both the failure set and
metric are source-typed.

## Failure-set stratification

Capability can fail in several inequivalent ways. Write

\[
F=F_1\cup\cdots\cup F_r
\]

for closed typed failure strata, such as:

- loss of injectivity;
- violation of covariance;
- seam erasure;
- loss of complete positivity;
- or unauthorized constructor dependence.

Then

\[
d(x,F)=\min_j d(x,F_j).
\]

The nearest stratum identifies the first robustness mechanism to fail under
the frozen metric. Ties are genuine multi-mechanism boundary points and should
not be forced into a unique explanation.

This is a metric definition of “first failed law,” distinct from first in a
temporal or dependency ordering.

## DPC: nearest-failure explanation

The conjecture is:

> A quantitative capability explanation should identify its closed typed
> failure stratum and the source-authorized perturbation geometry. The distance
> to that stratum is the capability's robustness margin; a proposed proxy is
> explanatory only if it is proved equivalent or quantitatively comparable to
> this distance.

Within compact metric realization spaces the distance theorem is exact. The
conjectural work lies in deriving the correct failure stratum, quotient metric,
and authorized perturbation class from the source theory.

## Critics

### The metric can be chosen to force a desired answer

Correct. That is why metric authority is part of the theorem packet. A norm
selected after observing the target failure is not explanatory.

### Nearest mathematical perturbations may be unphysical

Correct. Ambient and authorized distances must be reported separately unless a
compiler theorem identifies them.

### Distance says how close, not why failure occurs

Correct. The typed failure stratum supplies the mechanism; distance supplies
robustness. Neither replaces the constructor-level invariant explaining why
the stratum is failure.

### Infinite-dimensional distance may not be attained

Correct. The finite compact theorem gives attainment. Infinite-dimensional
problems may have only infimizing sequences and need coercivity or compactness
of the relevant perturbation class.

## Machine-readable certificate

```json
{
  "code": "distance_to_typed_failure_margin",
  "realization": "x",
  "failure_stratum": "F_j",
  "metric": "source-authorized metric identifier",
  "ambient_margin": "d(x,F_j)",
  "authorized_margin": "path-cost or null",
  "nearest_failure_witness": "y or infimizing sequence",
  "gauge_quotient_applied": true,
  "margin_proxy": "sigma_min | lambda_min | other",
  "proxy_equivalence_proved": true
}
```

## Exact falsifiers

- A capability proxy with no typed failure set.
- A distance claim with no frozen metric or normalization.
- Determinant magnitude presented as nearest-singularity distance without an
  equivalence theorem.
- Ambient nearest perturbation presented as executable without constructor
  authority.
- Raw-coordinate distance used before quotienting physical gauge.
- A nonclosed failure set presented as having zero distance exactly on failure.
- An infinite-dimensional nearest point asserted without an attainment theorem.
- A unique nearest failure mechanism claimed at a tie between strata.

## Deutschian explanation

A robust capability persists because every admissible realization within a
definite source-measured radius remains outside the typed failure stratum. It
fails when a perturbation crosses that boundary. The nearest crossing identifies
both the vulnerable direction and the amount of protection.

This is harder to vary than an arbitrary score: changing the margin requires
changing the failure semantics, perturbation geometry, or authority boundary.
Those are visible theory changes rather than coefficient tuning.

## Claim boundary

This packet proves the compact metric distance theorem and its finite matrix
instances. It does not derive a physical perturbation metric or prove that
ambient nearest failures are executable.

## Process calibration

Pre-objective: excitement 10/10, confidence 9.5/10, expected information gain
10/10. The target was a source-relative but non-arbitrary capability margin.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Distance to a closed failure stratum is the canonical continuous margin
once perturbation geometry is frozen. The remaining authority problem is the
metric and the distinction between ambient and executable perturbations.
