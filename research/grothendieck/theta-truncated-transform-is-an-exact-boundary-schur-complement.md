# Theta truncated transform is an exact boundary Schur complement

## Finite terminal-value operator

Fix (L>0), let (f\in L^2(0,L)), and define

\[
 A_{s,L}G=G'+sG
\]

on the Sobolev domain

\[
 \mathsf D_L=\{G\in H^1(0,L):G(L)=0\}.
\]

The terminal condition is fixed before any transform zero is inspected.
For every complex (s), the operator (A_{s,L}:\mathsf D_L\to L^2(0,L))
is bijective, with

\[
 (A_{s,L}^{-1}u)(q)
 =-e^{-sq}\int_q^L e^{sv}u(v)\,dv.
\]

Let (\ell_0G=G(0)). Endpoint evaluation is continuous on
(H^1(0,L)).

## Canonical block pencil

Define

\[
 \mathcal T_{s,L}
 =\begin{pmatrix}
 A_{s,L}&f\\
 \ell_0&0
 \end{pmatrix}
 :\mathsf D_L\oplus\mathbb C
 \longrightarrow
 L^2(0,L)\oplus\mathbb C.
\]

Every entry is source-derived: first-order transport, the source forcing
vector, the terminal condition, and the finite endpoint trace.

The Schur complement of (A_{s,L}) is

\[
 -\ell_0A_{s,L}^{-1}f
 =\int_0^L f(v)e^{sv}\,dv
 =F_L(s).
\]

Thus the truncated transform is not appended as a fitted determinant. It is
the exact boundary Schur complement of the source tail system.

## Exact kernel bridge

If

\[
 \mathcal T_{s,L}(G,c)=0,
\]

then

\[
 G(q)=c e^{-sq}\int_q^L f(v)e^{sv}\,dv
\]

and

\[
 cF_L(s)=0.
\]

Because (A_{s,L}) is injective, a nonzero kernel state must have (c\ne0).
Therefore

\[
 \ker\mathcal T_{s,L}\ne0
 \quad\Longleftrightarrow\quad
 F_L(s)=0.
\]

This proves the finite zero-to-state bridge in the correct derivational
direction.

## Relation to the reciprocal norm

At fixed finite (L), the reciprocal cosh weight is bounded for every
(s). Its condition number, however, grows at least like

\[
 e^{2|\delta|L}.
\]

Hence finite-cutoff kernel states do not yield zero confinement. The seam is
selected only if the completed operator domain retains a cutoff-uniform full
reciprocal graph norm. Packet 204 shows that this uniformity does not follow
from the two endpoint equations alone.

The remaining theorem is now sharply typed: construct a compatible limit of
the pencils (\mathcal T_{s,L}) together with the primitive, square,
connected-tail, seam, and archimedean channels, and prove that its graph domain
is the completion selected by those source operations.

## Hostile multiplier response

Multiplying (F_L) by an arbitrary divisor-bearing factor does not preserve
this block pencil. It requires changing the forcing vector, endpoint trace,
transport block, or adjoining a new summand. Thus the construction has a
finite canonical-section rigidity absent from scalar reformulations.

That rigidity is not yet uniform in (L). A hostile family could enter by
changing the completion or by appending cutoff-dependent summands whose graph
norms escape at infinity.

## Falsifier

The finite bridge fails if (A_{s,L}) is not bijective on the declared
terminal domain, if endpoint evaluation is discontinuous in its graph norm,
or if the computed Schur complement differs from (F_L). The completed route
fails if cutoff inclusions do not intertwine the block pencils and all typed
boundary channels, or if their inverse and trace bounds are not controlled in
the source-selected topology.

## Scope

This constructs the first exact source-derived Fredholm-style pencil whose
kernel is equivalent to a truncated transform zero. It does not construct the
infinite adelic completion, prove cutoff-uniform graph control, identify the
completed determinant, or prove RH.
