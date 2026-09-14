# The endpoint contour block has Nevanlinna index one, while the full completed differential is not an ordinary upper-half-plane Herglotz function

## Proposed positive factorization

The unified finite-stage contour differential is

\[
\Omega_S(z)
=
\frac1{2i}\partial_z
\log\frac{M_S(z)}{M_S^\#(z)}
+
\varepsilon_{end}
\frac{2z}{z^2+1/4}.
\]

A previous note proposed realizing this through an operator-valued Herglotz function on the upper half-plane. That proposal fails before positivity is tested.

## Holomorphy obstruction

An ordinary operator-valued Herglotz function `K` must be holomorphic on

\[
\mathbb C_+=\{z:\operatorname{Im}z>0\}
\]

and satisfy

\[
\operatorname{Im}K(z)\succeq0.
\]

The endpoint kernel

\[
\frac{2z}{z^2+1/4}
\]

has a pole at

\[
z=i/2\in\mathbb C_+.
\]

Therefore no ordinary upper-half-plane Herglotz function can equal `Omega_S`, nor can a holomorphic compression

\[
B(z)^*K(z)B(z)
\]

produce this pole if `B` is holomorphic there.

Thus the requested ordinary Herglotz factorization is impossible as stated.

## Correct analytic domain

The natural domain of the completed local factors is the critical strip

\[
\mathfrak S=
\{z:|\operatorname{Im}z|<1/2\}.
\]

The endpoint points `plus-or-minus i/2` lie on its boundary, not in its interior. The inverse Euler factors also have zeros on these boundary lines:

\[
z=-\frac{2\pi n}{\log p}+\frac{i}{2}
\]

and their reflections on `Im z=-1/2`.

Hence the correct positivity question is a strip-valued boundary-kernel problem, not an upper-half-plane Herglotz problem containing the endpoint poles in its interior.

A conformal map from the strip to the disk sends both endpoint lines to the unit circle. Endpoint evaluations and prime-factor zeros then become boundary singularities.

## Endpoint negative index

On convolution-square endpoint coordinates

\[
v=(\widehat g(i/2),\widehat g(-i/2)),
\]

the residue polarization is

\[
v^*
\begin{pmatrix}0&1\\1&0\end{pmatrix}
v.
\]

This matrix has inertia

\[
(1,1):
\quad
\text{one positive square and one negative square}.
\]

Therefore the bare endpoint boundary kernel belongs naturally to a Pontryagin space of negative index one. It is not a positive Hilbert kernel.

In generalized Nevanlinna terminology, the minimal expected class is

\[
\boxed{N_1,}
\]

not `N_0`.

## Kernel formulation

For an operator-valued analytic function `K`, the Nevanlinna kernel is

\[
\mathcal N_K(z,w)
=
\frac{K(z)-K(w)^*}{z-\bar w}.
\]

A Herglotz function has

\[
\mathcal N_K\succeq0.
\]

A generalized Nevanlinna function of class `N_kappa` has at most `kappa` negative squares, with equality for some finite test set.

The endpoint swap matrix already supplies one negative square. Consequently any faithful completed kernel has at least this endpoint obstruction unless the gamma--prime bulk cancels it through a nonorthogonal coupling. Whether the full uncompressed kernel lies in any finite `N_kappa` class remains open.

## Why a trivial matrix lift does not solve the problem

Given a signed scalar boundary density `omega(t)`, one can formally form

\[
\begin{pmatrix}
c(t)&\omega(t)\\
\omega(t)&c(t)
\end{pmatrix}
\]

and make it pointwise positive by choosing

\[
c(t)\ge|\omega(t)|.
\]

But this adds the new diagonal functional `c`, which is absent from the Weil formula. Recovering `omega` then requires a signed compression and loses positivity again.

Moreover, the minimal choice `c=|omega|` is generally not the boundary value of an analytic function compatible with prime transitions. Such a lift is an external majorant, not a factorization of the source form.

## Schur cancellation criterion

Let the completed strip kernel have a block decomposition

\[
\mathcal K_S=
\begin{pmatrix}
K_{bulk,S}&B_S\\
B_S^*&J_{end}
\end{pmatrix},
\qquad
J_{end}=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

After parity diagonalization,

\[
J_{end}=
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Write `b_odd,S` for the bulk coupling to the negative endpoint line. Eliminating that line by a Pontryagin-space Schur complement requires a bulk vector of exactly the corresponding negative norm. In finite-dimensional notation, positivity after elimination is equivalent to a source-fixed cancellation of the form

\[
K_{bulk,S}
-
b_{odd,S}b_{odd,S}^*
\succeq0,
\]

with the sign depending on which block is eliminated.

This is not implied by `K_bulk,S>=0`; it is precisely the contractive endpoint estimate.

## Prime-transition compatibility

Adjoining prime `q` changes the logarithmic boundary differential additively:

\[
\Delta_q\Omega
=
\frac1{2i}
\partial_z\log
\frac{m_q}{m_q^\#}.
\]

A coherent generalized Nevanlinna realization requires embeddings

\[
\mathcal P_S\to\mathcal P_{S\cup\{q\}}
\]

between Pontryagin spaces that preserve the same single negative endpoint line. Adding a prime must enlarge or modify the positive bulk without introducing an independent negative square.

Thus a sufficient target transition law would be

\[
\boxed{
\kappa(\mathcal K_S)=1
\quad\text{for every finite }S,
}
\]

followed by cancellation of that one stable negative direction in the completed observation space. This equality has not been proved: the prime current can carry infinite-rank negative sectors before a positive-bulk realization is found.

If a proposed construction makes the negative index grow merely by splitting primes into independent hostile channels, the construction has split primes into independent hostile channels and cannot yield the desired common-bulk realization.

## Relation to rung four

The exact source contour naturally defines a signed kernel containing one endpoint negative square, with the negative index of its local part still unknown. Producing rung-four positivity means showing that the physical convolution-square observation and endpoint--bulk sewing leave negative index zero. If the local terms are first absorbed into a positive common bulk, this reduces to:

\[
\boxed{
N_1
\xrightarrow{\text{physical compression}}
N_0.
}
\]

This is a precise reformulation of the desired positivity theorem. It is not obtained by choosing a larger positive matrix kernel externally.

## Disposition

The ordinary upper-half-plane Herglotz fork is closed:

\[
\boxed{
\text{the pole at }i/2
\text{ forbids an }N_0
\text{ function holomorphic on }\mathbb C_+.
}
\]

The correct domain is the strip, and its endpoint block is a generalized Nevanlinna kernel with one negative square supplied by odd parity. The full kernel's negative index is not yet controlled. The next task is to determine whether the gamma--prime terms admit a positive common-bulk realization leaving only that endpoint direction; only then can physical compression be tested for cancellation.
