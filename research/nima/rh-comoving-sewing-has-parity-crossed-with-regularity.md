# RH comoving sewing has parity crossed with regularity

## Question

What is the minimum faithful state carried by the two comoving boundary charts,
and what does that force on the missing rigged sewing constructor?

## Two-chart source cell

The inner and outer limiting front profiles are

\[
a_-(u)=H(u)-1,
\qquad
a_+(u)=-H(u).
\]

They satisfy

\[
a_-+a_+=-1.
\]

Reflection exchanges them. Therefore their canonical parity decomposition is

\[
T=a_-+a_+,
\qquad
O=a_--a_+.
\]

The overlap channel (T) is the constant fifth-wall carrier and is reflection
even. The front channel (O) records which boundary face is entrance and
which is exit; it is reflection odd.

## Scalar-overlap no-go

Projecting a chart pair to its overlap sum retains (T) and annihilates the
anti-diagonal chart direction. Hence it cannot recover (O). Two chart pairs
with the same overlap but opposite front orientation have identical scalar
overlap readout.

This is not a numerical conditioning problem. It is an exact kernel caused by
the quotient.

## Crossing with arithmetic regularity

Primitive and square scale measures occupy distinct completion grades:

- primitive: exponential/Laplace boundary grade;
- square: tempered boundary grade.

The minimum faithful completed boundary packet must therefore retain four
typed lanes:

```text
primitive overlap
primitive oriented front
square overlap
square oriented front
```

Equivalently, it has parity crossed with regularity. This statement does not
assert that all four lanes are independent physical degrees of freedom. It
asserts that neither parity nor regularity may be quotiented before the source
sewing law determines the allowed relations.

## Necessary sewing form

The missing archimedean/reciprocal sewing must:

1. act on both comoving charts before pushforward to the observation scale;
2. preserve the even overlap and odd front characters;
3. act continuously on the exponential and tempered grades separately;
4. retain the constant--delta overlap incidence under Fourier transport;
5. commute with reflection by fixing (T) and reversing (O);
6. recover every finite moving-window cell after pushforward;
7. avoid any undeclared continuous inclusion from the primitive grade into the
   square Hilbert grade.

## Finite falsifiers

- Delete either chart: the constant overlap identity is lost.
- Keep only the sum: front orientation is erased.
- Identify exponential and tempered grades: the primitive current is either
  excluded or continuity is weakened beyond the square/Clark gate.
- Apply reflection without reversing the front channel: the source chart law
  fails.
- Reconstruct moving support from a single stationary chart: one front escapes
  to infinity.

## Exact checker

On a four-point grid away from the discontinuity, the checker verifies:

- the two profiles sum to the constant negative-one carrier;
- reflection exchanges the profiles;
- (T) is even and (O) is odd;
- overlap projection has a one-dimensional anti-diagonal kernel;
- two regularity grades crossed with two parity characters produce four typed
  lanes.

## Claim boundary

This packet derives the minimum typing of the sewing domain. It does not
construct the continuous Fourier--Tate sewing operator, prove a completion
margin, or establish positivity or RH.

## Disposition

The sewing constructor is now more sharply specified: it is a two-chart,
two-regularity, parity-aware relative pushforward. Any scalar or single-chart
candidate is finitely falsified before analytic completion.

