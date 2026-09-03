# Mpmath interval cannot enclose the accelerated gamma tail

## Question

Can the accelerated erfc series be certified using the remaining `mpmath.iv` special functions after interval `erfc` failed?

## Capability test

A directed preflight separately evaluated interval Hurwitz zeta and digamma at point intervals. Evaluation stopped in Hurwitz zeta with

`AttributeError: MPIntervalContext has no attribute bernoulli`.

The earlier interval-erfc preflight failed with `NoConvergence`. Therefore all three special functions used by the accelerated representation—scaled erfc, Hurwitz zeta, and digamma—lack a working interval implementation in this backend.

## Exact elementary replacement

The obstruction is implementation-specific, not analytic. Each unavailable function has a bounded elementary replacement:

1. scaled erfc: small-argument erf Taylor enclosure and large-argument alternating asymptotic enclosure;
2. digamma difference: Euler--Maclaurin expansion using rational Bernoulli numbers, interval `log`, and a next-term remainder;
3. Hurwitz zeta tail: finite rational power sum plus integral-test or Euler--Maclaurin remainder;
4. constants `pi`, Euler's constant, and `log pi`: fixed rational enclosures verified independently;
5. all final arithmetic: rational intervals, avoiding reliance on undocumented libm rounding.

The required absolute source-value width is only `1e-6`, so low-order Euler--Maclaurin bounds suffice. The analytic erfc and prime tails are already many orders smaller.

## Authority boundary

Implementing a rational outward-rounding kernel is repository code and remains executable with the admitted Python surface. Installing Arb/python-flint would alter the environment and was not authorized. No installation was attempted.

## Disposition

Do not call `mpmath.iv` a certification backend for this checker. Either implement the bounded rational kernel above or obtain explicit authority for an Arb-backed execution surface. Until then, the rank-two signs remain numerical observations.