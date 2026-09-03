# Deeper meaning of opposed limits and Douglas descent

## Question

Why must source limits and observer limits travel in opposite directions, and why do compatibility and uniform contraction appear as separate final gates?

## Claim boundary

The argument explains the categorical mechanism and verifies finite models. It does not construct the arithmetic contractions.

## Observation reverses variance

A source approximation is generative. Refinement adds generators:

\[
X_1\longrightarrow X_2\longrightarrow\cdots.
\]

Its completed source is a colimit. An observer into a fixed target reverses this direction. Under the relevant continuity assumptions,

\[
\operatorname{Hom}\left(\operatorname*{colim}_N X_N,Y\right)
\cong
\operatorname*{lim}_N\operatorname{Hom}(X_N,Y).
\]

This is the categorical reason for the opposed limits. The source asks what can be generated; the observer asks whether every finite restriction agrees. Generation is covariant, while testing is contravariant.

The order structure reverses for the same reason. Adding a source generator enlarges the object. Adding a positivity test intersects the admissible cone and makes it smaller.

## Conformance before order

At finite cutoff write

\[
Q_N(f)=\|A_Nf\|^2-\|B_Nf\|^2.
\]

The identities must first prove

\[
\ker A_N\subseteq\ker B_N.
\]

Only then does

\[
C_N(A_Nf)=B_Nf
\]

define a map. This is a conformance statement: equivalent presentations under \(A_N\) must remain equivalent under \(B_N\).

The order statement is separate:

\[
\|C_N\|\leq1.
\]

Conformance constructs the comparison arrow. Contractivity admits that arrow to the positive cone.

## Descent to the apex

The cutoff index \(N\) and observer-packet index \(I\) have different roles. Labelled cutoff rows \(A_N,B_N\) must first embed by appending coordinates and converge with tail control to global rows \(A,B\). Their partial forms need not be positive, so no contraction is required at finite arithmetic cutoff.

After completion, conformance defines \(C(Af)=Bf\). Positivity is then tested contravariantly on every finite observer span \(V_I\). Contractivity on all such spans gives the global contraction. Then

\[
D=(1-C^*C)^{1/2}
\]

gives the apex certificate

\[
Q(f)=\|DAf\|^2.
\]

Every finite Gram certificate is a restriction of this one object.

## Why both conditions are necessary

A compatible family \(\operatorname{diag}(1,2,\ldots,N)\) defines a coherent algebraic map but its norms diverge, so no bounded completed map exists.

The alternating family \((-1)^NI_N\) has norm one at every stage but fails restriction compatibility, so it defines no map on direct-limit equivalence classes.

The checker verifies both hostile families and a compatible uniformly contractive family through eight stages.

## Interpretation

The uniform compatible contraction has three meanings at once:

- a descent datum across cutoff stages;
- a no-leak-at-infinity estimate;
- an order-preserving cell connecting the construction pyramids to the positivity pyramid.

This also explains why endpoint, gamma, and prime sectors cannot receive independent contractions. Their negative and positive directions cancel only after entering the common completed form. The contraction belongs to the coupled apex, not to its presentation summands.

## Disposition

The remaining task is exact: prove labelled cutoff-row convergence with a tail bound, form the global coupled \(A,B\), and then prove contraction on every finite observer span. Positivity of partial arithmetic cutoffs is neither required nor expected. The direct source completion must occur before the inverse observer restrictions are tested.

## Verification

- `research/voevodsky/opposed-limits-douglas-descent-meaning-v1.json`
- `research/voevodsky/checkers/check_opposed_limits_douglas_descent_meaning.py`
- `research/voevodsky/results/opposed_limits_douglas_descent_meaning.json`
