---
id: 457
date: 2026-08-17
title: The Twisted Cartier Layer Forces Residues Three and Four
---

# The Twisted Cartier Layer Forces Residues Three and Four

Entry 456 derived the twist section

\[
w=\frac18(b-1)^3(b+1)^4.
\]

Transporting the source derivative through the twisted generator gives the
connection

\[
\nabla=d+d\log w
=d+\left(\frac3{b-1}+\frac4{b+1}\right)db.
\]

The poles are forced.  A regular polynomial coefficient (A(b)) would require
(w'=Aw), but (w) does not divide (w').  Thus the twisted Cartier lattice
is preserved by a logarithmic connection, not by a regular one.

Its finite residues are

\[
\operatorname{res}_{b=1}\nabla=3,
\qquad
\operatorname{res}_{b=-1}\nabla=4.
\]

After compactifying the (b)-axis, the residue theorem forces

\[
\operatorname{res}_{\infty}\nabla=-(3+4)=-7.
\]

This recovers, from the boundary geometry alone, the integer in the frozen
Euler operator

\[
c(a\partial_a-7).
\]

The equality is structural: the degree-seven Euler resonance is the Fuchs
balance of the two boundary multiplicities produced by the weighted Rees and
incidence twists.  It was not an unrelated coefficient in the exact-form
matrix.

This is still one step short of identifying cohomologies.  The correct object
to compare with the Euler-resonance quotient is now the logarithmic de Rham
complex of the twisted Cartier line, with residues ((3,4,-7)), together with
the square-zero (a)-layer.  Its algebraic de Rham cohomology must be computed
with the chosen lattice; using only the punctured generic local system would
forget the boundary data just recovered.

The next gate is that logarithmic de Rham calculation and an explicit map from
its classes to ([1]) and ([a^7(b+1)]).

The executable audit is
research/voevodsky/check_soft_axis_twisted_cartier_connection.py.
