# Finite Affine Compatibility Does Not Survive Without a Uniform Right Inverse

At cutoff (N), let

\[
\Phi_N:V_N^G\to D_N,
\qquad
\Phi_N(N')=L_NN'H_N,
\]

and let the symmetry-fixed actuator defect be

\[
d_N=-L_NB_{G,N}H_N.
\]

Finite equivariant nondisturbance is the solvability condition

\[
\Phi_N n_N=d_N.
\]

Completion-stable compatibility additionally requires solutions with uniformly
bounded norm. The sharp cost is

\[
\mu_N=inf\{\|n\|:\Phi_Nn=d_N\}.
\]

When (d_N) lies in the range, this is the norm of the Moore–Penrose solution
in the frozen source metrics. Finite range membership alone does not bound it.

The smallest hostile is one dimensional:

\[
\Phi_N=N^{-1},
\qquad d_N=1.
\]

Every cutoff has the unique solution (n_N=N), so the symmetry and
nondisturbance laws are exactly compatible at every finite stage. Yet

\[
\mu_N=N\to\infty.
\]

No bounded actuator correction survives completion. Equivalently, the
smallest singular value of (\Phi_N) collapses while the defect retains fixed
size.

The correct completion certificate is a uniformly bounded right inverse on
the actual defect family, or the weaker direct estimate

\[
\sup_N\mu_N<\infty.
\]

A global right inverse on all of (D_N) may be stronger than necessary; only
source-generated defects require correction. Conversely, rescaling the shear
norm to hide (\mu_N) is valid only under the covariant uniform-equivalence
rules already established.

## Falsifiers

- Every cutoff is solvable but least correction norms diverge.
- The singular value of (\Phi_N) collapses along the source defect direction.
- A cutoff-dependent metric makes (n_N) bounded without uniform equivalence.
- Solutions use increasingly many unauthorized actuator generators.
- Scalar cancellation survives while typed actuator graphs diverge.

## Process calibration

Pre-objective: excitement 9/10, confidence 10/10, expected information gain
9/10. Solvability, least correction norm, singular value, and uniform actuator
bound were frozen.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Finite affine compatibility split cleanly from completion-stable
compatibility. The operative invariant is the least source-metric shear needed
to cancel the actual defect, not mere range membership.
