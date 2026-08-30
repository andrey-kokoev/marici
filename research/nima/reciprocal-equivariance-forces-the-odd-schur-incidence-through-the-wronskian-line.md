# Reciprocal equivariance forces the odd Schur incidence through the Wronskian line

## Endpoint character decomposition

Let reciprocal endpoint reflection exchange the two traces:

\[
R_\partial
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

Its even and odd eigenspaces are

\[
E_+
=
\mathbb C
\begin{pmatrix}
1\\
1
\end{pmatrix},
\qquad
E_-
=
\mathbb C
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
\]

The completed Wronskian odd column

\[
j_\theta
=
\begin{pmatrix}
\frac14\\
-\frac14
\end{pmatrix}
\]

spans \(E_-\).

## Character-selection theorem

Let \(\mathcal K_{p,-}\) be the reduced reciprocal-odd auxiliary carrier,
and let

\[
R_{p,-}u=-u
\]

on that character sector. Suppose the endpoint incidence

\[
C_{p,-}:
\mathcal K_{p,-}
\longrightarrow
E_{12}
\]

is reciprocal-equivariant:

\[
R_\partial C_{p,-}
=
C_{p,-}R_{p,-}.
\]

Then

\[
R_\partial C_{p,-}=-C_{p,-},
\]

so

\[
\operatorname{ran}C_{p,-}
\subseteq E_-.
\]

Because \(E_-\) is one-dimensional, there is a unique continuous functional
\(c_p^*\) such that

\[
C_{p,-}=j_\theta c_p^*.
\]

Thus rank-one Wronskian factorization is not an additional ansatz. It follows
from typed reciprocal equivariance once the eliminated auxiliary block is
purely odd.

## Source support for purity

The completed theta history splits as

\[
H_\Phi=M_\Phi I+H_KD.
\]

Under causal reversal, the wall mass is even, while the odd history is

\[
H_\Phi-H_\Phi^*
=
H_KD-(H_KD)^*.
\]

Therefore the reciprocal-odd auxiliary sector contains no independent wall
mass. Its endpoint trace must carry the odd character.

The fixed ordered identities

\[
j_\theta=\frac14S_{\mathrm{ord}},
\qquad
Bj_\theta=-\frac12H_K
\]

then select the normalization and orientation of the unique endpoint line.

## Consequence for the Schur return

For either reciprocal sheet,

\[
C_{p,-}D_{p,\pm}^{\dagger}C_{p,-}^*
=
q_{p,\pm}
|j_\theta\rangle\langle j_\theta|,
\]

where

\[
q_{p,\pm}
=
\langle
c_p,
D_{p,\pm}^{\dagger}c_p
\rangle.
\]

Hence

\[
R_{p,\pm}
=
\frac{q_{p,\pm}}{16}
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
\]

The two diagonal loading tests collapse to the single inequality

\[
q_{p,\pm}<16a_p,
\]

because \(a_p\le b_p\).

## What remains unproved

Character selection determines the range and rank of \(C_{p,-}\), but not
the auxiliary functional \(c_p^*\). The remaining source calculation is
precisely the magnitude and spectral measure of that functional.

It must be obtained from the polarized Green identity connecting:

- the bivariate window derivative;
- the ordered port;
- the tail convolution;
- the odd auxiliary resolvent.

No scalar endpoint normalization may be fitted afterward.

## Mixed auxiliary sectors

The conclusion fails if the eliminated block combines even and odd
characters. For a general auxiliary carrier

\[
\mathcal K_p=\mathcal K_{p,+}\oplus\mathcal K_{p,-},
\]

equivariance gives

\[
C_p
=
w_\theta d_p^*
+
j_\theta c_p^*.
\]

The even wall functional \(d_p^*\) must be retained separately or shown to
vanish on the eliminated sector. Otherwise the Schur return can have rank two
and unequal diagonal loadings.

Thus the source block decomposition must occur before elimination.

## Completion compatibility

The character-selection argument survives completion if:

- reciprocal reflection is bounded on the completed carriers;
- the odd sector is closed;
- the incidence graph is closed and reflection-invariant;
- radical reduction commutes with reflection;
- prime truncations commute with both reflection and incidence.

Under these conditions, no second odd endpoint direction can appear in the
limit.

## Minimal hostiles

1. A finite odd incidence that is not reflection-equivariant.
2. An even wall component silently included in the eliminated odd block.
3. Equivariance on the algebraic core but not on the closed graph.
4. A quotient radical not invariant under reflection.
5. Correct rank-one range with a source-free choice of the functional
   \(c_p^*\).

## Verdict

The source reciprocal character closes the rank question. A purely odd
auxiliary Schur incidence is forced through the one-dimensional Wronskian
endpoint line.

The first unresolved local quantity is therefore no longer a two-vector
incidence matrix. It is one scalar spectral measure per prime and reciprocal
sheet:

\[
q_{p,\pm}
=
\langle
c_p,D_{p,\pm}^{\dagger}c_p
\rangle.
\]

Proving its uniform separation from \(16a_p\) is the remaining Schur-survival
gate.
