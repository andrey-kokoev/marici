# No unitary can simultaneously intertwine the semilocal scaling and degree operators because the Euler weight changes the cyclic measure

## Two canonical structures

For each finite place set `S`, the cyclic-pair construction gives:

1. the scaling operator, represented spectrally by multiplication
   \[
   X_S=M_s
   \]
   on `L2(R,dm_S)`;
2. the degree/Hermite operator
   \[
   N_S P_n^S=nP_n^S,
   \]
   where `P_n^S` are the orthonormal polynomials for `dm_S`.

The semilocal prolate candidate is built from both structures:

\[
W_{\lambda,S}
=
-X_S^2+
2\lambda^2(4N_S+1)
-
\frac14
\]

up to the source normalization.

## Scaling intertwiner

The two stationary maps `Omega_S^plus-or-minus` satisfy

\[
X_S\Omega_S^\pm
=
\Omega_S^\pm X_\infty.
\]

They realize the Euler scattering phase exactly. But they do not map the archimedean orthogonal-polynomial filtration to the semilocal one.

## Degree intertwiner

There is separately a canonical unitary

\[
Z_S:L^2(\mathbb R,dm_\infty)
\to
L^2(\mathbb R,dm_S)
\]

defined by

\[
Z_SP_n^\infty=P_n^S.
\]

It satisfies

\[
\boxed{
N_SZ_S=Z_SN_\infty.
}
\]

But generally

\[
X_SZ_S
\ne
Z_SX_\infty,
\]

because the Jacobi recurrence coefficients depend on the measure.

Thus the scaling and degree towers have different canonical transition maps.

## Rigidity theorem

Suppose a unitary

\[
U:H_\infty	o H_S
\]

satisfied all three conditions

\[
X_SU=UX_\infty,
\]

\[
N_SU=UN_\infty,
\]

and mapped the normalized degree-zero cyclic vector to the normalized degree-zero cyclic vector.

The cyclic-vector condition follows from the second relation up to a phase, since the zero eigenspace of `N` is the constant-polynomial line; fix that phase. Let

\[
d\mu_S=dm_S/dm_S(\mathbb R),
\qquad
d\mu_\infty=dm_\infty/dm_\infty(\mathbb R).
\]

Then for every integer `n>=0`, cyclic intertwining gives

\[
\int s^n\,d\mu_S(s)
=
\int s^n\,d\mu_\infty(s).
\]

Hence the two normalized measures have identical moments.

The archimedean gamma measure has exponential decay and satisfies a determinate Hamburger moment problem. The finite Euler modification remains comparable to it because the finite product of local factors is bounded above and below on the real line. Therefore the modified moment problem is also determinate.

Identical moments imply

\[
\boxed{
dm_S=dm_\infty.}
\]

But

\[
\frac{dm_S}{dm_\infty}
=
\prod_{p\in S\setminus\{\infty\}}
|L_p(1/2-is)|^2
\]

is nonconstant whenever a finite prime is present. This is a contradiction.

Therefore:

\[
\boxed{
S\ne\{\infty\}
\quad\Longrightarrow\quad
\text{no unitary simultaneously intertwines }X,N,
\text{ and the cyclic vector}.}
\]

## Filtration version

Even without explicitly requiring `UN=NU`, suppose `U` intertwines scaling and carries every polynomial filtration

\[
\operatorname{span}\{1,s,\ldots,s^n\}
\]

onto the corresponding semilocal orthogonal-polynomial filtration while fixing the cyclic line. Then the Gram matrices of all monomials agree, so all moments agree and the same contradiction follows.

Thus the failure is not an artifact of the chosen orthonormal bases.

## Curvature/holonomy operator

The mismatch between the two transition maps is measured by

\[
\boxed{
\mathcal H_S
=Z_S^*\Omega_S^-.
}
\]

This is a unitary on the archimedean carrier. If the scaling and degree squares commuted, `mathcal H_S` would commute with both `X_infinity` and `N_infinity` and fix the cyclic vector, forcing it to be the identity. For a nonempty finite-prime set it is nontrivial.

Equivalently, transport the semilocal degree operator through the scaling intertwiner:

\[
\widetilde N_S
=(\Omega_S^-)^*N_S\Omega_S^-.
\]

Then

\[
\boxed{
\widetilde N_S-N_\infty
\ne0.
}
\]

This difference is the discrete curvature between the prime scattering tower and the prolate grading tower.

## Transported prolate operator

Under the scaling intertwiner,

\[
(\Omega_S^-)^*
W_{\lambda,S}
\Omega_S^-
=
-X_\infty^2
+2\lambda^2(4\widetilde N_S+1)
-
\frac14.
\]

Therefore the entire semilocal perturbation relative to the archimedean prolate operator is

\[
\boxed{
(\Omega_S^-)^*
W_{\lambda,S}
\Omega_S^-
-W_{\lambda,\infty}
=
8\lambda^2
(\widetilde N_S-N_\infty).
}
\]

The missing scattering comparison has now been localized exactly to the transported degree-operator difference.

## Trace-class audit

The source paper explicitly defers computation of the general semilocal Jacobi coefficients. It supplies no estimate showing that

\[
\widetilde N_S-N_\infty
\]

is compact, trace class, or relatively trace class with respect to the prolate operator.

Without such an estimate, standard Birman--Krein scattering theory cannot be applied to the prolate pair. The stationary Euler phase of the scaling pair cannot simply be declared to be the prolate scattering determinant.

## Correct next theorem

A viable relative comparison does not require exact intertwining. It would suffice to prove, for a suitable resolvent power,

\[
\boxed{
(\widetilde N_S-N_\infty)
(W_{\lambda,\infty}-i)^{-m}
\in
\mathcal L^1
}
\]

or the corresponding semifinite trace ideal.

One could then define a spectral-shift function for the transported prolate pair and compare its determinant phase with `J_S`.

The required equality would still be a theorem, not a consequence of Hilbertian Sonin stability.

## Transition compatibility

For nested place sets, the curvatures obey a cocycle rather than a simple additive law because orthogonalization changes globally:

\[
\mathcal H_{S\cup\{p\}}
=
Z_{S\cup\{p\}}^*
\Omega_{S\cup\{p\}}^-
\]

cannot be obtained by multiplying `mathcal H_S` with a scalar local factor alone. This is where deterministic cross-prime polarization enters the semilocal prolate system.

## Disposition

The exact Jacobi--prolate intertwiner does not exist once a finite prime changes the cyclic measure. The obstruction is rigid and elementary: simultaneous scaling, grading, and cyclic-vector intertwining would force equality of all moments and hence equality of the measures.

The remaining bridge is a relative perturbation theorem for

\[
\boxed{
\widetilde N_S-N_\infty.
}
\]

Its trace-ideal class, spectral shift, and compatibility under adding places are presently not provided by the source.
