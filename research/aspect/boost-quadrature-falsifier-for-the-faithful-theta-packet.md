# Boost-quadrature falsifier for the faithful theta packet

## Radial response channel

Write `z=a+i tau` and let

`M(z)=integral rho(q) cosh(zq) dq`,

`N(z)=integral rho(q) sinh(zq) dq`,

`P(z)=(z^2-1/4)/2`.

The faithful ports are

`S(z)=1/2+2P(z)M(z)`

and

`A(z)=2P(z)N(z)`.

On the seam `a=0`, `M` is real, `N` is imaginary, and `P` is real.  Hence
`Re A=0`.  The real quadrature of `A` is therefore a direct off-seam
falsifier at every scalar null.

Its first boost derivative at the seam is real and source-derived:

`K(tau)=d_a Re A(a+i tau)|_(a=0)`

`=-2 tau integral rho(q) sin(tau q)dq`

` -(tau^2+1/4) integral rho(q)q cos(tau q)dq`.

Where `K(tau)` is nonzero, a calibrated horizontal modulation makes `Re A`
a locally faithful radial coordinate.

## Positive hostile

Positivity and the Wick rotation do not force confinement.  Take the positive
two-atom half-source

`rho=delta_1+2 delta_(6/5)`.

Then

`M(z)=cosh(z)+2cosh(6z/5)`

and

`N(z)=sinh(z)+2sinh(6z/5)`.

The scalar port has the real off-seam zero

`z=-0.3047410165495805761...`,

which lies inside `|Re z|<1/2`.  At that zero,

`A=0.1661316823868194023...`.

Thus the scalar port is dark while the forbidden real antisymmetric
quadrature is plainly nonzero.  The three-port instrument detects the
failure immediately.

## Optical protocol

At each candidate scalar null:

1. lock the scalar port `S` to its null;
2. homodyne both quadratures of `A`;
3. modulate the horizontal boost by `a=plus/minus h`;
4. estimate `K` from the centered real-quadrature difference;
5. report a seam-compatible null only when `Re A` is within its preregistered
   uncertainty and the boost calibration is nondegenerate.

The control port must simultaneously remain at `B=3/2`.  Otherwise the
candidate is not on the completed theta zero fiber at all.

## Boundary of the test

`Re A=0` is necessary for the reciprocal fixed seam but is not sufficient to
infer the base coordinate without a source-faithfulness theorem.  Zeros of
`K` require a higher boost jet or another independent response port.  The
hostile proves that the first quadrature already rejects positive
hyperbolic-moment sources that scalar readout alone cannot distinguish.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_boost_quadrature_falsifier.py
```
