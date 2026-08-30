# Fourier--Tate reflection reverses drift, not forcing variance

## Source audit

The centered theta-tail equations already derived in the common source frame
are

\[
\psi_+'=-z\psi_+-F,
\qquad
\psi_-'=\overline z\psi_--F.
\]

Thus reciprocal Fourier--Tate reflection changes the spectral drift while the
same real theta forcing enters both equations with the same forward incidence.
This is the actual source law used in the full complex mixed-residual packet,
not a provisional model.

The two triangular control blocks have the schematic form

\[
A_+=
\begin{pmatrix}
A_{0,+}&B\
0&0
\end{pmatrix},
\qquad
A_-=
\begin{pmatrix}
A_{0,-}&B\
0&0
\end{pmatrix}.
\]

Reflection transports `B` to another forward `B`. It does not create the
lower-left adjoint arrow `B*`.

## Consequence of the path no-go

The recently proved incompatibility of pointwise common-path cancellation
applies directly to the native reciprocal theta double. The shared nonconstant
forcing prevents a nonzero solution from satisfying `u+v=0` throughout an
interval.

Therefore neither of these operations closes the Green residual:

- reciprocal reflection of the forward tail;
- promotion of terminal Evans cancellation to pathwise anti-diagonality.

The direct reflected-double route is closed.

## Variance is the missing constructor

The required completion must contain a contravariant operation

\[
B:\mathcal U\longrightarrow\mathcal H
\quad\longmapsto\quad
B^*:\mathcal H\longrightarrow\mathcal U.
\]

This reverses the source--state incidence. It is categorically different from
moving the same forward arrow to the reciprocal sector.

On a Hilbert tail space with source vector `F`, the formal adjoint is the
functional

\[
B^*G=\langle F,G\rangle.
\]

The formula is canonical once the common domain and metric are fixed, but its
existence as a bounded or rigged map is not enough. Fourier--Tate source
geometry must authorize it as dynamics or boundary incidence, and it must
retain the primitive, square, seam, and archimedean grades.

## Minimal block obstruction

With a role-preserving block-diagonal pairing, cross-adjointness of two upper
triangular forward systems forces `B=0`. This is incompatible with the
nontrivial theta forcing. Consequently no choice of endpoint boundary
condition repairs the missing lower incidence; the defect is in the bulk
arrow direction.

## Revised next gate

Construct the source-derived lower incidence at finite cutoff:

\[
B_{-,X}:\mathcal H_X\longrightarrow\mathcal U_X,
\]

and test the typed residual

\[
R_X^{\rm adj}=B_{-,X}-B_{+,X}^*.
\]

This comparison must include domain, graph norm, and all boundary grades. A
scalar equality after aggregation is insufficient.

The RH programme has therefore reached a constructor boundary rather than an
uncomputed sign: Fourier--Tate reflection supplies covariance, but not the
variance reversal required for conservative adjoint completion.

## Provenance

This synthesis uses the full complex forcing equations from
[Theta primitive seam current leaves an explicit mixed bulk residual](theta-primitive-seam-current-leaves-an-explicit-mixed-bulk-residual.md)
and the block-variance obstruction in Nima's
`theta-reciprocal-doubling-is-not-yet-adjoint-completion.md`. Its new content is
that the pointwise common-path no-go now closes the native reflected-double
shortcut and makes the adjoint-incidence constructor the unique surviving
local route.
