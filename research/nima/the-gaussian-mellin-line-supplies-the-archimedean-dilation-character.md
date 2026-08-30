# The Gaussian Mellin line supplies the archimedean dilation character

## Labelled vacuum line

Let

\[
\phi_n(x)=e^{-\pi n^2x^2}
\]

and let \(R_a\) act by dilation,

\[
(R_af)(x)=f(ax).
\]

Then

\[
\phi_n=R_n\phi_1,
\qquad
R_aR_b=R_{ab}.
\]

The Mellin readout at parameter \(s\) is

\[
\mathcal M_s(f)
=
\int_0^\infty f(x)x^{s-1}\,dx
\]

on its source domain. Change of variables gives the exact line
semi-invariance law

\[
\mathcal M_sR_a
=
a^{-s}\mathcal M_s.
\]

Thus the archimedean dilation generator has line character

\[
\chi_s(a)=a^{-s}.
\]

Because

\[
\chi_s(ab)=\chi_s(a)\chi_s(b),
\]

this character respects the complete multiplicative relation system. It
constructs the archimedean row of the zero sieve for dilation words before any
scalar aggregation over arithmetic labels.

## Prime-power and Adams specialization

For a prime-power scale \(a=p^k\),

\[
\chi_s(p^k)=p^{-ks}.
\]

Under Adams grade raising \(k\mapsto rk\), the relative archimedean character is

\[
\frac{\chi_s(p^{rk})}{\chi_s(p^k)}
=
p^{-(r-1)ks}.
\]

At the central half-density \(s=1/2\),

\[
p^{-(r-1)k/2}
\]

is exactly the exponential part of the Euler Adams residue. Therefore

\[
\rho_r(p,k)
=
\frac1r
\frac{\chi_{1/2}(p^{rk})}{\chi_{1/2}(p^k)}.
\]

The factor \(1/r\) is the prime-power multiplicity ratio
\((rk)^{-1}/k^{-1}\). Hence the Euler half-density cocycle splits canonically
into:

1. an archimedean Mellin dilation character;
2. an arithmetic logarithmic-multiplicity character.

This identifies the scalar Adams residue as an adelic product of two
source-derived one-dimensional characters rather than an unexplained
coefficient correction.

## Gaussian source authorization

The dilation character alone is universal for Mellin transformation and does
not distinguish the standard archimedean source. Source authorization comes
from the Gaussian vacuum equation

\[
a_n\phi_n=0,
\qquad
a_n=\partial_x+2\pi n^2x,
\]

together with covariance

\[
a_{pn}R_p=pR_pa_n.
\]

This makes the family of vacuum lines stable under prime dilation. The Mellin
character is therefore attached to a source-defined invariant family, not to
an arbitrary profile chosen after scalar completion.

Integration by parts gives

\[
2\pi M(s+2)=sM(s),
\qquad
M(s)=\mathcal M_s(\phi_1).
\]

With source normalization and the required growth condition, this recurrence
selects the standard gamma line. The recurrence by itself is not the
constructor; it is the scalar shadow of the vacuum covariance.

## Zero-sieve consequence

For every dilation word \(w\),

\[
\mathcal M_s(R_wf)
=
\chi_s(w)\mathcal M_s(f).
\]

Therefore

\[
\mathcal M_s(f)=0
\quad\Longrightarrow\quad
\mathcal M_s(R_wf)=0.
\]

The archimedean dilation subcategory has an exact zero-sieve factorization.
Moreover, \(\chi_s(a)\ne0\) for every \(a>0\) and finite \(s\), so dilation
neither creates nor removes a Mellin zero.

This is a propagation theorem for the archimedean orbit. It is not RH:
off-seam zeros can still enter through the arithmetic aggregation or the
relative endpoint determinant.

## Relation to the relative endpoint complex

Endpoint translation is additive in the logarithmic scale
\(q=\log a\), while archimedean dilation is multiplicative in \(a\). The
Mellin character turns additive scale displacement into

\[
\chi_s(e^q)=e^{-sq}.
\]

For the prime-power cut \(q=k\log p\), this is \(p^{-ks}\). Thus the
archimedean character is the natural multiplicative line attached to the same
scale displacement carried additively by the relative endpoint interval.

However, it does not by itself totalize the endpoint complex. The primitive
and square endpoint currents remain divergent before the third-order relative
determinant and archimedean countercurrent are assembled.

The required comparison cell must show that the determinant of oriented
endpoint concatenation transforms by \(\chi_s\), with the first two arithmetic
orders retained as explicit counterterms.

## Reciprocal behavior

Under the reciprocal parameter change \(s\mapsto1-s\),

\[
\chi_{1-s}(a)=a^{s-1}.
\]

The product

\[
\chi_s(a)\chi_{1-s}(a)=a^{-1}
\]

is parameter-independent. This gives a rigid scalar compatibility for doubled
sector transport. It does not supply the anti-linear reciprocal comparison or
the completed functional equation; those require the source Fourier--Poisson
cell and determinant-line orientation.

Any proposed reciprocal sewing whose archimedean dilation multipliers do not
have product \(a^{-1}\) is incompatible with the Gaussian Mellin line.

## Hostile tests

1. A proposed archimedean multiplier different from \(a^{-s}\) fails direct
   Mellin change of variables.
2. A multiplier obeying dilation covariance but attached to a non-Gaussian
   Fourier-fixed hostile lacks vacuum authorization.
3. Erasing the multiplicity factor \(1/r\) falsely identifies the full Euler
   residue with the archimedean character.
4. Treating the nonvanishing gamma line as proof of arithmetic nonvanishing
   confuses one generator row with the completed readout.
5. A reciprocal pair whose product depends on \(s\) fails the doubled
   character identity.

## Consequence for categorical RH

Two generator rows now meet exactly:

- Adams grade transport contributes the arithmetic factor \(1/r\);
- Gaussian dilation contributes
  \(p^{-(r-1)ks}\).

At \(s=1/2\), their product is the established Euler residue. This supplies a
source-derived compatibility cell between arithmetic grade change and the
archimedean Mellin line.

The next unresolved line is not the local gamma multiplier. It is the
third-order relative determinant comparison that joins this nonvanishing
archimedean character to the primitive, square, seam, and connected endpoint
currents.

## Verdict

The Gaussian Mellin line carries the exact archimedean dilation character
\(a^{-s}\). Its central relative character combines with prime-power
multiplicity to reproduce the Euler Adams cocycle. The archimedean zero-sieve
row is therefore constructed locally; global categorical RH still requires
the relative endpoint determinant and reciprocal completion cell.
