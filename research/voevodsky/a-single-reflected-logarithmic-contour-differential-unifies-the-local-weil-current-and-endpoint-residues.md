# A single reflected logarithmic contour differential unifies the local Weil current and endpoint residues

## Analytic reflection

For a holomorphic function `H`, define

\[
H^\#(z)=\overline{H(\bar z)}.
\]

On the real axis,

\[
H^\#(t)=\overline{H(t)}.
\]

Let the finite-stage local multiplier be

\[
M_S(z)=M_\infty(z)
\prod_{p\in S}
(1-p^{-1/2-iz}),
\]

with `M_infinity` chosen in the same completed-zeta normalization as the archimedean explicit formula.

Define the reflected scattering ratio

\[
\mathcal S_S(z)=
\frac{M_S(z)}{M_S^\#(z)}.
\]

Where it is defined on the real axis,

\[
|\mathcal S_S(t)|=1.
\]

## Local current as a boundary logarithmic derivative

On the real axis,

\[
\partial_t\log\mathcal S_S(t)
=
\frac{M_S'(t)}{M_S(t)}
-
\overline{
\frac{M_S'(t)}{M_S(t)}
}.
\]

Therefore

\[
\boxed{
V_{loc,S}(t)
=
\operatorname{Im}
\frac{M_S'(t)}{M_S(t)}
=
\frac1{2i}
\partial_t\log\mathcal S_S(t).
}
\]

For each finite prime,

\[
\operatorname{Im}
\partial_t\log(1-p^{-1/2-it})
=
(\log p)
\sum_{k\ge1}p^{-k/2}
\cos(kt\log p).
\]

Thus the gamma--prime Weil current is the real-axis boundary value of one meromorphic logarithmic differential.

## Endpoint residue kernel

For any entire observer `F`, Cauchy's residue theorem gives

\[
\boxed{
\frac1{2\pi i}
\oint_\Gamma
F(z)
\frac{2z}{z^2+1/4}dz
=
F(i/2)+F(-i/2),
}
\]

provided `Gamma` encloses both endpoint poles and no other singularities of the integrand.

Indeed the residue of

\[
\frac{2z}{z^2+1/4}
\]

at each of `plus-or-minus i/2` is `1`.

For a convolution square,

\[
F(z)=
\widehat g(z)
\overline{\widehat g(\bar z)},
\]

this becomes

\[
F(i/2)+F(-i/2)
=
2\operatorname{Re}
\left(
\widehat g(i/2)
\overline{\widehat g(-i/2)}
\right),
\]

which is exactly the swap-polarized endpoint form.

## Unified completed differential

Define the finite-stage completed contour differential

\[
\boxed{
\Omega_S(z)dz
=
\left[
\frac1{2i}
\partial_z\log\mathcal S_S(z)
+
\varepsilon_{end}
\frac{2z}{z^2+1/4}
\right]dz,
}
\]

where `epsilon_end=plus-or-minus 1` is fixed by the explicit-formula orientation.

Pairing an analytic observer against `Omega_S` has two components:

1. deforming the contour to the real axis produces the gamma--prime logarithmic current;
2. crossing `plus-or-minus i/2` produces the two endpoint residues.

Consequently endpoint, gamma, and finite primes are now boundary and residue pieces of one meromorphic one-form rather than separately appended functionals.

## Prime tower compatibility

Adjoining `q` changes the scattering ratio by

\[
\mathcal S_{S\cup\{q\}}
=
\mathcal S_S
\frac{m_q}{m_q^\#}.
\]

Hence

\[
\boxed{
\Omega_{S\cup\{q\}}-
\Omega_S
=
\frac1{2i}
\partial_z
\log\frac{m_q}{m_q^\#}dz.
}
\]

The increment is additive and independent of the order in which primes are adjoined. The endpoint rational differential is unchanged. This is the contour-level `2x2` tower law.

## Prime-factor singularities and the endpoint boundary

The zeros of

\[
m_p(z)=1-p^{-1/2-iz}
\]

satisfy

\[
z=-\frac{2\pi n}{\log p}+\frac{i}{2},
\qquad n\in\mathbb Z.
\]

Thus the Euler inverse-factor zeros lie on the upper endpoint line

\[
\operatorname{Im}z=1/2.
\]

The reflected zeros lie on `Im z=-1/2`. Therefore the natural prime-free contour strip is precisely

\[
|\operatorname{Im}z|<1/2,
\]

and its boundary is the same displacement that carries the completed endpoint evaluations.

This explains structurally why endpoint control changes when prime translations become active: the endpoint contour is also the accumulation line of all local inverse-Euler zeros.

## Relation with the Clifford resolvent

The endpoint denominator

\[
z^2+\frac14
\]

is the analytic continuation of the endpoint mass operator `X^2+1/4` in the four-component Clifford square. The logarithmic term is the `Gamma_12` phase channel. Thus the contour differential can be viewed schematically as a matrix-weighted resolvent/logarithmic derivative of the Clifford family.

A precise operator determinant formula would require relative determinants because neither the free nor local first-order operator has a naive determinant on the line.

## Positivity test

The unified contour identity does not by itself produce positivity. On the real axis,

\[
\frac1{2i}
\partial_t\log\mathcal S_S(t)
=V_{loc,S}(t)
\]

changes sign. At the endpoint poles, convolution-square residues form the indefinite swap matrix

\[
J_{end}=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Therefore `Omega_S` is not the boundary measure of an obviously positive scalar Herglotz function.

If one could construct a matrix-valued Herglotz function `K_S(z)` such that

\[
\Omega_S
=
B_S^*(z)K_S(z)B_S(z)
\]

in a source-derived boundary sense, then positivity would follow from

\[
\operatorname{Im}K_S(z)\succeq0
\qquad(\operatorname{Im}z>0).
\]

But the negative odd endpoint residue shows that such a factorization must be matrix-valued and must mix endpoint with the continuous gamma--prime channel. A scalar positive measure cannot work.

## Exact remaining factorization problem

Seek a `2x2` operator-valued analytic function

\[
K_S(z)=K_S(z)^\#
\]

with positive imaginary part in the upper half-plane and a boundary observation map `B_S` such that its compressed jump and residues reproduce

\[
\frac1{2i}\partial_z\log\mathcal S_S(z)
+
\varepsilon_{end}
\frac{2z}{z^2+1/4}.
\]

Transition compatibility requires

\[
K_{S\cup\{q\}}-K_S
\]

to realize the logarithmic differential of `m_q/m_q#` inside the same positive kernel, not as an orthogonal prime block.

This is a concrete matrix Nevanlinna-factorization problem. Its solvability is stronger than the contour identity and is the actual positivity gate.

## Disposition

The desired single contour object has been constructed:

\[
\boxed{
\Omega_S(z)dz
=
\left[
\frac1{2i}
\partial_z\log
\frac{M_S(z)}{M_S^\#(z)}
+
\varepsilon_{end}
\frac{2z}{z^2+1/4}
\right]dz.
}
\]

Its real-axis boundary gives gamma plus prime powers, and its two residues give the complete endpoint swap form. The remaining rung-four problem is now an operator-valued Herglotz/Nevanlinna factorization of this signed meromorphic differential with coherent prime transitions.
