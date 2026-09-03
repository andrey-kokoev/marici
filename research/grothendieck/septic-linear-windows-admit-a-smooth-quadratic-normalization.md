# Septic linear windows admit a smooth quadratic normalization

## Problem

The septic pair `s(t),1-s(t)` is a linear partition. The logarithmic IMS identity requires windows whose squares sum to one. Substituting the linear windows into the quadratic identity changes the principal symbol because

`s^2+(1-s)^2` is not one.

## Quadratic normalization

Define

`d(t)=sqrt(s(t)^2+(1-s(t))^2)`,

`rho_1(t)=s(t)/d(t)`,

`rho_2(t)=(1-s(t))/d(t)`.

Since

`d(t)>=1/sqrt(2)`,

the denominator never vanishes. The identities are exact:

`rho_1^2+rho_2^2=1`,

`rho_2(t)=rho_1(1-t)`.

The septic profile and its first three derivatives match constant extensions at both endpoints. Composition with the smooth normalization map preserves `C^3` regularity. Thus `rho_1,rho_2` are proper subordinate windows admissible for the quadratic IMS formula.

## Scaled commutator budget

On overlap width `h`, set `rho_(j,h)(x)=rho_j(x/h)`. Then

`||rho_(j,h)'''||_1=h^(-2)||rho_j'''||_1`.

For two transitions and two complementary windows, Aspect's Fourier-moment estimate gives

`C_loc^quad(h)<= (pi/6) * 4 h^(-2)||rho_1'''||_1`.

This constant must replace the linear septic constant when the quadratic IMS identity is used.

## Relation to the linear convention

The original linear partition remains valid for nonsymmetric left/right localization formulas, but it does not directly produce a sum of localized quadratic forms with unchanged principal coefficient. Quadratic normalization avoids that ambiguity at the cost of a new derivative constant.

The normalized and linear localizations still differ by bounded terms after each is defined with its own correct identity. Their constants are not numerically interchangeable.

## Disposition

The normalization mismatch is repaired constructively. The next mechanical task is exact or directed evaluation of `||rho_1'''||_1`; a numerical scout can locate its sign changes, but publication use requires certified roots or interval quadrature.
