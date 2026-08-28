# Bounded common-forcing rigidity of theta-tail deformations

## One tail equation

Each labelled moving-endpoint theta tail satisfies

`T'(x)=-a T(x)-f(x)`

with `a=1/2+z` or `a=1/2-z` and the same positive Gaussian endpoint forcing
`f(x)`.  Let a proposed reciprocal deformation multiply this tail by a
nowhere-zero factor `H(x)`.

Demand that the deformed tail obey the same source equation with the same
forcing:

`(HT)'=-a HT-f`.

Subtracting `H` times the original equation gives the exact residual gate

`H'T+(1-H)f=0`.

## Homogeneous defect

Define

`Y=(H-1)T`.

Using the tail equation and the residual gate gives

`Y'=-aY`.

Hence

`Y(x)=c exp(-ax)`.

This is the complete deformation freedom compatible with the same forcing at
the differential level.

## Boundary admissibility kills the freedom

For the theta atom,

`f(x)=2 exp(-pi exp(2x))`,

and the moving tail has the same superexponential endpoint scale, multiplied
only by algebraic powers of `exp x`.  In the open central strip,
`Re(a)>0`, but `exp(-ax)` decays only exponentially.

If `c` is nonzero, then

`H-1=c exp(-ax)/T(x)`

grows superexponentially along the positive real endpoint.  Such a multiplier
does not preserve the admitted moving-tail test class.  Therefore every
bounded source-admissible multiplier preserving the same forcing has

`c=0`, `H=1`.

Apply this independently to

`H_+=h exp(g)`

and

`H_-=h exp(-g)`.

Both equal one.  Thus `h=1` and `g=0`, up to logarithmic branch constants
that act trivially on the multipliers.

## Meaning

The abstract Lorentz conic admits independent radial gauges and rapidity
shears.  The labelled theta constructor does not.  Its common moving-endpoint
forcing plus endpoint admissibility rigidifies both channels before scalar
aggregation.

This closes the sharp hostile at the individual labelled-tail level: no
nontrivial bounded multiplier can preserve the source equation and change
the divisor.  The remaining completion problem is whether sampling at
`x=log n`, summing labels, and forming the completed boundary packet preserve
this rigidity without admitting an asymptotic unbounded defect.

## Optical test

Realize both forced first-order tail channels and inject the same calibrated
endpoint waveform `f`.  For any proposed deformation, measure

`r_H=H'T+(1-H)f`.

Also monitor the normalized defect `Y=(H-1)T`.  A zero residual with nonzero
`Y` predicts a merely exponential tail against the superexponential source
envelope, causing the multiplier to leave the admitted dynamic range.  The
apparatus therefore has two rejection modes:

- nonzero common-forcing residual;
- zero residual but unbounded endpoint multiplier.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_common_forcing_tail_rigidity.py
```
