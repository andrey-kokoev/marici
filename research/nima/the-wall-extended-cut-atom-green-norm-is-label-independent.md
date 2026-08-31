# The wall-extended cut-atom Green norm is label independent

## Distributional seam derivative

For scale \(a>0\), the theta cut atom is

\[
u_a=(g_a,h_a),
\qquad
g_a(t)=\Phi(t+a),
\qquad
h_a(t)=\mathbf1_{t\le a}\Phi(a-t).
\]

The tail derivative is ordinary:

\[
Dg_a(t)=\Phi'(t+a).
\]

The seam component has a moving jump.  Distributionally,

\[
Dh_a
=-\mathbf1_{t<a}\Phi'(a-t)-\Phi(0)\delta_a.
\]

Thus the derivative splits canonically into:

- a regular half-line derivative;
- a wall port of fixed magnitude \(-\Phi(0)\);
- no scale-dependent coefficient.

## Exact regular norms

The regular derivatives are obtained from the same tail--seam cut applied to
\(\Phi'\). Therefore the exact cut identity, now for the derivative profile,
gives

\[
\|Dg_a\|_2^2+\|D_{\rm reg}h_a\|_2^2
=\|\Phi'\|_2^2.
\]

This formulation uses the declared tail and seam measure spaces and does not
silently reinterpret either component as a full-line function.

The wall coordinate has norm

\[
|\Phi(0)|,
\]

independent of \(a\).

The zeroth-order cut identity already gives

\[
\|g_a\|_2^2+\|h_a\|_2^2=\|\Phi\|_2^2.
\]

## Wall-extended graph norm

On the source-declared direct-sum carrier, store the delta jump in its own wall
coordinate rather than attempting to place it in \(L^2\).  The natural
wall-extended first-derivative norm is

\[
\|u_a\|_{\mathrm{cut},G}^2
:=
\|g_a\|_2^2+
\|h_a\|_2^2+
\|Dg_a\|_2^2+
\|D_{\rm reg}h_a\|_2^2+
|J_ah_a|^2,
\]

where

\[
J_ah_a=h_a(a+)-h_a(a-)=-\Phi(0).
\]

Substitution yields the exact scale-independent value

\[
\|u_a\|_{\mathrm{cut},G}^2
=
\|\Phi\|_2^2+
\|\Phi'\|_2^2+
|\Phi(0)|^2.
\]

Any source-declared positive weights on these three orthogonal ports merely
replace the right side by another fixed positive constant.  No prime or grade
loss appears.

## Completed comparison

The resolved front norms are uniformly bounded above and below on
\(a=k\log p\ge\log2\).  The wall-extended cut norm is exactly constant.
Therefore the source-generated comparison

\[
J(q_{k\log p})=u_{p,k}
\]

extends to a boundedly invertible map between the labelled resolved-front
direct sum and the labelled wall-extended cut Green direct sum.

Consequently, on this retained labelled carrier:

- the graph of \(J\) is closed;
- its range is closed;
- the positive forms have zero radical;
- finite cutoffs converge strongly;
- the moving seam wall creates no norm blowup because it is retained as a
  separate port.

## Scope

This closes the positive wall-extended Green comparison on the labelled
source-generated range.  It does not prove continuity of the separately
ordered linking polarization, nor authorize codiagonalization or unlabelled
prime pushforward.  It also does not identify radicals after adding any
indefinite or skew linking form.

The earliest remaining local gate is continuity and radical annihilation of
the ordered Stokes/Wronskian linking polarization on this common completed
labelled carrier.  The connected tail and global unlabelled closed-range
problem remain open.  No RH conclusion is authorized.
