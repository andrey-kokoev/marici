# The tail boundary system is a singular pencil, not a deficiency family

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact fixed-carrier typing obstruction

## Audit of the source-derived tail system

The homogeneous tail augmentation is

\[
\mathcal D_s=
\begin{pmatrix}
\partial_q+s&f(q)\\
0&\partial_q
\end{pmatrix}.
\]

Separating the spectral parameter gives

\[
\mathcal D_s=D_0+sP,
\qquad
P=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

The weight \(P\) has rank one. Therefore this is a singular operator pencil,
not an ordinary deficiency equation \((S-zI)\Psi=0\) for one fixed symmetric
operator.

No invertible left change of variables can turn the coefficient of \(s\) into
the identity, because that would require a left inverse for singular \(P\).
Deleting the null-weight component is not allowed: it is the constant source
channel whose coupling \(f(q)\) creates the original inhomogeneous tail
equation.

## Reciprocal doubling does not repair the type

Combining the two reciprocal sheets changes the spectral weight to a signed
block such as

\[
P_{\mathrm{dbl}}=\operatorname{diag}(1,0,-1,0).
\]

It remains singular. The doubled positive bulk identity therefore does not by
itself promote the family to deficiency spaces of a fixed self-adjoint
operator.

## Consequence for the Lagrangian programme

The abstract forbidden-incidence theorem applies to Cauchy data

\[
L_z=\Gamma\ker(S^*-z)
\]

of one fixed closed symmetric carrier \(S\). The tail construction currently
supplies Cauchy data of a singular pencil instead. Identifying the two would
silently discard the source channel and is not authorized.

This is the first concrete obstruction to constructing the missing spectral
Cauchy family \(L_z\).

## The singularity and one-way incidence are the same obstruction

The fixed source coupling is triangular:

\[
N_f=\begin{pmatrix}0&f\\0&0\end{pmatrix}.
\]

It is not self-adjoint. The smallest symmetric completion is

\[
\widetilde N_f=\begin{pmatrix}0&f\\f&0\end{pmatrix}.
\]

Its lower-left entry changes the source-channel equation by adding
backreaction from \(G\) to the constant channel. Thus symmetrizing the pencil
is not a choice of metric or notation. It requires a new reverse source
incidence.

This identifies the singular-pencil defect with the previously isolated
one-way accumulator defect. The Weyl/Lagrangian route has reached the same
structural frontier rather than bypassing it.

## Legitimate repair routes

There are three mathematically distinct possibilities.

1. Develop a self-adjoint linear-relation or descriptor-system theorem for
   the singular pencil, with its own Green form and forbidden-nonreal
   incidence result.
2. Add a source-derived dynamical partner that gives the constant channel a
   nonzero spectral weight, producing a regular fixed-carrier system.
3. Eliminate the constant channel and accept the resulting nonlocal spectral
   dependence, then prove independently that it is a Weyl function of a
   fixed symmetric relation.

The second route is the most explanatory but requires a genuinely new source
operation. The third is at greatest risk of manufacturing the operator from
the scalar transform.

## Generalized energy gate

For a pencil \(A-zP\) with self-adjoint \(A) and nonnegative \(P\), an
eigenstate with positive weight obeys a reality identity involving

\[
\langle P\Psi,\Psi\rangle.
\]

Singularity leaves a null sector where this argument has no force. Therefore
the exact next question is whether the completed theta zero-state has
strictly positive pencil weight and whether the full bordered operator is
self-adjoint as a linear relation. Neither fact follows from the existing
tail equation.

## Falsifiers

The route fails if:

- the bordered pencil cannot be made symmetric on a source-derived rigged
  domain;
- a nonzero zero-state lies entirely in the null spectral-weight channel;
- reciprocal doubling leaves an indefinite weighted norm on admissible
  states; or
- regularization requires a source channel chosen after inspecting \(\xi\).

## Scope

Singularity of the spectral weight and persistence under reciprocal doubling
are exact. No claim is made that singular-pencil methods cannot ultimately
prove confinement. The ordinary self-adjoint deficiency theorem is simply
not yet applicable.

## Verification

The checker verifies the rank defect, the impossibility of converting the
weight to the identity by a left change, the essential forcing carried by the
null-weight channel, persistence of singularity after doubling, and the lower
backreaction forced by symmetric completion.
