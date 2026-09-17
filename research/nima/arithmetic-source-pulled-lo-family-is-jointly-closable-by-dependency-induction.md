# The arithmetic source-pulled L/O family is jointly closable by dependency induction

## Abstract lemma

Let `E,G,B` be Hausdorff complete locally convex carriers. Suppose

\[
U:E\to G
\]

is continuous, `M:G superset D(M) -> G` is closable, and `O:G superset D(O) -> B` is closable. On a common dense core `E_0`, consider

\[
U,
\qquad MU,
\qquad OU,
\qquad OMU.
\]

This family is jointly closable.

Indeed, let `x_alpha -> 0` in `E` and assume all four coordinates converge:

\[
Ux_\alpha\to y_U,
\quad MUx_\alpha\to y_M,
\quad OUx_\alpha\to y_O,
\quad OMUx_\alpha\to y_{OM}.
\]

Continuity gives `y_U=0`. Since `Ux_alpha -> 0` and `MUx_alpha -> y_M`, closability of `M` gives `y_M=0`. Closability of `O` applied to `Ux_alpha` gives `y_O=0`; applied to `MUx_alpha` gives `y_OM=0`. Therefore no nonzero vertical graph vector exists.

The same induction applies to any finite acyclic dependency graph whose roots are continuous and whose edge operators are closable.

## Application

Take

\[
E=\mathcal A_{\exp}^{\mathrm{Laur}},
\qquad U=U_4,
\]

with the declared forward projective-to-retained-graph continuity. Let `M=M_a` be an admitted closed Mellin multiplier and let `O` be retained closed observation, not bare-`L2` point evaluation. The lemma proves joint closability of

\[
U_4,
M_aU_4,
OU_4,
OM_aU_4.
\]

Hence the source-pulled graph closure has no vertical vectors, its first projection is faithful, and it is homeomorphic to its projected source domain equipped with the pulled-back graph topology.

For a finite observer family, include all coordinates in one finite dependency graph. For a pro-family, take the projective system of finite-family graph domains; this proves coordinatewise joint closability. A stronger uniform Hilbert record norm still requires uniform multiplier estimates and is not claimed.

## Consequence

The closability gate discovered by the homeomorphism audit closes in the retained graph scope. It would reopen if any of the following substitutions were made:

- replace continuous `U_4` by an unproved native-topology comparison;
- admit a nonclosable multiplier;
- replace retained closed observation by raw point evaluation on bare `L2`;
- demand a stronger infinite-family topology than the projective coordinatewise one.
