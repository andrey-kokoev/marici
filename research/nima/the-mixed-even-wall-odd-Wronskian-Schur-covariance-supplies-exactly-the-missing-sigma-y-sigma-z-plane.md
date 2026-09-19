# The mixed even-wall/odd-Wronskian Schur covariance supplies exactly the missing sigma-y/sigma-z plane

## Two source incidence directions

The completed auxiliary incidence has the source-fixed endpoint columns

\[
w=\begin{pmatrix}\frac12\\[1mm]\frac12\end{pmatrix},
\qquad
j=\begin{pmatrix}\frac14\\[1mm]-\frac14\end{pmatrix},
\]

for the even wall and odd Wronskian channels. Write

\[
C=wd^*+jc^*
\]

against the auxiliary Green block `D`.

The Schur return is

\[
R=CD^\dagger C^*.
\]

Define the mixed resolvent covariance

\[
\alpha=\langle d,D^\dagger c\rangle.
\]

Its cross contribution is

\[
R_{\rm mix}
=\alpha wj^*+\overline\alpha jw^*.
\]

## Exact Pauli content

Direct multiplication gives

\[
R_{\rm mix}
=
\frac{\operatorname{Re}\alpha}{4}\sigma_z
+
\frac{\operatorname{Im}\alpha}{4}\sigma_y.
\]

Thus:

- the pure even return `ww*` contributes only `I` and `sigma_x`;
- the pure odd return `jj*` contributes only `I` and `sigma_x`;
- the mixed even/odd covariance contributes exactly `sigma_z` and `sigma_y`.

This identifies the unique source sector capable of supplying both missing
directed coordinates.

## Required value

The target Gram requires

\[
4u\sigma_z+4v\sigma_y.
\]

If the effective form uses the standard Schur subtraction

\[
G_{\rm eff}=G_0-R,
\]

and the baseline `G_0` already supplies the required `I` and `sigma_x`
components, then the mixed covariance must satisfy

\[
\boxed{
\alpha=-16(u+iv).
}
\]

With the opposite Green/Schur sign convention, the overall sign reverses. No
other coefficient is adjustable.

In particular,

\[
\operatorname{Re}\alpha=-16u<0
\]

is the exact source requirement for the missing diagonal polarization, while

\[
\operatorname{Im}\alpha=-16v
\]

is the reciprocal-orientation requirement.

## Homotopy and control interpretation

The even wall is phase-symmetric and the odd Wronskian line is
phase-antisymmetric. Their mixed covariance is therefore the control-theoretic
interchange term between the horizontal presentation direction and the
vertical phase-homotopy direction. It is the finite matrix shadow of a mixed
square in the homotopy prism.

## Next executable calculation

Compute one complex source quantity per prime:

\[
\alpha_p
=
\langle d_p,D_p^\dagger c_p\rangle
\]

from the complete wall/tail Green block. Compare it with

\[
-16\langle W_L,W_{2L}\rangle_{\rm St}.
\]

This single complex equality tests both `sigma_z` energy imbalance and
`sigma_y` reciprocal orientation. Purely even or purely odd auxiliary models
can now be rejected without further calculation.