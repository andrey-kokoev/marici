# SCC gap audit of the current shifted-Gaussian RH model

## Question

What does kernel-checking the current implication chain reveal as the first missing mathematical constructor?

## Checked chain

The new UniMath/Rocq module

`research/grothendieck/scc/WeilGaussianRHReduction.v`

encodes the chain

\[
\begin{aligned}
&\text{broad Gaussian positivity}
+\text{finite-threshold character coercivity}
+\text{finite double-contact exclusion}\\
&\qquad\Longrightarrow\text{all-scale Gaussian positivity}\\
&\qquad\Longrightarrow\text{positive completed Weil distribution}\\
&\qquad\Longrightarrow\text{Weil quadratic positivity}\\
&\qquad\Longrightarrow\text{RH}.
\end{aligned}
\]

It kernel-checks with Rocq 9.0.1, OCaml 4.14.2, and the compatible UniMath Foundations build.

## Result

The proof term composes exactly when a term of type

`FiniteDoubleContactExclusion`

is supplied. The current model supplies no constructor for that type. This is the first missing mathematical object after accepting the reviewed broad-positivity and coercivity inputs.

The missing statement is

\[
\neg\exists(t,\xi)\in(0,\infty)\times\mathbb R:
\Theta(t,\xi)=0,
\quad
\partial_\xi\Theta(t,\xi)=0,
\quad
\partial_\xi^2\Theta(t,\xi)\ge0
\]

at a first finite threshold, with the threshold and compactness hypotheses typed explicitly.

## What the certificate does not prove

The SCC module treats the following arrows as contexts rather than constructed theorems:

- threshold reduction from broad positivity, coercivity, and contact exclusion;
- Gaussian approximate-identity promotion;
- positive-distribution to multiplicative Weil quadratic positivity;
- Weil's criterion.

These arrows have paper-level derivations or direct source support, but have not been formalized in UniMath. Kernel acceptance certifies only their composition. It does not elevate the current RH argument to a formal proof.

The earlier `CompactWeilSourceIdentity.v` is still weaker: its main theorem repeats the explicit-formula hypothesis verbatim, finite prime support is also supplied as a hypothesis, the normalization contexts are unused by the proof term, and no positivity object occurs. Its manifest entry `sector_sum_is_hermitian` has no corresponding theorem in that module and must not be treated as certified.

## Exact frontier

There are two distinct residuals:

1. **Mathematical residual:** construct `FiniteDoubleContactExclusion` from arithmetic properties of the endpoint, gamma, and von Mangoldt terms.
2. **Formalization residual:** replace the four implication contexts above by definitions and checked proofs over declared distribution and Mellin-test objects.

Only the first residual blocks the informal mathematical proof. Both block a kernel-checked RH proof.

## Disposition

The SCC comparison confirms that no normalization, escape-to-infinity, or Gaussian-to-Weil promotion step is the current mathematical bottleneck. The sole unconstructed mathematical proposition in the accepted chain is finite double-contact exclusion. The strongest existing partial constraints are the value--slope moment ellipse and the curvature covariance inequality; neither supplies a global constructor.
