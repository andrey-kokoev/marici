# Form domination forces the Green radical to be gauge before RH normalization

## Radical and frame

Let

\[
B_X\ge0
\]

be the complete diagonal Green boundary form and let

\[
F_X=U_XU_X^*\ge0
\]

be the arithmetic synthesis frame. Define the Green radical

\[
N_X=\ker B_X.
\]

The residual is

\[
R_X=B_X-F_X.
\]

Before forming any Moore--Penrose Birman--Schwinger operator, the status of
\(N_X\) must be decided in the source category.

## Domination theorem

Suppose the arithmetic frame is relatively form-bounded by the Green form:

\[
F_X\le c_XB_X
\]

for some finite \(c_X\).

For \(h\in N_X\),

\[
0\le\langle h,F_Xh\rangle
\le
c_X\langle h,B_Xh\rangle
=0.
\]

Hence

\[
F_X^{1/2}h=0
\]

and therefore

\[
F_Xh=0.
\]

Thus

\[
\ker B_X\subseteq\ker F_X.
\]

Consequently,

\[
R_Xh=0
\]

for every \(h\in N_X\).

This proves:

> On the unquotiented carrier, form domination and residual injectivity imply
> \(\ker B_X=0\).

A semidefinite Green form cannot support both a bounded normalized incidence
operator and exact zero exclusion unless its radical is removed from the
admissible state object.

## Three radical dispositions

Every Green-null direction must receive exactly one typed disposition.

### Gauge radical

A subspace \(N_X\) is gauge when all source operations, observers, reciprocal
maps, and determinant lines descend to the quotient

\[
\overline H_X=H_X/N_X.
\]

Then \(N_X\) is not an admissible physical or arithmetic state sector. The
Green form becomes nondegenerate on the quotient.

This is the only disposition compatible with form domination and RH
normalization when \(N_X\ne0\).

### Unreachable radical

A Green-null direction may be absent from the source-generated range:

\[
N_X\cap\operatorname{ran}U_X=0.
\]

Unreachability alone does not authorize quotienting. The direction can still
enter through seam, endpoint, reciprocal, or completion operations.

To promote unreachable to gauge, one must prove invariance of \(N_X\) under
the complete source category and vanishing of every authorized readout on it.

### Admissible radical

If \(N_X\) contains a genuine source state, it cannot be erased. Under form
domination it lies in \(\ker F_X\) and hence in \(\ker R_X\), producing an
immediate residual zero.

In that case the positive Birman--Schwinger route fails before spectral
analysis. A different indefinite or enlarged boundary geometry is required.

## Quotient construction

Assume \(N_X\) is source-authorized gauge. Let

\[
q_X:H_X\to\overline H_X
\]

be the quotient map. The Green form descends to a positive definite form

\[
\overline B_X
\]

on \(\overline H_X\). Form domination ensures that \(F_X\) descends to

\[
\overline F_X.
\]

One may then define

\[
\overline K_X
=
\overline B_X^{-1/2}
\overline F_X
\overline B_X^{-1/2}.
\]

Residual kernels on the quotient satisfy

\[
\ker(\overline B_X-\overline F_X)
\cong
\ker(I-\overline K_X).
\]

The quotient must precede normalization. Moore--Penrose inversion on the
unquotiented carrier is only a computational presentation of the same support
restriction; it does not decide gauge authority.

## Reciprocal congruence

Let \(J_X\) be the source reciprocal transport between sectors. The correct
comparison is congruence of pencils:

\[
J_X^*B_{-,X}(1-s)J_X=B_{+,X}(s),
\]

\[
J_X^*F_{-,X}(1-s)J_X=F_{+,X}(s).
\]

This implies

\[
J_X^{-1}N_{+,X}=N_{-,X}.
\]

Therefore reciprocal transport preserves the radical and descends to the
quotients. Generalized eigenvalues, including \(\lambda=1\), are preserved
without identifying independently chosen inverse square roots.

If the radicals are not carried into one another, the reciprocal determinant
frame is already inconsistent.

## Support projection stability

Let

\[
P_X=1_{(0,\infty)}(B_X)
\]

be the Green support projection. Finite quotienting is not enough. Completion
requires the projections \(P_X\) to converge in the topology used by the
relative determinant and observer family.

Two failures are distinct.

### Collapsing positive direction

A sequence of unit vectors \(h_X\) may satisfy

\[
\langle h_X,B_Xh_X\rangle\to0
\]

while \(h_X\in\operatorname{ran}P_X\) at every finite cutoff. A new Green-null
direction then appears only at completion.

### Rotating support

The dimensions of \(N_X\) may remain fixed while \(P_X\) fails to converge.
Finite normalized operators can each have a spectral gap at one, yet act on
incompatible supports. No completed pencil follows.

Thus support convergence is logically prior to uniform spectral separation.

## Spectral pollution gate

Assume quotient supports converge. Finite gaps

\[
\operatorname{dist}
\left(
1,\sigma(\overline K_X)
\right)>0
\]

can still shrink to zero. Worse, weak or non-norm convergence can create
spectral pollution near one even when each finite spectrum appears separated.

A completion-safe theorem requires an admitted convergence mode such as:

- norm-resolvent convergence of the quotient pencils;
- norm convergence in the relevant determinant ideal;
- collectively compact convergence with verified spectral exactness;
- another source-derived theorem excluding pollution at one.

Only after spectral exactness is established does a uniform finite gap imply
absence of a completion collision.

## Coercivity after quotient

On each compact \(C\) in an open sector, a convenient sufficient condition is

\[
\overline B_X(s)\ge\beta_C I
\]

with \(\beta_C>0\) independent of \(X\) and \(s\in C\).

This gives uniform inverse-square-root control. It is stronger than
nondegeneracy of each finite quotient.

The full ordered theorem is then:

1. radical is source-authorized gauge;
2. quotient supports converge reciprocally;
3. quotient Green forms are compact-locally coercive;
4. quotient normalized frames converge spectrally exactly;
5. their spectra remain uniformly separated from one.

## Interaction with graph augmentation

The arithmetic identity channel in the graph carrier does not authorize
quotienting the Green radical. It preserves arithmetic provenance, while the
Green quotient concerns analytic boundary directions.

A Green-null vector with a nonzero retained arithmetic component may not be
gauge. The quotient decision must be made on the complete graph state and its
matching residual, not on the analytic projection alone.

This prevents source labels from disappearing under a convenient support
restriction.

## Hostile tests

1. Form domination with a nonzero unquotiented Green radical produces an
   immediate residual kernel.
2. Unreachability is not gauge authority.
3. Moore--Penrose normalization before radical typing hides common-null states.
4. Reciprocal maps that do not preserve radicals cannot descend to the pencil
   quotient.
5. Positive eigenvalues tending to zero create a completion radical.
6. Nonconvergent support projections invalidate comparison of finite spectra.
7. Pointwise finite spectral gaps do not exclude pollution at one.

## Consequence for categorical RH

Kitaev's two-stage gate sharpens to a necessary theorem:

- first prove that the complete Green radical is a reciprocal source-gauge
  subobject and that its quotient is completion-stable;
- only then study separation of the normalized quotient spectrum from one.

If the radical is admissible, the positive Green route is closed. If it is
gauge, the RH problem lives on the reciprocal quotient pencil.

## Verdict

Relative form domination forces every Green-null direction to be frame-null
and hence residual-null. Therefore a semidefinite Green form can support RH
normalization only after its radical is source-authorized as gauge and removed.
The next completion hazards are support collapse, rotating radicals, and
spectral pollution at the generalized eigenvalue one.
