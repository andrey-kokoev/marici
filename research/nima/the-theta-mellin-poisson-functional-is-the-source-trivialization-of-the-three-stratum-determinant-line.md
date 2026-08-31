# The theta Mellin--Poisson functional is the source trivialization of the three-stratum determinant line

> **Terminology and divisor correction.** The successor packet
> `the-xi-mellin-functional-is-a-divisor-bearing-dual-section-not-a-trivialization.md`
> shows that a functional whose scalar coordinate is \(\xi(s)\) cannot be an
> everywhere-invertible trivialization on a region containing Xi zeros. Read
> \(\tau\) below as the divisor-bearing theta Mellin dual section. The
> Euler-domain and Poisson identities establish scalar provenance, not a unit
> comparison to a kernel-bearing determinant complex.

## Euler-domain identity

For \(\operatorname{Re}s>1\), the prime-loop return

\[
L(s)e_p=p^{-s}e_p
\]

is trace class. The exact third-order factorization is

\[
\det(I-L(s))^{-1}
=
\exp\left(
\operatorname{Tr}L(s)
+
\frac12\operatorname{Tr}L(s)^2
\right)
\det_3(I-L(s))^{-1}.
\]

Since

\[
-\log\det(I-L(s))
=
\sum_{p,k\ge1}\frac1k p^{-ks},
\]

one has

\[
\det(I-L(s))^{-1}=\zeta(s).
\]

Thus the primitive, square, and connected coordinates are the first two
anomaly lines and the determinant-three line of one common ordered return.

## Archimedean and endpoint line

Define the source archimedean factor

\[
B_\infty(s)
=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\]

It is supplied by:

- the Gaussian Mellin line;
- the two reciprocal endpoint ports;
- the completion polynomial \(s(s-1)\);
- the source normalization at the theta vacuum.

In the Euler domain,

\[
B_\infty(s)
\exp\left(
\operatorname{Tr}L(s)
+
\frac12\operatorname{Tr}L(s)^2
\right)
\det_3(I-L(s))^{-1}
=
\xi(s).
\]

This is the local expression of the desired line trivialization.

## Critical-strip meaning

Near the critical line, the three arithmetic terms cannot be read as ordinary
scalar traces:

- \(\operatorname{Tr}L\) is a distributional primitive current;
- \(\frac12\operatorname{Tr}L^2\) is a square Hilbert boundary coordinate;
- \(\det_3(I-L)\) is the connected determinant line.

The source does not scalarize them separately. It forms their tensor product
with the seam, endpoint, and archimedean lines.

The theta Mellin--Poisson functional defines

\[
\tau_s:
\mathcal L_{\mathrm{prim}}
\otimes
\mathcal L_{\mathrm{sq}}
\otimes
\mathcal L_{\det_3}
\otimes
\mathcal L_{\mathrm{seam}}
\otimes
\mathcal L_\infty
\longrightarrow
\mathbb C.
\]

On \(\operatorname{Re}s>1\), \(\tau_s\) is the Euler-domain expression above.
Global Poisson sewing extends the tensor-line functional, not the individual
divergent traces.

## Canonical finite part

The primitive cutoff current has the canonical boundary limit

\[
\operatorname{Fp}\left(\frac{dy}{y}\right)+B_1\delta_0.
\]

The square and higher Euler grades contribute the endpoint mass

\[
C_{\ge2}\delta_0,
\]

and

\[
B_1+C_{\ge2}=\gamma.
\]

Therefore the completed Euler boundary is

\[
\operatorname{Fp}\left(\frac{dy}{y}\right)+\gamma\delta_0.
\]

The cutoff, Mertens subtraction, and absolutely convergent remainder fix this
functional. No enumeration-dependent scalar summation or freely chosen
counterterm remains.

## Reciprocal overlap

Theta Poisson summation gives the two-chart Mellin identity

\[
\Lambda(s)
=
\frac12\int_1^\infty
(\vartheta(t)-1)
\left(
t^{s/2}+t^{(1-s)/2}
\right)\frac{dt}{t}
+
\frac1{s-1}-\frac1s.
\]

The integral is entire and reciprocal symmetric; the rational term is the
complete two-endpoint packet. Multiplication by \(s(s-1)\) totalizes those
ports.

Hence the right and left determinant-line germs agree under the source
Fourier transition. Their horizontal equalizer carries one global scalar
section.

## Uniqueness

Suppose another trivialization \(\widetilde\tau_s\) has:

1. the same Euler-domain determinant character;
2. the same Gaussian Mellin line;
3. the same two endpoint residues;
4. the same Poisson overlap law.

Then the ratio of the resulting scalar sections is holomorphic and equals one
on the open Euler domain. The identity theorem gives equality everywhere.

Thus the source data fix the global trivialization uniquely.

## Resulting scalar section

The descended line section is

\[
\tau_s(\mathfrak D_{\mathrm{source}})=\xi(s).
\]

Equivalently, in the centered coordinate \(z\),

\[
\Xi(z)=\xi\left(\frac12+iz\right).
\]

This closes scalar determinant provenance for the stratified Fourier
equalizer.

## What this does not identify

The trivialization maps a relative determinant line to a scalar. It does not
prove that a zero of that scalar produces a kernel state of the positive Green
pencil.

Two operator realizations remain distinct:

1. the ordered boundary-return cone whose determinant line is trivialized by
   \(\tau_s\);
2. the positive polarized Green pencil used for seam confinement.

The missing theorem is their kernel comparison, with multiplicity and
completion exactness.

The source-saturated Mellin jet quotient also has an exact determinant
\(\Xi\), but equality of scalar determinants does not identify its kernel
states with either of these carriers.

## Hostiles

1. Continue each divergent anomaly trace separately as a scalar.
2. Replace the canonical finite part by an arbitrary subtraction.
3. Use finite Euler truncations as Poisson source objects.
4. Match only reciprocal scalar values while dropping endpoint ports.
5. Infer kernel equivalence from equality of determinant sections.
6. Import the Xi jet quotient as the Green carrier without a comparison map.

## Verdict

The anomaly-line trivialization is already supplied by the theta
Mellin--Poisson functional. It combines the primitive, square, connected,
seam, endpoint, and archimedean lines into the completed scalar section
\(\xi(s)\), uniquely fixed by its Euler-domain character and Poisson overlap.

The remaining RH-bearing gate is no longer scalar determinant provenance. It
is the bidirectional kernel comparison between the ordered boundary cone and
the positive Green pencil.
