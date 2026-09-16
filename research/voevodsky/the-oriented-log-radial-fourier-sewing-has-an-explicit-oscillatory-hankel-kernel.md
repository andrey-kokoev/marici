# The oriented log-radial Fourier sewing has an explicit oscillatory Hankel kernel

## Question

What is the actual source-derived Fourier operator after oriented log-radialization, and can it be replaced by the algebraic polynomial square root of radial reflection?

## Claim boundary

The transported Fourier operator is an explicit nonlocal oscillatory Hankel transform whose kernel depends on the sum of logarithmic radii. The polynomial metaplectic lift has the correct fourth power and spectrum but is not thereby this operator. Equality with external G4 sewing now has an exact kernel test.

## Half-density radial chart

Use the Fourier convention

$$
(\mathcal Ff)(y)=\int_{\mathbb R}f(x)e^{-2\pi ixy}\,dx.
$$

For \(\epsilon\in\{+1,-1\}\), define oriented logarithmic half-density coordinates

$$
g_\epsilon(u)=e^{u/2}f(\epsilon e^u).
$$

This chart is unitary from \(L^2(\mathbb R^\times,dx)\) to the oriented radial double \(L^2(\mathbb R,du)\oplus L^2(\mathbb R,du)\).

## Transported kernel

Let \(h=\rho_*\mathcal F\rho_*^{-1}g\). For output orientation \(\epsilon'\) and logarithmic radius \(v\), substitution \(x=\epsilon e^u\) gives

$$
h_{\epsilon'}(v)
=
\sum_{\epsilon=\pm1}
\int_{\mathbb R}
K_{\epsilon',\epsilon}(v,u)g_\epsilon(u)\,du,
$$

with

$$
K_{\epsilon',\epsilon}(v,u)
=
\exp\left(\frac{u+v}{2}\right)
\exp\left(-2\pi i\epsilon\epsilon'e^{u+v}\right).
$$

The kernel depends on \(u+v\), so the operator is Hankel-type in logarithmic coordinates. It mixes both radial orientations and is nonlocal in \(u\).

## Exact structural laws

Because the half-density chart is unitary and the additive Fourier transform is unitary,

$$
W_{\rm or}=\rho_*\mathcal F\rho_*^{-1}
$$

is unitary. Moreover,

$$
W_{\rm or}^2(g_+,g_-)=(g_-,g_+),
\qquad
W_{\rm or}^4=I,
$$

up to the fixed Fourier normalization already displayed. Thus its square is precisely radial reflection/channel swap.

## Comparison with the algebraic lift

The previously constructed operator

$$
R_u=P_++iP_-
$$

is a polynomial square root of an involution. It is local in the spectral projectors of that involution. The source-derived \(W_{\rm or}\) is the oscillatory integral operator above. Equal spectrum and equal square do not identify them.

Any claim that the polynomial metaplectic lift *is* Fourier sewing requires a separate conjugating map carrying its cyclic seed and integral kernel. Without that map, the polynomial lift remains a representation-theoretic model only.

## External G4 acceptance test

An external sewing operator \(W_{\rm G4}\) agrees with source Fourier sewing in this chart only if its distribution kernel equals

$$
K_{\epsilon',\epsilon}(v,u)
$$

on a common test core, including:

- the half-density factor \(e^{(u+v)/2}\);
- the orientation product \(\epsilon\epsilon'\);
- the Fourier phase \(2\pi\);
- the zero-endpoint port handled separately.

Agreement of fourth powers, spectra, or reciprocal signs is insufficient.

## Disposition

The source-derived oriented radial Fourier sewing is now explicit as an oscillatory Hankel kernel. This supplies the decisive external G4 comparison formula and prevents substitution of the abstract metaplectic square root for the actual Fourier operator.