# The magnetic Hall ordering is inherited from source labels

Companion to `checkers/magnetic_hall_functor_checks.py` (7/7, exit 0) and
`results/magnetic_hall_functor.json`.

On the even alternate-chart family (q=2g+8, k=g/2+4), label every source
column by pole depth and reflected branch,

\[
(a,\sigma),qquad a\in\{0,2,\ldots,g+8\},quad\sigma\in\{-,+\}.
\]

The preferred Hall matching has the closed formula

\[
H_g(a,-)=
\begin{cases}
1,&a=0,\\
-g-a,&a\ge2,
\end{cases}
\]

and

\[
H_g(a,+)=
\begin{cases}
2g+8,&a=0,\\
g+8-a,&a\ge2.
\end{cases}
\]

The alternate chart changes only (H_g(0,-)) from (1) to (3).  Removing
the endpoint labels ((0,-)) and ((g+8,+)) leaves (g+8) interior labels.
Their order is inherited from increasing (a), with the fixed reflected
branch order (-,+).

This formula agrees exactly with the augmenting-path matching for every even
(2\le g\le60), and every assigned coefficient is nonzero.  The Hall order is
therefore derived from source semantics rather than from Gaussian elimination
or array position.

## Naturality

Let a legal relabelling preserve the semantic pair ((a,\sigma)) and the
orientation of the target exponent line.  Then:

- arbitrary storage permutations are erased by semantic canonicalization;
- arbitrary display-token renamings leave ((a,\sigma)) unchanged;
- a uniform target translation (r\mapsto r+t) transports
  (H_g\mapsto H_g+t) and leaves the coefficient matrix literally unchanged.

These equivariance statements are checked on 45 hostile storage orders, 60
translated matrices, and all source-token renamings through grade (30).

The swapped-first-two-row control is not legal.  At (g=8) it changes the
observation offsets by

\[
(-34,+34,0,0,\ldots),
\]

which is neither a uniform target translation nor compatible with
(r(a,\sigma)=H_g(a,\sigma)).  Its failure of oscillation therefore does not
refute the source-oriented coefficient law.

## Scope

The formula and nonzero assignments are exact through grade (60); the
equivariance audit is exact through grade (30).  The notion of legal
relabelling here explicitly retains pole-depth order, reflected-branch type,
and target orientation.  Enlarging the automorphism class would require a new
source symmetry, not an arbitrary row permutation.
