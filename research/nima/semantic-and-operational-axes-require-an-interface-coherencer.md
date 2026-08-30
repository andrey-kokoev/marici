# Semantic and operational axes require an interface coherencer

## Result

Passing the semantic-and-authority axis and the operational axis separately does
not yet construct an operative arrow. The two actions must also satisfy a typed
interface law.

If \(S\) is a semantic transport and \(O\) is an operational restriction, the
compiler needs an authorized comparison between the two routes

The two routes are \(O'S\) and \(S'O\).

Depending on the setting, this comparison may be strict equality, a specified
invertible cell, a Beck–Chevalley map, or a declared residual transformation.
Without it, the apparent product of the axes is path-dependent.

## Exact hostile

On \(\mathbb R^2\), let the semantic symmetry exchange the two coordinates,

\[
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

and let the operational rule retain the first resource port,

\[
O=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

The symmetry is a valid semantic equivalence for a swap-invariant target. The
projection is a valid operational discard when the first port is the declared
retained resource. Nevertheless,

\[
OS\ne SO.
\]

For the first basis state, semantic transport followed by restriction gives
zero, while restriction followed by semantic transport gives the second basis
state. Both component actions were individually admitted; their undeclared
composition is not.

## Architectural consequence

The operative compiler has three pieces:

```text
semantic-and-authority profile
operational profile
cross-axis coherence cell
```

The third piece is not another independent axis. It states how the first two
interact. In categorical terms, a plain product must be replaced by a structured
product carrying a distributive law or Beck–Chevalley comparison.

This explains why order repeatedly becomes a final obstruction. Resource
restriction can erase distinctions needed by later semantic normalization;
semantic transport can move states across the boundary declared by an
operational policy.

## Falsifier

The matrix commutator \(OS-SO\) is nonzero. Any compiler that admits the combined
constructor from the two component verdicts alone is rejected with
`missing_cross_axis_coherence`.
