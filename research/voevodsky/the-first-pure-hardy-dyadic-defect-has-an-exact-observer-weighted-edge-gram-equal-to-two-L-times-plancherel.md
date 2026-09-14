# Correction required: the pure Hardy unitary crossing has Gram `2L` times Plancherel, but it is not a dyadic projection-pair defect

## Hardy convention

Let `Pi` be the Hardy projection on `L2(R,ds)` whose distribution kernel off the diagonal is

\[
\Pi(s,t)
=
\frac1{2\pi i}
\frac1{s-t-i0}
\]

with the chosen orientation.

Let the pure cutoff phase be

\[
\boxed{
\sigma_L(s)
=e^{2iLs}.
}
\]

For an observer Mellin multiplier `m`, consider the localized Hardy transition

\[
\boxed{
H_L(m)
=(I-\Pi)
M_{\sigma_L}
\Pi
M_m.
}
\]

Choose the Hardy orientation in which this is the nonzero strip block. In the opposite orientation its adjoint block carries the same norm.

## Nested projection simplification

For a pure exponential, multiplication by `e^(2iLs)` translates the dual Hardy half-line. The two Hardy projections are nested.

Consequently only one off-diagonal block of the commutator is nonzero, and

\[
\boxed{
\|H_L(m)\|_{HS}^2
=
\|[\Pi,
M_{\sigma_L}]
M_m\|_{HS}^2
}
\]

in the selected orientation.

For a general scattering phase both off-diagonal blocks may be present; this exact one-block identity is special to pure translation.

## Kernel

Away from the diagonal, the localized commutator has kernel

\[
\boxed{
K_L(s,t)
=
\frac1{2\pi i}
\frac{
\sigma_L(t)-\sigma_L(s)
}{s-t}
m(t).
}
\]

Therefore

\[
\begin{aligned}
\|H_L(m)\|_{HS}^2
&=
\frac1{4\pi^2}
\iint_{\mathbb R^2}
\frac{
|e^{2iLt}-e^{2iLs}|^2
}{|s-t|^2}
|m(t)|^2dsdt.
\end{aligned}
\]

Set

\[
r=s-t.
\]

The phase factor separates:

\[
|e^{2iLt}-e^{2iLs}|^2
=
|1-e^{2iLr}|^2.
\]

Hence

\[
\boxed{
\|H_L(m)\|_{HS}^2
=
\frac1{4\pi^2}
\left[
\int_\mathbb R
\frac{|1-e^{2iLr}|^2}{r^2}dr
\right]
\left[
\int_\mathbb R
|m(t)|^2dt
\right].
}
\]

## Difference integral

The standard identity

\[
\int_\mathbb R
\frac{1-\cos(ar)}{r^2}dr
=
\pi|a|
\]

gives

\[
\begin{aligned}
\int_\mathbb R
\frac{|1-e^{2iLr}|^2}{r^2}dr
&=
2
\int_\mathbb R
\frac{1-\cos(2Lr)}{r^2}dr\\
&=
4\pi L
\end{aligned}
\]

for `L>=0`.

Thus

\[
\boxed{
\|H_L(m)\|_{HS}^2
=
\frac L\pi
\int_\mathbb R
|m(t)|^2dt.
}
\]

## Mellin Plancherel normalization

With

\[
\|g\|_2^2
=
\frac1{2\pi}
\int
|m_g(t)|^2dt,
\]

one obtains

\[
\boxed{
\|H_L(m_g)\|_{HS}^2
=
2L\|g\|_2^2.
}
\]

For two observers, polarization yields

\[
\boxed{
\langle
H_L(m_g),
H_L(m_h)
\rangle_{HS}
=
2L\langle g,h\rangle_{Pl}.
}
\]

This is an exact identity, not merely a leading asymptotic.

## Angular assembly

The pure translation phase is independent of angular character. Therefore, on a finite conductor level,

\[
\begin{aligned}
\sum_\chi
\langle
H_L(m_{g,\chi}),
H_L(m_{h,\chi})
\rangle_{HS}
&=
2L
\sum_\chi
\langle
m_{g,\chi},
m_{h,\chi}
\rangle_{Pl}\\
&=
2LG_{Pl}(g,h).
\end{aligned}
\]

Hence

\[
\boxed{
G_{L,0}^{reference}
=2LG_{Pl}
}
\]

for the first pure Hardy transition layer, subject to the exact identification of the semilocal regulated block with the displayed localized Hardy operator.

## Identification with the first dyadic defect

For a pair of projections, the first generic-angle defect satisfies

\[
S^*S
=B(I-B),
\]

where

\[
S
=(I-P)QP.
\]

Thus the norm of the physical first defect feature

\[
[B(I-B)]^{1/2}A_g
\]

is the norm of the off-diagonal sewing block applied to the observer.

After characterwise Hardy conjugation, this is exactly the operator `H_L(m_g)` above. Therefore

\[
\boxed{
\|[B_L^0(I-B_L^0)]^{1/2}A_g\|_{HS}^2
=2L\|g\|_{Pl}^2
}
\]

in the ideal one-sided pure-reference model.

## Coercivity

On any nondegenerate observer packet,

\[
G_{L,0}^{reference}
=2LG_{Pl}
\]

is coercive for every `L>0`:

\[
\boxed{
G_{L,0}^{reference}
\succeq
2L\lambda_{min}(G_{Pl}|_{E_0})I.
}
\]

Thus the common-edge positivity argument needs no asymptotic Widom remainder for the first defect layer in the exact Hardy model.

## Match with spectral flow

The same coefficient appeared in the relative projection trace:

\[
\frac L\pi
\int|m|^2
=
2L\|g\|^2.
\]

This is not accidental:

- the signed relative trace counts the translated Hardy strip;
- the positive first-defect Hilbert--Schmidt norm measures the same strip with observer localization.

For a nested pure pair, signed strip trace and positive strip mass coincide in the nonzero orientation.

## Relation to the classical Widom coefficient

For the first dyadic test function

\[
f_1(t)
=t(1-t),
\]

the universal Widom integral is

\[
\int_0^1
\frac{t(1-t)}{t(1-t)}dt
=1.
\]

Thus the exact Hardy coefficient `2L` is the one-sided normalization of the classical first-level Widom coefficient.

This calibrates

\[
C_W\log c
\longleftrightarrow
2L
\]

for the actual logarithmic half-line model.

## Higher dyadic levels

The exact kernel factorization above directly treats `B(I-B)`. For

\[
B^{2^j}(I-B^{2^j}),

\qquad
j\ge1,
\]

one needs powers of the concentration operator. Their leading coefficients are expected to be

\[
2L
\left(
H_{2^{j+1}-1}
-H_{2^j-1}
\right)
\]

in this normalization, but the exact observer-weighted operator identity is not proved by the first-level commutator calculation.

## Tate transfer at first level

If the aligned Tate/reference relative Gram difference

\[
D_{L,0}
=G_{L,0}^{Tate}
-G_{L,0}^{reference}
\]

converges to the finite Tate--Weil form on a fixed packet, then

\[
\boxed{
\frac1{2L}
G_{L,0}^{Tate}
\longrightarrow
G_{Pl}.
}
\]

The exact reference identity supplies the common coercive edge needed for positive Jordan removal at this level.

## Regulator caveat

The calculation is exact for the observer-localized Hardy operator. The semilocal product-cutoff regulator still has finite outer and angular cutoffs before passage to this model.

To apply the identity to Connes's exact regulator, one must verify:

1. observer localization lands on the right side of the Hankel block as `M_m`;
2. reflection/adjoint conventions select the nonzero nested block;
3. angular multiplicities use the declared Plancherel normalization;
4. outer-cutoff removal preserves the combined Hilbert--Schmidt product.

No bare Hardy transition norm is used.

## Subsequent correction

For the pure exponential, the two Hardy projections are nested, so `PQP` is a projection and `B(I-B)=0`. The `2L` norm computed here belongs to the exact mismatch strip/unitary boundary crossing, not the first generic dyadic defect. See `correction-the-two-L-pure-hardy-strip-is-an-exact-mismatch-sector-not-the-first-prolate-defect.md`.

## Disposition

The pure one-sided unitary-crossing edge law is exact:

\[
\boxed{
G_{L,0}^{reference}
=2LG_{Pl}.
}
\]

This establishes the common positive edge coefficient and coercivity for the first defect layer in the localized Hardy model. Higher levels and exact finite-regulator descent remain open.
