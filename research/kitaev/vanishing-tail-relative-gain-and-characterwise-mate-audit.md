# Vanishing-tail relative-gain theorem and characterwise mate audit

## Question

When can a norm-small coherence tail do more than repair a finite algebraic identity, and which additional structure is required for that repair to remain faithful under completion?

## Claim boundary

Let \(S_N\) be the source-authorized reachable subspace with Gram norm \(\|\cdot\|_{G_N}\). Let \(A_N:S_N\to Y_N\) be the comparison cell without the tail, let \(T_N\) be the tail contribution, and write \(\beta_N=A_N+T_N\).

Suppose a normalized hidden direction exists:

\[
v_N\in S_N,\qquad \|v_N\|_{G_N}=1,\qquad A_Nv_N=0.
\]

Then

\[
c(\beta_N\mid S_N)
\le
\|\beta_Nv_N\|
=
\|T_Nv_N\|.
\]

Consequently, if \(\|T_Nv_N\|\to0\), the tail cannot by itself produce uniform conditioned coherence. It may make every finite \(\beta_N\) injective, but its inverse norm must diverge.

This gives four, and only four, structural escape routes from completion collapse.

1. Authorized localization: the hidden direction is absent from the declared task quotient. This changes the state object but does not add information.
2. Relative renormalization: the source Gram norm of the hidden direction shrinks at the same rate, so the generalized gain remains bounded. This is legitimate only when that Gram form is source-derived and cutoff-natural.
3. Independent observation: another authorized constructor contributes an order-one row on the hidden direction.
4. Dynamical exposure: although the instantaneous tail row is small, source dynamics moves the hidden direction into an order-one observed sector, making the observability Gramian uniformly positive.

No fifth mechanism is available in finite-dimensional linear semantics: a uniformly positive restricted gain must arise from removing the direction, changing its authorized size, observing it independently, or transporting it into an observed direction.

### Three different small-tail limits

The current theta discussion contains three limits that must not be identified.

- Seam scaling: \(u\to0\). The dominant two-label term vanishes in a coherence-sensitive derivative, so an exponentially small but fixed modular contribution controls the orientation.
- Label cutoff: \(X\to\infty\). The omitted remainder beyond X tends to zero. This is the limit relevant to pro-object naturality and inverse-norm escape.
- Scalar projection: typed boundary directions are annihilated by the completed scalar matrix coefficient. This is information loss, not asymptotic smallness.

The scale \(e^{-8\pi}\) in the two-label seam calculation is small but fixed. By itself it does not imply that the completed mate has lower gain tending to zero with X. Therefore the known seam calculation establishes singular perturbation and exact modular sewing, but does not yet place the full system in Case 3 rather than Case 4. That classification requires the generalized gain in the cutoff limit.

### Associated-graded interpretation

The tail may be leading in the coherence filtration even when it is high order in the analytic norm filtration. If the dominant route vanishes on a graded component, the first nonzero tail term is the principal symbol on that component. It can therefore decide the sign or orientation exactly.

This explains qualitative decisiveness without implying robust observability. Principal-symbol nonvanishing proves finite transversality. Uniform coherence additionally requires an elliptic estimate: the symbol must dominate the authorized source norm with a cutoff-independent constant.

Thus the missing theorem has the form

\[
\|v\|_{G_X}
\le
C\left(
\|\beta_Xv\|_{H_X}+\|q_Xv\|
\right),
\]

where \(q_X\) records only an independently authorized task quotient or gauge. Exact modular sewing proves a relation inside \(\beta_X\); it does not prove this estimate.

### Fourier-character refinement

Nima's boundary quotient decomposes as

\[
W=W_1\oplus W_{-1}\oplus W_i\oplus W_{-i}.
\]

If the comparison mate is Fourier-equivariant, it decomposes into character blocks \(\beta_{X,\chi}\). Its conditioned gain is the minimum of the gains on the reachable character blocks:

\[
c_X=\min_{\chi:S_{X,\chi}\ne0}c(\beta_{X,\chi}\mid S_{X,\chi}).
\]

A seam tail that repairs one odd-orientation block does not certify the other blocks. A scalar invariant readout sees only the trivial character and cannot measure the repaired odd gain. The first useful finite audit is therefore not the rank of one aggregate scalar row, but the four blockwise generalized gains and their cutoff behavior.

### Tail taxonomy

For each character block, the modular residue \(\Delta_X=W_\infty|_X-W_X\) has one of three types.

- Syzygy tail: its image under the backward defect map vanishes. It repairs forward presentation coherence but adds no mate information.
- Transversality tail: it is the first nonzero comparison symbol on a reachable hidden block. It repairs finite typed faithfulness, with strength given by its relative gain.
- Frame tail: it selects the sign or sheet of an already nonzero block but does not add a new linear coordinate.

These types are distinguished by the pair

\[
\left(
B_{X,s}\Delta_X,
\;c(\beta_{X,\chi}\mid S_{X,\chi})
\right)
\]

together with the cutoff cocycle. Scalar values cannot distinguish them.

### Highest-information application

For the Green–Ward mate, construct at each cutoff:

1. the four reachable character subspaces \(S_{X,\chi}\);
2. the block maps \(W_{X,\chi}\) and \(B_{X,s,\chi}\);
3. the mate residual \(D_{X,\chi}=W_{X,\chi}-B_{X,s,\chi}\);
4. the tail image \(B_{X,s,\chi}\Delta_X\);
5. the generalized lower gain of the corrected block.

Then ask in order:

- Does deletion of \(\Delta_X\) create a nonzero typed residual?
- Does its restoration cancel that residual before scalar projection?
- Is the repaired block reachable from the admitted source constructors?
- Is its generalized gain bounded below uniformly in X?
- Does the family obey cutoff refinement?

The first failure localizes the obstruction without conflating algebraic closure, task adequacy, and analytic stability.

## Disposition

The new theorem sharpens the atlas and corrects an overinterpretation: the exponentially small two-label seam tail is not evidence by itself for completion collapse. It proves that analytic size and coherence order differ. If an omitted cutoff tail tends to zero on a normalized hidden direction, then uniform repair by that tail alone is impossible; one of the four escape mechanisms is necessary.

The most informative next object is a Fourier-character-valued mate matrix, not another scalar identity. Its blockwise relative gains will decide whether the modular tail is merely a forward syzygy, a finite transversality repair, or a stable component of the completed Green–Ward coherencer.