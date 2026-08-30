# Fourier exchange makes the constant-delta wall anti-symplectic, not a quarter-turn

## Exact wall-plane calculation

In the ordered wall basis

\[
(w_{\mathrm{const}},w_{\delta}),
\]

the normalized Fourier–Tate exchange has the real matrix form

\[
F_{\mathrm{wall}}
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]

up to source-fixed scalar and sign conventions.

Let

\[
J_{\mathrm{wall}}
=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

Then

\[
F_{\mathrm{wall}}^{2}=I,
\]

and

\[
F_{\mathrm{wall}}^{T}
J_{\mathrm{wall}}
F_{\mathrm{wall}}
=
-J_{\mathrm{wall}}.
\]

Thus the constant-delta Fourier exchange is anti-symplectic. It reverses the wall orientation; it is not the symplectic quarter-turn \(J_{\mathrm{wall}}\).

## Consequence

This is compatible with reciprocal reflection. An anti-symplectic involution naturally exchanges incoming and outgoing or constant and delta polarizations while reversing the oriented Green current.

But it cannot by itself serve as the continuous canonical evolution on the wall plane.

Therefore two structures must remain distinct:

- wall symplectic form \(J_{\mathrm{wall}}\), derived from the antisymmetric Green pairing;
- Fourier–Tate reflection \(F_{\mathrm{wall}}\), which reverses that form.

The relation to prove is anti-symplectic covariance, not equality:

\[
F_{\mathrm{wall}}^{*}
\Omega_{\mathrm{wall}}
F_{\mathrm{wall}}
=
-\Omega_{\mathrm{wall}}.
\]

## Orientation authority

Changing the order of the wall basis or inserting a sign in one Fourier image changes the displayed matrices. The invariant statement is that the source Fourier involution has determinant \(-1\) on the real wall plane and reverses its symplectic orientation.

Multiplying by an imported complex phase to turn the exchange into a quarter-turn would reintroduce the earlier authority defect. Any such phase must arise from causal history or an independently typed complex structure.

## Four-dimensional compatibility

For the full state

\[
Y=(G_+,G_-,w_{\mathrm{const}},w_\delta),
\]

the reciprocal/Fourier sewing operator \(\mathcal R\) should satisfy

\[
\mathcal R^{*}\Omega\mathcal R=-\Omega.
\]

This condition constrains the tail-wall cross block \(K\). It is stronger than requiring anti-symplecticity on each diagonal block separately.

Likewise the canonical Hamiltonian should transform with the reciprocal spectral parameter so that the complete generator pencil is equivariant. A sign error in \(K\) may preserve scalar Fourier exchange while violating the full anti-symplectic sewing law.

## Immediate finite test

The next \(4\times4\) packet should be tested in this order:

1. derive \(\Omega\) from Green polarization;
2. derive \(\mathcal R\) from reciprocal and Fourier sewing;
3. verify \(\mathcal R^{*}\Omega\mathcal R=-\Omega\);
4. derive \(\mathcal A_0,\mathcal A_1\);
5. verify the corresponding reciprocal covariance of the generator;
6. only then test positivity of \(\Omega\mathcal A_1\).

The smallest hostile uses the correct constant-delta swap and correct scalar endpoint transform but a cross block \(K\) whose sign makes the full sewing symplectic instead of anti-symplectic.
