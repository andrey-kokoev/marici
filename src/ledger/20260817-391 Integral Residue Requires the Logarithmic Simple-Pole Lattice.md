---
id: 391
date: 2026-08-17
title: Integral Residue Requires the Logarithmic Simple-Pole Lattice
---

# Integral Residue Requires the Logarithmic Simple-Pole Lattice

Entry 390 isolated the second stage of physical realization as an operation
that kills the cone of the dual localization arrow. Entry 376 proposed the
oriented Cartier residue as the noncircular geometric candidate, with one
decisive condition: higher negative powers must disappear by boundary
relations rather than by decree.

That condition fails for the ordinary integral principal-parts complex.

## Higher-pole calculation

Let \(A=\mathbb Z[\ldots,x]\), with \(x=x_3\), and consider the principal
parts \(A[x^{-1}]/A\). In the relative de Rham complex,
\[
 d(x^{-m})=-m x^{-(m+1)}dx.
\]
The simple pole \(x^{-1}dx\) has no principal-part primitive and spans the
free residue line. For a pole of order \(n\ge2\), however, the boundary
coefficient is only \(n-1\). Consequently its integral quotient is
\[
 [x^{-n}dx]\in \mathbb Z/(n-1).
\]
The double pole vanishes, but the triple pole leaves \(\mathbb Z/2\), the
fourth-order pole leaves \(\mathbb Z/3\), and so on. Ordinary residue sends
these classes to zero but does not make them boundaries. Therefore it does
not annihilate the entire telescope cone integrally.

After tensoring with \(\mathbb Q\), all \(n-1\) become invertible and the
higher poles contract. That explains why the fixed-characteristic-zero
Cartier calculations close, but it is not an integral construction and
cannot be silently used for the universal theory.

## The forced refinement

The physical coefficient operation must select the logarithmic lattice
before applying residue:
\[
 \Omega^1_A(\log x)/\Omega^1_A
 = A/(x)\cdot d\log x.
\]
This object contains only the simple-pole class. Its oriented residue is the
canonical unit
\[
 \operatorname{res}_x(d\log x)=1.
\]
Thus the missing stage is not arbitrary Verdier localization and not
ordinary residue on all principal parts. It is a geometrically authorized
pole-order truncation to the logarithmic/simple-pole subquotient, followed by
the already normalized residue.

The repository already contains the likely geometric source of this
truncation: the logarithmic blowup of the marked \(D_{03}\) middle corner.
Its relative dualizing carrier and positive \(d\log X_{03}\) orientation were
constructed in the central-flip DNC audit. What remains is to promote that
logarithmic carrier to the raw-\(q^!\)-to-PC functor and prove that its
simple-pole lattice:

1. retains the generic \(q_{03}^{Q}\) leg;
2. maps \(d\log x_3\) to the positive Cartier unit;
3. is compatible with both endpoints and \(D_3\);
4. supplies the required Beck--Chevalley homotopy.

Connector existence remains open, but the coefficient operation is now
specified more narrowly: **logarithmic pole-order truncation followed by
oriented residue**.

The executable audit is
research/voevodsky/check_d03_integral_residue_tail_gate.py.
