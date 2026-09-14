# Two directional path spaces give a 2-Segal baseline

## Question

Can the forward and backward coherence directions be represented as the two path spaces in the 2-Segal path-space criterion?

## Construction

Let \(X\) be the nerve of the one-object category with arrow group \(C_2\). Thus

\[
X_n=C_2^n.
\]

Define the initial and final path spaces by décalage:

\[
(P^{\triangleleft}X)_n=X_{n+1},
\qquad
(P^{\triangleright}X)_n=X_{n+1}.
\]

The initial path space omits the first face operator; the final path space omits the last.

## Exact result

For both path spaces, the Segal map from an \(n\)-simplex to its chain of adjacent 1-simplices is bijective. The checker verifies this through degree six. By the path-space criterion, \(X\) is 2-Segal.

The two path spaces are not extra planes inserted into \(X\). They are two directional projections of the same simplicial object.

## Four-periodic typing

Assign type grade

\[
\operatorname{type}(X_n)=n\bmod 4.
\]

Both path-space constructions shift the type grade by one:

\[
\operatorname{type}((P^{\triangleleft}X)_n)
=
\operatorname{type}((P^{\triangleright}X)_n)
=
(n+1)\bmod 4.
\]

This shift is compatible with the four-grade recurrence as a bookkeeping rule.

## Residual

The construction establishes two directional 1-Segal path spaces. It does not establish that they have opposite induced orientations or that their geometric realizations meet orthogonally. Those require, respectively, an orientation pairing and a metric or normal-bundle structure.

Thus the 2-Segal abstraction captures the two coherence channels and their common simplicial source, but not the proposed \(90^\circ\) geometry.

## Verification

```text
python research/voevodsky/checkers/check_two_directional_path_spaces.py
```

Artifacts:

- `research/voevodsky/checkers/check_two_directional_path_spaces.py`
- `research/voevodsky/results/two_directional_path_spaces.json`
