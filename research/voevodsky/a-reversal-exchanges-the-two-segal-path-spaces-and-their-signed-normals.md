# Reversal exchanges the two Segal path spaces and their signed normals

## Question

Can one 2-Segal object carry two directional path spaces whose normal directions are orthogonal and exchanged with sign reversal?

## Reversal on the simplicial object

Use the nerve of the one-object category \(C_2\):

\[
X_n=C_2^n.
\]

Define reversal by reversing simplex order. Group inversion is trivial in \(C_2\):

\[
r_n(g_1,\ldots,g_n)=(g_n,\ldots,g_1).
\]

It is involutive and reverses face position:

\[
r_{n-1}d_i=d_{n-i}r_n.
\]

It similarly reverses degeneracy position.

For the initial and final path spaces, reversal gives an isomorphism

\[
r:P^{\triangleleft}X\longrightarrow P^{\triangleright}X.
\]

Thus the two directional 1-Segal structures are exchanged by one simplicial involution.

## Orthogonal signed normal representation

Attach the normal space

\[
N=\mathbb Q^2
\]

with its standard pairing and basis

\[
\nu_{\triangleleft}=(1,0),
\qquad
\nu_{\triangleright}=(0,1).
\]

The basis directions are orthogonal. Let reversal act by

\[
J=
\begin{pmatrix}
0&-1\\
-1&0
\end{pmatrix}.
\]

Then

\[
J\nu_{\triangleleft}=-\nu_{\triangleright},
\qquad
J\nu_{\triangleright}=-\nu_{\triangleleft},
\qquad
J^2=1.
\]

This simultaneously exchanges the two channels and reverses their orientation labels while preserving orthogonality.

## Disposition

The construction now contains:

- one 2-Segal simplicial object;
- two directional 1-Segal path spaces;
- an involution exchanging them;
- a rank-two orthogonal normal representation;
- sign reversal under the same involution.

The \(90^\circ\) statement is algebraic: the normal pairing is zero. No literal geometric embedding of two planes has been constructed. The reversal and pairing are selected model data, not derived from an external source.

## Verification

```text
python research/voevodsky/checkers/check_reversal_orthogonal_two_segal.py
```

The checker verifies 768 face-reversal identities, 768 degeneracy-reversal identities, 640 initial/final path-space exchange identities, involutivity, sign exchange, and orthogonality.

Artifacts:

- `research/voevodsky/checkers/check_reversal_orthogonal_two_segal.py`
- `research/voevodsky/results/reversal_orthogonal_two_segal.json`
