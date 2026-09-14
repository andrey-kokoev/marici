# Each prime phase current is a positive Poisson density minus a common Plancherel baseline

## Local prime current

For a prime `p`, put

\[
r_p=p^{-1/2},
\qquad
\theta_p(t)=t\log p.
\]

The real logarithmic phase current is

\[
V_p(t)
=(\log p)
\sum_{k\ge1}r_p^k\cos(k\theta_p(t)).
\]

The Poisson kernel of the disk is

\[
P_r(\theta)
=
\frac{1-r^2}{|1-re^{i\theta}|^2}
=
1+2\sum_{k\ge1}r^k\cos(k\theta).
\]

Therefore

\[
\boxed{
V_p(t)
=
\frac{\log p}{2}
\left(P_{p^{-1/2}}(t\log p)-1\right).
}
\]

This is an exact identity, including every prime power.

## Positive local carrier

Since

\[
P_r(\theta)>0,
\]

the measure

\[
d\mu_p(t)
=
\frac{\log p}{2}
P_{p^{-1/2}}(t\log p)dt
\]

is positive. For a convolution-square spectral observer

\[
\chi_g(t)=|\widehat g(t)|^2,
\]

one obtains

\[
\int\chi_gV_pdt
=
\|\widehat g\|_{L^2(d\mu_p)}^2
-
\frac{\log p}{2}
\|\widehat g\|_{L^2(dt)}^2.
\]

Thus one prime current is a positive Poisson norm minus a scalar multiple of the common Plancherel norm.

## Finite-stage common bulk

For a finite set `S`, define

\[
\rho_S(t)
=
\frac12
\sum_{p\in S}
(\log p)
P_{p^{-1/2}}(t\log p),
\]

and

\[
c_S=
\frac12
\sum_{p\in S}\log p.
\]

Then

\[
\boxed{
V_S(t)=\rho_S(t)-c_S,
\qquad
\rho_S(t)>0.
}
\]

Consequently

\[
\boxed{
\int|\widehat g|^2V_Sdt
=
\|\widehat g\|_{L^2(\rho_Sdt)}^2
-
c_S
\|\widehat g\|_{L^2(dt)}^2.
}
\]

All active primes have therefore been absorbed into one positive multiplication density `rho_S`. The only remainder in this orientation is one common Plancherel baseline, not one negative coordinate per prime.

## Transition under adjoining a prime

If `q notin S`, then

\[
\rho_{S\cup\{q\}}
=
\rho_S+
\frac{\log q}{2}
P_{q^{-1/2}}(t\log q),
\]

\[
c_{S\cup\{q\}}
=c_S+\frac12\log q.
\]

The positive carrier embeds isometrically by the usual Radon--Nikodym map into

\[
L^2((\rho_S+
ho_q)dt),
\]

or, more canonically, all stages sit in the single ambient direct integral over the real spectral line with increasing density. Prime additions commute.

This is a common bulk in the spectral variable; it does not orthogonalize prime labels.

## Deterministic polarization

The polarized form is

\[
\int
\widehat g(t)
\overline{\widehat h(t)}
V_S(t)dt
=
\langle\widehat g,\widehat h\rangle_{\rho_Sdt}
-
c_S
\langle\widehat g,\widehat h\rangle_{dt}.
\]

Because `rho_S` is summed before taking the inner product, every observer uses one deterministic common metric. No arbitrary orthogonality between prime sectors is introduced.

## Explicit-formula sign audit

The usefulness of this decomposition depends on orientation. In the usual completed explicit formula, the prime distribution appears with the hostile sign relative to the zero sum. If the Weil convention uses

\[
-V_S,
\]

then

\[
-V_S
=c_S-
ho_S
\]

and the decomposition becomes

\[
\int|\widehat g|^2(-V_S)dt
=
c_S\|\widehat g\|_2^2
-
\|\widehat g\|_{L^2(\rho_Sdt)}^2.
\]

The hostile component is then the full positive Poisson bulk with a minus sign. It is infinite-rank, exactly as predicted by the first-prime-crossing audit. The scalar baseline cannot dominate it pointwise because Poisson kernels exceed their mean near `theta=0`.

Therefore the Poisson factorization does not prove Weil positivity. It gives the exact positive operator whose subtraction must be controlled by gamma and endpoint completion.

## Toeplitz/Szegő realization

The Poisson kernel has the Hardy-space factorization

\[
P_r(\theta)
=
\left|
\frac{\sqrt{1-r^2}}
     {1-re^{i\theta}}
\right|^2.
\]

Hence define

\[
(C_pg)(t)
=
\sqrt{\frac{\log p}{2}}
\frac{\sqrt{1-p^{-1}}}
     {1-p^{-1/2}e^{it\log p}}
\widehat g(t).
\]

Then

\[
\|C_pg\|_{L^2(dt)}^2
=
\frac{\log p}{2}
\int
P_{p^{-1/2}}(t\log p)
|\widehat g(t)|^2dt.
\]

For finite `S`, one common feature can be chosen as multiplication by

\[
C_S(t)=\sqrt{\rho_S(t)}.
\]

This removes prime labels entirely:

\[
\|C_Sg\|_2^2
=
\sum_{p\in S}\|C_pg\|_2^2.
\]

The equality is canonical because it is an equality of densities, not a declaration that prime spaces are orthogonal.

## Interaction with the gamma baseline

The remainder

\[
c_S\|\widehat g\|_2^2
\]

has the same Plancherel type as constant terms in the gamma logarithmic derivative. This creates a concrete possibility: combine the prime baseline with the archimedean constant before estimating either sector.

However,

\[
c_S
\longrightarrow
+\infty
\]

as primes are exhausted. Any global cancellation must therefore occur at the regularized explicit-formula level; the finite-stage constants cannot be passed to the limit separately.

## Revised common-bulk target

At a finite stage the completed form should be organized schematically as

\[
Q_S(g)
=
Q_{end+gamma+baseline,S}(g)
-
\|C_Sg\|^2.
\]

Rung-four positivity is equivalent to a source-derived contraction

\[
\boxed{
\|C_Sg\|^2
\le
Q_{end+gamma+baseline,S}(g)
}
\]

uniformly under support and place enlargement.

This is the semilocal analogue of the Connes--Consani rank-one estimate, except that `C_S` is now infinite-rank after the first prime enters.

## Disposition

The prime current has an exact common positive factorization:

\[
\boxed{
V_S=
ho_S-c_S,

the
\rho_S=
\frac12\sum_{p\in S}
(\log p)
P_{p^{-1/2}}(t\log p)>0.
}
\]

With the hostile explicit-formula sign, the complete prime sector is one negative Poisson norm plus one positive common baseline. The remaining theorem is a uniform contraction of this Poisson feature into the endpoint--gamma--baseline carrier.
