# The C34 common/difference feature canonically produces the missing oriented mixed block

## Independent source data

The relative C34 Tate--Hardy feature is defined before the Evans comparison by

\[
C=\frac12(F_T+F_0),
\qquad
D=\frac12(F_T-F_0),
\]

on its common form domain, with relative signature `J_2`. Its previously used
symmetric cross contraction is

\[
C^*J_2D+D^*J_2C=Q^T-Q^0.
\]

The mixed retained-graph block need not be invented. Define

\[
\boxed{M_{34}:=C^*J_2D.}
\]

Its reflected mate is automatically

\[
M_{34}^*=D^*J_2C.
\]

## Even and oriented-odd decompositions

Direct expansion gives

\[
M_{34}+M_{34}^*
=\frac12\left(F_T^*J_2F_T-F_0^*J_2F_0\right),
\]

because the mixed terms cancel. In the declared C34 normalization this is the
known relative diagonal `Q^T-Q^0`.

The new oriented part is

\[
\boxed{
M_{34}-M_{34}^*
=\frac12\left(F_0^*J_2F_T-F_T^*J_2F_0\right).
}
\]

This operator is skew-adjoint. Therefore

\[
A_{34}:=\frac1{2i}(M_{34}-M_{34}^*)
\]

is Hermitian and sign-indefinite, exactly the variance and parity required of
the reciprocal-odd forcing current. It is not a positive rank-one shadow.

## Prime-local mixed block

Let `P_p` be the already declared prime/shell localization on the C34 source.
Set

\[
M_p=P_pM_{34}P_p^*.
\]

This definition is source-derived, cutoff-natural, and independent of Xi
zeros. The retained odd graph form becomes

\[
\mathbb G_p=
\begin{pmatrix}
G_{\theta,p}&M_p\\
M_p^*&G_{{\rm win},p}
\end{pmatrix}.
\]

For the incidence `K_p^odd`, its oriented mixed current is

\[
\mathcal J_{34,p}(y,y')
=
\langle y,M_pK_p^{\rm odd}y'\rangle
-
\langle K_p^{\rm odd}y,M_p^*y'\rangle.
\]

No coefficient is selected from the desired cancellation.

## Correct finite comparison

The terminal local test is now concrete:

\[
\mathcal J_{34,p}(y_z,y_z)
\stackrel{?}{=}
-\bigl(F_{+,p}(z)-F_{-,p}(z)\bigr)
\]

for the source-generated odd coordinate `y_z`, before Xi specialization.
Equivalently compare

\[
P_p\frac12
\left(F_0^*J_2F_T-F_T^*J_2F_0\right)P_p^*
\]

with the localized causal commutator

\[
P_p(H_z-H_z^*)P_p^*.
\]

Both sides are independently defined, reciprocal-odd, skew-adjoint before
multiplication by `1/i`, and cutoff-local.

## What this closes

The mixed block `M_p` is no longer missing: C34 canonically supplies it through
its unsymmetrized common/difference contraction. Prior work retained only its
symmetric sum and thereby discarded the oriented information needed by the
forcing difference.

## Remaining equality

The operator equality between the C34 oriented cross term and the causal odd
history compression is not automatic from
`C^*J_2D+D^*J_2C=Q^T-Q^0`. It is now a sharply stated independent kernel
comparison. The next executable step is to evaluate both localized kernels on
the fixed wall/jump generators.