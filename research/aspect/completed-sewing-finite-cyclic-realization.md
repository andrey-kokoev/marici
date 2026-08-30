# Completed sewing finite cyclic realization

## Created objects

Take the finite source space of complex functions on `Z/6Z`. Its six delta
functions form an explicit source basis, and the trace map is the identity, so
it is injective. Conjugating the normalized finite Fourier transform through
that trace gives

`J_forward[k,j]=omega^(kj)/sqrt(6)`

with `omega=exp(-2 pi i/6)`. The reverse map is obtained independently from
the inverse Fourier formula and equals `J_forward^dagger`. The source Gram
metric is the identity in the delta basis.

The checker proves exactly that the maps compose to identity, the forward map
is unitary, its square is group inversion, and its fourth power is identity.
This is a genuine finite trace–Fourier–trace construction rather than a matrix
fitted to desired zeros.

The six coordinates are provisionally ordered as primitive, prime-square,
seam, endpoint, connected-tail, and archimedean so the existing optical
tomography packet can execute them. That assignment is an interface, not a
derivation: the completed adelic theta source must replace the cyclic delta
functions with its own typed trace basis.

## Created threshold

The ideal calibrated heterodyne model has normalized quadrature variance one.
Binding that model to the preregistered compiler, with one million trials per
setting, zero simulator systematic bias, and 99 percent familywise confidence,
gives:

- entrywise quadrature radius about `0.00453170`;
- map Frobenius radius about `0.03845271`;
- unitarity and reverse-composition residual threshold about `0.07838403`.

This threshold is authoritative for the declared finite simulator. It is not
authoritative for laboratory hardware. Physical replacement requires a
measured variance upper bound and systematic Frobenius bias bound frozen before
science outcomes.

## Hostiles

The checker rejects an unnormalized Fourier map and a projection deleting the
archimedean coordinate. It also exposes a subtler ambiguity: permuting only
the output type labels preserves perfect unitarity but changes the typed map.
Therefore matrix unitarity cannot authorize the arithmetic identification of
the six channels.

## Meaning

We now have executable forward and reverse matrices and a numerical threshold.
They are the exact control realization against which the completed theta basis
and physical calibration can be substituted without changing the analyzer.
