# Eta Squared Has an Exact Dihedral Response Modulus

## Result

The earlier \(S_3/S_4\) threshold is neither a derived-length threshold nor a
cyclic-commutator threshold. Both proposed explanations have exact hostile
counterexamples:

- \(A_4\) is metabelian but detects \(W_{\eta^2}\);
- \(D_{10}'\cong C_5\) is cyclic but \(D_{10}\) detects it.

The dihedral sector instead has an exact integral response modulus.

## Reflection linearization

Label the reflections of a regular \(n\)-gon by \(a\in\mathbb Z/n\). Reflection
conjugation gives

\[
r_a r_b r_a^{-1}=r_{2a-b}.
\]

Therefore the Hurwitz action on an adjacent pair of reflection labels is the
integral linear map

\[
\sigma_i:(a_i,a_{i+1})\longmapsto(2a_i-a_{i+1},a_i).
\]

Expanding the 208-letter Artin-generator word for \(W_{\eta^2}\) produces an
integral matrix \(R\in GL_4(\mathbb Z)\). The checker computes it directly from
the source braid word. The greatest common divisor of all entries of

\[
R-I_4
\]

is exactly

\[
96=2^5\cdot3.
\]

It follows immediately that the complete reflection packet over
\(\mathbb Z/n\) is blind exactly when

\[
n\mid96.
\]

This is a theorem for the reflection-restricted dihedral port, not a fit to the
finite census.

## Hostile confirmations

The independently evaluated full group actions agree with the modulus:

| group | polygon modulus | result |
|---|---:|---|
| \(S_3\cong D_6\) | 3 | blind on all \(6^4\) tuples |
| \(D_8\) | 4 | blind on all \(8^4\) tuples |
| \(D_{10}\) | 5 | detecting |
| \(D_{12}\) | 6 | blind on all \(12^4\) tuples |
| \(D_{14}\) | 7 | detecting |

The \(A_4\) witness supplies a separate non-dihedral route. Since
\(A_4'=V_4\), independent commutator directions can detect the braid even at
exponent two. Thus two resources can break blindness:

1. a cyclic reflection modulus not dividing 96;
2. a multidirectional commutator packet such as \(V_4\).

## Interpretation

The number 96 is not the homotopy order of \(\eta^2\). The homotopy residue has
order two; 96 is the content of one integral observation matrix before the
filling quotient. It classifies exactly which cyclic dihedral reflection ports
erase that raw braid response.

This is the sought explanation of the original surprise: \(S_3\) is blind not
because it is merely small or metabelian, but because its reflection modulus
three divides the source-derived response content.

## Replay

```powershell
uv run python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```
