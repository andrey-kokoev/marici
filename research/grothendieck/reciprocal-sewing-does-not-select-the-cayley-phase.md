# Reciprocal sewing does not select the Cayley phase

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact sewing-rigidity obstruction

## Stronger hostile test

The previous phase-selection obstruction retained a maximal commuting Weyl
algebra and a cyclic state. One might hope that Fourier–Tate reciprocity
removes the ambiguity. It does not.

Let the reciprocal involution exchange two spectral atoms:

\[
R=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

For every phase \(a\in S^1\) away from the Cayley pole, define

\[
U_a=\operatorname{diag}(a,\bar a).
\]

Then

\[
R U_a R=U_a^*.
\]

The common cyclic vector \((1,1)/\sqrt2\) is fixed by \(R\), and every
\(U_a\) belongs to the same maximal abelian boundary algebra. Nevertheless,
the Cayley generators

\[
A_a=i(1+U_a)(1-U_a)^{-1}
\]

vary with \(a\).

## Meaning

Reciprocal sewing restricts the two sheet phases to be conjugates. It does
not choose their angle. The data currently retained by the programme leave a
continuous moduli space of self-adjoint boundary conditions.

Therefore the missing selector cannot be merely:

- maximal rational incidence;
- a common cyclic theta state; or
- Fourier–Tate covariance.

It must include an oriented source datum that fixes motion along the phase
circle. Candidate forms are a labelled boundary current, a distinguished
infinitesimal generator, or an order structure compatible with the complete
prime and archimedean channels.

## Geometric-algebra reading

Reciprocity fixes the plane and reverses its orientation coordinate, but it
does not fix the rotor angle. The scalar determinant changes with that angle.
The missing object is therefore not another plane. It is a source-derived
rotor parameter, or equivalently a connection that determines parallel
transport inside the already selected plane.

## Sharp next gate

Derive a one-parameter source transport \(U_t\) before evaluating the scalar
section and identify its generator \(Q\). Reciprocity should imply

\[
RQR=-Q.
\]

That relation alone still permits many odd generators. The decisive theorem
must show that the labelled theta/Tate boundary currents determine \(Q\)
uniquely up to a harmless gauge unit.

## Scope

This exact counterexample closes phase selection by abstract reciprocal
covariance. It does not rule out a phase selected by the full labelled source
or by an independently constructed Green current.

## Verification

The checker uses two exact roots of unity, verifies all reciprocal and
self-adjointness identities, and obtains distinct Cayley generators.
