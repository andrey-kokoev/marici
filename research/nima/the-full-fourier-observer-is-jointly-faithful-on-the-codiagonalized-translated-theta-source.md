# The full Fourier observer is jointly faithful on the codiagonalized translated-theta source

## Question

Does summing the labelled translated theta atoms into one common full-line history necessarily erase prime-power labels?

## Claim boundary

No at the level of uniqueness. The complete Fourier transform of the common history factors into the nonzero theta transform times the Fourier transform of an absolutely summable discrete measure supported at the signed prime-power displacements. Those displacements are distinct, so the common-history synthesis is injective on the projective source. This gives a jointly faithful observer, but not a continuous coefficient recovery map or Hilbert lower bound.

## Common-history synthesis

Let \(\lambda=(p,k)\),

\[
L_\lambda=k\log p,
\qquad
a_\lambda=\frac1k e^{-L_\lambda/2},
\]

and use the signed displacement set

\[
\mathcal D=\{+L_\lambda,-L_\lambda\}.
\]

The codiagonalized history is

\[
(C\mathcal Ic)(t)
=\sum_\lambda a_\lambda
\left(c_\lambda^+\tau_{L_\lambda}\Phi(t)
+c_\lambda^-\tau_{-L_\lambda}\Phi(t)\right).
\]

Projective exponential summability implies absolute convergence in every rapid-history seminorm.

## Fourier factorization

With the translation convention absorbed into the phase sign,

\[
\widehat{C\mathcal Ic}(\xi)
=\widehat\Phi(\xi)F_c(\xi),
\]

where

\[
F_c(\xi)
=\sum_\lambda a_\lambda
\left(c_\lambda^+e^{i\xi L_\lambda}
+c_\lambda^-e^{-i\xi L_\lambda}\right).
\]

Because the coefficient packet has every exponential moment, \(F_c\) extends to an entire function of \(\xi\).

## Distinct signed supports

If

\[
k\log p=\ell\log q,
\]

then \(p^k=q^\ell\). Unique factorization forces \(p=q\) and \(k=\ell\). Since every \(L_\lambda>0\), the positive and negative supports are also disjoint. Thus every point of \(\mathcal D\) has one source label and orientation.

## Injectivity

The completed-theta atom is nonzero, so its Fourier transform is not identically zero. There is a real open interval on which \(\widehat\Phi\ne0\). If

\[
C\mathcal Ic=0,
\]

then \(F_c=0\) on that interval. Entire continuation gives

\[
F_c\equiv0.
\]

Equivalently, the Fourier transform of the finite signed measure

\[
\mu_c
=\sum_\lambda a_\lambda
\left(c_\lambda^+\delta_{L_\lambda}
+c_\lambda^-\delta_{-L_\lambda}\right)
\]

vanishes. Fourier uniqueness for finite measures implies \(\mu_c=0\). Distinct support and nonzero \(a_\lambda\) then give

\[
c_\lambda^+=c_\lambda^-=0
\]

for every \(\lambda\). Therefore

\[
\ker(C\mathcal I)=0.
\]

## What is not recovered

Injectivity is not stable reconstruction. The translated atoms can become nearly dependent in a Hilbert norm, and dividing by \(\widehat\Phi\) near its zeros can amplify errors. No estimate here bounds individual coefficients by one common-history Hilbert norm.

The full Fourier family is jointly faithful as an observer. A finite set of frequencies, one Laplace value, one scalar theta sum, or one Evans zero need not be faithful. Continuous projective recovery after codiagonalization requires quantitative interpolation bounds for the nonuniform displacement set and control of division by \(\widehat\Phi\).

## Consequences

The common-history codiagonal preserves source identity algebraically even though it can destroy Hilbert closed range. Hence:

- codiagonalization does not create a source radical on the projective packet;
- cross-prime Gram entries may still appear;
- prime labels remain reconstructible only through the complete observer family;
- determinant or Green coercivity does not follow from injectivity.

## Direction rescore

- Joint faithfulness of the full Fourier observer: completed.
- Algebraic recovery after common-history codiagonalization: uniqueness completed.
- Continuous projective coefficient recovery from common history: 9/10; requires nonuniform interpolation estimates.
- Hilbert-stable recovery: 2/10 and likely false without an additional observer norm.
- Finite-frequency or scalar recovery: 0/10.

## Disposition

The codiagonalized translated-theta source is injective. The next depth-first gate is quantitative: determine whether the signed logarithmic prime-power displacement set admits a continuous interpolation map in the declared rapid/projective topology. No RH conclusion is authorized.
