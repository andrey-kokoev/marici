# The theta source has a canonical infinite moment ladder

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact source realization

## Positive moment coordinates

For (u\ge0), put

\[
x_n(u)=\pi n^2e^{2u}
\]

and define

\[
M_k(u)=e^{u/2}\sum_{n\ge1}x_n(u)^ke^{-x_n(u)},
\qquad k\ge0.
\]

Every (M_k) is strictly positive. The completed theta source on this chart
is the finite readout

\[
\Phi(u)=4M_2(u)-6M_1(u).
\]

## Exact raising law

Since (x_n'=2x_n), termwise differentiation gives

\[
DM_k=\left(2k+\frac12\right)M_k-2M_{k+1}.
\]

Thus the source has a canonical constant-coefficient infinite realization
(DM=AM), where (A) is upper bidiagonal, with diagonal entry (2k+1/2)
in row (k) and superdiagonal entry (-2). The scalar theta function is a
compression of this positive tower, not its state space.

## The exact finite-wall residual

Let

\[
R_N=\sum_{k=0}^Nc_kM_k.
\]

Differentiating produces only one term outside the retained span:

\[
DR_N=
\sum_{k=0}^N\left(2k+\frac12\right)c_kM_k
-2\sum_{k=0}^{N-1}c_kM_{k+1}
-2c_NM_{N+1}.
\]

The last summand is the exact truncation defect. A finite scalar closure can
exist only when its top coefficient vanishes, after which the same argument
descends recursively and kills every coefficient.

## Interpretation

The additional comparison channel is not one more scalar derivative. It is
the incidence map from moment grade (k) to grade (k+1). Any finite model
must retain its outward boundary current

\[
J_N=-2c_NM_{N+1}.
\]

Discarding (J_N) makes the truncated system appear closed. Retaining it
shows exactly how information leaves the finite presentation. The full
theta/Tate Green system should therefore be built on two reciprocal copies of
this graded moment module, together with the primitive, square, seam, and
archimedean boundary ports already isolated in the programme.

## Scope

This is an exact realization of the positive-chart theta source and its
finite truncation residual. It does not yet derive the reciprocal-sheet action
on the full tower, the completed Green current, a positive conserved form, or
RH. Those are now the concrete next operations.

