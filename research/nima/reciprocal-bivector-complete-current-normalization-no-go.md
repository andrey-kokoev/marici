# Reciprocal bivector complete-current normalization no-go

## Model packet

For the source tail

\[
f(q)=e^{-\lambda q}v,
\qquad \lambda>\max(\operatorname{Re}s,1-\operatorname{Re}s),
\]

let `D` be the squared norm of the augmentation bivector `Omega wedge v`. The direct-sheet Green packet is

\[
E_s=\frac{D}{2\lambda(\lambda-s)^2},
\qquad
B_s=\frac{D}{(\lambda-s)^2},
\qquad
F_s=\frac{D}{2\lambda(\lambda-s)}.
\]

The reciprocal packet replaces `s` by `1-s`.

## Scale-invariant ratios

A scalar sheet normalization multiplies `E_s`, `B_s`, and `F_s` by the same positive factor. It cannot change

\[
\frac{E_s}{B_s}=\frac1{2\lambda}
\]

or

\[
\frac{F_s}{B_s}=\frac{\lambda-s}{2\lambda}.
\]

The energy-to-boundary ratio agrees automatically between reciprocal sheets. The forcing-to-boundary ratios differ by

\[
\frac{F_s}{B_s}-
\frac{F_{1-s}}{B_{1-s}}
=
\frac{1-2s}{2\lambda}.
\]

Therefore any scalar normalization matching the boundary coordinates also matches the energies, but cannot match the forcing coordinates away from `s=1/2`.

## Consequence

Normalized state or boundary isometry is weaker than complete-current sewing. The reciprocal mate must transport

\[
(E_s,B_s,F_s)
\]

as one packet. Away from the seam, this requires either:

1. an additional typed source current carrying the forcing-ratio defect; or
2. a non-scalar current-valued mate that changes more than the common sheet frame.

Primitive, square, connected, seam, and archimedean channels may be tested as sources for this defect only before scalar aggregation.

## Next microstep

Write the defect as

\[
\mathfrak A_{s,\lambda}
=
\frac{1-2s}{2\lambda}B,
\]

and compare its dependence on `lambda` with each existing boundary channel. Any candidate independent of the source decay parameter cannot cancel this family pointwise without an additional source-state map.

## Verification

`research/nima/checkers/check_reciprocal_bivector_complete_current_normalization_no_go.py` verifies the ratios and the obstruction on an exact rational off-seam fixture.
