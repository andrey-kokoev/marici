# Angular theta current and the Herglotz gate

The normalized function below agrees, up to the exact factor four, with the
earlier `reduced_F` Loewner target. The current work supplies a new
denominator-free and source-operator interpretation, not a new equivalence;
see `theta-loewner-rediscovery-and-meaning-audit.md`.

## Entire function in the natural coordinate

Because the completed Mellin source is even, there is an entire real function
\(C\) such that

\[
B(z)=C(w),
\qquad w=z^2.
\]

Put

\[
\zeta=w-\frac14,
\qquad
\mathcal E(w)=|C(w)|^2.
\]

On \(w=1/4+Re^{i\vartheta}\), define the clockwise angular current

\[
P(w)=-\partial_\vartheta\mathcal E(w).
\]

Direct differentiation gives the exact denominator-free identity

\[
\boxed{
P(w)=2\Im\!\left(\zeta C'(w)\overline{C(w)}\right).
}
\]

This is the same cone numerator, with \(P=Q/2\) under the normalization used
in the characteristic calculation.

## Normalized current

Where \(C(w)\ne0\), define

\[
H(w)=\zeta\frac{C'(w)}{C(w)}.
\]

Then

\[
\boxed{P(w)=2|C(w)|^2\Im H(w).}
\]

Therefore strict angular energy flow is equivalent to

\[
\boxed{\Im H(w)>0\qquad(\Im w>0).}
\]

In other words, the basis-free energy conjecture is exactly the assertion
that \(H\) is a Herglotz function on the upper half-plane.

This normalization is analytically useful but logically secondary: the
denominator-free current \(P\) remains smooth at boundary zeros, whereas
\(H\) has poles there.

## Harmonicity and its limitation

On any zero-free patch, \(H\) is analytic and \(\Im H\) is harmonic. This is
the strongest available maximum-principle structure for the current.

However, it does not by itself prove positivity. For a real entire \(C\), the
boundary value of \(H\) is real away from real zeros, so
\(\Im H=0\) on the regular real boundary. A positive harmonic extension must
be selected by its pole data and growth at infinity. Assuming those poles all
lie on the real axis would assume the desired zero geometry.

Thus the naive argument

\[
\text{real boundary values}+\text{maximum principle}
\Longrightarrow\Im H>0
\]

is invalid. It omits precisely the singularity and infinity data that carry
the RH-strength content.

## Conditional zero expansion explains the sign

Suppose, only for interpretation, that \(C\) has a genus-zero product with
zeros \(\rho_n<1/4\):

\[
C(w)=C(0)\prod_n\left(1-\frac{w}{\rho_n}\right).
\]

Then

\[
H(w)=\sum_n\frac{w-1/4}{w-\rho_n},
\]

up to any separately audited entire prefactor, and each summand satisfies

\[
\boxed{
\Im\frac{w-1/4}{w-\rho_n}
=\frac{(1/4-\rho_n)\Im w}{|w-\rho_n|^2}>0.
}
\]

This gives a transparent spectral explanation of the angular current: every
real zero lying to the left of the circle center contributes a positive
Poisson kernel.

For the Riemann source, RH places the nontrivial zeros at
\(w=-\gamma_n^2<0\), so they have exactly the required sign. This calculation
is an equivalence/explanation, not a proof, because invoking that zero
placement assumes RH.

## New proof target

The useful opportunity is now sharply stated:

> Derive the Herglotz property of
> \((w-1/4)C'(w)/C(w)\) from the completed theta source without using a zero
> product whose pole locations already assume RH.

Possible noncircular inputs are:

1. a positive resolvent or Stieltjes representation derived directly from
   the theta measure;
2. a Loewner-positive kernel for \(H\);
3. a source differential equation whose boundary and infinity data force the
   Herglotz sign; or
4. a denominator-free positive representation of
   \(\Im((w-1/4)C'\overline C)\).

The exact denominator-free Loewner kernel is now isolated:

\[
L_C(x,y)=\frac{(x-1/4)C'(x)C(y)-(y-1/4)C'(y)C(x)}{x-y}.
\]

Its finite matrices are congruent to the Loewner matrices of \(H\), but it
extends through real zeros of \(C\). Conditional on real zero geometry it is
a sum of positive rank-one spectral atoms. See
`theta-denominator-free-loewner-kernel.md`.

The first two reconnect the energy-flow program to the earlier
source-derived self-adjoint/Loewner program, now with the exact function and
normalization specified rather than guessed.

The factor \(w-1/4\) is now derived directly from the source:
\(\Phi=(\partial_u^2-1/4)A\) for the modular theta profile \(A\). The same
operator produces the completed-zeta pole cancellation, so a resolvent proof
must retain its endpoint contribution. See
`theta-source-operator-quarter-center.md`.

## Falsifiers

The angular-current conjecture is falsified by one upper-half-plane point
where \(\Im H\le0\), equivalently \(P\le0\) away from a zero.

A proposed maximum-principle proof is falsified if it cannot supply both:

- the singular measure/pole contribution without assuming zero locations;
- the correct growth contribution at infinity.

Subharmonicity of \(|C|^2\) alone is insufficient and must not be presented as
closing either gap.
