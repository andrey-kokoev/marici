# The Ternary Braid Port Misses a Hyperbolic Commutator

## Question

Is the \(\mathbb Z/3\) spherical pure-braid residue sufficient for path
coherence?

## Projective monodromy detector

Define

\[
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
U=\begin{pmatrix}1&0\\-1&1\end{pmatrix},
\]

and assign

\[
\sigma_1\mapsto T,
\qquad
\sigma_2\mapsto U,
\qquad
\sigma_3\mapsto T.
\]

The Artin braid relations hold. The spherical relation maps to \(-I\), so the
assignment defines a projective representation into \(PSL_2(\mathbb Z)\).

## Abelian-invisible hostile

Consider

\[
w=[\sigma_1^2,\sigma_2^2].
\]

This word has identity endpoint permutation and exponent sum zero. It is
therefore invisible to the static \(A_3\) packet, the \(\mathbb Z/6\)
abelianization, and the endpoint-invisible \(\mathbb Z/3\) port.

Nevertheless,

\[
\rho(w)=
\begin{pmatrix}
13&8\\
8&5
\end{pmatrix}.
\]

Its trace is eighteen, so it is nontrivial and hyperbolic in
\(PSL_2(\mathbb Z)\).

## Consequence

The ternary port is only the first path-coherence rung. A finite nonabelian
monodromy port already separates a braid that every endpoint and abelian
readout misses.

The required witness hierarchy is now

```text
endpoint permutation
A3 static redistribution
Z3 abelian pure-braid residue
projective nonabelian monodromy
```

The projective matrix is a detector, not yet a faithful classifier of all
spherical braids. Its kernel must be audited before it can terminate the
coherence tower.

## Disposition

The first explicit post-ternary hostile is an exponent-zero pure commutator.
Its projective monodromy gives a source-neutral finite witness of the missing
nonabelian coherence.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/nonabelian_spherical_braid_hostile_checks.py
```
